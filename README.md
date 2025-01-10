Social Media Analytics with LangFlow Integration using reactjs(vite)

This project is a FastAPI-based application integrated with the LangFlow API to enable AI-powered chat responses. It features a React-based frontend built with Vite for a seamless user interface and interaction with the backend. The application is designed with modularity and security in mind, utilizing .env files for sensitive data management.

Features

AI Chat Integration: Leverages the LangFlow API for intelligent chat responses.

Frontend-Backend Communication: Supports CORS for secure and flexible interaction with the frontend.

Secure Data Handling: Environment variables used to safeguard sensitive data.

Simplified API: Easy-to-use API response structure for frontend integration.

Frontend Framework: React.js with Vite for lightning-fast performance.



---

Installation

Follow the steps below to set up and run the project locally:

1. Clone the Repository

git clone link
cd name

2. Backend Setup (FastAPI)

Prerequisites:

Python 3.9+

Virtual Environment


Steps:

1. Navigate to the backend directory:

cd backend


2. Create and activate a virtual environment:

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file:

Add sensitive data like LangFlow API keys in the .env file.


LANGFLOW_API_KEY=your_api_key


5. Run the backend server:

uvicorn main:app --reload



3. Frontend Setup (React.js with Vite)

Prerequisites:

Node.js 18+

npm or yarn


Steps:

1. Navigate to the frontend directory:

cd ../frontend


2. Install dependencies:

npm install


3. Start the development server:

npm run dev




---

API Endpoints

Base URL

http://localhost:8000

Endpoints

POST /chat:
Sends a chat message to LangFlow and receives a response.

Request Body:  
{  
  "message": "Your query here"  
}  

Response:  
{  
  "response": "AI-generated response"  
}



---

Technologies Used

Backend:

FastAPI: For creating RESTful APIs.

LangFlow API: For AI-powered chat responses.

Python-dotenv: For managing environment variables.

Uvicorn: For running the FastAPI server.


Frontend:

React.js: For building the user interface.

Vite: For faster development and build process.

Axios: For handling API request.


---

Contributing

Feel free to contribute by:

Creating issues for bugs or feature requests.

Forking the repository and submitting pull requests.



---

License

This project is licensed under the MIT License.


---

Contact

For queries, contact Vedant A. Nawale.


---

This README provides detailed instructions for installation, setup, and usage, ensuring developers and users can easily understand and work with your project.

