from project.song import Song


class Album:

    def __init__(self, name: str, *args: tuple[Song]):
        self.name = name
        self.published = False
        self.songs: list = list(args)

    def add_song(self, song: Song) -> str:
        if self.published:
            return f"Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f"Cannot remove songs. Album is published."
        song_to_remove = next(
            (song for song in self.songs if song.name == song_name), None
        )
        if song_to_remove:
            self.songs.remove(song_to_remove)
            return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = [
            f"Album {self.name}",
            *[f"== {song.get_info()}" for song in self.songs],
        ]
        return "\n".join(result)
