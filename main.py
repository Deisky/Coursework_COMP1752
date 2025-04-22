# Import the main GUI application class from gui_app module
from gui_app import TrackPlayerApp

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Create an instance of the TrackPlayerApp
    app = TrackPlayerApp()

    # Start the GUI application
    app.run()
