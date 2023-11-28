#BMI Calculator

def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            if weight < 0:
                print("Invalid input! Weight cannot be negative.")
                continue
            return weight
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_height():
    while True:
        try:
            height = float(input("Enter your height (in meters): "))
            if height < 0:
                print("Invalid input! Height cannot be negative.")
                continue
            return height
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = get_weight()
    height = get_height()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
  
    print(f"Your BMI is {bmi:.2f} and you are classified as {category}.")

if __name__ == "__main__":
    main()
