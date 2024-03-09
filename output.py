# DISPLAY ITEMS WITH 2 DIGITS LIKE 10 TO BE ALIGNED CORRECTLY
def display_10_option(specific_list):
    for card in specific_list:
        if card['name'] == '10':
            print(f"{card['name']}  : {card['type']}")
        else:
            print(f"{card['name']}   : {card['type']}")


# PRINT THE STARTING CARD
def display_starting_card(card):
    print('STARTING CARD')
    print(f'{card["name"]} : {card["type"]}')
    print("*"*30)


# PRINT LENGTH OF A LIST OF CARDS
def print_len_of(list_string_name, list_name):
    print(f"{list_string_name.upper()} = {len(list_name)} cards.")
    print("*"*30)
    display_10_option(list_name)
    print("*"*30)
