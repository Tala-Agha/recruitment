def main():
    #write your code here
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]

    cv = {}
    name = input("Enter your name:  ")
    cv['name'] = name

    age = int(input("Enter your age:  "))
    cv['age'] = age

    experience = int(input("Enter years of experience:  "))
    cv['experience'] = experience

    cv['skills'] = []

    index = 1
    for skill in skills:
        print("{} . {}".format(index,skill))
        index += 1

    while(True):
        choose = int(input("Choose a skill in numbers:  "))
        if choose > 0 or choose < 7:
            cv['skills']=[]
            cv['skills'].append(skills[choose - 1])
            break
        else:
            print("enter valid number:  ")

    while(True):
        extra = int(input("Add another skill in numbers:  "))
        if extra > 0 or extra < 7:
            cv['skills'].append(skills[extra - 1])
            break
        else:
            print("enter valid number:  ")


    accepted = True
    if not(age > 25 and age < 40):
        accepted = False
    if not(experience >= 5):
        accepted = False
    if 'Eating' not in cv['skills']:
        accepted = False

    if accepted == True:
        print("You have been accepted, {}.".format(name))
    else:
        print("You have been rejected, {}.".format(name))








if __name__ == '__main__':
    main()
