import google.generativeai as ai

# API key (replace with your actual API key)
API_KEY = 'AIzaSyATcGnT4KY0BLPDhgAkdNlCH8oBn_xuY-E'  # Replace this with your actual API key

# Configure the API using the API key
ai.configure(api_key=API_KEY)

# Select a supported model (you can change this to another model if needed)
model_name = "gemini-2.5-pro-exp-03-25"  # You can replace this with a different model (e.g., "gemini-3-0")

# Create a new model instance
try:
    model = ai.GenerativeModel(model_name)
    chat = model.start_chat()
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Store conversation history for contextual awareness
context_history = []

# STEM topics and subjects (example)
stem_topics = {
    'math': ['algebra', 'geometry', 'trigonometry', 'calculus', 'statistics'],
    'physics': ['force', 'motion', 'energy', 'electricity', 'magnetism'],
    'chemistry': ['elements', 'compounds', 'reactions', 'stoichiometry'],
    'biology': ['cells', 'genetics', 'evolution', 'ecology'],
    'engineering': ['mechanical', 'civil', 'electrical', 'software'],
}

# Custom response logic (e.g., greeting and STEM topic recognition)
def custom_response(message):
    greetings = ['hi', 'hello', 'hey']
    if any(greet in message.lower() for greet in greetings):
        return "Hello! How can I assist you today with STEM subjects?"
    
    # Check for a STEM topic mention
    for subject, topics in stem_topics.items():
        if any(topic in message.lower() for topic in topics):
            return f"Sure, I can help with {subject} topics. What specific question do you have?"
    
    return None  # No custom response, fallback to AI

# Start the conversation loop
while True:
    message = input('You: ')  # Takes user input
    if message.lower() == 'bye':  # Exit condition for the chatbot
        print('Chatbot: Goodbye!')
        break

    # Check for custom responses (e.g., greetings and topic recognition)
    response = custom_response(message)
    if response:
        print('STEM-Bot:', response)  # Display the custom response
    else:
        try:
            # Add the user's message to the context history for conversation awareness
            context_history.append(message)

            # Send the entire conversation history to the model for context-aware response generation
            ai_response = chat.send_message("\n".join(context_history))
            print('Chatbot:', ai_response.text)  # Display the model's response

            # Add the model's response to the context history for next interaction
            context_history.append(ai_response.text)

        except Exception as e:
            print(f"Error: {e}")
            break  # Exit the loop if an error occurs


