# Base Class
class Hospital:
    def __init__(self):
        self.doctors = []        # list to store doctor info
        self.appointments = []   # list to store booked appointments

    def add_doctor(self, name, specialization, timing):
        doctor = {
            "name": name,
            "specialization": specialization,
            "timing": timing
        }
        self.doctors.append(doctor)
        print(f" Doctor {name} added successfully!")

    def show_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        else:
            print("\n List of Doctors:")
            for doc in self.doctors:
                print(f" {doc['name']} | {doc['specialization']} | Available: {doc['timing']}")
            print()


# Derived Class
class Patient(Hospital):
    def __init__(self):
        super().__init__() 
        self.patients = [] 

    def register_patient(self, name, age, disease):
        patient = {
            "name": name,
            "age": age,
            "disease": disease
        }
        self.patients.append(patient)
        print(f" Patient {name} registered successfully!")

    def book_appointment(self, patient_name, doctor_name):
       
        doctor_found = any(doc["name"] == doctor_name for doc in self.doctors)
        patient_found = any(p["name"] == patient_name for p in self.patients)

        if not doctor_found:
            print(f" Doctor {doctor_name} not found.")
        elif not patient_found:
            print(f" Patient {patient_name} not found.")
        else:
            self.appointments.append({"patient": patient_name, "doctor": doctor_name})
            print(f" Appointment booked: {patient_name} with Dr. {doctor_name}")

    def show_appointments(self):
        if not self.appointments:
            print("No appointments booked yet.")
        else:
            print("\n All Appointments:")
            for app in self.appointments:
                print(f"{app['patient']} → Dr. {app['doctor']}")
            print()


hospital = Patient()

# Add doctors
hospital.add_doctor("Dr. Smith", "Cardiologist", "9 AM - 2 PM")
hospital.add_doctor("Dr. Anita", "Dermatologist", "10 AM - 4 PM")

# Register patients
hospital.register_patient("John Doe", 30, "Chest Pain")
hospital.register_patient("Emma Watson", 25, "Skin Allergy")

# Show all doctors
hospital.show_doctors()

# Book appointments
hospital.book_appointment("John Doe", "Dr. Smith")
hospital.book_appointment("Emma Watson", "Dr. Anita")

# Show all appointments
hospital.show_appointments()
