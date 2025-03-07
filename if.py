#boolean - a T/F conditional test

cat = 'garfield'

print("Lilly = 'cat', right?")
print(cat == 'lilly')



#range of numbers to check
numbers = range(1, 4)

#loops through each number
for number in numbers:
    print(number)
#indent the if statment to put it inside of the loop - will check if printed number are even/odd
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

# is the coffee too expensive?
coffee = 5.00
if coffee >= 4.50:
    print('This coffee is too expensive.')
else:
    print('this coffee is reasonably priced.')
    
#how to find out if you have a driver license 
age = 3

if age >= 16:
    print('you have a driver license')
elif age == 15:
    print('you have a driver permit')
else:
    print('you are too young to drive')
    
# checking hotdog prices
hotdogs = 14

if hotdogs <= 2:
    price = 1.25
elif hotdogs <= 4:
    price = 6.99
elif hotdogs <= 7:
    price = 8.99
elif hotdogs <= 13:
    price = 14.00
else:
    price = 1000000.00
    
print(f"your total is ${price}.")

#when elif statements are not good for loops. 
#the elif will stop at the first one that satisfies the test.
#here it is checking to see the accessories a customer has requested when they purchased their new car.
#w/ the if it will check all the options to see if they are in the list - an else/elif would stop at the first one that is in the list and not check for the rest of the add-ons.

accessories = ['heated seats', 'leather interior']
additional_price = 0

if 'leather interior' in accessories:
    additional_price += 1030
if 'sunroof' in accessories:
    additional_price += 400
if 'heated steering wheel' in accessories:
    additional_price += 2.00
if 'heated seats' in accessories:
    additional_price += 3530
    
print("\nFiished adding your accessories! Here is the addtional and total prices.")
print (additional_price)


#alien color test

aliencolor = ['g', 'r', 'b']
points = 0

if 'g' in aliencolor:
    points +=5
    print("\nYou got the Green Alien!")
    print(points)
if 'y' in aliencolor:
    points += 7
    print("\nYou got the Yellow Alien!")
    print(points)
if 'b' in aliencolor:
    points += 3
    print("\nYou got the Blue Alien!")
    print(points)
else:
    print('\nYou missed the Aliens :(')
    print(points)

print(f'points total: {points}!'.upper())


#Life stage
years_old = 8

if years_old < 2:
    print('baby')
elif 2 <= years_old < 4:
    print('toddler')
elif 4 <= years_old < 13:
    print('kid')
elif 13 <= years_old < 20:
    print('teen')
else:
    print('adult')
    
#fruits

favfruits = ['blueberries', 'pineapples', 'pears']

if 'blueberries' in favfruits:
    print('correct')
if 'pineapples' in favfruits:
    print('correct')
if 'watermelon' not in favfruits:
    print('yuck')
if 'pomegranate' not in favfruits:
    print('yuck')
if 'kiwi' in favfruits:
    print('correct')
if 'tacos' not in favfruits:
    print('that is because tacos are not a fruit')
    
print(favfruits)


#example for using multiple lists - page 87 - checking to see if stores are closed. 
#create the list of all stores and the ones that are opened. 
all_stores = ['pet store', 'grocery store', 'jewelry store', 'book store', 'hardware store']
open_stores = ['pet store', 'grocery store', 'jewelry store']
closed_stores =[]

for store in all_stores:
    if store == 'pet store':
        print('Pet store is open at 11')
#added pet store being opened later to add variety to the opened stores. All other opened stores will print out as opened. 
        print('\nOpen store')
    elif store in open_stores:
        print(f'The {store} is open.')
    else:
#appneds all remaining stores to the closed store list so i can make a list of the stores that are closed today.
        closed_stores.append(store)
#any store that was not listed in the opened store will be assumed closed and listed below.
if closed_stores:
    print('\nClosed stores:')
    for closed_store in closed_stores:
        print(f"The {closed_store} is closed today")
else:
    print("\nAll stores are open!")

    
    
#try it yourself page 89 - hello admin.
username = ['kramer', 'geroge', 'art vandelay', 'elaine', 'newman']

for name in username:
    if name == 'newman':
        print('NEWMAN')
    else:
        print(f'hello {name}')
    if name not in username:
        print('who are you?')
    
username.clear()
if name not in username:
    print('\nwhere is everyone?')
    
#5-10 pg. 88
    
new_dogs = ['Barkley', 'Bark Twaint', 'Furrdinand', 'Pawcasso', 'Bark Obama', 'Woofy Goldberg' ]
adoption_pending = ['Barkley', 'Droolius Caesar', 'Bark Obama', 'Sir Waggington', 'Woofy Goldberg']

print('\nAdoption Status')

for adopted in new_dogs:
    if adopted.lower() in [dog.lower() for dog in adoption_pending]:
        if adopted in adoption_pending:
            print(f'Ope.{adopted} is already adopted!')
        if adopted not in adoption_pending:
            print(f'\nHello {adopted}. We will find you an owner soon!')

# 5-11 pg 88

z = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
numbers = range(1, 10)
for n in numbers:
    # Use n-1 to get the correct index for the suffixes list
    suffix = z[n - 1]
    print(f"\nYou finished {n}{suffix} place!")
        
place = range(1, 10)
for p in place:
    if p == 1:
        a = 'st'
    elif p == 2:
        a = 'nd'
    elif p == 3:
        a = 'rd'
    else:
        a = 'th'
    print(f'\n{p}{a}')
