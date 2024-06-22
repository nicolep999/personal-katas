def main():
    plunder_days = int(input())
    daily_plunder = int(input())
    plunder_target = float(input())

    total_plunder = 0
    days_passed = 0

    while True:

        days_passed += 1

        total_plunder += daily_plunder

        if days_passed % 3 == 0:
            total_plunder += daily_plunder * 0.5
        if days_passed % 5 == 0:
            total_plunder -= total_plunder * 0.3

        if days_passed >= plunder_days:
            if total_plunder >= plunder_target:
                print(f"Ahoy! {total_plunder:.2f} plunder gained.")
                break
            print(
                f"Collected only {(total_plunder / plunder_target) * 100:.2f}% of the plunder."
            )
            break


main()
