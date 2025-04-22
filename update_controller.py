import track_library as library  # Importing the track_library module to interact with the library data
from base_controller import BaseController  # Importing the BaseController class to extend the functionality

class UpdateController(BaseController):  # UpdateController inherits from BaseController to access common methods
    def update_tracks_clicked(self):  # Method called when the "Update Track Rating" button is clicked
        try:
            # Attempt to retrieve and format the track ID and rating from the entry fields
            key = "%02d" % int(self.w.text1_entry.get().strip())  # Format the track ID as a two-digit string
            rating = int(self.w.text3_entry.get().strip())  # Get the rating and ensure it's an integer

            # Check if the rating is within the valid range (1 to 5)
            if not (1 <= rating <= 5):
                info = f"Invalid rating {rating}. Must be 1–5."  # Inform the user if the rating is invalid
            # Check if the track with the given ID exists in the library
            elif library.get_name(key) is not None:
                old = library.get_rating(key)  # Retrieve the current rating of the track
                library.set_rating(key, rating)  # Update the track rating in the library
                # Provide information about the updated rating
                info = f"Updated rating of '{library.get_name(key)}' from {old} to {rating}"
            else:
                info = f"Track ID {key} not found."  # Inform the user if the track ID is not found in the library
        except ValueError:
            info = "Please enter valid ID and rating."  # Catch invalid input and notify the user

        self.w.status_lbl.config(text=info)  # Display the result message in the status label
