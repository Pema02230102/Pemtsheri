from queue import Queue

Register_patient = Queue()
Remove_patient = Queue()
current_patient = None

while True:
    print ("Desktop Manager - Patient Registeration and Appointment System\n")
    print("""
        1. Press 1 to Register the patient
        2. Press 2 to Remove the Patient
        3. Press 3 Display the patient 
        4. press 4 to Exit
        """)
    userinput = input(">>> ")
    print()

    if userinput == "1":
        patient_name = input('Enter patient name:')
        Register_patient.put(patient_name)
        current_patient = patient_name
        print(f"Patient {patient_name} successfully Registered\n")

    elif userinput == "2":
        Register_patient.get()
        print (f"Patient {current_patient} removed after meeting the doctor.\n")

    elif userinput == "3":
        print("Current Patient Queue")
        for i in Register_patient.queue:
            print (i)

    elif userinput == "4":
        print("Exited")
        SystemExit.exit()
    
    else:
        print("Invalid Input. Follow the instruction Well.\n\n")








