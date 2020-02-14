
:~/246$ mut.py --target workouts.py --unit-test test_workouts.py --runner pytest --coverage -m


[*] Start mutation process:
   - targets: workouts.py
   - tests: test_workouts.py
[*] 4 tests passed:
   - test_workouts [0.10061 s]
[*] Start mutants generation and execution:
   - [#   1] COI workouts:
--------------------------------------------------------------------------------
  10:        that (partially) match the workout string passed in. If no
  11:        workout matches, print 'No matching workout'
  12:     """
  13:     days = [day.title() for (day, wo) in my_workouts.items() if \
- 14:         workout.lower() in wo.lower()]
+ 14:         workout.lower() not in wo.lower()]
  15:     print(', '.join(days) if days else 'No matching workout')
--------------------------------------------------------------------------------
[0.10138 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#   2] CRP workouts:
--------------------------------------------------------------------------------
-  1: WORKOUTS = {'mon': 'upper body #1', \
+  1: WORKOUTS = {'mutpy': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
--------------------------------------------------------------------------------
[0.09425 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#   3] CRP workouts:
--------------------------------------------------------------------------------
-  1: WORKOUTS = {'mon': 'upper body #1', \
+  1: WORKOUTS = {'': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
--------------------------------------------------------------------------------
[0.09486 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#   4] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
-  2:     'tue': 'lower body #1', \
+  2:     'mutpy': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
--------------------------------------------------------------------------------
[0.10021 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#   5] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
-  2:     'tue': 'lower body #1', \
+  2:     '': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
--------------------------------------------------------------------------------
[0.10124 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#   6] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
-  3:     'wed': '30 min cardio', \
+  3:     'mutpy': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
--------------------------------------------------------------------------------
[0.10011 s] killed by test_workouts.py::test_print_workout_days[cardio-Wed]
   - [#   7] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
-  3:     'wed': '30 min cardio', \
+  3:     '': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
--------------------------------------------------------------------------------
[0.10207 s] killed by test_workouts.py::test_print_workout_days[cardio-Wed]
   - [#   8] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
-  4:     'thu': 'upper body #2', \
+  4:     'mutpy': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
--------------------------------------------------------------------------------
[0.10167 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#   9] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
-  4:     'thu': 'upper body #2', \
+  4:     '': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
--------------------------------------------------------------------------------
[0.10276 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  10] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
-  5:     'fri': 'lower body #2'}
+  5:     'mutpy': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
   9:     """Print the days (comma separated and title cased) of my_workouts
--------------------------------------------------------------------------------
[0.09992 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  11] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
-  5:     'fri': 'lower body #2'}
+  5:     '': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
   9:     """Print the days (comma separated and title cased) of my_workouts
--------------------------------------------------------------------------------
[0.10619 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  12] CRP workouts:
--------------------------------------------------------------------------------
-  1: WORKOUTS = {'mon': 'upper body #1', \
+  1: WORKOUTS = {'mon': 'mutpy', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
--------------------------------------------------------------------------------
[0.10173 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  13] CRP workouts:
--------------------------------------------------------------------------------
-  1: WORKOUTS = {'mon': 'upper body #1', \
+  1: WORKOUTS = {'mon': '', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
--------------------------------------------------------------------------------
[0.10133 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  14] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
-  2:     'tue': 'lower body #1', \
+  2:     'tue': 'mutpy', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
--------------------------------------------------------------------------------
[0.10035 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  15] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
-  2:     'tue': 'lower body #1', \
+  2:     'tue': '', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
--------------------------------------------------------------------------------
[0.12304 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  16] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
-  3:     'wed': '30 min cardio', \
+  3:     'wed': 'mutpy', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
--------------------------------------------------------------------------------
[0.09917 s] killed by test_workouts.py::test_print_workout_days[cardio-Wed]
   - [#  17] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
-  3:     'wed': '30 min cardio', \
+  3:     'wed': '', \
   4:     'thu': 'upper body #2', \
   5:     'fri': 'lower body #2'}
   6:
   7:
--------------------------------------------------------------------------------
[0.09853 s] killed by test_workouts.py::test_print_workout_days[cardio-Wed]
   - [#  18] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
-  4:     'thu': 'upper body #2', \
+  4:     'thu': 'mutpy', \
   5:     'fri': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
--------------------------------------------------------------------------------
[0.10012 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  19] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
-  4:     'thu': 'upper body #2', \
+  4:     'thu': '', \
   5:     'fri': 'lower body #2'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
--------------------------------------------------------------------------------
[0.09762 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  20] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
-  5:     'fri': 'lower body #2'}
+  5:     'fri': 'mutpy'}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
   9:     """Print the days (comma separated and title cased) of my_workouts
--------------------------------------------------------------------------------
[0.09690 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  21] CRP workouts:
--------------------------------------------------------------------------------
   1: WORKOUTS = {'mon': 'upper body #1', \
   2:     'tue': 'lower body #1', \
   3:     'wed': '30 min cardio', \
   4:     'thu': 'upper body #2', \
-  5:     'fri': 'lower body #2'}
+  5:     'fri': ''}
   6:
   7:
   8: def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
   9:     """Print the days (comma separated and title cased) of my_workouts
--------------------------------------------------------------------------------
[0.09875 s] killed by test_workouts.py::test_print_workout_days[lower body-Tue, Fri]
   - [#  22] CRP workouts:
--------------------------------------------------------------------------------
  11:        workout matches, print 'No matching workout'
  12:     """
  13:     days = [day.title() for (day, wo) in my_workouts.items() if \
  14:         workout.lower() in wo.lower()]
- 15:     print(', '.join(days) if days else 'No matching workout')
+ 15:     print('mutpy'.join(days) if days else 'No matching workout')
--------------------------------------------------------------------------------
[0.09616 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  23] CRP workouts:
--------------------------------------------------------------------------------
  11:        workout matches, print 'No matching workout'
  12:     """
  13:     days = [day.title() for (day, wo) in my_workouts.items() if \
  14:         workout.lower() in wo.lower()]
- 15:     print(', '.join(days) if days else 'No matching workout')
+ 15:     print(''.join(days) if days else 'No matching workout')
--------------------------------------------------------------------------------
[0.09542 s] killed by test_workouts.py::test_print_workout_days[upper body-Mon, Thu]
   - [#  24] CRP workouts:
--------------------------------------------------------------------------------
  11:        workout matches, print 'No matching workout'
  12:     """
  13:     days = [day.title() for (day, wo) in my_workouts.items() if \
  14:         workout.lower() in wo.lower()]
- 15:     print(', '.join(days) if days else 'No matching workout')
+ 15:     print(', '.join(days) if days else 'mutpy')
--------------------------------------------------------------------------------
[0.10159 s] killed by test_workouts.py::test_print_workout_days[This is not a workout-No matching workout]
   - [#  25] CRP workouts:
--------------------------------------------------------------------------------
  11:        workout matches, print 'No matching workout'
  12:     """
  13:     days = [day.title() for (day, wo) in my_workouts.items() if \
  14:         workout.lower() in wo.lower()]
- 15:     print(', '.join(days) if days else 'No matching workout')
+ 15:     print(', '.join(days) if days else '')
--------------------------------------------------------------------------------
[0.10263 s] killed by test_workouts.py::test_print_workout_days[This is not a workout-No matching workout]
[*] Mutation score [4.76644 s]: 100.0%
   - all: 25
   - killed: 25 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
[*] Coverage: 74 of 75 AST nodes (98.7%)
