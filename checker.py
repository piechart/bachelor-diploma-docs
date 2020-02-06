import os
import sys

README_FILENAME = 'readme.md'
FILES_DIR = 'files'
VALID_ROOT_CONTENT = (README_FILENAME, '.github', FILES_DIR, '.git', 'checker.py', 'contribute.md')

def fail(message):
    sys.exit('(!!) {0}'.format(message))

def log_important(message):
    print('>>> {0}'.format(message))

def filter_files(filenames):
    visible_files = filter(lambda item: not item.startswith('.'), filenames)
    # filenames = map(lambda item: item.split('.')[0], visible_files)
    return list(visible_files)

def check_readme_exists():
    log_important('Checking readme exists')
    if not os.path.isfile(README_FILENAME):
        fail('readme.md not found')

def check_files_dir_exists():
    log_important('Checking files dir exists')
    if not os.path.isdir(FILES_DIR):
        fail('files directory not found')

def check_all_files_mentioned_in_readme():
    log_important('Checking all_files_mentioned_in_readme')
    content_files = filter_files(os.listdir(FILES_DIR))
    readme_content = open(README_FILENAME).read()

    if content_files:
        for content_file in content_files:
            print('Checking file {0}'.format(content_file))

            if not content_file in readme_content:
                fail('File {0} not found in readme.md'.format(content_file))

            # if not content_file.endswith('pdf'):
            #     fail('File {0} has incorrect format. PDF is expected'.format(content_file))
    else:
        print('No files to check')

def check_correct_files_location():
    log_important('Checking correct_files_location')
    root_content = os.listdir()
    print('Root content:\n{0}'.format(root_content))

    root_content_as_set = set(root_content)
    valid_set = set(VALID_ROOT_CONTENT)

    if valid_set != root_content_as_set:
        invalid_objects = list(root_content_as_set - valid_set) if len(root_content_as_set) > len(valid_set) else list(valid_set - root_content_as_set)
        for invalid_object in invalid_objects:
            print('Found invalid file location: {0}'.format(invalid_object))
            print('All files must be placed in `files` directory')
        fail('Found files with invalid locations')

check_readme_exists()
check_files_dir_exists()
check_all_files_mentioned_in_readme()
check_correct_files_location()
