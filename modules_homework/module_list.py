import random
def listf(new_list):
    if len(new_list) == 0:
        return None
    else:
        return random.choice(new_list)


