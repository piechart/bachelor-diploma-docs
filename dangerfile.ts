import { danger, fail, warn } from 'danger'

// Critical
// ========

if (danger.github.pr.base.ref !== 'master') {
  fail('We only accept PRs to `master` branch.')
}

const prTitle = danger.github.pr.title
const patchMatch = prTitle.match(/patch.\d+/)
const addFileViaUpload = prTitle.includes('Add file') && prTitle.includes('via upload')

if patchMatch || addFileViaUpload {
  fail('Please list added files names in PR title.')
}

const importantFiles = [
  '.github/workflows/checker.yml',
  '.github/workflows/danger.yml',
  '.github/workflows/rebase.yml',
  '.github/CODEOWNERS',
  '.github/pull_request_template',

  'dangerfile.ts',
  'checker.py',
  'contribute.md'
]

const changedFiles = [
  ...danger.git.modified_files,
  ...danger.git.created_files,
  ...danger.git.deleted_files,
]

for (const changedFile of changedFiles) {
  if (importantFiles.includes(changedFile)) {
    fail(`Changed an important file: ${changedFile}`)
  }
}
