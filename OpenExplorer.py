import subprocess
import os
def explorer_on_file(url):
    """ opens a Windows explorer window """
    subprocess.Popen(fr'explorer /select,"{url}"')


# FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

# def explore(path):
#     # explorer would choke on forward slashes
#     path = os.path.normpath(path)
#
#     if os.path.isdir(path):
#         subprocess.Popen([FILEBROWSER_PATH, path])
#     elif os.path.isfile(path):
#         subprocess.Popen([FILEBROWSER_PATH, '/select,', path])


# file_name = '2B21167600_Дон Кихот_20240203.mov'
file_path = r"V:\DATA\2\B\1\1B20172800-Сильвия-20140404.mp4"
# file_path = r"V:/DATA/2/B/2/2B21167600_Дон Кихот_20240203.mov"
# file_path = r"\\big1\VIDEO\DATA\2\B\2\2B21167600_Дон Кихот_20240203.mov"
# file_path = r'C:\adb\adb.exe'

# explorer_on_file(file_path)

print(os.listdir(r'V:\DATA\2\B\1'))


# os.startfile(file_path, 'find')

# explore(file_path)