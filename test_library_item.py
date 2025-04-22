import pytest
from library_item import LibraryItem

# Creating test instances
lib_1 = LibraryItem("Song A", "Artist A", 1)
lib_2 = LibraryItem("Song B", "Artist B", 2)
lib_3 = LibraryItem("Song C", "Artist C", 3)
lib_4 = LibraryItem("Song D", "Artist D", 4)
lib_5 = LibraryItem("Song E", "Artist E", 5)

@pytest.mark.parametrize(
    "name, artist, rating",
    [
        ("Song A", "Artist A", 1),
        ("Song B", "Artist B", 2),
        ("Song C", "Artist C", 3),
        ("Song D", "Artist D", 4),
        ("Song E", "Artist E", 5),
    ]
)
def test_library_item_constructor(name, artist, rating):
    item = LibraryItem(name, artist, rating)
    assert item.name == name
    assert item.artist == artist
    assert item.rating == rating
    assert item.play_count == 0

def test_stars():
    """Ensure that star ratings are correctly assigned."""
    assert lib_1.rating == 1
    assert lib_2.rating == 2
    assert lib_3.rating == 3
    assert lib_4.rating == 4
    assert lib_5.rating == 5

def test_info():
    """Check if the info() method formats the output correctly."""
    assert lib_1.info() == "Song A - Artist A *"
    assert lib_2.info() == "Song B - Artist B **"
    assert lib_3.info() == "Song C - Artist C ***"
    assert lib_4.info() == "Song D - Artist D ****"
    assert lib_5.info() == "Song E - Artist E *****"

# Run the tests when executed as a script
if __name__ == "__main__":
    pytest.main(["-v"])  # '-v' for verbose output
