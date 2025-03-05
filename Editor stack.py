class Editor:
    def __init__(self):
        self.text = ""
        self.history_stack = []
        self.redo_stack = []

    def append_text(self, text):
        self.history_stack.append(self.text)
        self.text += text

    def undo(self):
        if self.history_stack:
            self.redo_stack.append(self.text)
            self.text = self.history_stack.pop()
        else:
            print("Undo operation not possible. No history available.")

    def redo(self):
        if self.redo_stack:
            self.history_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Redo operation not possible. No redo history \
                   available.")

    def display_text(self):
        print(self.text)


editor = Editor()

editor.append_text("Hello, ")
editor.append_text("CodeSignal!")
editor.display_text()
editor.undo()
editor.display_text()
editor.undo()
editor.redo()
editor.display_text()
editor.redo()
editor.display_text()
editor.redo()
editor.undo()

