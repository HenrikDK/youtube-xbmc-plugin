class Addon:
    """Addon class.
    
    Addon(id) -- Creates a new Addon class.
    
    id          : string - id of the addon.
    
    *Note, You can use the above as a keyword.
    
    example:
     - self.Addon = xbmcaddon.Addon(id='script.recentlyadded')
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

    def getAddonInfo(*args):
        """getAddonInfo(id) -- Returns the value of an addon property as a string.
        
        id        : string - id of the property that the module needs to access.
        
        *Note, choices are (author, changelog, description, disclaimer, fanart. icon, id, name, path
                            profile, stars, summary, type, version)
        
               You can use the above as keywords for arguments.
        
        example:
          - version = self.Addon.getAddonInfo('version')
        """

    def getLocalizedString(*args):
        """getLocalizedString(id) -- Returns an addon's localized 'unicode string'.
        
        id             : integer - id# for string you want to localize.
        
        *Note, You can use the above as keywords for arguments.
        
        example:
          - locstr = self.Addon.getLocalizedString(id=6)
        """

    def getSetting(*args):
        """getSetting(id) -- Returns the value of a setting as a unicode string.
        
        id        : string - id of the setting that the module needs to access.
        
        *Note, You can use the above as a keyword.
        
        example:
          - apikey = self.Addon.getSetting('apikey')
        """

    def openSettings(*args):
        """openSettings() -- Opens this scripts settings dialog.
        
        example:
          - self.Settings.openSettings()
        """

    def setSetting(*args):
        """setSetting(id, value) -- Sets a script setting.
        
        id        : string - id of the setting that the module needs to access.
        value     : string or unicode - value of the setting.
        
        *Note, You can use the above as keywords for arguments.
        
        example:
          - self.Settings.setSetting(id='username', value='teamxbmc')
        """



__author__ = str
__credits__ = str
__date__ = str
__platform__ = str
__version__ = str
