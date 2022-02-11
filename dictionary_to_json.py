'''
Author: Angela Zhang
Date: Feb. 10, 2022
Purpose: A Python Program converting the Kaprekar's Constant
    dictionary into a JSON file
'''

import json
from kaprekars_constant import find_num_steps_to_kaprekar_for_all_nums

d = find_num_steps_to_kaprekar_for_all_nums(True)

with open("kaprekar.json", "w") as outfile:
    json.dump(d, outfile, sort_keys=True)