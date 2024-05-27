def main():
    # List of questions
    questions = [
        "How emo is your girlfriend? (on a scale from 1 to 10): ",
        "How sexy is your girlfriend? (on a scale from 1 to 10): ",
        "How soft is your girlfriend? (on a scale from 1 to 10): ",
        "How funny is your girlfriend? (on a scale from 1 to 10): ",
        "How intelligent is your girlfriend? (on a scale from 1 to 10): ",
        "How kind is your girlfriend? (on a scale from 1 to 10): ",
        "How caring is your girlfriend? (on a scale from 1 to 10): ",
        "How supportive is your girlfriend? (on a scale from 1 to 10): ",
        "How adventurous is your girlfriend? (on a scale from 1 to 10): ",
        "How creative is your girlfriend? (on a scale from 1 to 10): "
    ]

    total_score = 0
    low_scores = []

    for question in questions:
        while True:
            try:
                answer = float(input(question))
                if 1 <= answer <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 10.")
        
        total_score += answer
        if answer < 9:
            low_scores.append(question)
            print(":( Warning: You have dared to rate your girlfriend lower than 9, you cunt. "
                  "Please reconsider your face by looking in the mirror you are not even a 5")

    average_score = total_score / len(questions)
    
    if low_scores:
        print("\nWarning: You rated your girlfriend lower than 9 for the following qualities:")
        for qs in low_scores:
            print(qs)
        print("Please reconsider your ratings.")

    if average_score < 9:
        print("\nYOU DON'T LOVE HER ENOUGH, TRY AGAIN BITCH")
    else:
        print("\nWELL, YOU ALMOST LOVE YOUR SHAWTY AS MUCH AS I LOVE MINE, GOOD JOB")

if __name__ == "__main__":
    main()
