# explore.py
# Kordel France
########################################################################################################################
# This file establishes the specification for a series of exploratory commands the robot can perform for calibration.
########################################################################################################################

from random import random
import sys
import json
import time

sys.path.append('..')
from dorna2 import dorna
from mark_iii import settings


def cmd_return_to_home(robot: dorna):
    """
    Return to home (zeroed) position at a moderate velocity.
    :param robot: dorna - instance of 'dorna' object
    :return: None
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: returning to home...')

    command = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': 0,
               'j1': 0,
               'j2': 0,
               'j3': 0,
               'j4': 0,
               'vel': 50,
               'accel': 300,
               'jerk': 1000
               }
    robot.play(**command)
    # track = robot.play(track=True, message=None, **command)
    # print(track.complete())


def cmd_random_motion_fast(robot: dorna):
    """
    Perform a random motion on j0-j4 at a fast velocity
    :param robot: dorna - instance of 'dorna' object
    :return: None
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing random motion (fast)...')

    j0: float = -90 + random() * 180
    j1: float = -45 + random() * 135
    j2: float = max(-90, -2.7 * j1 - 60) + random() * (90 - max(-90, -2.7 * j1 - 60))
    j3: float = -90 + random() * 180
    j4: float = 0

    command = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0,
               'j1': j1,
               'j2': j2,
               'j3': j3,
               'j4': j4,
               'vel': 100,
               'accel': 700,
               'jerk': 3000
               }
    robot.play(**command)


def cmd_random_motion_slow(robot: dorna):
    """
    Perform a random motion on j0-j4 at a slow velocity
    :param robot: dorna - instance of 'dorna' object
    :return: None
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing random motion (slow)...')

    j0: float = -90 + random() * 180
    j1: float = -45 + random() * 135
    j2: float = max(-90, -2.7 * j1 - 60) + random() * (90 - max(-90, -2.7 * j1 - 60))
    j3: float = -90 + random() * 180
    j4: float = 0

    command = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0,
               'j1': j1,
               'j2': j2,
               'j3': j3,
               'j4': j4,
               'vel': 10,
               'accel': 70,
               'jerk': 300
               }
    robot.play(**command)


def cmd_extend_full_fast(robot: dorna):
    """
    A two-part command to fully extend the arm at a fast velocity.
    :param robot: dorna - instance of 'dorna' object
    :return: None
    """

    """
    If we extend the shoulder (j1) before the wrist (j2) and elbow (j3, j4),
    then there will not be enough ROM to extend wrist and elbow since they
    are both at a negative angle.
    Need two commands - first extend wrist and elbow, then extend shoulder.
    """

    # extend wrist and elbow
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing full arm extension - wrist and forearm (fast)...')

    j0_0: float = 0.0
    j1_0: float = 0.0
    j2_0: float = 142.0
    j3_0: float = 135.0
    j4_0: float = 0.0

    command0 = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0_0,
               'j1': j1_0,
               'j2': j2_0,
               'j3': j3_0,
               'j4': j4_0,
               'vel': 100,
               'accel': 700,
               'jerk': 3000
               }
    robot.play(**command0)

    # extend shoulder
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing full arm extension - shoulder (fast)...')

    j0_1: float = 0.0
    j1_1: float = 180.0
    j2_1: float = 0.0
    j3_1: float = 0.0
    j4_1: float = 0.0

    command1 = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0_1,
               'j1': j1_1,
               'j2': j2_1,
               'j3': j3_1,
               'j4': j4_1,
               'vel': 10,
               'accel': 70,
               'jerk': 300
               }
    robot.play(**command1)


def cmd_extend_full_slow(robot: dorna):
    """
    A two-part command to fully extend the arm at a slow velocity.
    :param robot: dorna - instance of 'dorna' object
    :return: None
    """

    """
    If we extend the shoulder (j1) before the wrist (j2) and elbow (j3, j4),
    then there will not be enough ROM to extend wrist and elbow since they
    are both at a negative angle.
    Need two commands - first extend wrist and elbow, then extend shoulder.
    """
    # extend wrist and elbow
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing full arm extension - wrist and forearm (slow)...')

    j0_0: float = 0.0
    j1_0: float = 0.0
    j2_0: float = 142.0
    j3_0: float = 135.0
    j4_0: float = 0.0

    command0 = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0_0,
               'j1': j1_0,
               'j2': j2_0,
               'j3': j3_0,
               'j4': j4_0,
               'vel': 10,
               'accel': 70,
               'jerk': 300
               }
    robot.play(**command0)

    # extend shoulder
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: performing full arm extension - shoulder (slow)...')

    j0_1: float = 0.0
    j1_1: float = 180.0
    j2_1: float = 0.0
    j3_1: float = 0.0
    j4_1: float = 0.0
    command1 = {'cmd': 'jmove',
               'rel': 0,
               'id': robot.rand_id(),
               'j0': j0_1,
               'j1': j1_1,
               'j2': j2_1,
               'j3': j3_1,
               'j4': j4_1,
               'vel': 10,
               'accel': 70,
               'jerk': 300
               }
    robot.play(**command1)


def robot_init(config_path):
    """
    Initialize the robot and connect it to appropriate ip address.
    :param: str - config_path:
    :return: dorna - robot, instance of 'dorna' object
    """
    with open(config_path) as json_file:
        keys = json.load(json_file)

    robot = dorna()
    robot.connect(keys['ip'], keys['port'])

    if robot.connected:
        print(f'\n\n{settings.ROBOT_NAME}: robot connected')

    return robot


if __name__ == '__main__':
    robot_mark3 = robot_init('mark_iii_config.json')

    if robot_mark3.connected:

        # slow
        cmd_random_motion_slow(robot_mark3)
        time.sleep(5000)

        cmd_return_to_home(robot_mark3)
        time.sleep(5000)

        # cmd_extend_full_slow(robot_mark3)
        # time.sleep(5000)

        # fast
        cmd_random_motion_fast(robot_mark3)
        time.sleep(5000)

        cmd_return_to_home(robot_mark3)
        time.sleep(5000)

        # cmd_extend_full_fast(robot_mark3)
        # time.sleep(5000)

        # return home
        cmd_return_to_home(robot_mark3)



