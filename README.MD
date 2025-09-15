# MULTI-SERVICE TEXTBOARD Platform

## Description
This app is packaged using docker that allows teams and multiple individual to collaborate using a chat-board. Simple, no authentication, just field for name and message content to start with. All messages were saved persistent and can be deployed almost anywhere.

## 🛠 Tech Stack

**Backend:**  
- Python  
- FastAPI  
- Flask  
- Bash  

**Database:**  
- SQLite3  

**Frontend / Web:**  
- HTML  

**Web Server & Deployment:**  
- Nginx  
- Docker

## 🚀 Installation

I used ubuntu LTS 22.04, if you need to install docker, please follow the official docs!

1. **Clone the repository**
```bash
git git@github.com:nrobbyjay/textboard-cortico.git
cd textboard-cortico
```
2. **Find and modify .env file**
```bash
DATA_SERVER_STORAGE_BLOCK=/tmp
```
Set a directory for DATA_SERVER_STORAGE_BLOCK. This is where all localstate data of the app will be saved (such as messages, logs, and events)

3. **Start the application**
```bash
sudo docker compose up
```

4. **Access the app**  
    Open your browser and go to:
    

```
http://localhost/
```
4. **Click plus sign to add new content on board and refresh manually to get new content**  