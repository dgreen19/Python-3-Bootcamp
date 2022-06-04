import zipfile
import os

file_path = 'your/file_path/goes/here'

os.chdir(os.path.dirname(file_path))
with zipfile.ZipFile(file_path + '.zip',
                     "w",
                     zipfile.ZIP_DEFLATED,
                     allowZip64=True) as zf:
    for root, _, filenames in os.walk(os.path.basename(file_path)):
        for name in filenames:
            name = os.path.join(root, name)
            name = os.path.normpath(name)
            zf.write(name, name)