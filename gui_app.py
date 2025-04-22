# Import necessary modules
import tkinter as tk  # Tkinter for building the GUI
from widgets import Widgets  # Custom module that sets up GUI widgets
from main_controller import MainController  # Logic/controller handling user interaction
import font_manager as fonts  # Module to manage fonts

# Main application class for the track player
class TrackPlayerApp:
    def __init__(self):
        # Create the main application window
        self.window = tk.Tk()
        self.window.geometry("760x370")  # Set window size
        self.window.title("JukeBox")  # Set window title
        self.window.configure(bg="misty rose")  # Set background color
        self.window.resizable(False, False)  # Disable window resizing

        # Apply custom font configuration
        fonts.configure()

        # Initialize GUI widgets and controller logic
        self.widgets = Widgets(self.window)  # Set up GUI components
        self.controller = MainController(self.widgets)  # Connect widgets to logic

    def run(self):
        # Start the Tkinter event loop
        self.window.mainloop()
