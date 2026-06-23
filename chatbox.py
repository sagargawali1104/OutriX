print("======================================")
print("      AI CHATBOT USING PYTHON")
print("======================================")
print("Type 'bye' to exit the chatbot")
print()

while True:

    user = input("You : ").lower()

    if user == "hello":
        print("Bot : Hello! How can I help you today?")

    elif user == "hi":
        print("Bot : Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot : I am fine and ready to help you.")

    elif user == "what is your name":
        print("Bot : My name is AI Chatbot.")

    elif user == "who created you":
        print("Bot : I was created using Python programming.")

    elif user == "what is python":
        print("Bot : Python is a high-level programming language.")

    elif user == "what is ai":
        print("Bot : AI stands for Artificial Intelligence.")

    elif user == "what is machine learning":
        print("Bot : Machine Learning enables computers to learn from data.")

    elif user == "what is data science":
        print("Bot : Data Science is the study of data for extracting knowledge.")

    elif user == "what is college":
        print("Bot : A college is an educational institution.")

    elif user == "which college":
        print("Bot : I can provide information about engineering colleges.")

    elif user == "what is dsa":
        print("Bot : DSA stands for Data Structures and Algorithms.")

    elif user == "what is oop":
        print("Bot : OOP stands for Object Oriented Programming.")

    elif user == "what is c++":
        print("Bot : C++ is an object-oriented programming language.")

    elif user == "what is java":
        print("Bot : Java is a popular object-oriented programming language.")

    elif user == "what is html":
        print("Bot : HTML is used to create web pages.")

    elif user == "what is css":
        print("Bot : CSS is used to style web pages.")

    elif user == "what is javascript":
        print("Bot : JavaScript is used to add interactivity to websites.")

    elif user == "what is github":
        print("Bot : GitHub is a platform for hosting code repositories.")

    elif user == "what is internship":
        print("Bot : An internship provides practical industry experience.")

    elif user == "thank you":
        print("Bot : You are welcome.")

    elif user == "thanks":
        print("Bot : Happy to help.")

    elif user == "good morning":
        print("Bot : Good Morning!")

    elif user == "good afternoon":
        print("Bot : Good Afternoon!")

    elif user == "good evening":
        print("Bot : Good Evening!")

    elif user == "bye":
        print("Bot : Goodbye! Have a nice day.")
        break

    else:
        print("Bot : Sorry, I do not understand that question.")