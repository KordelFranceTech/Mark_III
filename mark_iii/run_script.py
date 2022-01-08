# run_script.py
# Kordel France
########################################################################################################################
# This file establishes the specification for a procedure that interprets a text document with commands for the robot.
########################################################################################################################

import sys
import json
sys.path.append('..')
from dorna2 import dorna


def main(config_path):
    with open(config_path) as json_file:
        keys = json.load(json_file)

    agent = dorna()
    agent.connect(keys["ip"], keys["port"])
    agent.play_script("explore_script.txt")
    agent.wait(id=1000, stat=2)
    agent.close()

if __name__ == '__main__':
    main('mark_iii_config.json')

