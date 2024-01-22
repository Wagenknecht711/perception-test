def ask_question_scale(question):
    response = input(question + " (rate 1-5): ").strip()
    if response.isdigit():
        return int(response)
    else:
        return 0

def main():
    print("Answer the following questions on a scale of 1 to 5 (1 being 'strongly disagree', 5 being 'strongly agree') to find out more about your experience.")
    
    memory = ask_question_scale("This experience is based on a real memory.")
    factual_accuracy = ask_question_scale("The facts in this memory are accurate.")
    reliving = ask_question_scale("I am consciously trying to relive a past experience.")
    
    if memory > 3 and factual_accuracy > 3 and reliving < 3:
        print("Your experience seems to be a clear memory.")
    elif memory < 3 and reliving < 3:
        print("Your experience may be more of a dream or imagination.")
    elif reliving > 3:
        print("You seem to be reliving a past experience.")
    else:
        print("Your experience is complex and doesn't fit neatly into a specific category.")

    if input("Would you like to analyze another experience? (yes/no): ").strip().lower() != 'yes':
        return False
    return True

while(main()):
    print()
