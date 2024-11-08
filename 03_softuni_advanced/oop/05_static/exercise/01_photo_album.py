class PhotoAlbum:

    PAGE_SIZE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: list[list[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        pages_needed = (photos_count + 3) // PhotoAlbum.PAGE_SIZE
        return cls(pages_needed)

    def add_photo(self, photo: str) -> str:
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_SIZE:
                page.append(photo)
                return (
                    f"{photo} photo added successfully on page {i + 1} slot {len(page)}"
                )
        return "No more free slots"

    def display(self) -> str:
        result = "-----------\n"
        for page in self.photos:
            result += " ".join("[]" for _ in page) + "\n"
            result += "-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
