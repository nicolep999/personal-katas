def accommodate(*args, **kwargs):
    accommodations = {}
    unaccommodated_guests = 0

    rooms = sorted(kwargs.items(), key=lambda r: (r[1], r[0]))

    for guests in args:
        is_accommodated = False

        for room_key, capacity in rooms:
            if capacity >= guests:
                room_number = room_key.split("_")[1]
                accommodations[room_number] = guests
                rooms.remove((room_key, capacity))
                is_accommodated = True
                break

        if not is_accommodated:
            unaccommodated_guests += guests

    if accommodations:
        result = [f"A total of {len(accommodations)} accommodations were completed!"]
        for room_number in sorted(accommodations.keys(), key=lambda x: int(x)):
            result.append(
                f"<Room {room_number} accommodates {accommodations[room_number]} guests>"
            )
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result).strip()
