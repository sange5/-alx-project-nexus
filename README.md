📌 Online Poll System Backend.
A Scalable and Real-Time Polling API
🚀 Efficiently create, manage, and analyze online polls with real-time voting and result computation.

🌍 Real-World Application
This project simulates a backend system for online polling platforms that require real-time data processing. It offers developers hands-on experience with:
✅ Building scalable APIs for voting systems.
✅ Optimizing database schemas for high-performance queries
✅ Documenting APIs for public access using Swagger.

🔍 Overview
This project provides RESTful APIs for:

Poll creation with multiple options.
User voting while preventing duplicate submissions.
Real-time result computation for each poll option.
Detailed API documentation using Swagger.
It follows best practices in Django REST Framework (DRF) and PostgreSQL for scalability and performance.

🎯 Project Goals
Objective	Description
📡 API Development	Build endpoints for poll creation, voting, and fetching results.
💾 Database Efficiency	Optimize schemas for real-time vote counting.
📝 Documentation	Provide Swagger API documentation for easy integration.
🛠️ Technologies Used
Technology	Purpose
Django	Backend framework for rapid API development.
Django REST Framework (DRF)	API development and serialization.
PostgreSQL	Relational database optimized for polling data.
Swagger (drf-yasg)	API documentation.
🚀 Key Features
1️⃣ Poll Management
✅ Create polls with multiple options.
✅ Store creation date and expiry date for each poll.

2️⃣ Voting System
✅ Users can cast votes securely.
✅ Validations prevent multiple votes on the same poll.

3️⃣ Result Computation
✅ Real-time vote counting per option.
✅ Optimized database queries for fast results retrieval.

4️⃣ API Documentation
✅ Swagger UI for API documentation.
✅ Accessible at /api/docs/ after deployment.

⚙️ Implementation Process
📌 Git Commit Workflow
Commit Type	Example
Initial Setup	feat: set up Django project with PostgreSQL
Feature Development	feat: implement poll creation and voting APIs
Optimization	perf: optimize vote counting queries
Documentation	feat: integrate Swagger documentation
docs: update README with API usage
📊 Evaluation Criteria
✅ Functionality – Polls, options, and votes work correctly.
✅ Code Quality – Clean, modular, and follows Django best practices.
✅ Performance – Efficient vote counting & real-time results.
✅ Documentation – Clear API documentation via Swagger & README.
