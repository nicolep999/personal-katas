from typing import Union


class Integer:

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> Union["Integer", str]:
        if isinstance(float_value, float):
            return cls(int(float_value))
        return f"value is not a float"

    @classmethod
    def from_roman(cls, value: str) -> Union["Integer", str]:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0
        for numeral in reversed(value):
            current_value = roman_values.get(numeral)
            if current_value is None:
                return "invalid Roman numeral"
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        return cls(total)

    @classmethod
    def from_string(cls, value: str) -> Union["Integer", str]:
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
