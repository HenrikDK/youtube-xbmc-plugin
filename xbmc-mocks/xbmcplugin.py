SORT_METHOD_ALBUM = int
SORT_METHOD_ALBUM_IGNORE_THE = int
SORT_METHOD_ARTIST = int
SORT_METHOD_ARTIST_IGNORE_THE = int
SORT_METHOD_BITRATE = int
SORT_METHOD_DATE = int
SORT_METHOD_DRIVE_TYPE = int
SORT_METHOD_DURATION = int
SORT_METHOD_EPISODE = int
SORT_METHOD_FILE = int
SORT_METHOD_GENRE = int
SORT_METHOD_LABEL = int
SORT_METHOD_LABEL_IGNORE_THE = int
SORT_METHOD_LISTENERS = int
SORT_METHOD_MPAA_RATING = int
SORT_METHOD_NONE = int
SORT_METHOD_PLAYLIST_ORDER = int
SORT_METHOD_PRODUCTIONCODE = int
SORT_METHOD_PROGRAM_COUNT = int
SORT_METHOD_SIZE = int
SORT_METHOD_SONG_RATING = int
SORT_METHOD_STUDIO = int
SORT_METHOD_STUDIO_IGNORE_THE = int
SORT_METHOD_TITLE = int
SORT_METHOD_TITLE_IGNORE_THE = int
SORT_METHOD_TRACKNUM = int
SORT_METHOD_UNSORTED = int
SORT_METHOD_VIDEO_RATING = int
SORT_METHOD_VIDEO_RUNTIME = int
SORT_METHOD_VIDEO_TITLE = int
SORT_METHOD_VIDEO_YEAR = int
__author__ = str
__credits__ = str
__date__ = str
__platform__ = str
__version__ = str
def addDirectoryItem(*args):
    """addDirectoryItem(handle, url, listitem [,isFolder, totalItems]) -- Callback function to pass directory contents back to XBMC.
     - Returns a bool for successful completion.
    
    handle      : integer - handle the plugin was started with.
    url         : string - url of the entry. would be plugin:// for another virtual directory
    listitem    : ListItem - item to add.
    isFolder    : [opt] bool - True=folder / False=not a folder(default).
    totalItems  : [opt] integer - total number of items that will be passed.(used for progressbar)
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - if not xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'F:\\Trailers\\300.mov', listitem, totalItems=50): break
    """

def addDirectoryItems(*args):
    """addDirectoryItems(handle, items [,totalItems]) -- Callback function to pass directory contents back to XBMC as a list.
     - Returns a bool for successful completion.
    
    handle      : integer - handle the plugin was started with.
    items       : List - list of (url, listitem[, isFolder]) as a tuple to add.
    totalItems  : [opt] integer - total number of items that will be passed.(used for progressbar)
    
    *Note, You can use the above as keywords for arguments.
    
           Large lists benefit over using the standard addDirectoryItem()
           You may call this more than once to add items in chunks
    
    example:
      - if not xbmcplugin.addDirectoryItems(int(sys.argv[1]), [(url, listitem, False,)]: raise
    """

def addSortMethod(*args):
    """addSortMethod(handle, sortMethod, label2) -- Adds a sorting method for the media list.
    
    handle      : integer - handle the plugin was started with.
    sortMethod  : integer - number for sortmethod see FileItem.h.
    label2Mask  : [opt] string - the label mask to use for the second label.  Defaults to '%D'
                  applies to: SORT_METHOD_NONE, SORT_METHOD_UNSORTED, SORT_METHOD_VIDEO_TITLE,
                              SORT_METHOD_TRACKNUM, SORT_METHOD_FILE, SORT_METHOD_TITLE
                              SORT_METHOD_TITLE_IGNORE_THE, SORT_METHOD_LABEL
                              SORT_METHOD_LABEL_IGNORE_THE
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
    """

def endOfDirectory(*args):
    """endOfDirectory(handle[, succeeded, updateListing, cacheToDisc]) -- Callback function to tell XBMC that the end of the directory listing in a virtualPythonFolder module is reached.
    
    handle           : integer - handle the plugin was started with.
    succeeded        : [opt] bool - True=script completed successfully(Default)/False=Script did not.
    updateListing    : [opt] bool - True=this folder should update the current listing/False=Folder is a subfolder(Default).
    cacheToDisc      : [opt] bool - True=Folder will cache if extended time(default)/False=this folder will never cache to disc.
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    """

def getSetting(*args):
    """getSetting(handle, id) -- Returns the value of a setting as a string.
    
    handle    : integer - handle the plugin was started with.
    id        : string - id of the setting that the module needs to access.
    
    *Note, You can use the above as a keyword.
    
    example:
      - apikey = xbmcplugin.getSetting(int(sys.argv[1]), 'apikey')
    """

def setContent(*args):
    """setContent(handle, content) -- Sets the plugins content.
    
    handle      : integer - handle the plugin was started with.
    content     : string - content type (eg. movies)
    
    *Note, You can use the above as keywords for arguments.
           content: files, songs, artists, albums, movies, tvshows, episodes, musicvideos
    
    example:
      - xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    """

def setPluginCategory(*args):
    """setPluginCategory(handle, category) -- Sets the plugins name for skins to display.
    
    handle      : integer - handle the plugin was started with.
    category    : string or unicode - plugins sub category.
    
    *Note, You can use the above as keywords for arguments.
    
    example:
      - xbmcplugin.setPluginCategory(int(sys.argv[1]), 'Comedy')
    """

def setPluginFanart(*args):
    """setPluginFanart(handle, image, color1, color2, color3) -- Sets the plugins fanart and color for skins to display.
    
    handle      : integer - handle the plugin was started with.
    image       : [opt] string - path to fanart image.
    color1      : [opt] hexstring - color1. (e.g. '0xFFFFFFFF')
    color2      : [opt] hexstring - color2. (e.g. '0xFFFF3300')
    color3      : [opt] hexstring - color3. (e.g. '0xFF000000')
    
    *Note, You can use the above as keywords for arguments.
    
    example:
      - xbmcplugin.setPluginFanart(int(sys.argv[1]), 'special://home/addons/plugins/video/Apple movie trailers II/fanart.png', color2='0xFFFF3300')
    """

def setProperty(*args):
    """setProperty(handle, key, value) -- Sets a container property for this plugin.
    
    handle      : integer - handle the plugin was started with.
    key         : string - property name.
    value       : string or unicode - value of property.
    
    *Note, Key is NOT case sensitive.
           You can use the above as keywords for arguments.
    
    example:
      - xbmcplugin.setProperty(int(sys.argv[1]), 'Emulator', 'M.A.M.E.')
    """

def setResolvedUrl(*args):
    """setResolvedUrl(handle, succeeded, listitem) -- Callback function to tell XBMC that the file plugin has been resolved to a url
    
    handle           : integer - handle the plugin was started with.
    succeeded        : bool - True=script completed successfully/False=Script did not.
    listitem         : ListItem - item the file plugin resolved to for playback.
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
    """

def setSetting(*args):
    """setSetting(handle, id, value) -- Sets a plugin setting for the current running plugin.
    
    handle    : integer - handle the plugin was started with.
    id        : string - id of the setting that the module needs to access.
    value     : string or unicode - value of the setting.
    
    *Note, You can use the above as keywords for arguments.
    
    example:
      - xbmcplugin.setSetting(int(sys.argv[1]), id='username', value='teamxbmc')
    """

