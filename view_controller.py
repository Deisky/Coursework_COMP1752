# Import the track library for accessing track data
# Import the base controller to inherit common functionality
import track_library as library
from base_controller import BaseController


# Controller responsible for viewing the details of a specific track
class ViewController(BaseController):

    def view_tracks_clicked(self):
        """
        Handles the 'View Track's Detail' action.
        Retrieves the track ID from user input, fetches track details from the library,
        and displays them in the status text area. Shows an error if input is invalid or not found.
        """
        keys = self.w.text1_entry.get().strip()  # Get user input from the first entry field

        if not keys:
            # If no ID is entered, notify the user
            self.w.status_lbl.config(text="Please input ID")
            return

        try:
            key = "%02d" % int(keys)  # Format the input into a two-digit string (e.g., 01, 09, 10)
        except ValueError:
            # If the input is not a valid number, show an error message
            self.w.status_lbl.config(text="Invalid ID")
            return

        # If the track with the given ID exists
        if library.get_name(key):
            # Compose a string with all track details
            track_details = f"{library.get_name(key)}\n{library.get_artist(key)}\n" \
                            f"rating: {library.get_rating(key)}\nplays: {library.get_play_count(key)}"
            # Display the track details in the text area
            self.set_text(self.w.status_txt, track_details)
        else:
            # If no track found with that ID, show an error in the status label
            self.w.status_lbl.config(text=f"Track {key} not found")
