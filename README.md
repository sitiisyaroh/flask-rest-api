# Flask REST API

A simple REST API built with Flask to demonstrate the basics of creating a web service using Flask. Including simple html page to demostrate the api.

## Features

- Basic `/api` route that returns a JSON response.
- Built using Python and Flask.
- Easy to extend with more API endpoints and functionality.
- Include simple html page to demonstrate.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/sitiisyaroh/flask-rest-api.git
cd flask-rest-api
```
### 2. Set up the virtual environment
(Optional but recommended to avoid conflicts with other Python packages)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
This will include Flask and any other dependencies used in the project.
## Usage
To start the Flask server, run:
```bash
python api.py
```
The API will be accessible at http://127.0.0.1:5000/api.

## Example Request
Make a GET request to /api:

curl http://127.0.0.1:5000/api/users/

## Response
```json
[
  {
    "id": 3,
    "name": "Dhea",
    "email": "dhea@gmail.com",
    "jabatan": "Sekretaris",
    "usia": 27,
    "kota": ""
  },
  {
    "id": 7,
    "name": "Satria",
    "email": "satria@gmail.com",
    "jabatan": "Tour Guide",
    "usia": 20,
    "kota": ""
  },
  {
    "id": 9,
    "name": "Isya",
    "email": "sitiisyaroh17@gmail.com",
    "jabatan": "Bendahara",
    "usia": 21,
    "kota": "Semarang"
  }
]
```
## Documentations
- GET request
  
![image](https://github.com/user-attachments/assets/93793cae-b8a6-46e8-85cd-021fbf16375c)

- Demonstration from simple html page for GET, DELETE, PATH, and POST request
https://github.com/user-attachments/assets/9594b23b-3c73-4f8d-b03f-f6bf7b0f0463

