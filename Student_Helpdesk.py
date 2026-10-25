# AI Student Helpdesk Chatbot
# A simple rule-based AI project

def get_response(question):
    question = question.lower()

    if any(word in question for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to AI Student Helpdesk."

    elif "your name" in question or "who are you" in question:
        return "I am AI Student Helpdesk Chatbot."

    elif "what is ai" in question or "artificial intelligence" in question:
        return "AI means Artificial Intelligence. It helps computers perform tasks that require human intelligence."

    elif "syllabus" in question:
        return "Please check your university or subject syllabus for the latest topics."

    elif "exam" in question or "timetable" in question:
        return "Please check the official college notice board for exam dates."

    elif "attendance" in question:
        return "Please contact your faculty to check your attendance."

    elif "library" in question:
        return "Please check your college library notice for opening hours."

    elif "fee" in question or "fees" in question:
        return "Please contact the college office for fee details."

    elif "python" in question:
        return "Python is a simple and popular programming language."

    elif "thank" in question:
        return "You're welcome! Happy learning."

    elif "bye" in question or "exit" in question:
        return "Goodbye! Best wishes for your studies."

    else:
        return "Sorry, I don't know that answer yet. Please ask another question."


def start_chatbot():
    print("=" * 45)
    print("     AI STUDENT HELPDESK CHATBOT")
    print("=" * 45)
    print("Ask me about AI, exams, attendance, fees,")
    print("library or Python.")
    print("Type 'bye' to exit.")
    print("-" * 45)

    while True:
        question = input("You: ").strip()

        if question.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Best wishes for your studies.")
            break

        if question == "":
            print("Bot: Please enter a question.")
            continue

        answer = get_response(question)
        print("Bot:", answer)


start_chatbot()