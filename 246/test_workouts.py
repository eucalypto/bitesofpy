import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    'workout, expected',
    [
        ('upper body', 'Mon, Thu'),
        ('lower body', 'Tue, Fri'),
        ('cardio', 'Wed'),
        ('This is not a workout', 'No matching workout')
    ]
)
def test_print_workout_days(capsys, workout, expected):
    print_workout_days(workout)
    captured = capsys.readouterr().out.strip()
    assert captured == expected
