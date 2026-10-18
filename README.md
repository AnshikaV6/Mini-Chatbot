# Mini-Chatbot
## Gluco AI Chatbot

A simple command-line chatbot built in Python. It greets the user by name based on the time of day and answers questions using a dictionary of predefined replies.

### Features
- Time-based greeting (Good Morning / Afternoon / Evening / Night) using the system clock
- Personalised welcome using the user's name
- Keyword-based replies from a Python dictionary
- Handles questions like greetings, "what is python", and "motivate me"
- Friendly fallback message when it doesn't know the answer
- Type bye to exit

### How it works
1. The bot asks for your name and greets you according to the current hour.
2. The user types a question.
3. The question is converted to lowercase.
4. The bot loops through the dictionary keys and checks whether any key appears inside the user's question.
5. If a key matches, the stored reply is returned.
6. If nothing matches, the bot replies: "I am not able to tell that yet. I am still in learning mode".
7. The loop continues until the user types bye.

Example of the dictionary used as the chatbot's memory:

    responses = {
        "hello": "Hi,Welcome! How can I help you?",
        "what is python": "python is a programming language that is very popular in coding world"
    }

### Tech stack
- *Language:* Python 3
- *Modules:* datetime (time-based greeting)
- *Core concepts:* dictionary, functions, loops, conditionals, string methods
- *Interface:* Command line

### How to run
1. Make sure Python 3 is installed.
2. Clone the repository:

       git clone https://github.com/AnshikaV6/your-repo-name.git

3. Go to the project folder:

       cd your-repo-name

4. Run the program:

       python main.py

### What I learned
- Taking user input and processing it with string methods like lower()
- Using dictionaries to store and look up replies
- Writing a reusable function (getResponseOfBot)
- Using datetime to build time-based logic
- Running a continuous loop with an exit condition

### Limitations
- It only answers questions that contain a stored keyword
- It does not understand context or the meaning of sentences

### Future improvements
- Add more questions and replies
- Use NLP (for example NLTK) for smarter matching
- Connect to an AI API for open-ended answers
- Add a graphical or web interface
- Save conversation history

### Author
Anshika Vishwakarma | Computer Science and Engineering student
