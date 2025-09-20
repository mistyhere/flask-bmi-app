import csv

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value must be positive. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a whole number above 0.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a number above 0.")

def calculate_bmi(weight_kg, height_m):
    bmi=weight_kg / (height_m ** 2)
    return round(bmi, 1)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def check_temperature(temperature_c):
    if temperature_c > 37.5:
        return "Fever"
    else:
        return "Normal"
    
patients = []

while True: 
    patient_name = input("\nEnter patient name (or type 'done' to finish): ")
    if patient_name.lower() == 'done':
        break
    age = get_int(("Enter age: "))
    weight = get_float(("Enter weight in kg: "))
    height = get_float(("Enter patient height in meters: "))
    temperature = get_float(("Enter body temperature in Celsius: "))
    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)
    temp_status = check_temperature(temperature)

    patient = {
    "name": patient_name,
    "age": age,
    "bmi": bmi,
    "bmi_category": bmi_category,
    "temperature": temperature,
    "temp_status": temp_status
}
    patients.append(patient)

print("\n=== Patient Report ===")
for p in patients:
    print(f"\nName: {p['name']}")
    print(f"Age: {p['age']}")
    print(f"BMI: {p['bmi']} ({p['bmi_category']})")
    print(f"Temperature: {p['temperature']}°C ({p['temp_status']})")

import os
import csv

file_exists = os.path.exists("patient_report.csv")

with open("patient_report.csv", mode="a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "bmi", "bmi_category", "temperature", "temp_status"])
    if not file_exists:
        writer.writeheader()
    writer.writerows(patients)

print("\nReport saved to patient_report.csv ✅")