def copy(*args):
    """copy(source, destination) -- copy file to destination, returns true/false.
    
    source          : file to copy.
    destination     : destination file
    example:
      success = xbmcvfs.copy(source, destination)
    """

def delete(*args):
    """delete(file)
    
    file        : file to delete
    example:
      xbmcvfs.delete(file)
    """

def exists(*args):
    """exists(path)
    
    path        : file or folder
    example:
      success = xbmcvfs.exists(path)
    """

def rename(*args):
    """rename(file, newFileName)
    
    file        : file to reanamenewFileName : new filename, including the full path
    example:
      success = xbmcvfs.rename(file,newFileName)
    """

