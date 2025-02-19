import heapq
import random
import time

class EmergencyRoom:
    def __init__(self):
        self.patients_queue = []
        heapq.heapify(self.patients_queue)

    def add_patient(self, patient_name, priority):
        heapq.heappush(self.patients_queue, (priority, patient_name))

    def treat_patients(self):
        while self.patients_queue:
            priority, patient_name = heapq.heappop(self.patients_queue)
            print(f"Treating patient: {patient_name} (Priority: {priority})")
            time.sleep(1)  # Simulating treatment time

# Simulate patient arrivals and priority assignment
emergency_room = EmergencyRoom()

# Simulate patient arrivals and priority assignment
patients_data = [
    ("Harsha", random.randint(1, 5)),
    ("Ayush", random.randint(1, 5)),
    ("Prabal", random.randint(1, 5)),
    ("Kulhad", random.randint(1, 5)),
    ("Pizza", random.randint(1, 5))
]

print("Patients arriving at the Emergency Room:")
for patient_name, priority in patients_data:
    print(f"Patient: {patient_name}, Priority: {priority}")
    emergency_room.add_patient(patient_name, priority)

print("\nTreating patients based on priority:")
emergency_room.treat_patients()
