import csv

from tabulate import tabulate


class Note:
    """
    A class to represent a note element.

    Attributes
    ----------
    name: str
        note's title
    note: str
        some entry of a note
    rating: float
        note's rating (from 1 to 5)

    Methods
    -------
    get_field_values()
        Returns the list of attribute values of the note instance
    """

    def __init__(self, name: str, note: str, rating: float):
        self.name = name
        self.note = note
        self.rating = float(rating)

    def __str__(self):
        return f"{self.name} | {self.note} | {self.rating}"

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value: float):
        if value < 1 or value > 5:
            raise ValueError("`rating` cannot be lower than 1 or greater than 5")
        self._rating = value

    def get_field_values(self):
        return [v for v in self.__dict__.values()]


class Movie(Note):
    """
    A class to represent a movie.

    Attributes
    ----------
    name: str
        movie's title
    note: str
        some movie's notation
    rating: float
        movie's rating (from 1 to 5)
    """

    def __init__(self, name: str, note: str, rating: float):
        super().__init__(name, note, rating)


class NotesManager:
    """
    A class to represent a note's manager.

    Attributes
    ----------
    note: Note
        name of class that can represent a note (Note class or its inheritors)
    notes_list: list[note]
        list of notes
    filename: str
        file to interact with

    Methods
    -------
    read_notes()
        Reads all notes from file
    add_note(note)
        Writes the note to the file
    remove_note(index)
        Deletes the note from the file by its index
    print_notes()
        Prints to console all notes from file
    """

    def __init__(self, note, filename: str = "movieNotes.csv"):
        self.note = note
        self.filename = filename
        self.notes_list: list[Note] = []

    def read_notes(self):
        with open(self.filename, "r") as notes_file:
            reader = csv.reader(notes_file)
            self.notes_list = [self.note(*row) for row in reader]

    def add_note(self, note: Movie):
        with open(self.filename, "a") as notes_file:
            writer = csv.writer(notes_file)
            writer.writerow(note.get_field_values())
        self.notes_list.append(note)

    def remove_note(self, note_index: int):
        try:
            del self.notes_list[note_index]
        except IndexError:
            raise ValueError("No such note index in the file")

        with open(self.filename, "w") as notes_file:
            writer = csv.writer(notes_file)
            for elem in self.notes_list:
                writer.writerow(elem.get_field_values())

    def print_notes(self):
        with open(self.filename, "r") as notes_file:
            reader = csv.reader(notes_file)
            rows = [row for row in reader]
            print(tabulate(rows, tablefmt="grid"))


def get_top_rated_movies(movies: list[Movie], rating: float = None) -> list[Movie]:
    if rating is None:
        rating = max(movies, key=lambda movie: movie.rating).rating
    return [movie for movie in movies if movie.rating >= rating]


def get_low_rated_movies(movies: list[Movie], rating: float = None) -> list[Movie]:
    if rating is None:
        rating = min(movies, key=lambda movie: movie.rating).rating
    return [movie for movie in movies if movie.rating <= rating]


def get_avg_movies_rating(movies: list[Movie]) -> float:
    return sum([movie.rating for movie in movies]) / len(movies)
