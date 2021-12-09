import hashlib

class Status:
    def __init__(self):
        self.running = True


def check(hashed_value, proposed_solution):
    encoded_str = bytes(proposed_solution, encoding='ascii')
    return hashlib.md5(encoded_str).hexdigest() == hashed_value

def next_valid_character(char):
    if(char == 'Z'):
        return 'a'
    elif(char == 'z'):
        return None
    else:
        return chr(ord(char)+1)

def next_valid_string(string):
    if(string[-1] == 'z'):
        if(len(string) == 1):
            return None
        new_base = next_valid_string(string[0:-1])
        if(new_base == None):
            return None
        else:
            return new_base + 'A'
    else:
        return string[0:-1] + next_valid_character(string[-1])

def encode_str_as_num(string):
    total = 0
    for c in string:
        if(ord(c) >= ord('a')):
            total += (ord(c) - ord('a') + 26)
        else:
            total += (ord(c) - ord('A'))
        total *= 52
    total /= 52
    return total

def decode_num(num, string_length):
    x = num
    string = ""
    while(x != 0):
        remainder = x % 52
        if(x < 26):
            string = chr(int(ord("A") + remainder)) + string
        else:
            string = chr(int(ord("a") + remainder-26)) + string
        x = (x - remainder)/52
    while(len(string) != string_length):
        string = "A" + string
    return string


def divide_string_range(string1, string2, divisions):
    n1 = encode_str_as_num(string1)
    n2 = encode_str_as_num(string2)
    n = n2 - n1
    count_per_group = int(n//divisions)
    divider_values = [decode_num(count_per_group * (i+1) + n1, len(string1)) for i in range(divisions-1)]
    ranges = []
    ranges.append([string1, divider_values[0]])
    for i in range(1, len(divider_values)):
        ranges.append([next_valid_string(divider_values[i-1]), divider_values[i]])
    ranges.append([next_valid_string(divider_values[-1]), string2])
    return ranges




def search_for_hash_solution(hashed_value, starting_string, ending_string, status):
    print("Checking strings {0} through {1}...".format(starting_string, ending_string))
    total_iterations = encode_str_as_num(ending_string) - encode_str_as_num(starting_string) + 1
    current_string = starting_string
    counter = 0
    next_milestone = 5
    while(True):
        if(status.running == False):
            return None
        counter += 1
        progress_val = (100 * counter)//total_iterations
        if(progress_val >= next_milestone):
            print("Finished checking {0}%...".format(next_milestone))
            next_milestone += 5

        if(check(hashed_value, current_string)):
            print("\nSolution detected!")
            return current_string
        current_string = next_valid_string(current_string)
        if(current_string == ending_string):
            print("\nNo solution found in this range.")
            return None
