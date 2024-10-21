class Solution:
    def __init__(self):
        self.max_count = None

    def maxUniqueSplit(self, s: str) -> int:
        solution_set = set()
        self.max_count = 0

        def backtrack(start: int):
            if start == len(s):
                self.max_count = max(self.max_count, len(solution_set))
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring not in solution_set:
                    solution_set.add(substring)
                    backtrack(end)
                    solution_set.remove(substring)

        backtrack(0)
        return self.max_count


solution_instance = Solution()
print(solution_instance.maxUniqueSplit("ababccc"))  # Output: 5
print(solution_instance.maxUniqueSplit("aba"))  # Output: 2
print(solution_instance.maxUniqueSplit("aa"))  # Output: 1
