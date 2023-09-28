for i in range(100):

    while True:
        answer = input('Should we break?: ')
        if answer != "no" and answer != "yes":
            print("Don't understand you")
        else:
            break

    if answer == "yes":
        break
    print(i)
