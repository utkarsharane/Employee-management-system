from django.contrib import admin
from .models import DateRange,Department, Employee, EmployeeSalary
from django.utils.html import format_html

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1



class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]
    list_display = ('name', 'floor', 'display_hierarchy')
    search_fields = ('name',)

    def display_hierarchy(self, obj):
        hierarchy = obj.get_employee_hierarchy()
        return format_html(self.format_hierarchy(hierarchy))

    def format_hierarchy(self, hierarchy):
        html = f"<strong>{hierarchy['manager']}</strong><ul>"
        for employee in hierarchy['employees']:
            html += "<li>"
            html += self.format_hierarchy(employee)
            html += "</li>"
        html += "</ul>"
        return html

    display_hierarchy.short_description = 'Employee Hierarchy'

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'department', 'reporting_manager')
    list_filter = ('designation', 'department')
    search_fields = ('name', 'email')

# class DepartmentAdmin(admin.ModelAdmin):
#     inlines = [EmployeeInline]
#     list_display = ('name', 'floor')
#     search_fields = ('name',)


class EmployeeSalaryInline(admin.TabularInline):
    model = EmployeeSalary
    extra = 1

class DateRangeAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    search_fields = ('start_date', 'end_date')

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'date_range')
    list_filter = ('employee__department', 'date_range__start_date', 'date_range__end_date')
    search_fields = ('employee__name', 'date_range__start_date', 'date_range__end_date')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(DateRange, DateRangeAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)
