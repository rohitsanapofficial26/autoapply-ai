# AutoApply AI

AutoApply AI is a **full-stack AI-powered job application assistant** that helps users track job applications, match resumes with job roles, and manage application status through a clean dashboard.

This project is built as a **portfolio-ready system** demonstrating backend engineering, database design, API development, and frontend integration.
 Key Features
 **Resume-based job matching (AI-ready)**
**Dashboard to track job applications**
**Application status management** (Applied / Pending / Rejected)
**REST APIs built with FastAPI**
**SQLite database using SQLAlchemy ORM**
**React dashboard frontend**
**CORS-enabled for frontend-backend communication**

### Backend
* **Python**
* **FastAPI** – API framework
* **SQLAlchemy** – ORM
* **SQLite** – Database (easy local setup)
* **Uvicorn** – ASGI server
* **React.js**
* **Fetch API** for backend communication
* **CSS** for clean UI

---

## 📁 Project Structure
Autoapply-ai/
├── backend/
│   ├── main.py
│   ├── autoapply.db
│   ├── requirements.txt
│   └── app/
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── services/
│       └── schemas/
│
├── autoapply-dashboard/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md


### 2️. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Initialize Database

```bash
python -c "from app.core.init_db import init_db; init_db()"
```

#### Run Backend Server
python -m uvicorn main:app --reload
### 3️ Frontend Setup
```bash
cd autoapply-dashboard
npm install
npm start

## 📡 API Endpoints

| Method | Endpoint                  | Description            |
| ------ | ------------------------- | ---------------------- |
| GET    | `/dashboard/applications` | List all applications  |
| POST   | `/apply/execute`          | Save a new application |

## 🧪 Example API Request

```json
POST /apply/execute
{
  "company": "Google",
  "role": "Software Engineer",
  "status": "Applied",
  "job_url": "https://careers.google.com",
  "cover_letter": "Generated using AI"
}
##  Learning Outcomes

This project demonstrates:

* Clean backend architecture
* API-driven frontend-backend communication
* ORM-based database handling
* Debugging real-world integration issues
* Git & GitHub best practices

---

## Future Enhancements

*  User authentication
*  Resume-to-job AI scoring
*  LinkedIn / job portal scraping
*  Auto-apply bot integration
*  Analytics dashboard
