# fotos_by_folders
Sort photos by creation date in particular folder on Yandex Disk.
Yandex Disk connected as Disk Z in Windows via WebDav: https://yandex.ru/support/disk/webdav.html

Script creates new folders for each year and month.

First, it tries to extract date from filename. 
If no success, get creation date from file properties (maybe I should take it from properties only, hz)
