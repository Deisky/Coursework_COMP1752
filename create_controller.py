# Import the track library for accessing tracks
# Import the base controller class to inherit shared functionality
import track_library as library
from base_controller import BaseController
import shared_state

# Controller responsible for creating a custom track list
class CreateController(BaseController):

    def create_new_list(self):
        """
        Adds a selected track to the user's custom playlist based on input.
        Input can be a track ID, name, or artist.
        Updates the play list and shows a status message.
        """
        play_list = shared_state.play_list

        try:
            track_id = "%02d" % int(self.w.text1_entry.get().strip())

            # Check if the track exists
            track_name = library.get_name(track_id)
            play_count = library.get_play_count(track_id)

            if track_name:  # Assuming None or empty if not found
                new_track = f"{track_name} - (Plays: {play_count})\n"

                # Add the valid ID to the play_list
                play_list.append(track_id)

                # Update playlist display
                current = self.w.play_list.get("1.0", "end-1c")
                self.set_text(self.w.play_list, current + new_track)

                info = f"Track {track_id} added to new list."
            else:
                info = f"Track {track_id} not found."

            self.w.status_lbl.config(text=info)
        except ValueError:
            self.w.status_lbl.config(text="Please input ID")

    @staticmethod
    def search_track(query):
        """
        Searches for a track by ID, name, or artist.
        Returns the track ID if found, otherwise None.
        """
        try:
            query = "%02d" % int(query)  # Try to format as two-digit ID if it's a number
        except ValueError:
            query = query.lower()        # Otherwise, treat as lowercase string for name/artist matching

        # Search through the library for a matching track
        for key, item in library.library.items():
            if key == query or item.name.lower() == query or item.artist.lower() == query:
                return key
        return None  # Return None if no match found
