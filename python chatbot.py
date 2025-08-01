import tkinter as tk

responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hi there! How can I assist you today?",
    "hey": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you!",
    "bye": "Goodbye! Have a great day!",
    "what can you do": "I can answer your questions, chat with you, and help with basic tasks!",
    "who created you": "I was created by Satvika who loves AI!",
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
    "weather": "I can't fetch live weather updates yet, but it's always a great day to learn something new!",
    "favorite color": "I like all colors, but blue is often associated with intelligence!",
    "default": "I'm not sure how to respond to that. Can you rephrase?"
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

def send_message():
    user_text = user_input.get()
    chat_history.insert(tk.END, "You: " + user_text + "\n")
    bot_response = get_response(user_text)
    chat_history.insert(tk.END, "Bot: " + bot_response + "\n")
    user_input.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Rule-Based Chatbot")
root.configure(bg="lightblue")

chat_history = tk.Text(root, height=20, width=50, bg="white")
chat_history.pack(padx=10, pady=10)

user_input = tk.Entry(root, width=40)
user_input.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message, bg="lightgreen")
send_button.pack(pady=5)

root.mainloop()