import json
import os

from utility import clear
from employee import add_employee, get_all_employees
from patient import add_patient, get_all_patients
from save_block import save_block
from block import get_block, load_block


def run_test():
    add_employee('#234', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#221', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#223', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#222', 'Doctor', 'ABC', 20, 9818314852)
    add_employee('#224', 'Doctor', 'ABC', 20, 9818314852)

    add_patient('@p162', 'abc', 10, 98188, 'ABC', 'XYZ')
    add_patient('@p462', 'abc', 10, 92188, 'BBC', 'QYZ')
    add_patient('@p463', 'abc', 43, 92128, 'BCC', 'QEZ')
    add_patient('@p412', 'abc', 12, 98128, 'ACC', 'XEZ')
    add_patient('@p162', 'abc', 10, 98188, 'ABC', 'XYZ')
    print('Blocks after patient have been added!')
    # get_block()
    add_patient('@p162', 'abc', 10, 98188, 'ABC', 'XXXYZ')
    # get_block()
    save_block(filename='output.block')


if __name__ == '__main__':
    run_app = True
    run_test()
    clear()
    # load_block()
    while run_app:
        # clear()
        print('1. Load file!')
        print('2. Save file!')
        print('3. Add employee')
        print('4. Add patient')
        print('5. Get data of block!')
        print('q. Quit')

        # try:
        #     load_block()
        #     print('Block loaded sucessfully :)')
        # except ():
        #     print('loading failed :(')

        option = str(input('Enter choice: '))

        if option == '1':
            clear()
            try:
                filename = str(
                    input('\n' + "Enter filename (default: output.block): "))

                while filename == '':
                    print('Error... ...')
                    input = str(
                        input('\n' + "Enter filename (default: output.block): "))

                if load_block(filename=filename):
                    print('Block loaded sucessfully :)' + '\n')
                else:
                    print('Error in block...')

            except (FileNotFoundError):
                print('No data exists, file not found!')
                print('loading failed :(' + '\n')

            finally:
                print()


        if option == '2':
            clear()
            try:
                filename = str(
                    input('\n' + "Enter filename (default: output.block): "))

                while filename == '':
                    print('Error... ...')
                    filename = str(
                        input('\n' + "Enter filename (default: output.block): "))
                save_block(filename=filename)
                print('Block saved sucessfully!' + '\n')

            except (FileNotFoundError):
                print('File not found!')


        if option == '3':
            clear()
            print('Please provide employee details!')
            e_id = str(input('Employee id: '))
            e_type = str(input('Employee type (such as Doctor, nurse, etc): '))
            name = str(input('Employee name: '))
            age = input('Age: ')
            contact_number = input('Contact number: ')
            add_employee(e_id, e_type, name, age, contact_number)
            print('Employee list updated!' + '\n')

        if option == '4':
            clear()
            print('Please provide patient details!')
            p_id = str(input('Patient id: '))
            name = str(input('Patient name: '))
            age = input('Age: ')
            contact_number = input('Contact number: ')
            doctor_name = str(input("Patient's doctor: "))
            disease = str(input('Disease of patient: '))
            address = str(input("Patient's address: "))
            add_patient(p_id, name, age, contact_number,
                        doctor_name, disease, address)
            print('Patient list updated!' + '\n')

        if option == '5':
            clear()
            get_block()
            print()

        if option == 'q':
            run_app = False
