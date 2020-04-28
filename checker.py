import hashlib
import os
import sys
import re
from itertools import chain

README_FILENAME = 'readme.md'
FILES_DIR = 'files'
VALID_ROOT_CONTENT = (
    README_FILENAME,
    FILES_DIR,
    '.github',
    '.git',
    'checker.py',
    'contribute.md'
)
SPACE_CHAR = ' '
SPACE_FAIL_STR = 'Files must not have spaces in their names. Found space in `{0}`'
LIST_ITEM_PREFIX = '- '
README_FILENAME_EXAMPLE = 'filename.pdf'


def fail(message):
    text = '(!!) **{0}**'.format(message)
    print(text)
    sys.exit(1)


def log_important(message):
    print('> {0}'.format(message))


def filter_files(filenames):
    visible_files = filter(lambda item: not item.startswith('.'), filenames)
    return list(visible_files)


def md5(fname):
    """Calculates md5 hash for a given file"""
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicates(ini_dict):
    """Finds duplicates items in dict and returns filenames set."""
    rev_dict = {}
    for key, value in ini_dict.items():
        rev_dict.setdefault(value, set()).add(key)

    result = set(chain.from_iterable(
        values for key, values in rev_dict.items()
        if len(values) > 1))
    return result


def check_readme_exists():
    log_important('Checking readme exists')
    if not os.path.isfile(README_FILENAME):
        fail('`{0}` not found'.format(README_FILENAME))


def check_files_dir_exists():
    log_important('Checking files dir exists')
    if not os.path.isdir(FILES_DIR):
        fail('`{0}` directory not found'.format(FILES_DIR))


def check_all_files_mentioned_in_readme():
    log_important('Checking all_files_mentioned_in_readme')
    content_files = filter_files(os.listdir(FILES_DIR))
    readme_content = open(README_FILENAME).read()

    if content_files:
        for content_file in content_files:
            if README_FILENAME_EXAMPLE in content_file:
                continue
            if not content_file in readme_content:
                fail('File `{0}` not found in `{1}`'.format(content_file, README_FILENAME))
    else:
        print('No files to check')

    readme_files = re.findall('\(files/(.*?)\)\n', readme_content)
    for readme_file in readme_files:
        if README_FILENAME_EXAMPLE in readme_file:
            continue
        if not readme_file in content_files:
            fail('File `{0}` mentioned in `{1}` but not found in `{2}` directory. Please upload it'.format(
                readme_file,
                README_FILENAME,
                FILES_DIR,
            ))


def check_correct_files_location():
    log_important('Checking correct_files_location')
    root_content = os.listdir()

    root_content_as_set = set(root_content)
    valid_set = set(VALID_ROOT_CONTENT)

    if valid_set != root_content_as_set:
        invalid_objects = list(root_content_as_set - valid_set) \
            if len(root_content_as_set) > len(valid_set) \
            else list(valid_set - root_content_as_set)
        for invalid_object in invalid_objects:
            print('Found invalid file location: `{0}`'.format(invalid_object))
            print('All files must be placed in `{0}` directory'.format(FILES_DIR))
        fail('Found files with invalid locations')


def check_correct_filenames():
    log_important('Checking correct_filenames')
    content_files = filter_files(os.listdir(FILES_DIR))

    if content_files:
        for file_name in content_files:
            if SPACE_CHAR in file_name:
                fail(SPACE_FAIL_STR.format(file_name))
    else:
        print('No files to check')


def check_duplicate_files():
    log_important('Checking duplicate_files')
    content_files = filter_files(os.listdir(FILES_DIR))
    hash_dict = {}
    for filename in content_files:
        hash_dict[filename] = md5(os.path.join(FILES_DIR, filename))

    duplicates = find_duplicates(hash_dict)
    if duplicates:
        fail('Found duplicates:\n> ' + '\n> '.join(duplicates))


def check_references_dont_have_newlines_and_have_list_marker():
    log_important('Checking references_dont_have_newlines_and_have_list_marker')
    readme_content = open(README_FILENAME).read()
    lines = readme_content.split('\n')
    file_marker = '{0}/'.format(FILES_DIR)
    file_refs = list(filter(lambda item: file_marker in item, lines))
    invalid_refs = list(filter(lambda item: not item.startswith(LIST_ITEM_PREFIX), file_refs))
    if invalid_refs:
        fail('Invalid markdown references found. File reference name must have one line and must have list marker ("- ") at its beginning. Invalid refs:\n> ' + '\n> '.join(invalid_refs))


check_readme_exists()
check_files_dir_exists()
check_all_files_mentioned_in_readme()
check_correct_files_location()
check_correct_filenames()
check_duplicate_files()
check_references_dont_have_newlines_and_have_list_marker()
