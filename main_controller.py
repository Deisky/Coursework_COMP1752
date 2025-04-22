# Import individual controller classes for handling different user actions
from play_controller import PlayController
from list_controller import ListController
from view_controller import ViewController
from create_controller import CreateController
from update_controller import UpdateController

# Main controller that coordinates between the GUI widgets and functionality
class MainController:
    def __init__(self, widgets):
        # Instantiate each controller with access to the GUI widgets
        self.play = PlayController(widgets)
        self.listing = ListController(widgets)
        self.view = ViewController(widgets)
        self.create = CreateController(widgets)
        self.update = UpdateController(widgets)
        self.w = widgets  # Store widgets reference for use in event bindings

        # Bind GUI buttons to appropriate controller methods
        self.w.status_btn.config(command=self.route_option)       # Calls the method based on user selection
        self.w.play_btn.config(command=self.play.play_the_list)   # Starts playback
        self.w.reset_btn.config(command=self.play.reset_the_list) # Resets the current playlist

    # Routes the selected menu option from the ComboBox to the appropriate controller
    def route_option(self):
        choice = self.w.combo.get()  # Get selected option from the dropdown
        match choice:

            case "List All Track":
                self.listing.list_tracks_clicked()# Display all tracks
            case "Filter Artist":
                self.listing.filter_author()  # Filter tracks by artist
            case "View Track's Detail":
                self.view.view_tracks_clicked()  # Show track details
            case "Create Track List":
                self.create.create_new_list()  # Create a new playlist
            case "Update Track's Rating":
                self.update.update_tracks_clicked()  # Update rating of a track