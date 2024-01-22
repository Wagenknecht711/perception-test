def is_dream(memory, factual_accuracy, reliving):
    return not memory or (not factual_accuracy and memory) or not reliving

def is_reliving(memory, dream):
    return not dream and memory

def ask_question(question):
    response = input(question + " (yes/no): ").strip().lower()
    return response == 'yes'

def main():
    print("Answer the following questions with 'yes' or 'no' to find out if your experience is a dream, reliving, or confabulation.")

    memory = ask_question("Do you believe this experience is based on a real memory?")
    factual_accuracy = ask_question("Do you believe the facts in this memory are accurate?")
    reliving = ask_question("Are you consciously trying to relive a past experience?")
    dream = is_dream(memory, factual_accuracy, reliving)
    reliving = is_reliving(memory, dream)    
    if dream:
        print("Your experience is likely a DREAM.")
    elif reliving:
        print("Your experience is likely RELIVING a memory.")
    else:
        print("Your experience doesn't clearly fit into a specific category.")

while(True):
    main()
    print()