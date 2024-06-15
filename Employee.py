class Employee:
    num=0
    def __init__(self, name =None, position=None, department=None, salary=None, hire_date=None, contact_info=None):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
        self.contact_info = contact_info

employees = []

def add_employee():
    name = input("اسم الموظف: ")
    position = input("منصب الموظف: ")
    department = input("قسم الموظف: ")
    salary = input("راتب الموظف: ")
    hire_date = input("تاريخ تعيين الموظف: ")
    contact_info = input("معلومات الاتصال بالمُوظف: ")

    employee = Employee(name, position, department, salary, hire_date, contact_info)
    employees.append(employee)

    print("!!تم إضافة الموظف بنجاح!")

def show_employee():
    name = input("اسم المdfgdfgوظف: ")

    employee = find_employee(name)

    if employee is None:
        print("لا يوجد موظف بهذا الاسم.")
    else:
        print("اسم الموظف:", employee.name)
        print("منصب الموظف:", employee.position)
        print("قسم الموظف:", employee.department)
        print("راتب الموظف:", employee.salary)
        print("تاريخ تعيين الموظف:", employee.hire_date)
        print("معلومات الاتصال بالمُوظف:", employee.contact_info)

def find_employee(name):
    for employee in employees:
        if employee.name == name:
            return employee
    return None

def edit_employee():
    name = input("اسم الموظف: ")

    employee = find_employee(name)

    if employee is None:
        print("لا يوجد موظف بهذا الاسم.")
    else:
        new_position = input("منصب الموظف الجديد: ")
        new_department = input("قسم الموظف الجديد: ")
        new_salary = input("راتب الموظف الجديد: ")

        employee.position = new_position
        employee.department = new_department
        employee.salary = new_salary

        print("تم تعديل معلومات الموظف بنجاح!")

def delete_employee():
    name = input("اسم الموظف: ")

    employee = find_employee(name)

    if employee is None:
        print("لا يوجد موظف بهذا الاسم.")
    else:
        employees.remove(employee)

        print("تم حذف الموظف بنجاح!")

def employees_info():
    return Employee.num


while True:
    print("1. إضافة موظف جديد")
    print("2. عرض معلومات موظف")
    print("3. تعديل معلومات موظف")
    print("4. حذف موظف")
    print("5. الخروج")

    choice = input("اختر رقم الوظيفة: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_employee()
    elif choice == "3":
        edit_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        employees_info()
    elif choice == "6":
        break
    else:
        print("خيار غير صحيح!")
