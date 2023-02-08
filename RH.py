import csv
import random

CSV_FILE = "questions.csv"
    
def start():
    print("Hello ! De quels sujets voulez-vous parler ?")
    print("Voici la liste des points que j'ai :")
    rsc = read_subject_csv(CSV_FILE)
    rus = read_unique_subjects(rsc)
    for s in rus:
        print(s)
    ls = list_subjects()
    for s in ls:
        for q in list_questions(CSV_FILE,s):
            print(q[0])
    
def read_subject_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) #Saute l'en-tête
        subjects = []
        for row in reader:
            subjects.append(row)
    return subjects
  
def read_unique_subjects(data):
    newList = []
    for i in data:
        if i[1] not in newList:
            newList.append(i[1])
    return newList

def list_subjects():
    input_subjects = input("Entrez les sujets séparés par un ';' : ")
    subjects = list(map(str.strip, input_subjects.split(";")))
    for s in subjects:
        print(s)
    return subjects
    
def list_questions(file, subject):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader) #Saute l'en-tête
        questions = []
        for row in reader:
            if row[1] == subject:
                questions.append(row)
                
    return_questions = []
    return_questions.append(random.choice(questions))
    del questions[questions.index(random.choice(questions))]
    return_questions.append(random.choice(questions))
    del questions[questions.index(random.choice(questions))]
    return_questions.append(random.choice(questions))

    return return_questions
  
start()
input()
