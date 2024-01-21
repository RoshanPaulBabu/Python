class AttendanceSystem:
    def __init__(self):
        self.attendance = {}

    def mark_present(self, student_name):
        if student_name in self.attendance:
            self.attendance[student_name] += 1
        else:
            self.attendance[student_name] = 1

    def mark_absent(self, student_name):
        if student_name in self.attendance:
            self.attendance[student_name] -= 1
        else:
            self.attendance[student_name] = 0

    def get_attendance_status(self, student_name):
        if student_name in self.attendance:
            return f"{student_name} has attended {self.attendance[student_name]} classes."
        else:
            return f"{student_name} has not attended any classes."

    def get_all_attendance(self):
        return self.attendance

    def __str__(self):
        return "Attendance System"

attendance_system = AttendanceSystem()

while True:
    print("\nMenu")
    print("1. Mark Present")
    print("2. Mark Absent")
    print("3. Check Attendance Status")
    print("4. View All Attendance")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_name = input("Enter student name: ")
        attendance_system.mark_present(student_name)
        print(f"{student_name} has been marked present.")
    elif choice == 2:
        student_name = input("Enter student name: ")
        attendance_system.mark_absent(student_name)
        print(f"{student_name} has been marked absent.")
    elif choice == 3:
        student_name = input("Enter student name: ")
        status = attendance_system.get_attendance_status(student_name)
        print(status)
    elif choice == 4:
        all_attendance = attendance_system.get_all_attendance()
        for student, classes_attended in all_attendance.items():
            print(f"{student}: {classes_attended} classes attended.")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please select a valid option.")
