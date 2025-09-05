class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_text):
        self.undo_stack.append(self.document)
        self.redo_stack.clear()
        self.document = new_text

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()

    def display(self):
        print("Current Document State:")
        print(self.document)

# Example usage
editor = TextEditor()

editor.make_change("Hello, World!")
editor.display()

editor.make_change("Hello, OpenAI!")
editor.display()

editor.undo()
editor.display()

editor.redo()
editor.display()

editor.undo()
editor.display()

editor.make_change("Hello, OpenAI!")
editor.display()
