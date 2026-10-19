# TI AP Physics Python Programs

Beginner-friendly Python programs intended for the TI-84 Plus CE Python, designed to help with AP Physics 1 calculations.

## Programs

| Program | Description | Status |
|---|---|---|
| [KINEMATICS.py](TI-AP-PHYSICS-1/programs/KINEMATICS.py) | Constant-acceleration motion in one dimension | Available; desktop tested |
| [FORCES.py](TI-AP-PHYSICS-1/programs/FORCES.py) | Newton's laws and net force | Placeholder only |
| FRICT | Kinetic friction | Planned |
| ENERGY | Work, energy, and power | Planned |
| MOMENT | Momentum and impulse | Planned |
| CIRC | Circular motion | Planned |
| PROJ | Projectile motion | Planned |

## Kinematics

The program includes all six original calculations plus three new ones:

| Option | Find | Known values |
|---|---|---|
| 1 | Final velocity | Initial velocity, acceleration, time |
| 2 | Initial velocity | Final velocity, acceleration, time |
| 3 | Acceleration | Initial velocity, final velocity, time |
| 4 | Displacement | Initial velocity, acceleration, time |
| 5 | Time | Initial velocity, final velocity, acceleration |
| 6 | Displacement | Initial velocity, final velocity, time |
| 7 | Final velocity | Initial velocity, acceleration, displacement |
| 8 | Time | Initial velocity, acceleration, displacement |
| 9 | Acceleration | Initial velocity, final velocity, displacement |

- Equations appear before you enter values.
- Results include units and are rounded to four decimal places.
- Invalid numeric inputs can be retried without restarting.
- The program explains impossible or undetermined cases and rejects negative elapsed times.
- When two nonnegative times fit, both are shown. Option 7 pairs each time with its velocity.
- Press Enter after a calculation to return to the menu, choose **H** for help, or **0** to exit.

### Symbols and assumptions

| Symbol | Meaning | SI unit |
|---|---|---|
| vi | Initial velocity | m/s |
| vf | Final velocity | m/s |
| a | Constant acceleration | m/s^2 |
| t | Elapsed time | s |
| dx | Displacement: final position minus initial position | m |

Choose a positive direction and enter signed velocities, acceleration, and displacement. For example, with up positive, use a = -9.8 m/s^2 for free fall near Earth's surface when air resistance is neglected.

Displacement is not total distance traveled. Moving 5 m forward and 5 m back gives a distance of 10 m but a displacement of 0 m.

These calculations assume **constant acceleration in one dimension**. Changing-acceleration calculations are not included. If two possible events are returned, choose the one described in the problem.

## Getting started

1. Open [KINEMATICS.py](TI-AP-PHYSICS-1/programs/KINEMATICS.py) to view the source.
2. Transfer it using your calculator's supported Python transfer workflow. Use a short name such as `KINEM.py` for the calculator copy.
3. Run it from the calculator's Python app.
4. Enter decimal numbers, such as `0.5` instead of `1/2`.
5. Try the examples below on your calculator.

The code has been tested with desktop Python. Compatibility and screen layout still need verification on the physical TI-84 Plus CE Python.

### Examples

| Option | Inputs | Expected result |
|---|---|---|
| 1 | vi = 0, a = 2, t = 3 | vf = 6 m/s |
| 4 | vi = 0, a = 2, t = 3 | dx = 9 m |
| 7 | vi = 10, a = -10, dx = 0 | vf = 10 m/s at t = 0 s; vf = -10 m/s at t = 2 s |
| 8 | vi = 10, a = -10, dx = 4 | t = 0.5528 s and 1.4472 s |
| 9 | vi = 0, vf = 6, dx = 9 | a = 2 m/s^2 |

## Original backup

The original six-option program is saved as [backups/KINEMATICS.original.py](backups/KINEMATICS.original.py).

To restore it, copy that file over `TI-AP-PHYSICS-1/programs/KINEMATICS.py`. Save a copy of the newer version first if you want to keep both.

## Desktop tests

With Python installed, run this from the repository root:

```sh
python -m unittest discover -s tests -v
```

The tests cover the menu options, input validation, repeated calculations, special cases, turning-point rounding, and 1,000 generated motion problems. They use only Python's standard library. The test files do not need to be transferred to the calculator.

## Contributing

Suggestions, bug reports, and improvements are welcome.
