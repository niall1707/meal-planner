import re
import csv
import random


class User:
    def __init__(self, age=0, gender=0, weight=0, height=0, favorite=0, activity=0):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.favorite = favorite
        self.activity = activity


food_list = []
user = User()


def main():
    breakfast = []
    lunch = []
    dinner = []

    check_gender()
    age = input("Please enter your age in numbers (eg: 18): ")
    check_age(age)
    height = check_height()
    weight = check_weight()
    check_active()
    bmr = BMR()
    bmi = Bmi(height, weight)
    value = Bmi_range(bmi)
    calories = calorie_calc(bmr)
    calories = int(calories)
    print()
    print(f"Basal Metabolic rate: {bmr}")
    print(f"Needed calories: {calories}")
    print(f"Body Mass Index: {bmi}")
    print(f"According to your BMI, you are {value}")

    # Calories for meals
    bf_cal = calories * 2 / 3
    ln_cal = calories * 1 / 3

    # Send file name
    if not check_food("nutrients_csvfile.csv"):
        print("Error: nutrients_csvfile.csv not found.")
        return

    # Input calories into meals
    distribute_calories(breakfast, bf_cal)
    distribute_calories(lunch, ln_cal)
    distribute_calories(dinner, calories)

    # Print meals
    print_meal("Breakfast", breakfast)
    print_meal("Lunch", lunch)
    print_meal("Dinner", dinner)


def check_age(age):
    if Age := re.search(r"^([0-9][0-9]?)$", age):
        user.age = Age.group(1)
        return True
    else:
        print("Enter a valid age.")
        return check_age(input("Enter your age: "))


def check_gender():
    gender = input("Enter your Gender: ")
    if Gender := re.search(r"^(M|F|MALE|FEMALE)$", gender.upper()):
        user.gender = Gender.group().lower()
    else:
        print("Enter a valid gender")
        check_gender()


def check_height():
    height = input("Enter your height in Cms: ")
    if Height := re.search(r"^([1-9][0-9][0-9]?)$", height):
        user.height = Height.group()
        return Height.group()
    else:
        print("Enter a valid height")
        return check_height()


def check_weight():
    weight = input("Enter your weight in kilograms: ")
    if Weight := re.search(r"^([0-9][0-9]?[0-9]?)$", weight):
        user.weight = Weight.group()
        return Weight.group()
    else:
        print("Enter a valid weight")
        return check_weight()


def check_active():
    activity = input(
        "On a scale of 1-5, how active are you? 1 is sedentary, 5 is very active: "
    )
    if Activity := re.search(r"^([12345])$", activity):
        user.activity = Activity.group()
        return Activity.group()
    else:
        print("Enter a valid activity level.")
        return check_active()


def check_food(file):
    global food_list
    try:
        with open(file) as f:
            read = csv.DictReader(f)
            for line in read:
                food_list.append(line)
        return True
    except FileNotFoundError:
        return False


def BMR():
    if user.gender in ["male", "m"]:
        bmr = 66.5 + (13.75 * int(user.weight)) + (5.003 * int(user.height)) - (6.75 * int(user.age))
    else:
        bmr = 655.1 + (9.563 * int(user.weight)) + (1.850 * int(user.height)) - (4.676 * int(user.age))
    return bmr


def calorie_calc(bmr):
    return bmr * (1.2 + ((int(user.activity) - 1) * 0.175))


def Bmi(height, weight):
    return int(weight) / (int(height) / 100) ** 2


def Bmi_range(bmi):
    bmi = float(bmi)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Healthy"
    elif bmi < 29.9:
        return "Overweight"
    return "Obese"


def distribute_calories(meal_list, calorie_limit):
    global food_list
    calories = calorie_limit
    while calories > 0:
        num = random.randint(1, len(food_list) - 1)
        food_item = food_list[num]
        meal_list.append({"food": food_item["Food"], "grams": food_item["Grams"]})
        calories -= int(food_item["Calories"].replace(",", ""))


def print_meal(meal_name, meal):
    print(f"{meal_name}: ")
    for item in meal:
        print(f"- {item['grams']} gm {item['food']} ")


if __name__ == "__main__":
    main()
