class StudentNode:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.prev = None
        self.next = None

    def swap_data(self, other):
        """Swap data with another student node"""
        self.roll_no, other.roll_no = other.roll_no, self.roll_no
        self.name, other.name = other.name, self.name
        self.marks, other.marks = other.marks, self.marks


class StudentRecordSystem:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_node = StudentNode(roll_no, name, marks)
        if not self.head:
            self.head = new_node
            print("Student added.")
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print("Student added.")

    def delete_student(self, roll_no):
        temp = self.head
        while temp and temp.roll_no != roll_no:
            temp = temp.next

        if not temp:
            print("Student not found.")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Student deleted.")

    def update_student(self, roll_no):
        temp = self.head
        while temp and temp.roll_no != roll_no:
            temp = temp.next

        if not temp:
            print("Student not found.")
            return

        temp.name = input("Enter new name: ")
        try:
            temp.marks = float(input("Enter new marks: "))
        except ValueError:
            print("Invalid input for marks. Update cancelled.")
            return

        print("Student record updated.")

    def search_student(self, roll_no):
        temp = self.head
        while temp and temp.roll_no != roll_no:
            temp = temp.next

        if not temp:
            print("Student not found.")
            return

        print(f"Roll No: {temp.roll_no}, Name: {temp.name}, Marks: {temp.marks}")

    def sort_students(self, by_marks=True, ascending=True):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if by_marks:
                    condition = (current.marks > current.next.marks) if ascending else (current.marks < current.next.marks)
                else:
                    condition = (current.roll_no > current.next.roll_no) if ascending else (current.roll_no < current.next.roll_no)

                if condition:
                    current.swap_data(current.next)
                    swapped = True
                current = current.next

        print("Records sorted.")

    def display_records(self):
        if not self.head:
            print("No records to display.")
            return

        print("\nStudent Records:")
        temp = self.head
        while temp:
            print(f"Roll No: {temp.roll_no}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next


def main():
    system = StudentRecordSystem()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Sort Students")
        print("6. Display Records")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                roll = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                marks = float(input("Enter Marks: "))
                system.add_student(roll, name, marks)
            except ValueError:
                print("Invalid input. Try again.")

        elif choice == '2':
            try:
                roll = int(input("Enter Roll No to delete: "))
                system.delete_student(roll)
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            try:
                roll = int(input("Enter Roll No to update: "))
                system.update_student(roll)
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            try:
                roll = int(input("Enter Roll No to search: "))
                system.search_student(roll)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            sort_by = input("Sort by (roll/marks): ").strip().lower()
            order = input("Order (asc/desc): ").strip().lower()
            by_marks = True if sort_by == 'marks' else False
            ascending = True if order == 'asc' else False
            system.sort_students(by_marks=by_marks, ascending=ascending)

        elif choice == '6':
            system.display_records()

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
