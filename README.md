# Voice-Controlled Personal Assistant (Offline + Text Mode)

A robust Python-based personal assistant catered toward software developers that responds to both **voice commands** and **typed input**, supports hotword detection, developer tools, system automation, and can even control your VPN, send emails, and perform unit conversions.

---

## 🔧 Features

### 🎤 Input Modes
- **Voice Mode**: Say “Hey Assistant” to activate hotword detection and issue commands by voice
- **Text Mode**: Type commands into the terminal (fallback for devices without a microphone)

### 🗣️ Output
- Spoken responses using **gTTS** (Google Text-to-Speech) and `playsound`

### 💻 Developer Tools (100+ commands!)
- Open VS Code, Git Bash, Terminal, Command Prompt, etc.
- Run Git commands: `git status`, `git pull`, `git push`
- Create/activate Python virtual environments
- Launch Flask, Django, and Jupyter servers
- Install dependencies with `pip`

### 🌐 Web & System Utilities
- Open Google, search queries, or Wikipedia
- Check date and time
- Hear random jokes
- Launch Slack, Postman, and other developer tools
- Run terminal operations: `ipconfig`, `ping`, `dir`, etc.

### 📬 Email
- Send test email via Gmail SMTP

### 🔐 VPN Control
- Connect to **TunnelBear VPN** in selected countries (Germany, Canada, USA)

### 📁 File Management
- Copy, delete files and directories with voice/text commands

### 🔄 Unit Conversions
- Kilometers to miles, Celsius to Fahrenheit, etc.

---

## 🚀 Setup

### 1. Clone the Repo & Create a Virtual Environment

```bash
git clone [your-repo-url]
cd Voice-Assistant
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install gTTS playsound==1.2.2
```

### 3. Configure Email (Optional)
Update `commands.py` with your email and app password:
```python
msg["From"] = "youremail@example.com"
server.login("youremail@example.com", "your-app-password")
```

### 4. Ensure TunnelBear CLI is Installed (for VPN use)
- Must be installed and authenticated in advance

---

## 🧪 Run the Assistant

### Voice Mode (with hotword detection)
```bash
python main.py
```

### Text Mode (for systems without a mic)
Modify `main.py`:
```python
command = input(">>> ").lower().strip()
execute_command(command)
```

---

## 🔒 Privacy Notice
- Voice commands are only transcribed locally using `speechrecognition`
- TTS is handled through `gTTS` (requires internet for audio generation)

---

## 🛠️ Credits
- Built with `pyttsx3`, `gTTS`, `playsound`, `speechrecognition`, and Python 3
- Inspired by developer workflows, automation needs, and system admin tasks

---
