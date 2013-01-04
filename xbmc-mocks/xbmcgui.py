class Action:
    """Action class.
    
    For backwards compatibility reasons the == operator is extended so that itcan compare an action with other actions and action.GetID() with numbers  example: (action == ACTION_MOVE_LEFT)
    """

    def __delattr__(*args):
        """x.__delattr__('name') <==> del x.name
        """

    def __eq__(*args):
        """x.__eq__(y) <==> x==y
        """

    def __format__(*args):
        """default object formatter
        """

    def __ge__(*args):
        """x.__ge__(y) <==> x>=y
        """

    def __getattribute__(*args):
        """x.__getattribute__('name') <==> x.name
        """

    def __gt__(*args):
        """x.__gt__(y) <==> x>y
        """

    def __hash__(*args):
        """x.__hash__() <==> hash(x)
        """

    def __init__(*args):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """

    def __le__(*args):
        """x.__le__(y) <==> x<=y
        """

    def __lt__(*args):
        """x.__lt__(y) <==> x<y
        """

    def __ne__(*args):
        """x.__ne__(y) <==> x!=y
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

    def getAmount1(*args):
        """getAmount1() -- Returns the first amount of force applied to the thumbstick n.
        
        """

    def getAmount2(*args):
        """getAmount2() -- Returns the second amount of force applied to the thumbstick n.
        
        """

    def getButtonCode(*args):
        """getButtonCode() -- Returns the button code for this action.
        
        """

    def getId(*args):
        """getId() -- Returns the action's current id as a long or 0 if no action is mapped in the xml's.
        
        """



class ControlButton:
    """ControlButton class.
    
    ControlButton(x, y, width, height, label[, focusTexture, noFocusTexture, textOffsetX, textOffsetY,
                  alignment, font, textColor, disabledColor, angle, shadowColor, focusedColor])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    label          : string or unicode - text string.
    focusTexture   : [opt] string - filename for focus texture.
    noFocusTexture : [opt] string - filename for no focus texture.
    textOffsetX    : [opt] integer - x offset of label.
    textOffsetY    : [opt] integer - y offset of label.
    alignment      : [opt] integer - alignment of label - *Note, see xbfont.h
    font           : [opt] string - font used for label text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of enabled button's label. (e.g. '0xFFFFFFFF')
    disabledColor  : [opt] hexstring - color of disabled button's label. (e.g. '0xFFFF3300')
    angle          : [opt] integer - angle of control. (+ rotates CCW, - rotates CW)
    shadowColor    : [opt] hexstring - color of button's label's shadow. (e.g. '0xFF000000')
    focusedColor   : [opt] hexstring - color of focused button's label. (e.g. '0xFF00FFFF')
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.button = xbmcgui.ControlButton(100, 250, 200, 50, 'Status', font='font14')
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getLabel(*args):
        """getLabel() -- Returns the buttons label as a unicode string.
        
        example:
          - label = self.button.getLabel()
        """

    def getLabel2(*args):
        """getLabel2() -- Returns the buttons label2 as a unicode string.
        
        example:
          - label = self.button.getLabel2()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setDisabledColor(*args):
        """setDisabledColor(disabledColor) -- Set's this buttons disabled color.
        
        disabledColor  : hexstring - color of disabled button's label. (e.g. '0xFFFF3300')
        
        example:
          - self.button.setDisabledColor('0xFFFF3300')
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setLabel(*args):
        """setLabel([label, font, textColor, disabledColor, shadowColor, focusedColor]) -- Set's this buttons text attributes.
        
        label          : [opt] string or unicode - text string.
        font           : [opt] string - font used for label text. (e.g. 'font13')
        textColor      : [opt] hexstring - color of enabled button's label. (e.g. '0xFFFFFFFF')
        disabledColor  : [opt] hexstring - color of disabled button's label. (e.g. '0xFFFF3300')
        shadowColor    : [opt] hexstring - color of button's label's shadow. (e.g. '0xFF000000')
        focusedColor   : [opt] hexstring - color of focused button's label. (e.g. '0xFFFFFF00')
        label2         : [opt] string or unicode - text string.
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.button.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlCheckMark:
    """ControlCheckMark class.
    
    ControlCheckMark(x, y, width, height, label[, focusTexture, noFocusTexture,
                     checkWidth, checkHeight, alignment, font, textColor, disabledColor])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    label          : string or unicode - text string.
    focusTexture   : [opt] string - filename for focus texture.
    noFocusTexture : [opt] string - filename for no focus texture.
    checkWidth     : [opt] integer - width of checkmark.
    checkHeight    : [opt] integer - height of checkmark.
    alignment      : [opt] integer - alignment of label - *Note, see xbfont.h
    font           : [opt] string - font used for label text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of enabled checkmark's label. (e.g. '0xFFFFFFFF')
    disabledColor  : [opt] hexstring - color of disabled checkmark's label. (e.g. '0xFFFF3300')
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.checkmark = xbmcgui.ControlCheckMark(100, 250, 200, 50, 'Status', font='font14')
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getSelected(*args):
        """getSelected() -- Returns the selected status for this checkmark as a bool.
        
        example:
          - selected = self.checkmark.getSelected()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setDisabledColor(*args):
        """setDisabledColor(disabledColor) -- Set's this controls disabled color.
        
        disabledColor  : hexstring - color of disabled checkmark's label. (e.g. '0xFFFF3300')
        
        example:
          - self.checkmark.setDisabledColor('0xFFFF3300')
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setLabel(*args):
        """setLabel(label[, font, textColor, disabledColor]) -- Set's this controls text attributes.
        
        label          : string or unicode - text string.
        font           : [opt] string - font used for label text. (e.g. 'font13')
        textColor      : [opt] hexstring - color of enabled checkmark's label. (e.g. '0xFFFFFFFF')
        disabledColor  : [opt] hexstring - color of disabled checkmark's label. (e.g. '0xFFFF3300')
        
        example:
          - self.checkmark.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300')
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setSelected(*args):
        """setSelected(isOn) -- Sets this checkmark status to on or off.
        
        isOn           : bool - True=selected (on) / False=not selected (off)
        
        example:
          - self.checkmark.setSelected(True)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlFadeLabel:
    """ControlFadeLabel class.
    Control that scroll's lables
    ControlFadeLabel(x, y, width, height[, font, textColor, alignment])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    font           : [opt] string - font used for label text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of fadelabel's labels. (e.g. '0xFFFFFFFF')
    alignment      : [opt] integer - alignment of label - *Note, see xbfont.h
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.fadelabel = xbmcgui.ControlFadeLabel(100, 250, 200, 50, textColor='0xFFFFFFFF')
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def addLabel(*args):
        """addLabel(label) -- Add a label to this control for scrolling.
        
        label          : string or unicode - text string.
        
        example:
          - self.fadelabel.addLabel('This is a line of text that can scroll.')
        """

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def reset(*args):
        """reset() -- Clears this fadelabel.
        
        example:
          - self.fadelabel.reset()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlGroup:
    """ControlGroup class.
    
    ControlGroup(x, y, width, height
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    example:
      - self.group = xbmcgui.ControlGroup(100, 250, 125, 75)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlImage:
    """ControlImage class.
    
    ControlImage(x, y, width, height, filename[, colorKey, aspectRatio, colorDiffuse])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    filename       : string - image filename.
    colorKey       : [opt] hexString - (example, '0xFFFF3300')
    aspectRatio    : [opt] integer - (values 0 = stretch (default), 1 = scale up (crops), 2 = scale down (black bars)colorDiffuse   : hexString - (example, '0xC0FF0000' (red tint))
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.image = xbmcgui.ControlImage(100, 250, 125, 75, aspectRatio=2)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setColorDiffuse(*args):
        """setColorDiffuse(colorDiffuse) -- Changes the images color.
        
        colorDiffuse   : hexString - (example, '0xC0FF0000' (red tint))
        
        example:
          - self.image.setColorDiffuse('0xC0FF0000')
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setImage(*args):
        """setImage(filename, colorKey) -- Changes the image.
        
        filename       : string - image filename.
        
        example:
          - self.image.setImage('special://home/scripts/test.png')
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlLabel:
    """ControlLabel class.
    
    ControlLabel(x, y, width, height, label[, font, textColor, 
                 disabledColor, alignment, hasPath, angle])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    label          : string or unicode - text string.
    font           : [opt] string - font used for label text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of enabled label's label. (e.g. '0xFFFFFFFF')
    disabledColor  : [opt] hexstring - color of disabled label's label. (e.g. '0xFFFF3300')
    alignment      : [opt] integer - alignment of label - *Note, see xbfont.h
    hasPath        : [opt] bool - True=stores a path / False=no path.
    angle          : [opt] integer - angle of control. (+ rotates CCW, - rotates CW)
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.label = xbmcgui.ControlLabel(100, 250, 125, 75, 'Status', angle=45)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getLabel(*args):
        """getLabel() -- Returns the text value for this label.
        
        example:
          - label = self.label.getLabel()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setLabel(*args):
        """setLabel(label) -- Set's text for this label.
        
        label          : string or unicode - text string.
        
        example:
          - self.label.setLabel('Status')
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlList:
    """ControlList class.
    
    ControlList(x, y, width, height[, font, textColor, buttonTexture, buttonFocusTexture,
                selectedColor, imageWidth, imageHeight, itemTextXOffset, itemTextYOffset,
                itemHeight, space, alignmentY])
    
    x                  : integer - x coordinate of control.
    y                  : integer - y coordinate of control.
    width              : integer - width of control.
    height             : integer - height of control.
    font               : [opt] string - font used for items label. (e.g. 'font13')
    textColor          : [opt] hexstring - color of items label. (e.g. '0xFFFFFFFF')
    buttonTexture      : [opt] string - filename for focus texture.
    buttonFocusTexture : [opt] string - filename for no focus texture.
    selectedColor      : [opt] integer - x offset of label.
    imageWidth         : [opt] integer - width of items icon or thumbnail.
    imageHeight        : [opt] integer - height of items icon or thumbnail.
    itemTextXOffset    : [opt] integer - x offset of items label.
    itemTextYOffset    : [opt] integer - y offset of items label.
    itemHeight         : [opt] integer - height of items.
    space              : [opt] integer - space between items.
    alignmentY         : [opt] integer - Y-axis alignment of items label - *Note, see xbfont.h
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.cList = xbmcgui.ControlList(100, 250, 200, 250, 'font14', space=5)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def addItem(*args):
        """addItem(item) -- Add a new item to this list control.
        
        item               : string, unicode or ListItem - item to add.
        
        example:
          - cList.addItem('Reboot XBMC')
        """

    def addItems(*args):
        """addItems(items) -- Adds a list of listitems or strings to this list control.
        
        items                : List - list of strings, unicode objects or ListItems to add.
        
        *Note, You can use the above as keywords for arguments.
        
               Large lists benefit considerably, than using the standard addItem()
        example:
          - cList.addItems(items=listitems)
        """

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getItemHeight(*args):
        """getItemHeight() -- Returns the control's current item height as an integer.
        
        example:
          - item_height = self.cList.getItemHeight()
        """

    def getListItem(*args):
        """getListItem(index) -- Returns a given ListItem in this List.
        
        index           : integer - index number of item to return.
        
        *Note, throws a ValueError if index is out of range.
        
        example:
          - listitem = cList.getListItem(6)
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getSelectedItem(*args):
        """getSelectedItem() -- Returns the selected item as a ListItem object.
        
        *Note, Same as getSelectedPosition(), but instead of an integer a ListItem object
               is returned. Returns None for empty lists.
               See windowexample.py on how to use this.
        
        example:
          - item = cList.getSelectedItem()
        """

    def getSelectedPosition(*args):
        """getSelectedPosition() -- Returns the position of the selected item as an integer.
        
        *Note, Returns -1 for empty lists.
        
        example:
          - pos = cList.getSelectedPosition()
        """

    def getSpace(*args):
        """getSpace() -- Returns the control's space between items as an integer.
        
        example:
          - gap = self.cList.getSpace()
        """

    def getSpinControl(*args):
        """getSpinControl() -- returns the associated ControlSpin object.
        
        *Note, Not working completely yet -
               After adding this control list to a window it is not possible to change
               the settings of this spin control.
        
        example:
          - ctl = cList.getSpinControl()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def reset(*args):
        """reset() -- Clear all ListItems in this control list.
        
        example:
          - cList.reset()
        """

    def selectItem(*args):
        """selectItem(item) -- Select an item by index number.
        
        item               : integer - index number of the item to select.
        
        example:
          - cList.selectItem(12)
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setImageDimensions(*args):
        """setImageDimensions(imageWidth, imageHeight) -- Sets the width/height of items icon or thumbnail.
        
        imageWidth         : [opt] integer - width of items icon or thumbnail.
        imageHeight        : [opt] integer - height of items icon or thumbnail.
        
        example:
          - cList.setImageDimensions(18, 18)
        """

    def setItemHeight(*args):
        """setItemHeight(itemHeight) -- Sets the height of items.
        
        itemHeight         : integer - height of items.
        
        example:
          - cList.setItemHeight(25)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPageControlVisible(*args):
        """setPageControlVisible(visible) -- Sets the spin control's visible/hidden state.
        
        visible            : boolean - True=visible / False=hidden.
        
        example:
          - cList.setPageControlVisible(True)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setSpace(*args):
        """setSpace(space) -- Set's the space between items.
        
        space              : [opt] integer - space between items.
        
        example:
          - cList.setSpace(5)
        """

    def setStaticContent(*args):
        """setStaticContent(items) -- Fills a static list with a list of listitems.
        
        items                : List - list of listitems to add.
        
        *Note, You can use the above as keywords for arguments.
        
        example:
          - cList.setStaticContent(items=listitems)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """

    def size(*args):
        """size() -- Returns the total number of items in this list control as an integer.
        
        example:
          - cnt = cList.size()
        """



class ControlProgress:
    """ControlProgress class.
    
    ControlProgress(x, y, width, height[, texturebg, textureleft, texturemid, textureright, textureoverlay])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    texturebg      : [opt] string - image filename.
    textureleft    : [opt] string - image filename.
    texturemid     : [opt] string - image filename.
    textureright   : [opt] string - image filename.
    textureoverlay : [opt] string - image filename.
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.progress = xbmcgui.ControlProgress(100, 250, 125, 75)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPercent(*args):
        """getPercent() -- Returns a float of the percent of the progress.
        
        example:
          - print self.progress.getValue()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPercent(*args):
        """setPercent(percent) -- Sets the percentage of the progressbar to show.
        
        percent       : float - percentage of the bar to show.
        
        *Note, valid range for percent is 0-100
        
        example:
          - self.progress.setPercent(60)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlRadioButton:
    """ControlRadioButton class.
    
    ControlRadioButton(x, y, width, height, label[, focusTexture, noFocusTexture, textOffsetX, textOffsetY,
                  alignment, font, textColor, disabledColor, angle, shadowColor, focusedColor,
                  radioFocusTexture, noRadioFocusTexture])
    
    x                   : integer - x coordinate of control.
    y                   : integer - y coordinate of control.
    width               : integer - width of control.
    height              : integer - height of control.
    label               : string or unicode - text string.
    focusTexture        : [opt] string - filename for focus texture.
    noFocusTexture      : [opt] string - filename for no focus texture.
    textOffsetX         : [opt] integer - x offset of label.
    textOffsetY         : [opt] integer - y offset of label.
    alignment           : [opt] integer - alignment of label - *Note, see xbfont.h
    font                : [opt] string - font used for label text. (e.g. 'font13')
    textColor           : [opt] hexstring - color of enabled radio button's label. (e.g. '0xFFFFFFFF')
    disabledColor       : [opt] hexstring - color of disabled radio button's label. (e.g. '0xFFFF3300')
    angle               : [opt] integer - angle of control. (+ rotates CCW, - rotates CW)
    shadowColor         : [opt] hexstring - color of radio button's label's shadow. (e.g. '0xFF000000')
    focusedColor        : [opt] hexstring - color of focused radio button's label. (e.g. '0xFF00FFFF')
    radioFocusTexture   : [opt] string - filename for radio focus texture.
    noRadioFocusTexture : [opt] string - filename for radio no focus texture.
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.radiobutton = xbmcgui.ControlRadioButton(100, 250, 200, 50, 'Status', font='font14')
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def isSelected(*args):
        """isSelected() -- Returns the radio buttons's selected status.
        
        example:
          - is = self.radiobutton.isSelected()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setLabel(*args):
        """setLabel(label[, font, textColor, disabledColor, shadowColor, focusedColor]) -- Set's the radio buttons text attributes.
        
        label          : string or unicode - text string.
        font           : [opt] string - font used for label text. (e.g. 'font13')
        textColor      : [opt] hexstring - color of enabled radio button's label. (e.g. '0xFFFFFFFF')
        disabledColor  : [opt] hexstring - color of disabled radio button's label. (e.g. '0xFFFF3300')
        shadowColor    : [opt] hexstring - color of radio button's label's shadow. (e.g. '0xFF000000')
        focusedColor   : [opt] hexstring - color of focused radio button's label. (e.g. '0xFFFFFF00')
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.radiobutton.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setRadioDimension(*args):
        """setRadioDimension(x, y, width, height) -- Sets the radio buttons's radio texture's position and size.
        
        x                   : integer - x coordinate of radio texture.
        y                   : integer - y coordinate of radio texture.
        width               : integer - width of radio texture.
        height              : integer - height of radio texture.
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.radiobutton.setRadioDimension(x=100, y=5, width=20, height=20)
        """

    def setSelected(*args):
        """setSelected(selected) -- Sets the radio buttons's selected status.
        
        selected            : bool - True=selected (on) / False=not selected (off)
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.radiobutton.setSelected(True)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlSlider:
    """ControlSlider class.
    
    ControlSlider(x, y, width, height[, textureback, texture, texturefocus])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    textureback    : [opt] string - image filename.
    texture        : [opt] string - image filename.
    texturefocus   : [opt] string - image filename.
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.slider = xbmcgui.ControlSlider(100, 250, 350, 40)
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPercent(*args):
        """getPercent() -- Returns a float of the percent of the slider.
        
        example:
          - print self.slider.getPercent()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPercent(*args):
        """setPercent(50) -- Sets the percent of the slider.
        
        example:
        self.slider.setPercent(50)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class ControlTextBox:
    """ControlTextBox class.
    
    ControlTextBox(x, y, width, height[, font, textColor])
    
    x              : integer - x coordinate of control.
    y              : integer - y coordinate of control.
    width          : integer - width of control.
    height         : integer - height of control.
    font           : [opt] string - font used for text. (e.g. 'font13')
    textColor      : [opt] hexstring - color of textbox's text. (e.g. '0xFFFFFFFF')
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
           After you create the control, you need to add it to the window with addControl().
    
    example:
      - self.textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor='0xFFFFFFFF')
    """

    def __cmp__(*args):
        """x.__cmp__(y) <==> cmp(x,y)
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

    def controlDown(*args):
        """controlDown(control) -- Set's the controls down navigation.
        
        control        : control object - control to navigate to on down.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlDown(self.button1)
        """

    def controlLeft(*args):
        """controlLeft(control) -- Set's the controls left navigation.
        
        control        : control object - control to navigate to on left.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlLeft(self.button1)
        """

    def controlRight(*args):
        """controlRight(control) -- Set's the controls right navigation.
        
        control        : control object - control to navigate to on right.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlRight(self.button1)
        """

    def controlUp(*args):
        """controlUp(control) -- Set's the controls up navigation.
        
        control        : control object - control to navigate to on up.
        
        *Note, You can also use setNavigation(). Set to self to disable navigation.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.controlUp(self.button1)
        """

    def getHeight(*args):
        """getHeight() -- Returns the control's current height as an integer.
        
        example:
          - height = self.button.getHeight()
        """

    def getId(*args):
        """getId() -- Returns the control's current id as an integer.
        
        example:
          - id = self.button.getId()
        """

    def getPosition(*args):
        """getPosition() -- Returns the control's current position as a x,y integer tuple.
        
        example:
          - pos = self.button.getPosition()
        """

    def getWidth(*args):
        """getWidth() -- Returns the control's current width as an integer.
        
        example:
          - width = self.button.getWidth()
        """

    def reset(*args):
        """reset() -- Clear's this textbox.
        
        example:
          - self.textbox.reset()
        """

    def scroll(*args):
        """scroll(position) -- Scrolls to the given position.
        
        id           : integer - position to scroll to.
        
        example:
          - self.textbox.scroll(10)
        """

    def setAnimations(*args):
        """setAnimations([(event, attr,)*]) -- Set's the control's animations.
        
        [(event,attr,)*] : list - A list of tuples consisting of event and attributes pairs.
          - event        : string - The event to animate.
          - attr         : string - The whole attribute string separated by spaces.
        
        Animating your skin - http://wiki.xbmc.org/?title=Animating_Your_Skin 
        
        example:
          - self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
        """

    def setEnableCondition(*args):
        """setEnableCondition(enable) -- Set's the control's enabled condition.
            Allows XBMC to control the enabled status of the control.
        
        enable           : string - Enable condition.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setEnableCondition('System.InternetState')
        """

    def setEnabled(*args):
        """setEnabled(enabled) -- Set's the control's enabled/disabled state.
        
        enabled        : bool - True=enabled / False=disabled.
        
        example:
          - self.button.setEnabled(False)
        """

    def setHeight(*args):
        """setHeight(height) -- Set's the controls height.
        
        height         : integer - height of control.
        
        example:
          - self.image.setHeight(100)
        """

    def setNavigation(*args):
        """setNavigation(up, down, left, right) -- Set's the controls navigation.
        
        up             : control object - control to navigate to on up.
        down           : control object - control to navigate to on down.
        left           : control object - control to navigate to on left.
        right          : control object - control to navigate to on right.
        
        *Note, Same as controlUp(), controlDown(), controlLeft(), controlRight().
               Set to self to disable navigation for that direction.
        
        Throws: TypeError, if one of the supplied arguments is not a control type.
                ReferenceError, if one of the controls is not added to a window.
        
        example:
          - self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
        """

    def setPosition(*args):
        """setPosition(x, y) -- Set's the controls position.
        
        x              : integer - x coordinate of control.
        y              : integer - y coordinate of control.
        
        *Note, You may use negative integers. (e.g sliding a control into view)
        
        example:
          - self.button.setPosition(100, 250)
        """

    def setText(*args):
        """setText(text) -- Set's the text for this textbox.
        
        text           : string or unicode - text string.
        
        example:
          - self.textbox.setText('This is a line of text that can wrap.')
        """

    def setVisible(*args):
        """setVisible(visible) -- Set's the control's visible/hidden state.
        
        visible        : bool - True=visible / False=hidden.
        
        example:
          - self.button.setVisible(False)
        """

    def setVisibleCondition(*args):
        """setVisibleCondition(visible[,allowHiddenFocus]) -- Set's the control's visible condition.
            Allows XBMC to control the visible status of the control.
        
        visible          : string - Visible condition.
        allowHiddenFocus : bool - True=gains focus even if hidden.
        
        List of Conditions - http://wiki.xbmc.org/index.php?title=List_of_Boolean_Conditions 
        
        example:
          - self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
        """

    def setWidth(*args):
        """setWidth(width) -- Set's the controls width.
        
        width          : integer - width of control.
        
        example:
          - self.image.setWidth(100)
        """



class Dialog:
    """Dialog class.
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

    def browse(*args):
        """browse(type, heading, shares[, mask, useThumbs, treatAsFolder, default, enableMultiple]) -- Show a 'Browse' dialog.
        
        type           : integer - the type of browse dialog.
        heading        : string or unicode - dialog heading.
        shares         : string or unicode - from sources.xml. (i.e. 'myprograms')
        mask           : [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png')
        useThumbs      : [opt] boolean - if True autoswitch to Thumb view if files exist.
        treatAsFolder  : [opt] boolean - if True playlists and archives act as folders.
        default        : [opt] string - default path or file.
        
        enableMultiple : [opt] boolean - if True multiple file selection is enabled.
        Types:
          0 : ShowAndGetDirectory
          1 : ShowAndGetFile
          2 : ShowAndGetImage
          3 : ShowAndGetWriteableDirectory
        
        *Note, If enableMultiple is False (default): returns filename and/or path as a string
               to the location of the highlighted item, if user pressed 'Ok' or a masked item
               was selected. Returns the default value if dialog was canceled.
               If enableMultiple is True: returns tuple of marked filenames as a string,       if user pressed 'Ok' or a masked item was selected. Returns empty tuple if dialog was canceled.
        
               If type is 0 or 3 the enableMultiple parameter is ignored.
        example:
          - dialog = xbmcgui.Dialog()
          - fn = dialog.browse(3, 'XBMC', 'files', '', False, False, False, 'special://masterprofile/script_data/XBMC Lyrics')
        """

    def numeric(*args):
        """numeric(type, heading[, default]) -- Show a 'Numeric' dialog.
        
        type           : integer - the type of numeric dialog.
        heading        : string or unicode - dialog heading.
        default        : [opt] string - default value.
        
        Types:
          0 : ShowAndGetNumber    (default format: #)
          1 : ShowAndGetDate      (default format: DD/MM/YYYY)
          2 : ShowAndGetTime      (default format: HH:MM)
          3 : ShowAndGetIPAddress (default format: #.#.#.#)
        
        *Note, Returns the entered data as a string.
               Returns the default value if dialog was canceled.
        
        example:
          - dialog = xbmcgui.Dialog()
          - d = dialog.numeric(1, 'Enter date of birth')
        """

    def ok(*args):
        """ok(heading, line1[, line2, line3]) -- Show a dialog 'OK'.
        
        heading        : string or unicode - dialog heading.
        line1          : string or unicode - line #1 text.
        line2          : [opt] string or unicode - line #2 text.
        line3          : [opt] string or unicode - line #3 text.
        
        *Note, Returns True if 'Ok' was pressed, else False.
        
        example:
          - dialog = xbmcgui.Dialog()
          - ok = dialog.ok('XBMC', 'There was an error.')
        """

    def select(*args):
        """select(heading, list) -- Show a select dialog.
        
        heading        : string or unicode - dialog heading.
        list           : string list - list of items.
        autoclose      : [opt] integer - milliseconds to autoclose dialog. (default=do not autoclose)
        
        *Note, Returns the position of the highlighted item as an integer.
        
        example:
          - dialog = xbmcgui.Dialog()
          - ret = dialog.select('Choose a playlist', ['Playlist #1', 'Playlist #2, 'Playlist #3'])
        """

    def yesno(*args):
        """yesno(heading, line1[, line2, line3]) -- Show a dialog 'YES/NO'.
        
        heading        : string or unicode - dialog heading.
        line1          : string or unicode - line #1 text.
        line2          : [opt] string or unicode - line #2 text.
        line3          : [opt] string or unicode - line #3 text.
        nolabel        : [opt] label to put on the no button.
        yeslabel       : [opt] label to put on the yes button.
        
        *Note, Returns True if 'Yes' was pressed, else False.
        
        example:
          - dialog = xbmcgui.Dialog()
          - ret = dialog.yesno('XBMC', 'Do you want to exit this script?')
        """



class DialogProgress:
    """DialogProgress class.
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

    def close(*args):
        """close() -- Close the progress dialog.
        
        example:
          - pDialog.close()
        """

    def create(*args):
        """create(heading[, line1, line2, line3]) -- Create and show a progress dialog.
        
        heading        : string or unicode - dialog heading.
        line1          : string or unicode - line #1 text.
        line2          : [opt] string or unicode - line #2 text.
        line3          : [opt] string or unicode - line #3 text.
        
        *Note, Use update() to update lines and progressbar.
        
        example:
          - pDialog = xbmcgui.DialogProgress()
          - ret = pDialog.create('XBMC', 'Initializing script...')
        """

    def iscanceled(*args):
        """iscanceled() -- Returns True if the user pressed cancel.
        
        example:
          - if (pDialog.iscanceled()): return
        """

    def update(*args):
        """update(percent[, line1, line2, line3]) -- Update's the progress dialog.
        
        percent        : integer - percent complete. (0:100)
        line1          : [opt] string or unicode - line #1 text.
        line2          : [opt] string or unicode - line #2 text.
        line3          : [opt] string or unicode - line #3 text.
        
        *Note, If percent == 0, the progressbar will be hidden.
        
        example:
          - pDialog.update(25, 'Importing modules...')
        """



ICON_OVERLAY_HAS_TRAINER = int
ICON_OVERLAY_HD = int
ICON_OVERLAY_LOCKED = int
ICON_OVERLAY_NONE = int
ICON_OVERLAY_RAR = int
ICON_OVERLAY_TRAINED = int
ICON_OVERLAY_UNWATCHED = int
ICON_OVERLAY_WATCHED = int
ICON_OVERLAY_ZIP = int
class ListItem:
    """ListItem class.
    
    ListItem([label, label2, iconImage, thumbnailImage, path]) -- Creates a new ListItem.
    
    label          : [opt] string or unicode - label1 text.
    label2         : [opt] string or unicode - label2 text.
    iconImage      : [opt] string - icon filename.
    thumbnailImage : [opt] string - thumbnail filename.
    path           : [opt] string or unicode - listitem's path.
    
    *Note, You can use the above as keywords for arguments and skip certain optional arguments.
           Once you use a keyword, all following arguments require the keyword.
    
    example:
      - listitem = xbmcgui.ListItem('Casino Royale', '[PG-13]', 'blank-poster.tbn', 'poster.tbn', path='f:\\movies\\casino_royale.mov')
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

    def addContextMenuItems(*args):
        """addContextMenuItems([(label, action,)*], replaceItems) -- Adds item(s) to the context menu for media lists.
        
        items               : list - [(label, action,)*] A list of tuples consisting of label and action pairs.
          - label           : string or unicode - item's label.
          - action          : string or unicode - any built-in function to perform.
        replaceItems        : [opt] bool - True=only your items will show/False=your items will be added to context menu(Default).
        
        List of functions - http://wiki.xbmc.org/?title=List_of_Built_In_Functions 
        
        *Note, You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - listitem.addContextMenuItems([('Theater Showtimes', 'XBMC.RunScript(special://home/scripts/showtimes/default.py,Iron Man)',)])
        """

    def getLabel(*args):
        """getLabel() -- Returns the listitem label.
        
        example:
          - label = self.list.getSelectedItem().getLabel()
        """

    def getLabel2(*args):
        """getLabel2() -- Returns the listitem's second label.
        
        example:
          - label2 = self.list.getSelectedItem().getLabel2()
        """

    def getProperty(*args):
        """getProperty(key) -- Returns a listitem property as a string, similar to an infolabel.
        
        key            : string - property name.
        
        *Note, Key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - AspectRatio = self.list.getSelectedItem().getProperty('AspectRatio')
        """

    def isSelected(*args):
        """isSelected() -- Returns the listitem's selected status.
        
        example:
          - is = self.list.getSelectedItem().isSelected()
        """

    def select(*args):
        """select(selected) -- Sets the listitem's selected status.
        
        selected        : bool - True=selected/False=not selected
        
        example:
          - self.list.getSelectedItem().select(True)
        """

    def setIconImage(*args):
        """setIconImage(icon) -- Sets the listitem's icon image.
        
        icon            : string or unicode - image filename.
        
        example:
          - self.list.getSelectedItem().setIconImage('emailread.png')
        """

    def setInfo(*args):
        """setInfo(type, infoLabels) -- Sets the listitem's infoLabels.
        
        type              : string - type of media(video/music/pictures).
        infoLabels        : dictionary - pairs of { label: value }.
        
        *Note, To set pictures exif info, prepend 'exif:' to the label. Exif values must be passed
               as strings, separate value pairs with a comma. (eg. {'exif:resolution': '720,480'}
               See CPictureInfoTag::TranslateString in PictureInfoTag.cpp for valid strings.
        
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        General Values that apply to all types:
            count         : integer (12) - can be used to store an id for later, or for sorting purposes
            size          : long (1024) - size in bytes
            date          : string (%d.%m.%Y / 01.01.2009) - file date
        
        Video Values:
            genre         : string (Comedy)
            year          : integer (2009)
            episode       : integer (4)
            season        : integer (1)
            top250        : integer (192)
            tracknumber   : integer (3)
            rating        : float (6.4) - range is 0..10
            watched       : depreciated - use playcount instead
            playcount     : integer (2) - number of times this item has been played
            overlay       : integer (2) - range is 0..8.  See GUIListItem.h for values
            cast          : list (Michal C. Hall)
            castandrole   : list (Michael C. Hall|Dexter)
            director      : string (Dagur Kari)
            mpaa          : string (PG-13)
            plot          : string (Long Description)
            plotoutline   : string (Short Description)
            title         : string (Big Fan)
            originaltitle : string (Big Fan)
            duration      : string (3:18)
            studio        : string (Warner Bros.)
            tagline       : string (An awesome movie) - short description of movie
            writer        : string (Robert D. Siegel)
            tvshowtitle   : string (Heroes)
            premiered     : string (2005-03-04)
            status        : string (Continuing) - status of a TVshow
            code          : string (tt0110293) - IMDb code
            aired         : string (2008-12-07)
            credits       : string (Andy Kaufman) - writing credits
            lastplayed    : string (%Y-%m-%d %h:%m:%s = 2009-04-05 23:16:04)
            album         : string (The Joshua Tree)
            votes         : string (12345 votes)
            trailer       : string (/home/user/trailer.avi)
        
        Music Values:
            tracknumber   : integer (8)
            duration      : integer (245) - duration in seconds
            year          : integer (1998)
            genre         : string (Rock)
            album         : string (Pulse)
            artist        : string (Muse)
            title         : string (American Pie)
            rating        : string (3) - single character between 0 and 5
            lyrics        : string (On a dark desert highway...)
            playcount     : integer (2) - number of times this item has been played
            lastplayed    : string (%Y-%m-%d %h:%m:%s = 2009-04-05 23:16:04)
        
        Picture Values:
            title         : string (In the last summer-1)
            picturepath   : string (/home/username/pictures/img001.jpg)
            exif*         : string (See CPictureInfoTag::TranslateString in PictureInfoTag.cpp for valid strings)
        
        example:
          - self.list.getSelectedItem().setInfo('video', { 'Genre': 'Comedy' })
        """

    def setLabel(*args):
        """setLabel(label) -- Sets the listitem's label.
        
        label          : string or unicode - text string.
        
        example:
          - self.list.getSelectedItem().setLabel('Casino Royale')
        """

    def setLabel2(*args):
        """setLabel2(label2) -- Sets the listitem's second label.
        
        label2         : string or unicode - text string.
        
        example:
          - self.list.getSelectedItem().setLabel2('[pg-13]')
        """

    def setPath(*args):
        """setPath(path) -- Sets the listitem's path.
        
        path           : string or unicode - path, activated when item is clicked.
        
        *Note, You can use the above as keywords for arguments.
        
        example:
          - self.list.getSelectedItem().setPath(path='ActivateWindow(Weather)')
        """

    def setProperty(*args):
        """setProperty(key, value) -- Sets a listitem property, similar to an infolabel.
        
        key            : string - property name.
        value          : string or unicode - value of property.
        
        *Note, Key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
         Some of these are treated internally by XBMC, such as the 'StartOffset' property, which is
         the offset in seconds at which to start playback of an item.  Others may be used in the skin
         to add extra information, such as 'WatchedCount' for tvshow items
        
        example:
          - self.list.getSelectedItem().setProperty('AspectRatio', '1.85 : 1')
          - self.list.getSelectedItem().setProperty('StartOffset', '256.4')
        """

    def setThumbnailImage(*args):
        """setThumbnailImage(thumb) -- Sets the listitem's thumbnail image.
        
        thumb           : string or unicode - image filename.
        
        example:
          - self.list.getSelectedItem().setThumbnailImage('emailread.png')
        """



class Window:
    """Window class.
    
    Window(self[, int windowId) -- Create a new Window to draw on.
                                   Specify an id to use an existing window.
    
    Throws: ValueError, if supplied window Id does not exist.
            Exception, if more then 200 windows are created.
    
    Deleting this window will activate the old window that was active
    and resets (not delete) all controls that are associated with this window.
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

    def addControl(*args):
        """addControl(self, Control) -- Add a Control to this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                ReferenceError, if control is already used in another window
                RuntimeError, should not happen :-)
        
        The next controls can be added to a window atm
        
          -ControlLabel
          -ControlFadeLabel
          -ControlTextBox
          -ControlButton
          -ControlCheckMark
          -ControlList
          -ControlGroup
          -ControlImage
          -ControlRadioButton
          -ControlProgress
        """

    def clearProperties(*args):
        """clearProperties() -- Clears all window properties.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperties()
        """

    def clearProperty(*args):
        """clearProperty(key) -- Clears the specific window property.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive. Equivalent to setProperty(key,'')
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperty('Category')
        """

    def close(*args):
        """close(self) -- Closes this window.
        
        Closes this window by activating the old window.
        The window is not deleted with this method.
        """

    def doModal(*args):
        """doModal(self) -- Display this window until close() is called.
        """

    def getControl(*args):
        """getControl(self, int controlId) -- Get's the control from this window.
        
        Throws: Exception, if Control doesn't exist
        
        controlId doesn't have to be a python control, it can be a control id
        from a xbmc window too (you can find id's in the xml files
        
        Note, not python controls are not completely usable yet
        You can only use the Control functions
        """

    def getFocus(*args):
        """getFocus(self, Control) -- returns the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getFocusId(*args):
        """getFocusId(self, int) -- returns the id of the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getHeight(*args):
        """getHeight(self) -- Returns the height of this screen.
        """

    def getProperty(*args):
        """getProperty(key) -- Returns a window property as a string, similar to an infolabel.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - category = win.getProperty('Category')
        """

    def getResolution(*args):
        """getResolution(self) -- Returns the resolution of the screen. The returned value is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def getWidth(*args):
        """getWidth(self) -- Returns the width of this screen.
        """

    def onAction(*args):
        """onAction(self, Action action) -- onAction method.
        
        This method will recieve all actions that the main program will send
        to this window.
        By default, only the PREVIOUS_MENU action is handled.
        Overwrite this method to let your script handle all actions.
        Don't forget to capture ACTION_PREVIOUS_MENU, else the user can't close this window.
        """

    def onClick(*args):
        """onClick(self, Control control) -- onClick method.
        
        This method will recieve all click events that the main program will send
        to this window.
        """

    def onFocus(*args):
        """onFocus(self, Control control) -- onFocus method.
        
        This method will recieve all focus events that the main program will send
        to this window.
        """

    def onInit(*args):
        """onInit(self) -- onInit method.
        
        This method will be called to initialize the window
        """

    def removeControl(*args):
        """removeControl(self, Control) -- Removes the control from this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                RuntimeError, if control is not added to this window
        
        This will not delete the control. It is only removed from the window.
        """

    def setCoordinateResolution(*args):
        """setCoordinateResolution(self, int resolution) -- Sets the resolution
        that the coordinates of all controls are defined in.  Allows XBMC
        to scale control positions and width/heights to whatever resolution
        XBMC is currently using.
         resolution is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def setFocus(*args):
        """setFocus(self, Control) -- Give the supplied control focus.
        Throws: TypeError, if supplied argument is not a Control type
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setFocusId(*args):
        """setFocusId(self, int) -- Gives the control with the supplied focus.
        Throws: 
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setProperty(*args):
        """setProperty(key, value) -- Sets a window property, similar to an infolabel.
        
        key            : string - property name.
        value          : string or unicode - value of property.
        
        *Note, key is NOT case sensitive. Setting value to an empty string is equivalent to clearProperty(key)
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.setProperty('Category', 'Newest')
        """

    def show(*args):
        """show(self) -- Show this window.
        
        Shows this window by activating it, calling close() after it wil activate the
        current window again.
        Note, if your script ends this window will be closed to. To show it forever, 
        make a loop at the end of your script ar use doModal() instead
        """



class WindowDialog:
    """WindowDialog class.
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

    def addControl(*args):
        """addControl(self, Control) -- Add a Control to this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                ReferenceError, if control is already used in another window
                RuntimeError, should not happen :-)
        
        The next controls can be added to a window atm
        
          -ControlLabel
          -ControlFadeLabel
          -ControlTextBox
          -ControlButton
          -ControlCheckMark
          -ControlList
          -ControlGroup
          -ControlImage
          -ControlRadioButton
          -ControlProgress
        """

    def clearProperties(*args):
        """clearProperties() -- Clears all window properties.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperties()
        """

    def clearProperty(*args):
        """clearProperty(key) -- Clears the specific window property.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive. Equivalent to setProperty(key,'')
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperty('Category')
        """

    def close(*args):
        """close(self) -- Closes this window.
        
        Closes this window by activating the old window.
        The window is not deleted with this method.
        """

    def doModal(*args):
        """doModal(self) -- Display this window until close() is called.
        """

    def getControl(*args):
        """getControl(self, int controlId) -- Get's the control from this window.
        
        Throws: Exception, if Control doesn't exist
        
        controlId doesn't have to be a python control, it can be a control id
        from a xbmc window too (you can find id's in the xml files
        
        Note, not python controls are not completely usable yet
        You can only use the Control functions
        """

    def getFocus(*args):
        """getFocus(self, Control) -- returns the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getFocusId(*args):
        """getFocusId(self, int) -- returns the id of the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getHeight(*args):
        """getHeight(self) -- Returns the height of this screen.
        """

    def getProperty(*args):
        """getProperty(key) -- Returns a window property as a string, similar to an infolabel.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - category = win.getProperty('Category')
        """

    def getResolution(*args):
        """getResolution(self) -- Returns the resolution of the screen. The returned value is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def getWidth(*args):
        """getWidth(self) -- Returns the width of this screen.
        """

    def onAction(*args):
        """onAction(self, Action action) -- onAction method.
        
        This method will recieve all actions that the main program will send
        to this window.
        By default, only the PREVIOUS_MENU action is handled.
        Overwrite this method to let your script handle all actions.
        Don't forget to capture ACTION_PREVIOUS_MENU, else the user can't close this window.
        """

    def onClick(*args):
        """onClick(self, Control control) -- onClick method.
        
        This method will recieve all click events that the main program will send
        to this window.
        """

    def onFocus(*args):
        """onFocus(self, Control control) -- onFocus method.
        
        This method will recieve all focus events that the main program will send
        to this window.
        """

    def onInit(*args):
        """onInit(self) -- onInit method.
        
        This method will be called to initialize the window
        """

    def removeControl(*args):
        """removeControl(self, Control) -- Removes the control from this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                RuntimeError, if control is not added to this window
        
        This will not delete the control. It is only removed from the window.
        """

    def setCoordinateResolution(*args):
        """setCoordinateResolution(self, int resolution) -- Sets the resolution
        that the coordinates of all controls are defined in.  Allows XBMC
        to scale control positions and width/heights to whatever resolution
        XBMC is currently using.
         resolution is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def setFocus(*args):
        """setFocus(self, Control) -- Give the supplied control focus.
        Throws: TypeError, if supplied argument is not a Control type
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setFocusId(*args):
        """setFocusId(self, int) -- Gives the control with the supplied focus.
        Throws: 
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setProperty(*args):
        """setProperty(key, value) -- Sets a window property, similar to an infolabel.
        
        key            : string - property name.
        value          : string or unicode - value of property.
        
        *Note, key is NOT case sensitive. Setting value to an empty string is equivalent to clearProperty(key)
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.setProperty('Category', 'Newest')
        """

    def show(*args):
        """show(self) -- Show this window.
        
        Shows this window by activating it, calling close() after it wil activate the
        current window again.
        Note, if your script ends this window will be closed to. To show it forever, 
        make a loop at the end of your script ar use doModal() instead
        """



class WindowXML:
    """WindowXML class.
    
    WindowXML(self, xmlFilename, scriptPath[, defaultSkin, defaultRes]) -- Create a new WindowXML script.
    
    xmlFilename     : string - the name of the xml file to look for.
    scriptPath      : string - path to script. used to fallback to if the xml doesn't exist in the current skin. (eg os.getcwd())
    defaultSkin     : [opt] string - name of the folder in the skins path to look in for the xml. (default='Default')
    defaultRes      : [opt] string - default skins resolution. (default='720p')
    
    *Note, skin folder structure is eg(resources/skins/Default/720p)
    
    example:
     - ui = GUI('script-Lyrics-main.xml', os.getcwd(), 'LCARS', 'PAL')
       ui.doModal()
       del ui
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

    def addControl(*args):
        """addControl(self, Control) -- Add a Control to this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                ReferenceError, if control is already used in another window
                RuntimeError, should not happen :-)
        
        The next controls can be added to a window atm
        
          -ControlLabel
          -ControlFadeLabel
          -ControlTextBox
          -ControlButton
          -ControlCheckMark
          -ControlList
          -ControlGroup
          -ControlImage
          -ControlRadioButton
          -ControlProgress
        """

    def addItem(*args):
        """addItem(item[, position]) -- Add a new item to this Window List.
        
        item            : string, unicode or ListItem - item to add.
        position        : [opt] integer - position of item to add. (NO Int = Adds to bottom,0 adds to top, 1 adds to one below from top,-1 adds to one above from bottom etc etc )
                                        - If integer positions are greater than list size, negative positions will add to top of list, positive positions will add to bottom of list
        example:
          - self.addItem('Reboot XBMC', 0)
        """

    def clearList(*args):
        """clearList() -- Clear the Window List.
        
        example:
          - self.clearList()
        """

    def clearProperties(*args):
        """clearProperties() -- Clears all window properties.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperties()
        """

    def clearProperty(*args):
        """clearProperty(key) -- Clears the specific window property.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive. Equivalent to setProperty(key,'')
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperty('Category')
        """

    def close(*args):
        """close(self) -- Closes this window.
        
        Closes this window by activating the old window.
        The window is not deleted with this method.
        """

    def doModal(*args):
        """doModal(self) -- Display this window until close() is called.
        """

    def getControl(*args):
        """getControl(self, int controlId) -- Get's the control from this window.
        
        Throws: Exception, if Control doesn't exist
        
        controlId doesn't have to be a python control, it can be a control id
        from a xbmc window too (you can find id's in the xml files
        
        Note, not python controls are not completely usable yet
        You can only use the Control functions
        """

    def getCurrentListPosition(*args):
        """getCurrentListPosition() -- Gets the current position in the Window List.
        
        example:
          - pos = self.getCurrentListPosition()
        """

    def getFocus(*args):
        """getFocus(self, Control) -- returns the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getFocusId(*args):
        """getFocusId(self, int) -- returns the id of the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getHeight(*args):
        """getHeight(self) -- Returns the height of this screen.
        """

    def getListItem(*args):
        """getListItem(position) -- Returns a given ListItem in this Window List.
        
        position        : integer - position of item to return.
        
        example:
          - listitem = self.getListItem(6)
        """

    def getListSize(*args):
        """getListSize() -- Returns the number of items in this Window List.
        
        example:
          - listSize = self.getListSize()
        """

    def getProperty(*args):
        """getProperty(key) -- Returns a window property as a string, similar to an infolabel.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - category = win.getProperty('Category')
        """

    def getResolution(*args):
        """getResolution(self) -- Returns the resolution of the screen. The returned value is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def getWidth(*args):
        """getWidth(self) -- Returns the width of this screen.
        """

    def onAction(*args):
        """onAction(self, Action action) -- onAction method.
        
        This method will recieve all actions that the main program will send
        to this window.
        By default, only the PREVIOUS_MENU action is handled.
        Overwrite this method to let your script handle all actions.
        Don't forget to capture ACTION_PREVIOUS_MENU, else the user can't close this window.
        """

    def onClick(*args):
        """onClick(self, Control control) -- onClick method.
        
        This method will recieve all click events that the main program will send
        to this window.
        """

    def onFocus(*args):
        """onFocus(self, Control control) -- onFocus method.
        
        This method will recieve all focus events that the main program will send
        to this window.
        """

    def onInit(*args):
        """onInit(self) -- onInit method.
        
        This method will be called to initialize the window
        """

    def removeControl(*args):
        """removeControl(self, Control) -- Removes the control from this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                RuntimeError, if control is not added to this window
        
        This will not delete the control. It is only removed from the window.
        """

    def removeItem(*args):
        """removeItem(position) -- Removes a specified item based on position, from the Window List.
        
        position        : integer - position of item to remove.
        
        example:
          - self.removeItem(5)
        """

    def setCoordinateResolution(*args):
        """setCoordinateResolution(self, int resolution) -- Sets the resolution
        that the coordinates of all controls are defined in.  Allows XBMC
        to scale control positions and width/heights to whatever resolution
        XBMC is currently using.
         resolution is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def setCurrentListPosition(*args):
        """setCurrentListPosition(position) -- Set the current position in the Window List.
        
        position        : integer - position of item to set.
        
        example:
          - self.setCurrentListPosition(5)
        """

    def setFocus(*args):
        """setFocus(self, Control) -- Give the supplied control focus.
        Throws: TypeError, if supplied argument is not a Control type
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setFocusId(*args):
        """setFocusId(self, int) -- Gives the control with the supplied focus.
        Throws: 
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setProperty(*args):
        """setProperty(key, value) -- Sets a container property, similar to an infolabel.
        
        key            : string - property name.
        value          : string or unicode - value of property.
        
        *Note, Key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.setProperty('Category', 'Newest')
        """

    def show(*args):
        """show(self) -- Show this window.
        
        Shows this window by activating it, calling close() after it wil activate the
        current window again.
        Note, if your script ends this window will be closed to. To show it forever, 
        make a loop at the end of your script ar use doModal() instead
        """



class WindowXMLDialog:
    """WindowXMLDialog class.
    
    WindowXMLDialog(self, xmlFilename, scriptPath[, defaultSkin, defaultRes]) -- Create a new WindowXMLDialog script.
    
    xmlFilename     : string - the name of the xml file to look for.
    scriptPath      : string - path to script. used to fallback to if the xml doesn't exist in the current skin. (eg os.getcwd())
    defaultSkin     : [opt] string - name of the folder in the skins path to look in for the xml. (default='Default')
    defaultRes      : [opt] string - default skins resolution. (default='720p')
    
    *Note, skin folder structure is eg(resources/skins/Default/720p)
    
    example:
     - ui = GUI('script-Lyrics-main.xml', os.getcwd(), 'LCARS', 'PAL')
       ui.doModal()
       del ui
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

    def addControl(*args):
        """addControl(self, Control) -- Add a Control to this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                ReferenceError, if control is already used in another window
                RuntimeError, should not happen :-)
        
        The next controls can be added to a window atm
        
          -ControlLabel
          -ControlFadeLabel
          -ControlTextBox
          -ControlButton
          -ControlCheckMark
          -ControlList
          -ControlGroup
          -ControlImage
          -ControlRadioButton
          -ControlProgress
        """

    def addItem(*args):
        """addItem(item[, position]) -- Add a new item to this Window List.
        
        item            : string, unicode or ListItem - item to add.
        position        : [opt] integer - position of item to add. (NO Int = Adds to bottom,0 adds to top, 1 adds to one below from top,-1 adds to one above from bottom etc etc )
                                        - If integer positions are greater than list size, negative positions will add to top of list, positive positions will add to bottom of list
        example:
          - self.addItem('Reboot XBMC', 0)
        """

    def clearList(*args):
        """clearList() -- Clear the Window List.
        
        example:
          - self.clearList()
        """

    def clearProperties(*args):
        """clearProperties() -- Clears all window properties.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperties()
        """

    def clearProperty(*args):
        """clearProperty(key) -- Clears the specific window property.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive. Equivalent to setProperty(key,'')
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - win.clearProperty('Category')
        """

    def close(*args):
        """close(self) -- Closes this window.
        
        Closes this window by activating the old window.
        The window is not deleted with this method.
        """

    def doModal(*args):
        """doModal(self) -- Display this window until close() is called.
        """

    def getControl(*args):
        """getControl(self, int controlId) -- Get's the control from this window.
        
        Throws: Exception, if Control doesn't exist
        
        controlId doesn't have to be a python control, it can be a control id
        from a xbmc window too (you can find id's in the xml files
        
        Note, not python controls are not completely usable yet
        You can only use the Control functions
        """

    def getCurrentListPosition(*args):
        """getCurrentListPosition() -- Gets the current position in the Window List.
        
        example:
          - pos = self.getCurrentListPosition()
        """

    def getFocus(*args):
        """getFocus(self, Control) -- returns the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getFocusId(*args):
        """getFocusId(self, int) -- returns the id of the control which is focused.
        Throws: SystemError, on Internal error
                RuntimeError, if no control has focus
        
        """

    def getHeight(*args):
        """getHeight(self) -- Returns the height of this screen.
        """

    def getListItem(*args):
        """getListItem(position) -- Returns a given ListItem in this Window List.
        
        position        : integer - position of item to return.
        
        example:
          - listitem = self.getListItem(6)
        """

    def getListSize(*args):
        """getListSize() -- Returns the number of items in this Window List.
        
        example:
          - listSize = self.getListSize()
        """

    def getProperty(*args):
        """getProperty(key) -- Returns a window property as a string, similar to an infolabel.
        
        key            : string - property name.
        
        *Note, key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
          - category = win.getProperty('Category')
        """

    def getResolution(*args):
        """getResolution(self) -- Returns the resolution of the screen. The returned value is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def getWidth(*args):
        """getWidth(self) -- Returns the width of this screen.
        """

    def onAction(*args):
        """onAction(self, Action action) -- onAction method.
        
        This method will recieve all actions that the main program will send
        to this window.
        By default, only the PREVIOUS_MENU action is handled.
        Overwrite this method to let your script handle all actions.
        Don't forget to capture ACTION_PREVIOUS_MENU, else the user can't close this window.
        """

    def onClick(*args):
        """onClick(self, Control control) -- onClick method.
        
        This method will recieve all click events that the main program will send
        to this window.
        """

    def onFocus(*args):
        """onFocus(self, Control control) -- onFocus method.
        
        This method will recieve all focus events that the main program will send
        to this window.
        """

    def onInit(*args):
        """onInit(self) -- onInit method.
        
        This method will be called to initialize the window
        """

    def removeControl(*args):
        """removeControl(self, Control) -- Removes the control from this window.
        
        Throws: TypeError, if supplied argument is not a Control type
                RuntimeError, if control is not added to this window
        
        This will not delete the control. It is only removed from the window.
        """

    def removeItem(*args):
        """removeItem(position) -- Removes a specified item based on position, from the Window List.
        
        position        : integer - position of item to remove.
        
        example:
          - self.removeItem(5)
        """

    def setCoordinateResolution(*args):
        """setCoordinateResolution(self, int resolution) -- Sets the resolution
        that the coordinates of all controls are defined in.  Allows XBMC
        to scale control positions and width/heights to whatever resolution
        XBMC is currently using.
         resolution is one of the following:
           0 - 1080i      (1920x1080)
           1 - 720p       (1280x720)
           2 - 480p 4:3   (720x480)
           3 - 480p 16:9  (720x480)
           4 - NTSC 4:3   (720x480)
           5 - NTSC 16:9  (720x480)
           6 - PAL 4:3    (720x576)
           7 - PAL 16:9   (720x576)
           8 - PAL60 4:3  (720x480)
           9 - PAL60 16:9 (720x480)
        """

    def setCurrentListPosition(*args):
        """setCurrentListPosition(position) -- Set the current position in the Window List.
        
        position        : integer - position of item to set.
        
        example:
          - self.setCurrentListPosition(5)
        """

    def setFocus(*args):
        """setFocus(self, Control) -- Give the supplied control focus.
        Throws: TypeError, if supplied argument is not a Control type
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setFocusId(*args):
        """setFocusId(self, int) -- Gives the control with the supplied focus.
        Throws: 
                SystemError, on Internal error
                RuntimeError, if control is not added to a window
        
        """

    def setProperty(*args):
        """setProperty(key, value) -- Sets a container property, similar to an infolabel.
        
        key            : string - property name.
        value          : string or unicode - value of property.
        
        *Note, Key is NOT case sensitive.
               You can use the above as keywords for arguments and skip certain optional arguments.
               Once you use a keyword, all following arguments require the keyword.
        
        example:
          - self.setProperty('Category', 'Newest')
        """

    def show(*args):
        """show(self) -- Show this window.
        
        Shows this window by activating it, calling close() after it wil activate the
        current window again.
        Note, if your script ends this window will be closed to. To show it forever, 
        make a loop at the end of your script ar use doModal() instead
        """



__author__ = str
__credits__ = str
__date__ = str
__platform__ = str
__version__ = str
def getCurrentWindowDialogId(*args):
    """getCurrentWindowDialogId() -- Returns the id for the current 'active' dialog as an integer.
    
    example:
      - wid = xbmcgui.getCurrentWindowDialogId()
    """

def getCurrentWindowId(*args):
    """getCurrentWindowId() -- Returns the id for the current 'active' window as an integer.
    
    example:
      - wid = xbmcgui.getCurrentWindowId()
    """

def lock(*args):
    """lock() -- Lock the gui until xbmcgui.unlock() is called.
    
    *Note, This will improve performance when doing a lot of gui manipulation at once.
           The main program (xbmc itself) will freeze until xbmcgui.unlock() is called.
    
    example:
      - xbmcgui.lock()
    """

def unlock(*args):
    """unlock() -- Unlock the gui from a lock() call.
    
    example:
      - xbmcgui.unlock()
    """

