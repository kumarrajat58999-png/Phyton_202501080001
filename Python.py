from datetime import datetime

def age(dob):
    dob = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def inr_to_usd(salary):
    return salary / 83   # approx rate

dob = input("Birthdate (YYYY-MM-DD): ")
salary = float(input("Salary in ₹: "))

print("Age:", age(dob))
print("Salary in $:", round(inr_to_usd(salary), 2))
