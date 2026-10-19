"""Desktop tests for the standalone calculator program.
Run: python -m unittest discover -s tests -v
"""
import contextlib
import io
import math
from pathlib import Path
import random
import runpy
import unittest
from unittest.mock import patch

PROGRAM = Path(__file__).resolve().parents[1] / 'TI-AP-PHYSICS-1/programs/KINEMATICS.py'


def execute(answers):
    output = io.StringIO()
    with patch('builtins.input', side_effect=answers), contextlib.redirect_stdout(output):
        namespace = runpy.run_path(str(PROGRAM))
    return output.getvalue(), namespace


class KinematicsTests(unittest.TestCase):
    def test_interactive_cases(self):
        cases = [
            (['1','0','2','3'], ['Final v = 6.0 m/s']),
            (['2','6','2','3'], ['Initial v = 0.0 m/s']),
            (['3','0','6','3'], ['Accel = 2.0 m/s^2']),
            (['4','0','2','3'], ['dx = 9.0 m']),
            (['5','0','6','2'], ['Time = 3.0 s']),
            (['6','0','6','3'], ['dx = 9.0 m']),
            (['7','10','-10','0'], ['Final v = 10.0 m/s','Final v = -10.0 m/s']),
            (['8','10','-10','4'], ['Time = 0.5528 s','Time = 1.4472 s']),
            (['9','0','6','9'], ['Accel = 2.0 m/s^2']),
            (['1','bad','','1/2','nan','inf','0','2','-1','3'], ['Enter a decimal','Time must be','Final v = 6.0']),
            (['3','2','2','0'], ['Accel undetermined']),
            (['3','2','3','0'], ['No solution at t=0']),
            (['5','2','2','0'], ['Any time >= 0 fits']),
            (['5','2','3','0'], ['No solution: a=0']),
            (['5','2','1','1'], ['No time >= 0 fits']),
            (['6','2','3','0'], ['No solution at t=0']),
            (['8','0','0','0'], ['Any time >= 0 fits']),
            (['8','0','0','1'], ['No solution: at rest']),
            (['8','2','0','4'], ['Time = 2.0 s']),
            (['8','2','0','-4'], ['No time >= 0 fits']),
            (['8','0','-1','1'], ['Position not reached']),
            (['8','10','-10','5'], ['Time = 1.0 s']),
            (['8','0','2','0'], ['Time = 0.0 s']),
            (['9','1','2','0'], ['No solution at dx=0']),
            (['9','1','-1','0'], ['Accel undetermined']),
            (['9','1','-1','2'], ['No solution: avg v=0']),
            (['9','1','2','-2'], ['No time >= 0 fits']),
            (['H',''], ['free fall a = -9.8','Choose the event asked']),
        ]
        for answers, expected in cases:
            with self.subTest(answers=answers):
                output, _ = execute(answers + ['', '0'])
                for text in expected:
                    self.assertIn(text, output)

    def test_repeat_menu_and_exit(self):
        output, _ = execute(['x','1','0','2','3','','4','0','2','3','','0'])
        for text in ['Invalid choice', 'Final v = 6.0', 'dx = 9.0']:
            self.assertIn(text, output)

    def test_decimal_turning_point(self):
        output, _ = execute(['8','0.3','-0.1','0.45','','0'])
        self.assertIn('Time = 3.0 s', output)
        self.assertNotIn('Position not reached', output)

    def test_generated_motion(self):
        _, namespace = execute(['0'])
        solve = namespace['times_from_dx']
        rng = random.Random(84)
        for i in range(1000):
            vi = rng.uniform(-50, 50)
            a = rng.uniform(-20, 20)
            t = rng.uniform(0.01, 20)
            dx = vi*t + 0.5*a*t*t
            with self.subTest(case=i), contextlib.redirect_stdout(io.StringIO()):
                answers = solve(vi, a, dx)
                self.assertTrue(any(math.isclose(x, t, rel_tol=1e-8, abs_tol=1e-8) for x in answers))
                self.assertEqual(answers, sorted(answers))
                for x in answers:
                    self.assertGreaterEqual(x, 0)
                    self.assertTrue(math.isclose(vi*x + 0.5*a*x*x, dx, rel_tol=1e-8, abs_tol=1e-8))

    def test_root_counts_and_precision(self):
        _, namespace = execute(['0'])
        solve = namespace['times_from_dx']
        cases = [(10,-10,4,2), (10,-10,5,1), (10,-10,6,0),
                 (-10,-10,4,0), (0,2,4,1), (2,0,4,1),
                 (2,0,-4,0), (0,0,1,0), (0,2,0,1)]
        for vi, a, dx, count in cases:
            with self.subTest(values=(vi,a,dx)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(len(solve(vi,a,dx)), count)
        # Small positive root should survive cancellation in the quadratic.
        self.assertAlmostEqual(solve(1e8, 1, 1)[0], 1e-8, places=15)


if __name__ == '__main__':
    unittest.main()
