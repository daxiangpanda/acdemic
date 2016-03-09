#!/usr/bin/env python
# encoding: utf-8
import os
import win32file
import win32con
import simhash
ACTIONS = {
  1: u"新建文件",
  2: u"删除文件",
  3: u"更新文件",
  4: u"从某个文件名改为",
  5: u"改成某个文件名"
}
# Thanks to Claudio Grondi for the correct set of numbers
FILE_LIST_DIRECTORY = 0x0001
path_to_watch = r'E:\learn'
hDir = win32file.CreateFile (
  path_to_watch,
  FILE_LIST_DIRECTORY,
  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
  None,
  win32con.OPEN_EXISTING,
  win32con.FILE_FLAG_BACKUP_SEMANTICS,
  None
)
while 1:
  #
  # ReadDirectoryChangesW takes a previously-created
  #  handle to a directory, a buffer size for results,
  #  a flag to indicate whether to watch subtrees and
  #  a filter of what changes to notify.
  #
  # NB Tim Juchcinski reports that he needed to up
  #  the buffer size to be sure of picking up all
  #  events when a large number of files were
  #  deleted at once.
  #
  results = win32file.ReadDirectoryChangesW (
    hDir,
    1024,
    True,
    win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
     win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
     win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
     win32con.FILE_NOTIFY_CHANGE_SIZE |
     win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
     win32con.FILE_NOTIFY_CHANGE_SECURITY,
    None,
    None
  )
  print results
  if results[0][0] == 1:
    pass
  for action, file in results:
    full_filename = unicode(os.path.join(path_to_watch,file))
    print ACTIONS.get(action, "Unknown")
    if action == 1:
      with open(full_filename,'r') as f:
        content = f.read()
      print u'新建文件的simhash值为'+str(simhash.simhash(content))