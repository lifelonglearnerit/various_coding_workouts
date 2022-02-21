import random


def number_of_people():
    numb_guests = int(input('Enter the number of friends joining (including you):\n'))
    if numb_guests <= 0:
        print('No one is joining for the party')
    else:
        return guests_dict(numb_guests)

def guests_dict(numb_guests):
    flag = False
    guests = {}
    lucky_guest = ''
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(numb_guests):
        names = input()
        guests[names] = 0
    bill = int(input('Enter the total bill value:\n'))
    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky == 'Yes':
        lucky_guest = random.choice([x for x in guests.keys()])
        print(f'\n{lucky_guest} is the lucky one!')
        flag = True
    else:
        print('\nNo one is going to be lucky')
    bill_split(flag, bill, guests, lucky_guest)


def bill_split(flag, bill, guests, lucky_guest):
    for key in guests:
        guests[key] = round(bill / len(guests), 2)
    if flag:
        for key in guests:
            guests[key] = round(bill / (len(guests) - 1), 2)
            if guests[key] == guests[lucky_guest]:
                guests[key] = 0

    return guest_list(guests)


def guest_list(func):
    print(func)

number_of_people()
