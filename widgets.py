# Import necessary modules for GUI components
import tkinter as tk
import tkinter.scrolledtext as tkst  # For scrollable text areas
from tkinter import ttk  # For themed widgets like Combobox

# Class that creates and manages the GUI widgets
class Widgets:

    @staticmethod
    def limit_length(text):
        # Returns True if the input text is 50 characters or fewer
        return len(text) <= 50

    def __init__(self, window):
        # Register the input validator function with Tkinter
        len_limit = window.register(self.limit_length)

        # Dropdown menu for selecting an action
        self.combo = ttk.Combobox(window, justify="center", values=[
            "List All Track", "View Track's Detail",
            "Filter Artist", "Create Track List", "Update Track's Rating"
        ])
        self.combo.config(state="readonly")  # User cannot type in the box
        self.combo.set("List All Track")  # Default value
        self.combo.grid(row=0, column=1, padx=5, pady=5, sticky="E")

        # Label and entry for track information (ID or name)
        self.text1_lbl = tk.Label(window, text="Track's Information", bg="misty rose")
        self.text1_lbl.grid(row=0, column=0, padx=5, pady=5, sticky="NW")
        self.text1_entry = tk.Entry(window, width=20, validate='key', validatecommand=(len_limit, '%P'))
        self.text1_entry.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        # Label and entry for filtering by artist name
        self.text2_lbl = tk.Label(window, text="Artist to filter", bg="misty rose")
        self.text2_lbl.grid(row=1, column=0, padx=5, pady=5, sticky="NW")
        self.text2_entry = tk.Entry(window, width=20, validate='key', validatecommand=(len_limit, '%P'))
        self.text2_entry.grid(row=1, column=0, padx=5, pady=5, sticky="E")

        # Label and entry for updating a track's rating
        self.text3_lbl = tk.Label(window, text="Track's New Rating", bg="misty rose")
        self.text3_lbl.grid(row=1, column=1, padx=5, pady=5, sticky="NW")
        self.text3_entry = tk.Entry(window, width=22, validate='key', validatecommand=(len_limit, '%P'))
        self.text3_entry.grid(row=1, column=1, padx=5, pady=5, sticky="E")

        # Label for the dropdown menu
        self.combo_box_lbl = tk.Label(window, anchor="center", text="Menu Box", bg="misty rose")
        self.combo_box_lbl.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        # Scrollable text box to list all tracks or filtered results
        self.list_txt = tkst.ScrolledText(window, width=44, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, sticky="W", padx=(10,5), pady=10)
        self.list_txt.config(state="disabled")  # Make it read-only initially

        # Scrollable text box to display selected track list
        self.play_list = tkst.ScrolledText(window, width=42, height=4, wrap="none")
        self.play_list.grid(row=2, column=1, sticky="WS", padx=5, pady=(0,130))
        self.play_list.config(state="disabled")
        self.play_lbl = tk.Label(window, text="List of Tracks", background="misty rose")
        self.play_lbl.grid(row=2, column=1, sticky="WN", padx=5, pady=(8, 0))

        # Scrollable text box to show track details/status messages
        self.status_txt = tkst.ScrolledText(window, width=25, height=4, wrap="none")
        self.status_txt.grid(row=2, column=1, sticky="SW", padx=5, pady=(0,8))
        self.status_txt.config(state="disabled")
        self.status_lbl = tk.Label(window, text="Track Detail", background="misty rose")
        self.status_lbl.grid(row=2, column=1, sticky="SW", padx=5, pady=(0,92))

        # Footer message label
        self.status_lbl = tk.Label(window, text="Welcome to jukebox, hope you have a nice Day!", background="misty rose")
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10)

        # Buttons: ENTER, PLAY, RESET
        self.status_btn = tk.Button(window, text="ENTER", width=10, bg="slate blue", fg="cyan")
        self.status_btn.grid(row=2, column=1, sticky="SE", padx=(10,0), pady=(0,8))

        self.play_btn = tk.Button(window, text="PLAY", width=10, bg="slate blue", fg="cyan")
        self.play_btn.grid(row=2, column=1, sticky="SE", padx=(10,0), pady=(0,86))

        self.reset_btn = tk.Button(window, text="RESET", width=10, bg="slate blue", fg="cyan")
        self.reset_btn.grid(row=2, column=1, sticky="SE", padx=(10,0), pady=(0,47))
