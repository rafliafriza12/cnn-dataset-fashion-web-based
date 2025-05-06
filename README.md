# CNN Fashion Dataset Web-Based Project

This is a web-based application for CNN (Convolutional Neural Network) classification of fashion datasets.

## Prerequisites

- Git
- Python 3.x
- Node.js and npm/yarn

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rafliafriza12/cnn-dataset-fashion-web-based.git
```

### 2. Backend Setup

```bash
# Navigate to the project directory
cd cnn-dataset-fashion-web-based

# Navigate to the backend directory
cd backend

# Install dependencies
pip install flask flask-cors tensorflow numpy

# Run the backend server
# For Linux/macOS:
python3 server.py
# For Windows:
python server.py
```

### 3. Frontend Setup

Open a new terminal tab/window and:

```bash
# Navigate back to the project root
cd ..

# Navigate to the frontend directory
cd frontpage

# Install dependencies (choose one)
npm install
# OR
yarn install

# Run the development server
npm run dev
# OR
yarn dev
```

### 4. Access the Application

Open your browser and navigate to:

```
http://localhost:5173
```

## Project Structure

- `backend/`: Contains the Flask server and CNN model
- `frontpage/`: Contains the frontend application

## Technologies Used

- Backend: Flask, TensorFlow, NumPy
- Frontend: React (Vite)


## Author

Rafli Afriza Nugraha
