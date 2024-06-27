import subprocess
import os
def explorer_on_file(url):
    """ opens a windows explorer window """
    subprocess.Popen(r'explorer /select,"{url}"')


FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.Popen([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.Popen([FILEBROWSER_PATH, '/select,', path])


# file_name = '2B21167600_Дон Кихот_20240203.mov'
file_path = r"V:\DATA\2\B\2\2B21167600_Дон_Кихот_20240203.mov"
# file_path = r"V:/DATA/2/B/2/2B21167600_Дон Кихот_20240203.mov"
# file_path = r"\\big1\VIDEO\DATA\2\B\2\2B21167600_Дон Кихот_20240203.mov"
# file_path = r'C:\adb\adb.exe'

explorer_on_file(file_path)

# print(os.listdir(r'V:\DATA\2\B'))


# os.startfile(file_path, 'find')

# explore(file_path)