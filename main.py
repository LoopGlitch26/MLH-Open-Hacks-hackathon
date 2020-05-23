from employee import add_employee, get_all_employees
from patient import add_patient, get_all_patients
from block import get_block


if __name__ == '__main__':
    add_employee('#221', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#221', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#223', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#222', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#224', 'Doctor', 'ABC', 20, 9818314852)
    # print(len(employee_list))
    # get_all_employees()
    print('Blocks after employees have been added!')
    get_block()
    
    add_patient('@p162', 'abc', 10, 98188, 'ABC', 'XYZ')
    add_patient('@p462', 'abc', 10, 92188, 'BBC', 'QYZ')
    add_patient('@p463', 'abc', 43, 92128, 'BCC', 'QEZ')
    add_patient('@p412', 'abc', 12, 98128, 'ACC', 'XEZ')
    add_patient('@p162', 'abc', 10, 98188, 'ABC', 'XYZ')

    # get_all_patients()
    print('Blocks after patient have been added!')
    get_block()