# TI AP Physics 1 Python Programs

A beginner-friendly collection of Python programs for AP Physics 1 calculations, intended for the **TI-84 Plus CE Python**.

## Programs

| Program | Description | Status |
| --- | --- | --- |
| [KINEMATICS](TI-AP-PHYSICS-1/programs/KINEMATICS.py) | Constant-acceleration motion in one dimension | Available |
| [FORCES](TI-AP-PHYSICS-1/programs/FORCES.py) | Newton's laws and net force | Planned; placeholder file |
| FRICT | Kinetic friction | Planned |
| ENERGY | Work, energy, and power | Planned |
| MOMENT | Momentum and impulse | Planned |
| CIRC | Circular motion | Planned |
| PROJ | Projectile motion | Planned |

## Kinematics

Choose one of six calculations:

| Option | Find | Values needed |
| --- | --- | --- |
| 1 | Final velocity | Initial velocity, acceleration, time |
| 2 | Initial velocity | Final velocity, acceleration, time |
| 3 | Acceleration | Initial velocity, final velocity, time |
| 4 | Displacement | Initial velocity, acceleration, time |
| 5 | Time | Initial velocity, final velocity, acceleration |
| 6 | Displacement | Initial velocity, final velocity, time |

The program performs **one calculation per run** and rounds results to four decimal places. Run it again to make another calculation.

### Example

To find final velocity, choose **1** and enter:

```text
Initial v (m/s): 0
Accel (m/s^2): 2
Time (s): 3

Final v = 6.0 m/s
```

## Getting started

1. Open [KINEMATICS.py](TI-AP-PHYSICS-1/programs/KINEMATICS.py) to view the code.
2. Transfer the file using a supported Python transfer workflow for your calculator.
3. Open the program in the calculator's Python app and run it.
4. Choose a menu option and enter the requested values.
5. Check the example above before using the program for other problems.

Enter numbers as decimals, such as `0.5` instead of `1/2`.

## Units and signs

Use **SI units** consistently:

| Quantity | Unit |
| --- | --- |
| Displacement or distance | meters (m) |
| Time | seconds (s) |
| Velocity | meters per second (m/s) |
| Acceleration | meters per second squared (m/s^2) |
| Mass | kilograms (kg) |
| Force | newtons (N) |
| Energy | joules (J) |

Kinematics calculations assume **constant acceleration in one dimension**. Choose a positive direction before entering velocities, acceleration, or displacement.

**`dx` means displacement: final position minus initial position.** It is not total distance traveled. For example, moving 5 m forward and 5 m back gives a distance of 10 m but a displacement of 0 m.

## Contributing

Suggestions, bug reports, and improvements are welcome. When reporting a problem, include the menu option, input values, and result or error message.

## License

See [LICENSE](LICENSE) for details.
