import os
import sys
import re

README_FILENAME = 'readme.md'
FILES_DIR = 'files'
VALID_ROOT_CONTENT = (README_FILENAME, '.github', FILES_DIR, '.git', 'checker.py', 'contribute.md')
SPACE_CHAR = ' '

def fail(message):
    sys.exit('(!!) {0}'.format(message))

def log_important(message):
    print('>>> {0}'.format(message))

def filter_files(filenames):
    visible_files = filter(lambda item: not item.startswith('.'), filenames)
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
    else:
        print('No files to check')

    readme_files = re.findall('\(files/(.*?)\)', readme_content)
    for readme_file in readme_files:
        if not readme_file in content_files:
            fail('File {0} mentioned in readme.md but not found in `{1}` directory. Please upload it'.format(readme_file, FILES_DIR))

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
            print('All files must be placed in `{0}` directory'.format(FILES_DIR))
        fail('Found files with invalid locations')

def check_correct_filenames():
    log_important('Checking correct_filenames')
    content_files = filter_files(os.listdir(FILES_DIR))

    if content_files:
        for file_name in content_files:
            if SPACE_CHAR in file_name:
                fail('Files must not have spaces in their names. Found space in {0}'.format(file_name))
    else:
        print('No files to check')

check_readme_exists()
check_files_dir_exists()
check_all_files_mentioned_in_readme()
check_correct_files_location()
check_correct_filenames()
