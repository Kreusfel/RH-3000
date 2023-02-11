from dataset import Dataset


def main():
    dataset = Dataset("data/behavior-based-questions.csv")
    print("Hello ! De quels sujets voulez-vous parler ?")
    print("Voici la liste des points que j'ai :")
    for subject in dataset.getUniqueTags():
        print(subject)

    user_choice = input("Type in the subject you're interested in:")

    while user_choice not in dataset.getUniqueTags():
        user_choice = input(
            "Sorry, this subject is not in our database. Type in the subject you're interested in:"
        )

    print("Here is the list of questions associated to this subject:")
    for question in dataset.generateQuestionaire(user_choice):
        print(question)


main()
