from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.verify import authentication, form_varification
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .form import question_paper_form
from app.models import Subject_data
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def serve_android_csv(request):
  if request.method == "GET":
    file_path = os.path.join(settings.BASE_DIR, 'android.csv')
    return FileResponse(open(file_path, 'rb'), content_type='text/csv')


# Load the model from a file
with open("dataset/blooms_level.pkl", "rb") as f:
    blooms_model = pickle.load(f)
with open("dataset/blooms_vector.pkl", "rb") as f:
    blooms_vector = pickle.load(f)
# Create your views here.
def index(request):
    # return HttpResponse("This is Home page")    
    return render(request, "index.html")

def render_template(request):
  if request.method == "GET":
    return render(request, 'Template.html')  # Render the template
def log_in(request):
    if request.method == "POST":
        # return HttpResponse("This is Home page")  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("log_in")
    # return HttpResponse("This is Home page")    
    return render(request, "log_in.html")

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(fname, contact_no, ussername)
        verify = authentication(fname, lname, password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("/")
            
        else:
            messages.error(request, verify)
            return redirect("register")
    # return HttpResponse("This is Home page")    
    return render(request, "register.html")


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)

def dashboard(request):
    context = {
        'fname': request.user.first_name, 
        'form' : question_paper_form(),
        }
    if request.method == "POST":
        form = question_paper_form(request.POST, request.FILES)
        try:
            if form.is_valid():
                college_name = form.cleaned_data['college_name']
                branch_name = form.cleaned_data['branch_name']
                semester = form.cleaned_data['semester']
                subject_name = form.cleaned_data['subject_name']
                year = form.cleaned_data['year']
                faculty = form.cleaned_data['faculty']
                date = form.cleaned_data['date']
                qb = form.cleaned_data['qb']
                verify_from = form_varification(faculty)
                if verify_from == "Success":                
                    # Load the saved model
                    model = pickle.load(open('dataset/model.pkl', 'rb'))
                    vectorizer = pickle.load(open('dataset/vectorizer.pkl', 'rb'))
                    reader = pd.read_csv(qb)
                    X_new = vectorizer.transform(reader['question'])
                    # Make predictions using the loaded model
                    y_new_pred = model.predict(X_new)
                    y_new_pred = np.array(y_new_pred)
                    y_new_pred = y_new_pred.astype(int)
                    # Add the predicted marks to the new_data DataFrame
                    reader['predicted_marks'] = y_new_pred
                    # Filter the new_data DataFrame based on predicted marks
                    new_data_4 = reader[reader['predicted_marks'] == 4]
                    new_data_5 = reader[reader['predicted_marks'] == 5]
                    new_data_6 = reader[reader['predicted_marks'] == 6]
                    new_data_7 = reader[reader['predicted_marks'] == 7]
                    new_data_8 = reader[reader['predicted_marks'] == 8]

                    # Select 2 questions for each of the marks using the head method
                    selected_data = pd.concat([new_data_8.sample(n=2, random_state=24), new_data_7.sample(n=2, random_state=24), new_data_6.sample(n=2, random_state=24), new_data_5.sample(n=2, random_state=24), new_data_4.sample(n=2, random_state=24)], axis=0)
                    selected_list = []
                    blooms_level = []
                    for _,row in selected_data[['question']].iterrows():
                        new_question_vectorized = blooms_vector.transform(row)
                        predicted_blooms_level = blooms_model.predict(new_question_vectorized)[0]
                        blooms_level.append(predicted_blooms_level)
                    for _, row in selected_data[['question', 'predicted_marks']].iterrows():
                        selected_dict = row.to_list()
                        selected_list.append(selected_dict)
                    qus = []
                    [qus.extend([str(q), str(m)]) for q,m in selected_list]
                    filename = branch_name + "_"  + semester + "_" +  subject_name  + '_question_paper.csv'
                    subject_data  = Subject_data(college_name = college_name, branch_name = branch_name, semester = semester, subject_name = subject_name, year = year, faculty = faculty, qb = qb, q1 = qus[0],q2 = qus[2],q3 = qus[4],q4 = qus[6],q5 = qus[8],q6 = qus[10],q7 = qus[12],q8 = qus[14],q9 = qus[16],q10 = qus[18],m1 = qus[1],m2 = qus[3],m3 = qus[5],m4 = qus[7],m5 = qus[9],m6 = qus[11],m7 = qus[13],m8 = qus[15],m9 = qus[17] ,m10 = qus[19],bl1 = blooms_level[0],bl2 = blooms_level[1],bl3 = blooms_level[2],bl4 = blooms_level[3],bl5 = blooms_level[4],bl6 = blooms_level[5],bl7 = blooms_level[6],bl8 = blooms_level[7],bl9 = blooms_level[8] ,bl10 = blooms_level[9],date = date)
                    subject_data.save()

                    # Save the selected data to a CSV file
                    selected_data.to_csv(filename, index=False)
                    return redirect("result")
                else:
                    messages.error(request, verify_from)
                    return redirect("dashboard")
            else:
                messages.error(request, "Invalid Date")
                return redirect("dashboard")
        except:
            messages.error(request, "Uploaded Questions are Not Appropriate!!!")
            return redirect("dashboard")
    return render(request, "dashboard.html",context)



# def dashboard(request):
#     context = {
#         'fname': request.user.first_name, 
#         'form' : question_paper_form(),
#     }

#     if request.method == "POST":
#         form = question_paper_form(request.POST, request.FILES)
#         try:
#             if form.is_valid():
#                 college_name = form.cleaned_data['college_name']
#                 branch_name = form.cleaned_data['branch_name']
#                 semester = form.cleaned_data['semester']
#                 subject_name = form.cleaned_data['subject_name']
#                 year = form.cleaned_data['year']
#                 faculty = form.cleaned_data['faculty']
#                 date = form.cleaned_data['date']
#                 qb = form.cleaned_data['qb']
                
#                 # Load the saved model and vectorizer
#                 model = pickle.load(open('dataset/model.pkl', 'rb'))
#                 vectorizer = pickle.load(open('dataset/vectorizer.pkl', 'rb'))
                
#                 # Read the input CSV file
#                 reader = pd.read_csv(qb)
                
#                 # Vectorize the questions
#                 X_new = vectorizer.transform(reader['question'])
                
#                 # Make predictions using the loaded model
#                 y_new_pred = model.predict(X_new)
#                 y_new_pred = np.array(y_new_pred)
                
#                 # Add the predicted marks to the DataFrame
#                 reader['predicted_marks'] = y_new_pred
                
#                 # Sample random questions for each mark
#                 random_questions = []
#                 for mark in range(4, 9):
#                     mark_questions = reader.sample(n=min(1, len(reader)), random_state=24)
#                     random_questions.append(mark_questions)

#                 # Concatenate the sampled questions
#                 selected_data = pd.concat(random_questions, axis=0)
                
#                 # Prepare the data for saving to the database
#                 qus = []
#                 blooms_level = []
#                 for _, row in selected_data[['question', 'predicted_marks']].iterrows():
#                     qus.extend([row['question'], row['predicted_marks']])
#                     new_question_vectorized = blooms_vector.transform([row['question']])
#                     predicted_blooms_level = blooms_model.predict(new_question_vectorized)[0]
#                     blooms_level.append(predicted_blooms_level)
                
#                 print("Length of qus:", len(qus))
#                 print("Length of blooms_level:", len(blooms_level))
                
#                 # Save the selected data to a CSV file
#                 filename = f"{branch_name}_{semester}_{subject_name}_question_paper.csv"
#                 selected_data.to_csv(filename, index=False)
                
#                 # Create and save the Subject_data object
#                 subject_data = Subject_data.objects.create(
#                     college_name=college_name,
#                     branch_name=branch_name,
#                     semester=semester,
#                     subject_name=subject_name,
#                     year=year,
#                     faculty=faculty,
#                     date=date,
#                     qb=qb,
#                     q1=qus[0],
#                     q2=qus[2],
#                     q3=qus[4],
#                     q4=qus[6],
#                     q5=qus[8],
#                     q6=qus[10],
#                     q7=qus[12],
#                     q8=qus[14],
#                     q9=qus[16],
#                     q10=qus[18],
#                     m1=qus[1],
#                     m2=qus[3],
#                     m3=qus[5],
#                     m4=qus[7],
#                     m5=qus[9],
#                     m6=qus[11],
#                     m7=qus[13],
#                     m8=qus[15],
#                     m9=qus[17],
#                     m10=qus[19],
#                     bl1=blooms_level[0],
#                     bl2=blooms_level[1],
#                     bl3=blooms_level[2],
#                     bl4=blooms_level[3],
#                     bl5=blooms_level[4],
#                     bl6=blooms_level[5],
#                     bl7=blooms_level[6],
#                     bl8=blooms_level[7],
#                     bl9=blooms_level[8],
#                     bl10=blooms_level[9],
#                 )
                
#                 # Redirect to the result page
#                 return redirect("result")
#             else:
#                 messages.error(request, "Invalid Form Data")
#                 return redirect("dashboard")
#         except Exception as e:
#             messages.error(request, f"An error occurred: {str(e)}")
#             return redirect("dashboard")

#     return render(request, "dashboard.html", context)






@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def result(request):
    subject_data = Subject_data.objects.last()
    context = {
        'fname': request.user.first_name, 
        'subject_data' : subject_data,
        }
    if request.method == "POST":
        return redirect("print")
    return render(request, "result.html",context)