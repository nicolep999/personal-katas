n, m = input().split()

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}


end_set = n_set.intersection(m_set)
print(*end_set, sep="\n")
