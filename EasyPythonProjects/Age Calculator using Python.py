
def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)


y = int(input("Năm:"))
m = int(input("Tháng:"))
d = int(input("Ngày:"))
ageCalculator(y, m, d)
