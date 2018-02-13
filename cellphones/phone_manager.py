# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones


class Phone:

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None

    def assign(self, employee_id):
        self.employee_id = employee_id

    def is_assigned(self):
        return self.employee_id is not None

    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'\
            .format(self.id, self.make, self.model, self.employee_id)


class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


class PhoneAssignments:

    def __init__(self):
        self.phones = []
        self.employees = []

    def add_employee(self, employee):
        # this raises EmployeeException if two employees with same ID are added
        for employed in self.employees:
            if employed.id == employee.id:
                raise PhoneError("Employee already exists!")
        self.employees.append(employee)

    def add_phone(self, phone):
        for device in self.phones:
            if device.id == phone.id:
                raise PhoneError("Device already in system!")
        self.phones.append(phone)

    def assign(self, phone_id, employee):
        if self.phone_info(employee) is not None:
            if self.phone_info(employee) is phone_id:
                return
            else:
                raise PhoneError("Employee already has a phone!")
        for phone in self.phones:
            if phone.id == phone_id:
                if phone.is_assigned():
                    raise PhoneError("Phone is already assigned to an employee!")
                else:
                    phone.assign(employee.id)
                return

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None

    def phone_info(self, employee):
        if employee not in self.employees:
            raise PhoneError('Employee does not exist!')
        else:
            for phone in self.phones:
                if phone.employee_id == employee.id:
                    return phone
        return None


class PhoneError(Exception):
    pass
