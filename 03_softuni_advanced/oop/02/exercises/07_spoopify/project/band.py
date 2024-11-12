from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        is_added = next((a for a in self.albums if a._name == album._name), None)
        if is_added:
            return f"Band {self.name} already has {album._name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album._name}."

    def remove_album(self, album_name: str) -> str:
        album_to_remove = next((a for a in self.albums if a._name == album_name), None)
        if not album_to_remove:
            return f"Album {album_name} is not found."
        if album_to_remove.published and album_to_remove:
            return f"Album has been published. It cannot be removed."
        if album_to_remove:
            self.albums.remove(album_to_remove)
            return f"Album {album_name} has been removed."

    def details(self):
        result = [
            f"Band {self.name}",
            *[x.details() for x in self.albums],
        ]
        return f"\n".join(result)
