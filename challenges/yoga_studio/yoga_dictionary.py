yes_answers = [ 'yes', 'Yes', 'YES', 'y', 'Y', 'si', 'Si' ]
no_answers = [ 'no', 'No', 'NO', 'n', 'N']
ask_class = True
ask_reservation = True
class_num_is_valid = False

class_dict = {
#    id:  name   , reservations
    '1': ['Yoga 1', 0],
    '2': ['Yoga 2', 0],
    '3': ['Children\'s Yoga', 0],
    '4': ['Prenatal Yoga', 0],
    '5': ['Senior Yoga', 0]
}

print("""
Welcome to Downdog Yoga Studio! 
    
we have 5 classes to choose from:

    -------------------------
    |  1 - Yoga 1           |
    |  2 - Yoga 2           |
    |  3 - Children\'s Yoga  |
    |  4 - Prenatal Yoga    |
    |  5 - Senior Yoga      |
    -------------------------

  """
)


# PREVENT DICT KEY ERROR : OUT OF RANGE
while class_num_is_valid == False:
    class_num = input(str('- What class would you like to sign up for? \n (1-5) \n  '))
    check_valid_class_num = int(class_num)
    if check_valid_class_num == 5:
        class_num_is_valid = True
    if check_valid_class_num in range(5):
        class_num_is_valid = True

# CLASS NAME
while ask_class == True:
    class_id = class_dict[class_num]    # 1 :               key/id
    class_name = class_id[0]            #   : ['yoga1', ]   value1
    class_reservations = class_id[1]    #   : [       ,0]   value2


    if class_num in class_dict:
        correct_class = input (
            f'- Class number {class_num} is the {class_name} class, Correct? \n  ' )
        
        if correct_class in no_answers:
            class_num = input(
                '- Sorry about that, what class would you like to sign up for? \n  ')
        elif correct_class in yes_answers:
            print('- Fantastic!')
            ask_class = False
        else:
            correct_class = input(
                f'- (y/n) is class number {class_num}: {class_name} what you\'re looking for? \n  ')
    else:
        class_num = input(
        '- Of classes 1-5, what class would you like to sign up for? \n (1-5) ')

# RESERVATIONS
while ask_reservation == True:
    class_id = class_dict[class_num]    # 1 :               key/id
    class_name = class_id[0]            #   : ['yoga1', ]   value1
    class_reservations = class_id[1]    #   : [       ,0]   value2


    print(f'There are {class_reservations} reservations for {class_name} at the moment ')
    request_num = input(f'How many reservations for {class_name} would you like? (1-10) \n  ')

    if request_num.isdigit():

        confirm_reservations = input ( 
            f'{request_num} reservation/s for {class_name}. Correct? \n  ')

        if confirm_reservations in yes_answers:
            class_reservations += int(request_num)
            print(
                f'{request_num} reservation/s of class {class_num}: {class_name}, have been reserved! Thank you! ')
            print(
                f'There are now {class_reservations} reservations for {class_name}! \n  ')
            ask_reservation = False
        elif confirm_reservations in no_answers:
            request_num = input (
                'No worries, how many reservations would you like? \n  ')
        else:
            confirm_reservations = input(
                f'Not sure what you mean... is {class_reservations} reservation/s for {class_name} correct? (y/n) \n  ')

    else :
        request_num = input(f'from 1-10, How many reservations for {class_name} would you like? \n  ')
