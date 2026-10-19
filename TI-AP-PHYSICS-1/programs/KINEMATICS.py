# KINEMATICS

print("KINEMATICS")
print("1 Final velocity")
print("2 Initial velocity")
print("3 Acceleration")
print("4 Displacement")
print("5 Time (velocity)")
print("6 Displacement from vf")

choice = input("Choose 1-6: ")

if choice == "1":
    vi = float(input("Initial v (m/s): "))
    a = float(input("Accel (m/s^2): "))
    t = float(input("Time (s): "))
    vf = vi + a*t
    print("Final v =", round(vf, 4), "m/s")

elif choice == "2":
    vf = float(input("Final v (m/s): "))
    a = float(input("Accel (m/s^2): "))
    t = float(input("Time (s): "))
    vi = vf - a*t
    print("Initial v =", round(vi, 4), "m/s")

elif choice == "3":
    vi = float(input("Initial v (m/s): "))
    vf = float(input("Final v (m/s): "))
    t = float(input("Time (s): "))
    if t == 0:
        print("Time cannot be zero")
    else:
        a = (vf - vi)/t
        print("Accel =", round(a, 4), "m/s^2")

elif choice == "4":
    vi = float(input("Initial v (m/s): "))
    a = float(input("Accel (m/s^2): "))
    t = float(input("Time (s): "))
    dx = vi*t + 0.5*a*t**2
    print("Displacement =", round(dx, 4), "m")

elif choice == "5":
    vi = float(input("Initial v (m/s): "))
    vf = float(input("Final v (m/s): "))
    a = float(input("Accel (m/s^2): "))
    if a == 0:
        print("Acceleration is zero")
    else:
        t = (vf - vi)/a
        print("Time =", round(t, 4), "s")

elif choice == "6":
    vi = float(input("Initial v (m/s): "))
    vf = float(input("Final v (m/s): "))
    t = float(input("Time (s): "))
    dx = (vi + vf)*t/2
    print("Displacement =", round(dx, 4), "m")

else:
    print("Invalid choice")
