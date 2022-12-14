import json

points = 0


def show_question(question):
    global points

    print()
    print(question["pytanie"])
    print("a", question["a"])
    print("b", question["b"])
    print("c", question["c"])
    print("d", question["d"])
    print()

    answer = input("Którą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("Prawidłowa odpowiedź, masz", points, "pkt.")

    else:
        print("Zła odpowiedź, prawidłowa to " +
              question["prawidlowa_odpowiedz"] + ".")


with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])


print()
print("Koniec. Zdobyta liczba punktów: " + str(points) + ".")
