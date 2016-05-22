import os


def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating project directory' + directory)
        os.makedirs(directory)



#queue

def create_datafiles(project_name, url):
