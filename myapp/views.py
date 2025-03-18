from django.shortcuts import render
from .forms import StudentForm , EmployeeForm
from crud_operations import *
from mylogs import logger

mycollection = operation("my_db", "employee_db")

def student_form_view(request):
    try:
        form = StudentForm()

        if request.method == "POST":
            logger.info("POST.items")
            for i, j in request.POST.items():
                logger.info(f"{i} : {j}")

            form = StudentForm(request.POST)
            if form.is_valid():
                
                logger.info("{form.cleaned_data}")

                mydata = {
                    "name":form.cleaned_data["name"],
                    "enrollment_number":form.cleaned_data["enrollment_number"],
                    "department":form.cleaned_data["department"],
                    "dob":str(form.cleaned_data["date_of_birth"])
                }
            # Insert form data into MongoDB
            
                logger.info(f"this is my data: {mydata}")
                mycollection.create(mydata)
            
                return render(request, 'success.html', {"url":"/student-form/"})  # Redirect to a success page
            else :
                form = StudentForm()
    except Exception as e:
        logger.error(f"Error Occured:{e}")
    return render(request, 'student_form.html', {'form': form})

def employee_form_view(request):
    try:
        form = EmployeeForm()

        if request.method == "POST":
            logger.info("POST.items")
            for q, p in request.POST.items():
                logger.info(f'{q} : {p}')

            form = EmployeeForm(request.POST)   
            if form.is_valid():
                logger.info(f"data: {form.cleaned_data}")

                einfo = {
                    "name":form.cleaned_data["name"],
                    "employee_id":form.cleaned_data["employee_id"],
                    "doj":str(form.cleaned_data["date_of_joining"]),
                    "department":form.cleaned_data["department"]
                }
                logger.info(f"This is my data : {einfo}")
                mycollection.create(einfo)

                return render(request, "success.html", {"url":"/employee-form/"})
            else :
                logger.info(f"Errors are: {form.errors}")
                # form = EmployeeForm()
    except Exception as er:
        logger.error(f"Error Occured:{er}")
    return render(request, 'employee.html', {'form': form})
               

 
