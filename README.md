Please install a virtual enviornment aswell as import the google generative ai into your virtual enviornment! 
Tutorial:
Set Up a Python Virtual Environment

It’s a good practice to set up a virtual environment to keep dependencies isolated from other projects. Here's how to do it:

On Windows:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
This command will create and activate a virtual environment in the venv/ directory.

Install Required Dependencies

Once inside the virtual environment, users need to install the required Python libraries. These libraries are listed in your requirements.txt file.

To install them, run:

bash
Copy
Edit
pip install -r requirements.txt
This command will install all the necessary dependencies like google-generativeai, sympy, and others from the requirements.txt file.

Obtain an API Key for Google Gemini

Your project relies on the Google Gemini API. Users need to get their own API key to use the chatbot. Here’s how they can do that:

Go to the Google Cloud Console.

Create a new project (or select an existing one).

Navigate to API & Services > Credentials.

Create an API key.

Copy the key.

Once they have the API key, they need to store it in an .env file. Here’s the format for the .env file:

bash
Copy
Edit
API_KEY=your-api-key-here
The .env file should be placed in the root of the project folder.

Run the Code

Once the virtual environment is set up, the dependencies are installed, and the .env file is configured with the API key, they can run the chatbot:

bash
Copy
Edit
python chatbot.py
The chatbot will now be running, and they can start interacting with it in the terminal.

Exit the Chatbot

If users want to exit the chatbot, they can type bye and the chatbot will terminate the session.

Summary: What Users Need to Do
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/stem-chatbot.git
cd stem-chatbot
Set up a virtual environment and activate it:

Windows:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Get a Google Gemini API key, create a .env file with:

bash
Copy
Edit
API_KEY=your-api-key-here
Run the chatbot:

bash
Copy
Edit
python chatbot.py
