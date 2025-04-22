# Import the track management module and the base controller class
import track_library as library
from base_controller import BaseController


# Controller for listing and filtering tracks
class ListController(BaseController):

    def list_tracks_clicked(self):
        """
        Handles the 'List All Track' action.
        Retrieves all tracks from the library and displays them in the list text area.
        Also updates the status label to indicate the action taken.
        """
        track_list = library.list_all()  # Get a formatted string of all tracks
        self.set_text(self.w.list_txt, track_list)  # Display tracks in the GUI
        self.w.status_lbl.config(text="Successful")  # Update status message

    def filter_author(self):
        """
        Handles the 'Filter Artist' action.
        Filters the track list by the artist name entered by the user.
        Displays matching tracks or an error/status message if none found.
        """
        authors = self.w.text2_entry.get().strip()  # Get user input
        if len(authors) >= 3:
            author = authors
            if not author:
                # If no input provided, show an error in the status label
                self.w.status_lbl.config(text="Please Input Artist")
                return
            # Find all tracks matching the author (case-insensitive)
            matching = [f"{key}: {item.name}"
                    for key, item in library.library.items()
                        if author.lower() in item.artist.lower()]

            if not matching:
            # If no matches, notify user
                self.w.status_lbl.config(text=f"No Artist named: {author}")
            else:
            # Display matching tracks in the list area
                self.set_text(self.w.list_txt, f"Artist: {author}\nTracks:\n" + "\n".join(matching))
                self.w.status_lbl.config(text="Successful")
        else:
            self.w.status_lbl.config(text="It must be 3 or more characters")
