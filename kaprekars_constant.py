'''
Author: Angela Zhang
Date: Feb. 10, 2022
Purpose: A Python Program exploring Kaprekar's Constant (6174)
'''

'''
INPUT:
  values: an array of 4 ints between 0-9 inclusive
OUTPUT:
  the difference between the number formed by arranging 
      the ints in `values` in descending order and
      the ints in `values` in ascending order,
  in an array of 4 ints, where
      index 0 represents thousands, 1 hundreds, 2 tens, and 3 ones
'''
def find_ordered_difference(values):
    if len(values) != 4 or values[0] == values[1] == values[2] == values[3]:
        return []

    order = sorted(values)

    largest_to_smallest, smallest_to_largest = 0, 0
    tens_count = 1000
    for i in range(len(order)):
        largest_to_smallest += order[3 - i] * tens_count
        smallest_to_largest += order[i] * tens_count
        tens_count //= 10

    difference = largest_to_smallest - smallest_to_largest
    zero_padding = "0" * (4 - len(str(difference)))
    return [int(x) for x in zero_padding + str(difference)]

# print(find_ordered_difference([9, 2, 1, 8])) # [8, 5, 3, 2]

'''
INPUT:
  values: an array of 4 ints between 0-9 inclusive
OUTPUT:
  the number of steps in Kaprekar's Procedure to reach 6174
'''
def find_num_steps_to_kaprekar(values):
    steps = 0
    difference = values.copy()
    while difference != [6, 1, 7, 4]:
        difference = find_ordered_difference(difference)
        if difference is []:
            print("SOMETHING WENT WRONG AT STEP", steps)
            return -1
        steps += 1
        # print(difference, steps)
    return steps

# print(find_num_steps_to_kaprekar([9, 2, 1, 8])) # 2

'''
INPUT:
  holdNums: a boolean, where 
    TRUE -> value of each key (step #) will hold an array of 
        all non-negative 4-digit ints with that step #
    FALSE -> value of each key (step #) will hold an int representing
        # non-negative 4-digit ints with that step #
    NOTE: use dictionary_to_json.py to convert TRUE output into kaprekars.json
OUTPUT:
  a dictionary where the keys represent step # to reach Kaprekar's Constant,
   and associated values are information on all applicable numbers with that step #
    (values depend on )
'''
def find_num_steps_to_kaprekar_for_all_nums(holdNums=False):
    d = {}
    for thousands in range(10):
        for hundreds in range(10):
            for tens in range(10):
                for ones in range(10):
                    if not (thousands == hundreds == tens == ones):
                        value = (thousands * 1000) + (hundreds * 100) + (tens * 10) + ones
                        steps = find_num_steps_to_kaprekar([thousands, hundreds, tens, ones])
                        if steps == -1:
                            return None
                        if steps in d:
                            if holdNums:
                                d[steps].append(value)
                            else:
                                d[steps] += 1
                        else:
                            if holdNums:
                                d[steps] = [value]
                            else:
                                d[steps] = 1
    return d

# d1 = find_num_steps_to_kaprekar_for_all_nums()
# print(d1) # {5: 1518, 4: 1272, 6: 1656, 3: 2400, 7: 2184, 2: 576, 1: 383, 0: 1}
#
# d2 = find_num_steps_to_kaprekar_for_all_nums(True)
# print(d2) # see kaprekar.json