from drivetrain import Drivetrain
from vex import Brain, DistanceUnits, Motor, Ports, TimeUnits, Touchled


class Autopilot:
    def __init__(
            self,
            left_motor_port=Ports.PORT1, right_motor_port=Ports.PORT6,
            wheel_travel=200, track_width=176,
            distance_unit=DistanceUnits.MM,
            gear_ratio=1,
            touch_led_port=Ports.PORT2):
        self.brain = Brain()

        self.drivetrain = \
            Drivetrain(
                Motor(
                    left_motor_port,   # index
                    False   # reverse
                ),   # left_motor
                Motor(
                    right_motor_port,   # index
                    True   # reverse
                ),   # right_motor
                wheel_travel,   # wheel_travel
                track_width,   # track_width
                distance_unit,   # distanceUnits
                gear_ratio   # gear_ratio
            )

        self.touch_led = Touchled(touch_led_port)


AUTOPILOT = Autopilot()

AUTOPILOT.brain.sound.play(
    3,   # note
    3,   # octave
    1,   # duration
    TimeUnits.SEC   # timeUnit
)