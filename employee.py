from block import add_block

employee_list = list()


def employee_exists(employee):
    if not employee in employee_list:
        return False

    return True


def add_employee(e_id, e_type, name, age, contact_number):
    employee = {
        'employee_id': e_id,
        'employee_type': e_type.lower(),
        'employee_name': name.lower(),
        'employee_age': age,
        'contact_number': contact_number
    }

    if employee_exists(employee) == False:
        employee_list.append(employee)
        add_block(e_type)
    else:
        print(f'Employee: {employee} already exists!' + '\n')


def get_all_employees():
    print('Total Employees: ' + str(len(employee_list)))
    print(employee_list)
    return employee_list
