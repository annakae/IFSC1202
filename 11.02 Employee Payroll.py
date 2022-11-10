class Employee:
    def __init__(self, first_name, last_name, id_number, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.wage = wage
        self.hours_worked = 0

    def weekly_pay(self):
        return self.hours_worked * self.wage if self.hours_worked <= 40 else 40 * self.wage + (
                    self.hours_worked - 40) * (self.wage + self.wage / 2)

def find_employee(employee_list,employee_id):
    for i in range(len(employee_list)):
        if employee_list[i].id_number == employee_id:
            return i
    return -1

if __name__ == '__main__':
    employee_list = []
    with open("11.02 Employees.txt","r") as file:
        for line in file.readlines():
            line = [i.strip() for i in line.split(",")]
            employee_list.append(Employee(line[0],line[1],line[2],float(line[3])))
  
    with open("11.02 Hours.txt","r") as file:
        for line in file.readlines():
            line = [i.strip() for i in line.split(",")]
            ind = find_employee(employee_list,line[0])
            if ind != -1:
                employee_list[ind].hours_worked = int(line[1])
                
    print("{} {} {} {} {} {}".format("First Name".rjust(20),"Last Name".rjust(20),"ID Number".rjust(20),"Hours Worked".rjust(20),"Hourly Wage".rjust(20),"Weekly Pay").rjust(20))
    for i in range(len(employee_list)):
        print("{} {} {} {} {} {}".format(employee_list[i].first_name.rjust(20),employee_list[i].last_name.rjust(20),employee_list[i].id_number.rjust(20),("{:.2f}".format(employee_list[i].hours_worked)).rjust(20),("{:.2f}".format(employee_list[i].wage)).rjust(20),("{:.2f}".format(employee_list[i].weekly_pay())).rjust(20)))