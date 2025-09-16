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
Specify a directory for DATA_SERVER_STORAGE_BLOCK. All local state data of the app, including messages, logs, and events, will be stored here. The default location is /tmp; modify it according to your preference.

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

##


## 🐞 Debugging / Logs

All application logs are stored in the `logs` folder inside the path specified by the environment variable `DATA_SERVER_STORAGE_BLOCK`. Logs are rotated daily at midnight.

- **Current log file (today):**
    

```bash
tail -f ${DATA_SERVER_STORAGE_BLOCK}/logs/api.log
```

- **Previous logs (example format):**
    

```
2025-09-15 16:02:08,385 [INFO] textboard: Message has been fetched
2025-09-15 16:02:22,186 [INFO] textboard: Message content has been sent by tes successfully
2025-09-15 16:02:22,192 [INFO] textboard: Message has been fetched
2025-09-15 16:11:50,664 [ERROR] textboard: Validation error on /message/send: [{'type': 'missing', 'loc': ('body', 'name'), 'msg': 'Field required', 'input': {'nae': 'Danica', 'content': 'hello'}}] | Body: {'nae': 'Danica', 'content': 'hello'}
```

You can view older logs using:

```bash
cat ${DATA_SERVER_STORAGE_BLOCK}/logs/<date_formatted_file>
```

Replace `<date_formatted_file>` with the filename of the previous log you want to check. For example, yesterday's log could be named `api.log.2025-09-14`. The the file will also log malformed request

## 🧪 Automated Testing / Pytest

Automated testing has been deployed using **pytest**. The tests are located in `test_main.py` inside the `api` directory. Follow these steps to run the tests:

1. **Recommended environment**
    
    - Linux or macOS. If using Windows, use WSL.
        
    - Docker and Docker Compose must be installed.
        
2. **Give execute permission to the test script**
    

```bash
sudo chmod +x test.sh
```

3. **Run the test script**
    

```bash
sudo ./test.sh
```

> **What the script does:**
> 
> - Builds a Docker image and container named `api-test`.
>     
> - Runs automated tests from `api/test_main.py` for sending and receiving messages and images.
>     
> - Prunes/deletes the container after tests pass or fail.
>     

This allows users to quickly verify that the application is functioning as expected without manually setting up test containers.


## 📊 Monitoring

You can view real-time performance monitoring of the host server by opening your browser and navigating to:

```
http://localhost/performance
```

This page provides live metrics on system and application performance.