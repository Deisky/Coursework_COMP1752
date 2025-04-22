# BaseController serves as a parent class for other controllers
# It provides shared utilities, such as setting text in text areas.

class BaseController:
    def __init__(self, widgets):
        # Store reference to the GUI widgets (e.g., buttons, text fields)
        self.w = widgets

    @staticmethod
    def set_text(area, content):
        """
        Utility method to safely update a text widget.
        It enables the widget, clears existing text, inserts new content,
        and then disables it again to prevent user edits.
        """
        area.config(state='normal')    # Enable editing
        area.delete("1.0", "end")      # Clear existing content
        area.insert("1.0", content)    # Insert new content
        area.config(state='disabled')  # Disable editing to make it read-only
