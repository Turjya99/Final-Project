filename = "The_file_of_records_for_Students_of_CHemistry_department.txt"

def Add_records():
    
    name = input("Enter the student's name: ")
    roll = input("Enter the student's roll number: ")
    cgpa = input("Enter the student's CGPA: ")
    num = input("Enter the student's phone number: ")
    session = input("Enter the student's session: ")
    record = f"Name: {name}, Roll No: {roll}, CGPA: {cgpa}, Contaxt number: {num}, Session: {session} \n" 
  
    with open (filename, "a") as file:
        file.write(record + "\n")
        
    print("The record was added successfully to the file.")

def read_records():
   
    with open (filename, "r") as file: 
        records = file.readlines()
        
        for line in file:
            records = line.strip()
    
    if not records:
        print("No records found:(")
    
    else:
        print(records)

def Modify_records():
    
    record_number = int(input("Enter record number to modify: "))
    name = input("Enter the student's name: ")
    roll = input("Enter the student's roll number: ")
    cgpa = input("Enter the student's CGPA: ")
    num = input("Enter the student's phone number: ")
    session = input("Enter the student's session: ")
    record = f"Name: {name}, Roll No: {roll}, CGPA: {cgpa}, Contaxt number: {num}, Session: {session}" 
    
    with open (filename, "r") as file: 
        lines = file.readlines()
   
    if 1<=record_number<=len(lines):
        lines[record_number - 1] = record + '\n'
        with open (filename, "w") as file: 
            file.writelines(lines)

        print("Record Modified successfully :)")
    else: 
        print("Invalid record number.")

def Delete_records():
    
    record_number = int(input("Enter the record number you want to delete: "))
    
    with open (filename, "r") as file: 
        lines = file.readlines()

    if 1<= record_number <= len(lines):
        
        del(lines[record_number - 1])

        with open (filename, "w") as file: 
            file.writelines(lines)
        
        print("Record deleted succesfully. ")
    
    else: 
        print("Invalid record number:(")
    

def main():
    
    while True:
        print("======================")
        print("\nOperation Menu:")
        print("======================")
        print("1. Add Records")
        print("2. Read Records")
        print("3. Modify Recors")
        print("4. Delete Records")
        print("5. Exit")
        print("                     ")
    
        choice = int(input("Choose your option:"))
        
        if choice ==1:
            Add_records()
        
        elif choice == 2: 
            read_records()
        
        elif choice == 3:
            Modify_records()
        
        elif choice == 4:
            Delete_records()
        
        elif choice == 5:
            print("Closing the menu...")
            print("Thank you...")
            break
        
        else: 
            print("Invalid Choice... Please try again :(")

if __name__ == "__main__":
    main()