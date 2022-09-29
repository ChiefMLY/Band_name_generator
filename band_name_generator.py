#Greeting prompt for the user
print('Welcome to Band Name Generator')

#Ask the user what city they grew up in
city = input('What is the name of the city you grew up in: \n')

#Asks the user what the name of their pet
pet =  input("What is the name of your pet: \nIF YOU DON'T HAVE A PET PLEASE ENTER 'no': ")

#If the user does not have a pet, this prompts
if pet.lower() == 'no':
    favorite_color = input('What is your favorite color: ')

#Combine the name of their city and pet and show them their band name.
if pet.lower() == 'no':
    band_name = city.title() + " " + favorite_color.title()
else:
    band_name = city.title() + " " + pet.title()

#Print the suggested band name
print(f"Your band name could be: {band_name}")
