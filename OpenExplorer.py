import subprocess
import os
def explorer_on_file(url):
    """ opens a windows explorer window """
    subprocess.Popen(f'explorer /select,"{url}"')

file_name = '2B21167600_Дон Кихот_20240203.mov'
file_path = r"\\?\V:\DATA\2\B\2\2B21167600_Дон Кихот_20240203.mov"
# file_path = r"V:/DATA/2/B/2/2B21167600_Дон Кихот_20240203.mov"
# file_path = r"\\big1\VIDEO\DATA\2\B\2\2B21167600_Дон Кихот_20240203.mov"
# file_path = r'C:\adb\adb.exe'

explorer_on_file(file_path)

print(os.listdir(r'V:\DATA\2\B'))