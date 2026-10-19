# KINEMATICS - constant acceleration in one dimension.
# SI units: meters, seconds, m/s, and m/s^2.
from math import sqrt


# Keep asking if the input is not a finite decimal number.
def number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value - value == 0:
                return value
        except ValueError:
            pass

        print("Enter a decimal number.")
        print("Example: 0.5, not 1/2")


def elapsed_time():
    while True:
        t = number("Time (s): ")
        if t >= 0:
            return t

        print("Time must be >= 0.")


def result(label, value, unit):
    print()
    print(label, round(value, 4), unit)


def help_screen():
    print("\nCONSTANT ACCEL ONLY")
    print("Pick a + direction.")
    print("Use signed v, a, dx.")
    print("dx = displacement,")
    print("not distance traveled.")
    print("dx = final position")
    print("   - initial position")
    input("Enter for more: ")

    print("\nFor up positive:")
    print("free fall a = -9.8")
    print("Units: m/s^2")
    print("vi = initial velocity")
    print("vf = final velocity")
    print("Two times may fit.")
    print("Choose the event asked.")


# Solve dx = vi*t + a*t^2/2; return only nonnegative times.
def times_from_dx(vi, a, dx):
    if a == 0:
        if vi == 0:
            if dx == 0:
                print("Any time >= 0 fits.")
                print("Velocity stays zero.")
            else:
                print("No solution: at rest.")
            return []

        times = [dx / vi]

    else:
        disc = vi * vi + 2 * a * dx
        # Decimal rounding can make an exact turning point slightly negative.
        scale = abs(vi * vi) + abs(2 * a * dx)
        if disc < 0 and abs(disc) <= 1e-12 * scale:
            disc = 0.0

        if disc < 0:
            print("Position not reached.")
            return []

        # Stable quadratic formula avoids subtracting near-equals.
        root = sqrt(disc)
        if vi >= 0:
            q = -0.5 * (vi + root)
        else:
            q = -0.5 * (vi - root)

        if q == 0:
            times = [0.0]
        elif disc == 0:
            times = [-vi / a]
        else:
            times = [2 * q / a, -dx / q]

    valid = []
    for t in times:
        if t >= 0:
            valid.append(t)

    valid.sort()
    if not valid:
        print("No time >= 0 fits.")

    return valid


def run():
    print("CONSTANT ACCEL ONLY")
    print("SI units; signed values")
    print("Choose H for help.")

    while True:
        print("\nKINEMATICS\n")
        print("1. vf using vi,a,t")
        print("2. vi using vf,a,t")
        print("3. a using vi,vf,t")
        print("4. dx using vi,a,t")
        print("5. t using vi,vf,a")
        print("6. dx using vi,vf,t")
        print("7. vf using vi,a,dx")
        print("8. t using vi,a,dx")
        print("9. a using vi,vf,dx")
        print("H. Help   0. Exit")
        choice = input("\nChoose: ")
        print()

        if choice == "0":
            break

        elif choice in ["h", "H"]:
            help_screen()

        elif choice == "1":
            print("vf = vi + a*t\n")
            vi = number("Initial v (m/s): ")
            a = number("Accel (m/s^2): ")
            t = elapsed_time()

            result("Final v =", vi + a * t, "m/s")

        elif choice == "2":
            print("vi = vf - a*t\n")
            vf = number("Final v (m/s): ")
            a = number("Accel (m/s^2): ")
            t = elapsed_time()

            result("Initial v =", vf - a * t, "m/s")

        elif choice == "3":
            print("a = (vf-vi)/t\n")
            vi = number("Initial v (m/s): ")
            vf = number("Final v (m/s): ")
            t = elapsed_time()

            if t == 0:
                if vi == vf:
                    print("Accel undetermined.")
                else:
                    print("No solution at t=0.")
            else:
                result("Accel =", (vf - vi) / t, "m/s^2")

        elif choice == "4":
            print("dx = vi*t + a*t^2/2\n")
            vi = number("Initial v (m/s): ")
            a = number("Accel (m/s^2): ")
            t = elapsed_time()

            result("dx =", vi * t + 0.5 * a * t**2, "m")

        elif choice == "5":
            print("t = (vf-vi)/a\n")
            vi = number("Initial v (m/s): ")
            vf = number("Final v (m/s): ")
            a = number("Accel (m/s^2): ")

            if a == 0:
                if vi == vf:
                    print("Any time >= 0 fits.")
                else:
                    print("No solution: a=0.")
            else:
                t = (vf - vi) / a
                if t < 0:
                    print("No time >= 0 fits.")
                else:
                    result("Time =", t, "s")

        elif choice == "6":
            print("dx = (vi+vf)*t/2\n")
            vi = number("Initial v (m/s): ")
            vf = number("Final v (m/s): ")
            t = elapsed_time()

            if t == 0 and vi != vf:
                print("No solution at t=0.")
            else:
                result("dx =", (vi + vf) * t / 2, "m")

        elif choice in ["7", "8"]:
            if choice == "7":
                print("vf^2 = vi^2 + 2*a*dx")
            else:
                print("dx = vi*t + a*t^2/2")
            print()

            vi = number("Initial v (m/s): ")
            a = number("Accel (m/s^2): ")
            dx = number("Displacement (m): ")

            times = times_from_dx(vi, a, dx)
            if len(times) == 2:
                print("Two possible events.")

            for t in times:
                result("Time =", t, "s")
                if choice == "7":
                    # Keep each velocity next to its matching time.
                    print("Final v =", round(vi + a * t, 4), "m/s")

        elif choice == "9":
            print("a=(vf^2-vi^2)/(2*dx)\n")
            vi = number("Initial v (m/s): ")
            vf = number("Final v (m/s): ")
            dx = number("Displacement (m): ")

            if dx == 0:
                if vf * vf == vi * vi:
                    print("Accel undetermined.")
                else:
                    print("No solution at dx=0.")
            elif vi + vf == 0:
                print("No solution: avg v=0.")
            elif 2 * dx / (vi + vf) < 0:
                print("No time >= 0 fits.")
            else:
                result("Accel =", (vf**2 - vi**2) / (2 * dx), "m/s^2")

        else:
            print("Invalid choice.")
            continue

        input("\nEnter for menu: ")


run()
