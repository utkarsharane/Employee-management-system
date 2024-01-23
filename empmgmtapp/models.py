from django.db import models

# class Department(models.Model):
#     name = models.CharField(max_length=255)
#     floor = models.IntegerField()

#     def __str__(self):
#         return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

    def get_employee_hierarchy(self, manager=None):
        hierarchy = {'manager': manager, 'employees': []}

        if manager:
            employees = Employee.objects.filter(department=self, reporting_manager=manager)
        else:
            employees = Employee.objects.filter(department=self, reporting_manager=None)

        for employee in employees:
            hierarchy['employees'].append(self.get_employee_hierarchy(employee))

        return hierarchy
    
class Employee(models.Model):
    DESIGNATIONS = [
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=DESIGNATIONS)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class DateRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_range = models.ForeignKey(DateRange, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name} - {self.salary} ({self.date_range})"