# URL Shortener with Flask & JSON Storage

## 📌 Project Overview
This is a simple URL Shortener built using Python and Flask, which stores shortened URLs in a JSON file. It allows users to create short URLs, redirect to original URLs, and track click statistics.

---

## 🚀 Features
- Shorten long URLs to unique short codes.
- Store and retrieve data from a JSON file (No database required).
- Redirect users when they visit the short URL.
- Track the number of times a short URL has been accessed.
- Simple API endpoints for URL shortening and statistics retrieval.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the repository**
```sh
$ git clone [url-shortener.git](https://github.com/gourabdg47/flask-url-shortener.git)
$ cd url-shortener
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3️⃣ Install dependencies**
```sh
$ pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```sh
$ python app.py
```

The server will start at: `http://127.0.0.1:5000/`

---

## 🌍 API Endpoints

### 1️⃣ **Shorten a URL**
#### **Request:**
```http
POST /
Content-Type: application/json
{
    "url": "https://www.example.com"
}
```
#### **Response:**
```json
"127.0.0.1:5000/abc123"
```

---

### 2️⃣ **Redirect to Original URL**
#### **Request:**
```http
GET /<short_code>
```
#### **Response:**
Redirects to the original URL.

---

### 3️⃣ **Get Click Statistics**
#### **Request:**
```http
GET /stat/<short_code>
```
#### **Response:**
```json
"5"  # Number of times the short URL has been accessed
```

---

## 📂 Project Structure
```
📁 url-shortener
│── app.py                 # Flask app with API routes
│── url_shortner.py        # Core logic for URL shortening & storage
│── default.json           # JSON file to store shortened URLs
│── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 🛠️ To-Do Features
✅ Basic URL Shortener
✅ Click Tracking
✅ API Endpoints for Shortening & Redirecting
⬜ Store URLs in an SQLite or PostgreSQL Database
⬜ User Authentication (Optional Login for Users to Track Their URLs)
⬜ Custom Short Codes (Allow Users to Choose Their Own Codes)
⬜ Expiry Dates for Short Links
⬜ Admin Dashboard to View Statistics

---

## 🤝 Contribution
Feel free to fork this repository and submit a pull request! Any improvements are welcome. 🚀

---

## 📜 License
This project is open-source and available under the MIT License.

---

Happy coding! 😊


