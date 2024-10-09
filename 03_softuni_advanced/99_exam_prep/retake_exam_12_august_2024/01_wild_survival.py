from collections import deque


def main():
    bee_group = deque(int(x) for x in input().split())
    attackers_group = [int(x) for x in input().split()]

    while bee_group and attackers_group:
        defender = bee_group[0]
        attacker = attackers_group[-1]

        while True:

            defender -= 7

            if defender <= 0:
                bee_group.popleft()
                if defender == 0:
                    attacker -= 1
                    if attacker == 0:
                        attackers_group.pop()
                        break
                attackers_group[-1] = attacker
                break

            attacker -= 1

            if attacker <= 0:
                attackers_group.pop()
                bee_group[0] = defender
                bee_group.rotate(-1)
                break

    print("The final battle is over!")

    if not bee_group and not attackers_group:
        print("But no one made it out alive!")
    elif bee_group:
        print(f"Bee groups left: {', '.join(map(str, bee_group))}")
    else:
        print(f"Bee-eater groups left: {', '.join(map(str, attackers_group))}")


if __name__ == "__main__":
    main()
