# auto_zero.py
# Kordel France
########################################################################################################################
# This file establishes the specification for a procedure that automatically zeroes the robot and determines "home".
########################################################################################################################


from random import random
import sys
import json
import time

sys.path.append('..')
from dorna2 import dorna
from mark_iii import settings


def auto_zero_j0(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: zeroing j0...')

    success: bool = False
    return success


def auto_zero_j1(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: zeroing j1...')

    success: bool = False
    return success


def auto_zero_j2(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: zeroing j2...')

    success: bool = False
    return success


def auto_zero_j3(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: zeroing j3...')

    success: bool = False
    return success


def auto_zero_j4(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: zeroing j4...')

    success: bool = False
    return success


def auto_zero_init(robot: dorna) -> bool:
    """

    :param robot:
    :return: bool
    """
    if settings.VERBOSE_LOG:
        print(f'\n{settings.ROBOT_NAME}: initializing auto-zeroing procedure...')

    success: bool = False
    return success


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
