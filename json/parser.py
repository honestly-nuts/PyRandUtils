import re

def replace_expression(exp, replacement, line):
    if re.findall(exp, line) != []:
        return re.sub(exp, replacement, line)
    else:
        return line

def parse(data):
    preprocessed_data = data.split("\n")


    # replacing all the whitespaces and shit
    index = 0
    for line in preprocessed_data:
        line = replace_expression(r"^ +", "", line)
        line = replace_expression(r"^({|})", "", line)
        line = replace_expression('"', "", line)
        line = replace_expression("'", "", line)
        
        preprocessed_data[index] = line
        
        index += 1

    preprocessed_data = [pair for pair in preprocessed_data if pair != ""]


    parsed_data = {}
 
    #parsing the damn data
    for pair in preprocessed_data:
        parsed_pair = pair.split(":")

        try:
            # replacing other things again
            parsed_pair[1] = replace_expression(r"^\s", "", parsed_pair[1])
            parsed_pair[1] = replace_expression(r",\s*", "", parsed_pair[1])

            # now comes the "fun" part

            if re.findall(r"^\s*\d", parsed_pair[1]) != []:
                parsed_pair[1] = int(parsed_pair[1])

            elif parsed_pair[1] == 'false':
                parsed_pair[1] = False

            elif parsed_pair[1] == 'true':
                parsed_pair[1] = True

            parsed_data[parsed_pair[0]] = parsed_pair[1]
        except IndexError:
            print("Invalid Json")
            exit()

    return parsed_data

