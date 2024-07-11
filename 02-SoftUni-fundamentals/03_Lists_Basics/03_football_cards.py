a_team = 11
b_team = 11
terminated = False

command = set(map(str, input().split()))

for x in command:
    x = x.split("-")
    team = x[0]
    player = int(x[1])
    if team == "A":
        a_team -= 1
    else:
        b_team -= 1

    if a_team < 7 or b_team < 7:
        print(f"Team A - {a_team}; Team B - {b_team}")
        print("Game was terminated")
        terminated = True
        break

if not terminated:
    print(f"Team A - {a_team}; Team B - {b_team}")
