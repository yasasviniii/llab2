def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = " +str(bmi))
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
        return -1
    elif 18.5 <= bmi <= 25:
        print("Normal weight")
        return 0
    elif bmi > 25.0:
        print("Overweight")
        return 1 


def main():
    values = input("enter height followed by weight seperated by commas: ")
    inputval = values.split(",")
    bmi = calculate_bmi(float(inputval[0]),float(inputval[1]))
    classify_bmi(bmi)




if __name__ == "__main__":
    main()