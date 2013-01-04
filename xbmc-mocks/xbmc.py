DRIVE_NOT_READY = int
class InfoTagMusic:
    """InfoTagMusic class.
    
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def getAlbum(*args):
        """getAlbum() -- returns a string.
        """

    def getAlbumArtist(*args):
        """getAlbumArtist() -- returns a string.
        """

    def getArtist(*args):
        """getArtist() -- returns a string.
        """

    def getComment(*args):
        """getComment() -- returns a string.
        """

    def getDisc(*args):
        """getDisc() -- returns an integer.
        """

    def getDuration(*args):
        """getDuration() -- returns an integer.
        """

    def getGenre(*args):
        """getAlbum() -- returns a string.
        """

    def getLastPlayed(*args):
        """getLastPlayed() -- returns a string.
        """

    def getListeners(*args):
        """getListeners() -- returns an integer.
        """

    def getLyrics(*args):
        """getLyrics() -- returns a string.
        """

    def getPlayCount(*args):
        """getPlayCount() -- returns an integer.
        """

    def getReleaseDate(*args):
        """getReleaseDate() -- returns a string.
        """

    def getTitle(*args):
        """getTitle() -- returns a string.
        """

    def getTrack(*args):
        """getTrack() -- returns an integer.
        """

    def getTrackAndDisc(*args):
        """getTrackAndDisc() -- returns an integer.
        """

    def getURL(*args):
        """getURL() -- returns a string.
        """



class InfoTagVideo:
    """InfoTagVideo class.
    
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def getCast(*args):
        """getCast() -- returns a string.
        """

    def getDirector(*args):
        """getDirector() -- returns a string.
        """

    def getFile(*args):
        """getFile() -- returns a string.
        """

    def getFirstAired(*args):
        """getFirstAired() -- returns a string.
        """

    def getGenre(*args):
        """getGenre() -- returns a string.
        """

    def getIMDBNumber(*args):
        """getIMDBNumber() -- returns a string.
        """

    def getLastPlayed(*args):
        """getLastPlayed() -- returns a string.
        """

    def getOriginalTitle(*args):
        """getOriginalTitle() -- returns a string.
        """

    def getPath(*args):
        """getPath() -- returns a string.
        """

    def getPictureURL(*args):
        """getPictureURL() -- returns a string.
        """

    def getPlayCount(*args):
        """getPlayCount() -- returns a integer.
        """

    def getPlot(*args):
        """getPlot() -- returns a string.
        """

    def getPlotOutline(*args):
        """getPlotOutline() -- returns a string.
        """

    def getPremiered(*args):
        """getPremiered() -- returns a string.
        """

    def getRating(*args):
        """getRating() -- returns a float.
        """

    def getTagLine(*args):
        """getTagLine() -- returns a string.
        """

    def getTitle(*args):
        """getTitle() -- returns a string.
        """

    def getVotes(*args):
        """getVotes() -- returns a string.
        """

    def getWritingCredits(*args):
        """getWritingCredits() -- returns a string.
        """

    def getYear(*args):
        """getYear() -- returns a integer.
        """



class Keyboard:
    """Keyboard class.
    
    Keyboard([default, heading, hidden]) -- Creates a new Keyboard object with default text
                                    heading and hidden input flag if supplied.
    
    default        : [opt] string - default text entry.
    heading        : [opt] string - keyboard heading.
    hidden         : [opt] boolean - True for hidden text entry.
    
    example:
      - kb = xbmc.Keyboard('default', 'heading', True)
      - kb.setDefault('password') # optional
      - kb.setHeading('Enter password') # optional
      - kb.setHiddenInput(True) # optional
      - kb.doModal()
      - if (kb.isConfirmed()):
      -   text = kb.getText()
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def doModal(*args):
        """doModal([autoclose]) -- Show keyboard and wait for user action.
        
        autoclose      : [opt] integer - milliseconds to autoclose dialog. (default=do not autoclose)
        
        example:
          - kb.doModal(30000)
        """

    def getText(*args):
        """getText() -- Returns the user input as a string.
        
        *Note, This will always return the text entry even if you cancel the keyboard.
               Use the isConfirmed() method to check if user cancelled the keyboard.
        
        example:
          - text = kb.getText()
        """

    def isConfirmed(*args):
        """isConfirmed() -- Returns False if the user cancelled the input.
        
        example:
          - if (kb.isConfirmed()):
        """

    def setDefault(*args):
        """setDefault(default) -- Set the default text entry.
        
        default        : string - default text entry.
        
        example:
          - kb.setDefault('password')
        """

    def setHeading(*args):
        """setHeading(heading) -- Set the keyboard heading.
        
        heading        : string - keyboard heading.
        
        example:
          - kb.setHeading('Enter password')
        """

    def setHiddenInput(*args):
        """setHiddenInput(hidden) -- Allows hidden text entry.
        
        hidden        : boolean - True for hidden text entry.
        example:
          - kb.setHiddenInput(True)
        """



LOGDEBUG = int
LOGERROR = int
LOGFATAL = int
LOGINFO = int
LOGNONE = int
LOGNOTICE = int
LOGSEVERE = int
LOGWARNING = int
PLAYER_CORE_AUTO = int
PLAYER_CORE_DVDPLAYER = int
PLAYER_CORE_MPLAYER = int
PLAYER_CORE_PAPLAYER = int
PLAYLIST_MUSIC = int
PLAYLIST_VIDEO = int
class PlayList:
    """PlayList class.
    
    PlayList(int playlist) -- retrieve a reference from a valid xbmc playlist
    
    int playlist can be one of the next values:
    
      0 : xbmc.PLAYLIST_MUSIC
      1 : xbmc.PLAYLIST_VIDEO
    
    Use PlayList[int position] or __getitem__(int position) to get a PlayListItem.
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __getitem__(*args):
        """x.__getitem__(y) <==> x[y]
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __len__(*args):
        """x.__len__() <==> len(x)
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def add(*args):
        """add(url[, listitem, index]) -- Adds a new file to the playlist.
        
        url            : string or unicode - filename or url to add.
        listitem       : [opt] listitem - used with setInfo() to set different infolabels.
        index          : [opt] integer - position to add playlist item. (default=end)
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
          - video = 'F:\\movies\\Ironman.mov'
          - listitem = xbmcgui.ListItem('Ironman', thumbnailImage='F:\\movies\\Ironman.tbn')
          - listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
          - playlist.add(url=video, listitem=listitem, index=7)
        """

    def clear(*args):
        """clear() -- clear all items in the playlist.
        """

    def getposition(*args):
        """getposition() -- returns the position of the current song in this playlist.
        """

    def load(*args):
        """load(filename) -- Load a playlist.
        
        clear current playlist and copy items from the file to this Playlist
        filename can be like .pls or .m3u ...
        returns False if unable to load playlist, True otherwise.
        """

    def remove(*args):
        """remove(filename) -- remove an item with this filename from the playlist.
        """

    def shuffle(*args):
        """shuffle() -- shuffle the playlist.
        """

    def size(*args):
        """size() -- returns the total number of PlayListItems in this playlist.
        """

    def unshuffle(*args):
        """unshuffle() -- unshuffle the playlist.
        """



class PlayListItem:
    """PlayListItem class.
    
    PlayListItem() -- Creates a new PlaylistItem which can be added to a PlayList.
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def getdescription(*args):
        """getdescription() -- Returns the description of this PlayListItem.
        """

    def getduration(*args):
        """getduration() -- Returns the duration of this PlayListItem.
        """

    def getfilename(*args):
        """getfilename() -- Returns the filename of this PlayListItem.
        """



class Player:
    """Player class.
    
    Player([core]) -- Creates a new Player with as default the xbmc music playlist.
    
    core     : (optional) Use a specified playcore instead of letting xbmc decide the playercore to use.
             : - xbmc.PLAYER_CORE_AUTO
             : - xbmc.PLAYER_CORE_DVDPLAYER
             : - xbmc.PLAYER_CORE_MPLAYER
             : - xbmc.PLAYER_CORE_PAPLAYER
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __format__(*args):
        """default object formatter
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __new__(*args):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T
        """

    def __reduce__(*args):
        """helper for pickle
        """

    def __reduce_ex__(*args):
        """helper for pickle
        """

    def __repr__(*args):
        """x.__repr__() <==> repr(x)
        """

    def __setattr__(*args):
        """x.__setattr__('name', value) <==> x.name = value
        """

    def __sizeof__(*args):
        """__sizeof__() -> size of object in memory, in bytes
        """

    def __str__(*args):
        """x.__str__() <==> str(x)
        """

    def __subclasshook__(*args):
        """Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """

    def disableSubtitles(*args):
        """DisableSubtitles() -- disable subtitles
        """

    def getAvailableAudioStreams(*args):
        """getAvailableAudioStreams() -- get Audio stream names
        """

    def getMusicInfoTag(*args):
        """getMusicInfoTag() -- returns the MusicInfoTag of the current playing 'Song'.
        
        Throws: Exception, if player is not playing a file or current file is not a music file.
        """

    def getPlayingFile(*args):
        """getPlayingFile() -- returns the current playing file as a string.
        
        Throws: Exception, if player is not playing a file.
        """

    def getSubtitles(*args):
        """getSubtitles() -- get subtitle stream name
        """

    def getTime(*args):
        """getTime() -- Returns the current time of the current playing media as fractional seconds.
        
        Throws: Exception, if player is not playing a file.
        """

    def getTotalTime(*args):
        """getTotalTime() -- Returns the total time of the current playing media in
                          seconds.  This is only accurate to the full second.
        
        Throws: Exception, if player is not playing a file.
        """

    def getVideoInfoTag(*args):
        """getVideoInfoTag() -- returns the VideoInfoTag of the current playing Movie.
        
        Throws: Exception, if player is not playing a file or current file is not a movie file.
        
        Note, this doesn't work yet, it's not tested
        """

    def isPlaying(*args):
        """isPlaying() -- returns True is xbmc is playing a file.
        """

    def isPlayingAudio(*args):
        """isPlayingAudio() -- returns True is xbmc is playing an audio file.
        """

    def isPlayingVideo(*args):
        """isPlayingVideo() -- returns True if xbmc is playing a video.
        """

    def onPlayBackEnded(*args):
        """onPlayBackEnded() -- onPlayBackEnded method.
        
        Will be called when xbmc stops playing a file
        """

    def onPlayBackPaused(*args):
        """onPlayBackPaused() -- onPlayBackPaused method.
        
        Will be called when user pauses a playing file
        """

    def onPlayBackResumed(*args):
        """onPlayBackResumed() -- onPlayBackResumed method.
        
        Will be called when user resumes a paused file
        """

    def onPlayBackStarted(*args):
        """onPlayBackStarted() -- onPlayBackStarted method.
        
        Will be called when xbmc starts playing a file
        """

    def onPlayBackStopped(*args):
        """onPlayBackStopped() -- onPlayBackStopped method.
        
        Will be called when user stops xbmc playing a file
        """

    def pause(*args):
        """pause() -- Pause playing.
        """

    def play(*args):
        """play([item, listitem, windowed]) -- Play this item.
        
        item           : [opt] string - filename, url or playlist.
        listitem       : [opt] listitem - used with setInfo() to set different infolabels.
        windowed       : [opt] bool - true=play video windowed, false=play users preference.(default)
        
        *Note, If item is not given then the Player will try to play the current item
               in the current playlist.
        
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - listitem = xbmcgui.ListItem('Ironman')
          - listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
          - xbmc.Player( xbmc.PLAYER_CORE_MPLAYER ).play(url, listitem, windowed)
        """

    def playnext(*args):
        """playnext() -- Play next item in playlist.
        """

    def playprevious(*args):
        """playprevious() -- Play previous item in playlist.
        """

    def playselected(*args):
        """playselected() -- Play a certain item from the current playlist.
        """

    def seekTime(*args):
        """seekTime() -- Seeks the specified amount of time as fractional seconds.
                      The time specified is relative to the beginning of the
                      currently playing media file.
        
        Throws: Exception, if player is not playing a file.
        """

    def setAudioStream(*args):
        """setAudioStream(stream) -- set Audio Stream 
        
        stream           : int
        
        example:
          - setAudioStream(1)
        """

    def setSubtitles(*args):
        """setSubtitles(path) -- set subtitle file and enable subtitles
        
        path           : string or unicode - Path to subtitle
        
        example:
          - setSubtitles('/path/to/subtitle/test.srt')
        """

    def stop(*args):
        """stop() -- Stop playing.
        """



TRAY_CLOSED_MEDIA_PRESENT = int
TRAY_CLOSED_NO_MEDIA = int
TRAY_OPEN = int
__author__ = str
__credits__ = str
__date__ = str
__platform__ = str
__version__ = str
abortRequested = bool
def dashboard(*args):
    """dashboard() -- Boot to dashboard as set in My Pograms/General.
    
    example:
      - xbmc.dashboard()
    """

def enableNavSounds(*args):
    """enableNavSounds(yesNo) -- Enables/Disables nav sounds
    
    yesNo          : integer - enable (True) or disable (False) nav sounds
    
    example:
      - xbmc.enableNavSounds(True)
    """

def executeJSONRPC(*args):
    """executeJSONRPC(jsonrpccommand) -- Execute an JSONRPC command.
    
    jsonrpccommand    : string - jsonrpc command to execute.
    
    List of commands - 
    
    example:
      - response = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "JSONRPC.Introspect", "id": 1 }')
    """

def executebuiltin(*args):
    """executebuiltin(function) -- Execute a built in XBMC function.
    
    function       : string - builtin function to execute.
    
    List of functions - http://wiki.xbmc.org/?title=List_of_Built_In_Functions 
    
    NOTE: This function is executed asynchronously, so do not rely on it being done immediately
    
    example:
      - xbmc.executebuiltin('XBMC.RunXBE(c:\\avalaunch.xbe)')
    """

def executehttpapi(*args):
    """executehttpapi(httpcommand) -- Execute an HTTP API command.
    
    httpcommand    : string - http command to execute.
    
    List of commands - http://wiki.xbmc.org/?title=WebServerHTTP-API#The_Commands 
    
    example:
      - response = xbmc.executehttpapi('TakeScreenShot(special://temp/test.jpg,0,false,200,-1,90)')
    """

def executescript(*args):
    """executescript(script) -- Execute a python script.
    
    script         : string - script filename to execute.
    
    example:
      - xbmc.executescript('special://home/scripts/update.py')
    """

def getCacheThumbName(*args):
    """getCacheThumbName(path) -- Returns a thumb cache filename.
    
    path           : string or unicode - path to file
    
    example:
      - thumb = xbmc.getCacheThumbName('f:\\videos\\movie.avi')
    """

def getCleanMovieTitle(*args):
    """getCleanMovieTitle(path[, usefoldername]) -- Returns a clean movie title and year string if available.
    
    path           : string or unicode - String to clean
    bool           : [opt] bool - use folder names (defaults to false)
    
    example:
      - title, year = xbmc.getCleanMovieTitle('/path/to/moviefolder/test.avi', True)
    """

def getCondVisibility(*args):
    """getCondVisibility(condition) -- Returns True (1) or False (0) as a bool.
    
    condition      : string - condition to check.
    
    List of Conditions - http://wiki.xbmc.org/?title=List_of_Boolean_Conditions 
    
    *Note, You can combine two (or more) of the above settings by using "+" as an AND operator,
    "|" as an OR operator, "!" as a NOT operator, and "[" and "]" to bracket expressions.
    
    example:
      - visible = xbmc.getCondVisibility('[Control.IsVisible(41) + !Control.IsVisible(12)]')
    """

def getDVDState(*args):
    """getDVDState() -- Returns the dvd state as an integer.
    
    return values are:
       1 : xbmc.DRIVE_NOT_READY
      16 : xbmc.TRAY_OPEN
      64 : xbmc.TRAY_CLOSED_NO_MEDIA
      96 : xbmc.TRAY_CLOSED_MEDIA_PRESENT
    
    example:
      - dvdstate = xbmc.getDVDState()
    """

def getFreeMem(*args):
    """getFreeMem() -- Returns the amount of free memory in MB as an integer.
    
    example:
      - freemem = xbmc.getFreeMem()
    """

def getGlobalIdleTime(*args):
    """getGlobalIdleTime() -- Returns the elapsed idle time in seconds as an integer.
    
    example:
      - t = xbmc.getGlobalIdleTime()
    """

def getIPAddress(*args):
    """getIPAddress() -- Returns the current ip address as a string.
    
    example:
      - ip = xbmc.getIPAddress()
    """

def getInfoImage(*args):
    """getInfoImage(infotag) -- Returns a filename including path to the InfoImage's
                             thumbnail as a string.
    
    infotag        : string - infotag for value you want returned.
    
    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels 
    
    example:
      - filename = xbmc.getInfoImage('Weather.Conditions')
    """

def getInfoLabel(*args):
    """getInfoLabel(infotag) -- Returns an InfoLabel as a string.
    
    infotag        : string - infoTag for value you want returned.
    
    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels 
    
    example:
      - label = xbmc.getInfoLabel('Weather.Conditions')
    """

def getLanguage(*args):
    """getLanguage() -- Returns the active language as a string.
    
    example:
      - language = xbmc.getLanguage()
    """

def getLocalizedString(*args):
    """getLocalizedString(id) -- Returns a localized 'unicode string'.
    
    id             : integer - id# for string you want to localize.
    
    *Note, See strings.xml in \language\{yourlanguage}\ for which id
           you need for a string.
    
    example:
      - locstr = xbmc.getLocalizedString(6)
    """

def getRegion(*args):
    """getRegion(id) -- Returns your regions setting as a string for the specified id.
    
    id             : string - id of setting to return
    
    *Note, choices are (dateshort, datelong, time, meridiem, tempunit, speedunit)
    
           You can use the above as keywords for arguments.
    
    example:
      - date_long_format = xbmc.getRegion('datelong')
    """

def getSkinDir(*args):
    """getSkinDir() -- Returns the active skin directory as a string.
    
    *Note, This is not the full path like 'special://home/addons/MediaCenter', but only 'MediaCenter'.
    
    example:
      - skindir = xbmc.getSkinDir()
    """

def getSupportedMedia(*args):
    """getSupportedMedia(media) -- Returns the supported file types for the specific media as a string.
    
    media          : string - media type
    
    *Note, media type can be (video, music, picture).
    
           The return value is a pipe separated string of filetypes (eg. '.mov|.avi').
    
           You can use the above as keywords for arguments.
    
    example:
      - mTypes = xbmc.getSupportedMedia('video')
    """

def log(*args):
    """log(msg[, level]) -- Write a string to XBMC's log file.
    
    msg            : string - text to output.
    level          : [opt] integer - log level to ouput at. (default=LOGNOTICE)
    
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
           Text is written to the log for the following conditions.
             XBMC loglevel == -1 (NONE, nothing at all is logged)         XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)         XBMC loglevel == 1 (DEBUG, shows all)       See pydocs for valid values for level.
    
    example:
      - xbmc.log(msg='This is a test string.', level=xbmc.LOGDEBUG)
    """

def makeLegalFilename(*args):
    """makeLegalFilename(filename[, fatX]) -- Returns a legal filename or path as a string.
    
    filename       : string or unicode - filename/path to make legal
    fatX           : [opt] bool - True=Xbox file system(Default)
    
    *Note, If fatX is true you should pass a full path. If fatX is false only pass
           the basename of the path.
    
           You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - filename = xbmc.makeLegalFilename('F:\Trailers\Ice Age: The Meltdown.avi')
    """

def output(*args):
    """output(msg[, level]) -- Write a string to XBMC's log file and the debug window.
    
    msg            : string - text to output.
    level          : [opt] integer - log level to ouput at. (default=LOGNOTICE)
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
           Text is written to the log for the following conditions.
             XBMC loglevel == -1 (NONE, nothing at all is logged)         XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)         XBMC loglevel == 1 (DEBUG, shows all)       See pydocs for valid values for level.
    
    example:
      - xbmc.output(msg='This is a test string.', level=xbmc.LOGDEBUG)
    """

def playSFX(*args):
    """playSFX(filename) -- Plays a wav file by filename
    
    filename       : string - filename of the wav file to play.
    
    example:
      - xbmc.playSFX('special://xbmc/scripts/dingdong.wav')
    """

def restart(*args):
    """restart() -- Restart the xbox.
    
    example:
      - xbmc.restart()
    """

def shutdown(*args):
    """shutdown() -- Shutdown the xbox.
    
    example:
      - xbmc.shutdown()
    """

def skinHasImage(*args):
    """skinHasImage(image) -- Returns True if the image file exists in the skin.
    
    image          : string - image filename
    
    *Note, If the media resides in a subfolder include it. (eg. home-myfiles\\home-myfiles2.png)
    
           You can use the above as keywords for arguments.
    
    example:
      - exists = xbmc.skinHasImage('ButtonFocusedTexture.png')
    """

def sleep(*args):
    """sleep(time) -- Sleeps for 'time' msec.
    
    time           : integer - number of msec to sleep.
    
    *Note, This is useful if you have for example a Player class that is waiting
           for onPlayBackEnded() calls.
    
    Throws: PyExc_TypeError, if time is not an integer.
    
    example:
      - xbmc.sleep(2000) # sleeps for 2 seconds
    """

def subHashAndFileSize(*args):
    """subHashAndFileSize(file)
    
    file        : file to calculate subtitle hash and size for
    example:
     size,hash = xbmcvfs.subHashAndFileSize(file)
    """

def translatePath(*args):
    """translatePath(path) -- Returns the translated path.
    
    path           : string or unicode - Path to format
    
    *Note, Only useful if you are coding for both Linux and Windows/Xbox.
           e.g. Converts 'special://masterprofile/script_data' -> '/home/user/XBMC/UserData/script_data'
           on Linux. Would return 'special://masterprofile/script_data' on the Xbox.
    
    example:
      - fpath = xbmc.translatePath('special://masterprofile/script_data')
    """

def validatePath(*args):
    """validatePath(path) -- Returns the validated path.
    
    path           : string or unicode - Path to format
    
    *Note, Only useful if you are coding for both Linux and Windows/Xbox for fixing slash problems.
           e.g. Corrects 'Z://something' -> 'Z:\something'
    
    example:
      - fpath = xbmc.validatePath(somepath)
    """

