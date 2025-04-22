from library_item import LibraryItem  # Importing LibraryItem class
import csv  # Importing CSV module for file operations


# Function to list all items in the library
def list_all():
    output = ""
    for i in library:
        item = library[i]
        output += f"{i} {item.info()}\n"
    return output


# Function to get the name of an item using its key
def get_name(i):
    try:
        item = library[i]
        return item.name
    except KeyError:
        return None


# Function to get the artist of an item using its key
def get_artist(i):
    try:
        item = library[i]
        return item.artist
    except KeyError:
        return None


# Function to get the rating of an item using its key
def get_rating(i):
    try:
        item = library[i]
        return item.rating
    except KeyError:
        return -1  # Return -1 if the key is not found


# Function to set the rating of an item and update the library
def set_rating(i, rating):
    try:
        item = library[i]
        item.rating = rating
        update_library()  # Save changes to the CSV file
    except KeyError:
        return


# Function to get the play count of an item using its key
def get_play_count(i):
    try:
        item = library[i]
        return item.play_count
    except KeyError:
        return -1  # Return -1 if the key is not found


# Function to increment the play count of an item and update the library
def increment_play_count(i):
    try:
        item = library[i]
        item.play_count += 1
        update_library()  # Save changes to the CSV file
    except KeyError:
        return


# Function to update the library CSV file
def update_library():
    file_name = "_library.csv"

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Artist", "Rating", "Play Count"])  # Write header row

        for i in range(1, len(library) + 1):
            a = "%02d" % i  # Formatting key as two-digit string
            writer.writerow([
                library[a].name,
                library[a].artist,
                library[a].rating,
                library[a].play_count
            ])


# Function to read the library from a CSV file
def read_library():
    global library  # Initialize empty dictionary
    library = {}
    with open("_library.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        i = 1
        for detail in reader:
            try:
                rating = int(detail[2])  # Convert rating to integer
                # Ensure rating is within valid range (0-5)
                if rating < 0:
                    rating = 0
                elif rating > 5:
                    rating = 5
            except ValueError:
                rating = 0  # Default to 0 if invalid

            try:
                play_count = int(detail[3])  # Convert play count to integer
            except ValueError:
                play_count = 0  # Default to 0 if invalid

            a = "%02d" % i  # Formatting key as two-digit string
            library[a] = LibraryItem(detail[0], detail[1], rating)
            library[a].play_count = play_count
            i += 1

        return library


# Load library data from CSV file
library = read_library()

# Main execution block
if __name__ == "__main__":
    read_library()
    update_library()

    # Print the library contents
    print(library)
    for key in library:
        print(library[key].info())