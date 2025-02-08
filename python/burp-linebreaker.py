from burp import IBurpExtender
from burp import IMessageEditorTab
from burp import IMessageEditorTabFactory


class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Newline Renderer")
        callbacks.registerMessageEditorTabFactory(self)

    def createNewInstance(self, controller, editable):
        return NewlineRenderTab(self, controller, editable)


class NewlineRenderTab(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._editable = editable
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(editable)
        self._currentMessage = ""

    def getTabCaption(self):
        return "Newline View"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):
        return True

    def setMessage(self, content, isRequest):
        if content is None:
            self._txtInput.setText(None)
            self._currentMessage = None
        else:
            text = self._extender._helpers.bytesToString(content)
            text = text.replace("\\n", "\n")  # Replace literal \n with actual new lines
            self._currentMessage = self._extender._helpers.stringToBytes(text)
            self._txtInput.setText(self._currentMessage)

    def getMessage(self):
        if self._txtInput.isTextModified():
            return self._txtInput.getText()
        return self._currentMessage

    def isModified(self):
        return self._txtInput.isTextModified()

    def getSelectedData(self):
        return self._txtInput.getSelectedText()
