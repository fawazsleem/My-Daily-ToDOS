# My-Daily-ToDoS
A simple and user-friendly To-Do List application built with Python, Flet, and SQLite. My Daily ToDoS 
helps users organize their daily tasks, set completion times, and keep track of their progress.


✨ Features

	➕ Add tasks
	✅ Mark task as complete
	📋 Display tasks in an organized interface
	🔁 Save tasks
	🗑️ Delete tasks
	🎨 Simple and clean user interface
	💻 Designed with cross-platform support in mind


🛠️ Technologies Used
	
	Python — Main programming language
	Flet — User interface framework
	SQLite3 — Local database for storing tasks
	Datetime — Date and time handling



📁 Project Structure

	todolist/
	├── venv/          
	├── main.py      
	├── database.py
	├── todo.db        
	└── README.md  


1. Install Python
   
Install Python from the official website
	
	https://www.python.org/downloads/M

2.Clone or Download the Project

Download the project files and open the project folder in your terminal.

3.Create a Virtual Environment

	   python -m venv venv

4.Activate the Virtual Environment

Run in command prompt:
	
	.\venv\Scripts\Activate.ps1

5.Install Dependencies

Install the packages listed in your requirements.txt or install the required packages individually

6.Run the Application

	python main.py   

🗄️ Database

	The application uses SQLite to store task information locally.

	Each task can contain information such as:
		Task ID
		Task name
		Task entry time
		Task completion time
		Completion status
	
	SQLite is included with standard Python installations, so a separate SQLite server is not required

📱 Platform Support

	Windows: Desktop application development
	Android: Mobile support is a development goal
	iOS: Future possibility, depending on packaging and platform compatibility

👨‍💻 Author

Created as a personal Python project to learn application development, databases, UI design, and notifications.

📄 License

This project is currently intended for personal learning and development.

