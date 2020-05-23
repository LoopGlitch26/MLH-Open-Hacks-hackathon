from block import add_block

patient_list = list()


def check_patient_detail(patient):
    if not patient in patient_list:
        return False

    return True


def add_patient(p_id, name, age, contact_number, doctor_name, disease, address=None):

    p_type = 'patient'

    if address is None:
        address = ''

    patient = {
        'patient_id': p_id,
        'patient_name': name.lower(),
        'patient_age': age,
        'contact_number': contact_number,
        'doctor_name': doctor_name.lower(),
        'patient_disease': disease.lower(),
        'patient_address': address.lower()
    }

    if check_patient_detail(patient) == False:
        patient_list.append(patient)
        add_block(p_type)
    else:
        print(f'Patient: {patient} already exists!' + '\n')


def get_all_patients():
    print('Total Patient: ' + str(len(patient_list)))
    print(patient_list)
    return patient_list
