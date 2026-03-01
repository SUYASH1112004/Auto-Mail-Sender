# 🖥️ Process Logger & Auto Mail Sender (Python)

## 📌 Project Overview
This Python automation script creates a log file containing all running processes on the system and automatically sends the log file via email at scheduled intervals.

It uses `psutil` to fetch system process details and `smtplib` to send emails with the log file attached.

---

## 🚀 Features

- ✅ Logs all running processes
- ✅ Captures:
  - Process ID (PID)
  - Process Name
  - Username
  - Virtual Memory Usage (VMS in MB)
- ✅ Automatically creates a log directory
- ✅ Checks internet connectivity before sending email
- ✅ Sends log file as email attachment
- ✅ Runs at scheduled time intervals (in minutes)

---

## 🛠️ Technologies Used

- Python 3
- psutil
- smtplib
- schedule
- email (MIME)
- urllib

---

## 📂 Project Structure


Process_Logger/
│
├── ProcessLogger.py
├── Process_File/
│ └── Logfile.log
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2️⃣ Install Required Libraries
pip install psutil schedule
▶️ How to Run
python ProcessLogger.py <time_in_minutes>
Example:
python ProcessLogger.py 5
```
This will:

Create a process log every 5 minutes

Send the log file via email automatically

---

# 📧 Email Configuration

Update the following inside the script:

fromaddr = "your_email@gmail.com"
toaddr = "receiver_email@gmail.com"
s.login(fromaddr, "your_app_password")

---

# 🧠 How It Works

Collects running processes using psutil

Writes process details into Logfile.log

Checks internet connectivity

Sends the log file via Gmail SMTP server

Repeats task at scheduled interval using schedule

---

# 📌 Command Line Options
Argument	Description
-h	Help
-u	Usage instructions
<number>	Time interval in minutes

---

# 🔒 Security Note

For security reasons:

Never hardcode your real email password.

Use environment variables or .env file for credentials.

Add Process_File/ to .gitignore.

---

# 📸 Sample Log Output
--------------------------------------------------------------------------------
Process Logger : Mon Mar 1 12:45:30 2026
--------------------------------------------------------------------------------
{'pid': 1234, 'name': 'chrome.exe', 'username': 'Suyash', 'vms': 245.32}
{'pid': 5678, 'name': 'python.exe', 'username': 'Suyash', 'vms': 120.50}

---

# 🎯 Learning Outcomes

This project helps in understanding:

System Monitoring using Python

Process Management

SMTP Email Automation

Task Scheduling

File Handling

Exception Handling

---
# 👨‍💻 Author

Suyash Patil
