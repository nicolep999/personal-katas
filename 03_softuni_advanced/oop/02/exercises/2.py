class Time:

    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self) -> str:
        self.seconds += 1
        self.minutes += self.seconds // (Time.max_seconds + 1)
        self.hours += self.minutes // (Time.max_minutes + 1)

        self.seconds %= Time.max_seconds + 1
        self.minutes %= Time.max_minutes + 1
        self.hours %= Time.max_hours + 1

        return self.get_time()
