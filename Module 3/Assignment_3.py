import random

"""
1. Each of BigDog, SmallDog, HouseCat and StrayCat will all have a “speak” method and a
“description” attribute.  The BigDog and SmallDog will both have a “sit” method.  The
HouseCat will have a “purr” method.
    a. You should use inheritance whenever possible to reduce duplication of code.
"""


class Pet(object):
    # Create an empty speak method for the child classes to implement
    # first draft was decorated as @abstractmethod using abc
    def speak(self):
        raise NotImplementedError


class Dog(Pet):
    # Create the sit function here
    def sit(self):
        print("The dog sits")


class BigDog(Dog):
    # Create an __init__ function to set the description
    # class attribute not instance attribute
    description = "A large, muscular dog"

    # Create the speak method here
    def speak(self):
        print("Woof")


class SmallDog(Dog):
    # Create the SmallDog class here
    # class attribute not instance attribute
    description = "A tiny, cute dog"

    def speak(self):
        print("Yip")


class Cat(Pet):
    # Create the Cat class here
    def speak(self):
        print("Meow")


class HouseCat(Cat):
    # Create the HouseCat class here
    # class attribute not instance attribute
    description = "A cat with fluffy, white fur"

    def purr(self):
        print("Purrrr")


class StrayCat(Cat):
    # Create the StrayCat class here
    # class attribute not instance attribute
    description = "A cat with tousled, striped fur"


def main():
    # This line treats class definitions as objects. Isn't that cool?
    petClasses = [BigDog, SmallDog, HouseCat, StrayCat]
    """
    3. In the section indicated in the provided project skeleton, first ask the user to input a
    number of pets to generate.  The code to generate the pets using the random number
    generator is given.  Then, where indicated, do the following for each randomly generated
    pet:
    """
    # Change this line to ask the user to input how many pets to generate
    numberOfPets = 0
    while numberOfPets <= 0 or isinstance(numberOfPets, float):
        try:
            numberOfPets = eval(input("Input the number of pets you would like to generate : "))
        except (NameError, SyntaxError):
            print("Sorry, that value or expression does not evaluate to an integer. Goodbye!")
            break

    for petCount in range(0, numberOfPets):
        # This line creates new objects from the stored class definitions!
        pet = petClasses[random.randrange(4)]()
        # Print the info for part 3 of the assignment description here
        """
        3.a. Print “Pet number” followed by that pet’s number.
        """
        print("Pet number {}".format(petCount + 1))
        """
        3.b. Print its description
        """
        # print(getattr(pet, "description"))
        print(pet.description)
        """
        3.c. Call its speak method
        """
        pet.speak()

        if isinstance(pet, Dog):
            """
            3.d. If it's a dog of either type, call its sit() method
            """
            pet.sit()
        elif isinstance(pet, HouseCat):
            """
            3.d. If it's a HouseCat, call its purr() method
            """
            pet.purr()


main()
