# Installation and Usage Guide

## 1Question Configuration
 Edit question content in the `answers.json` file
## 2. Start the Server
``bash
ocker compose up -d
``
## 3. Expose Server to Internet

You can choose either Ngrok or JPRQ to expose your local server:

### Option 1: Using Ngrok
### Install Ngrok on Windows
. Visit [Ngrok download page](https://ngrok.com/download) and download
. Install Ngrok following the instructions
. Register an account at [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/setup/windows)
. Get authentication token from [setup page](https://dashboard.ngrok.com/get-started/setup/windows)
. Open terminal and run:
  ```bash
  ngrok authtoken <your-token>
  ```
### Expose Server
un the following command to expose the server:
``bash
grok tcp 1337
``
## 4. Connect to Server
### View Connection Information
fter running `ngrok tcp 1337`, you will see information like this:
[Ngrok connection information](image-1.png)
In this example:
 Server address: `0.tcp.ap.ngrok.io`
 Port: `13921`
 This server is forwarded to port `1337` on the local machine
### Connect
se the following command to connect to the server:
``bash
c 0.tcp.ap.ngrok.io 13921
``
Result when successfully connected:
[Successful connection](image.png)

### Option 2: Using JPRQ (Alternative)
JPRQ is a free and open-source alternative for exposing local servers to the internet.

#### Install JPRQ
```bash
curl -fsSL https://jprq.io/install.sh | sudo bash
```

#### Authentication
1. Get your authentication token from [JPRQ Auth Page](https://jprq.io/auth)
2. Authenticate using the token:
```bash
jprq auth <your-auth-token>
```

#### Expose Server
Run the following command to expose the TCP server:
```bash
jprq tcp 1337
```

The command will display a URL and port that you can use to connect to your server.