# Import the track library for accessing track data
# Import the base controller for common utilities like set_text
import track_library as library
from base_controller import BaseController
import shared_state

# Controller to handle actions related to playing and resetting the playlist
class PlayController(BaseController):

    def play_the_list(self):
        """
        Simulates playing the tracks in the playlist.
        For each track, it identifies and increments its play count in the library.
        Also updates the play list display to reflect new play counts.
        """
        # Make sure the play list exists
        play_list = shared_state.play_list

        if not play_list:
            # If play list is empty, display a warning
            self.w.status_lbl.config(text="There is nothing to PLAY!")
        else:
            track_counts = {}

            # Count how many times each track ID appears
            for track_id in play_list:
                track_counts[track_id] = track_counts.get(track_id, 0) + 1

            # Increment play counts in the library
            for key, count in track_counts.items():
                for _ in range(count):
                    library.increment_play_count(key)

            # Build updated play list text with new play counts
            new_text = ""
            for track_id in play_list:
                new_text += f"{library.get_name(track_id)} - (Plays: {library.get_play_count(track_id)})\n"
            # Update the display
            self.set_text(self.w.play_list, new_text)
            self.w.status_lbl.config(text="List played")

    def reset_the_list(self):
        """
        Clears the playlist text area and resets the status label.
        """
        # Check if playlist is empty
        if len(shared_state.play_list) == 0:
            self.w.status_lbl.config(text="There is nothing to DELETE!")
        else:
            # Clear the playlist and update status
            shared_state.play_list.clear()
            self.set_text(self.w.play_list, "")
            self.w.status_lbl.config(text="List was reset successfully")
