class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numbers = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        pass

    # TODO


solution_instance = Solution()
print(solution_instance.intToRoman(3749))
print(solution_instance.intToRoman(58))
print(solution_instance.intToRoman(1994))
