class BMICalculator:
    def __init__(self, weight_kg, height_cm):
        self.weight = weight_kg
        self.height = height_cm / 100

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def interpret_bmi(self, bmi):
        if bmi < 16:
            return 'Severely Underweight'
        elif bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Normal'
        elif bmi < 30:
            return 'Overweight'
        elif bmi < 35:
            return 'Obese Class I'
        elif bmi < 40:
            return 'Obese Class II'
        else:
            return 'Obese Class III'


if __name__ == '__main__':
    weight = float(input('Enter weight (kg): '))
    height = float(input('Enter height (cm): '))
    calc = BMICalculator(weight, height)
    bmi = calc.calculate_bmi()
    status = calc.interpret_bmi(bmi)
    print(f'BMI: {bmi:.2f} - {status}')
