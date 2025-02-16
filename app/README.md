# **📖 README: Streamlit Chatbot with Image Support 🖼️**
This repository contains a **Streamlit-based chatbot** that supports **text and image-based queries** using AWS Bedrock. You can run the app locally or inside a **Docker container**.

---

## **🚀 Getting Started (Windows)**
### **1️⃣ Clone the Repository**
```powershell
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Create a Virtual Environment**
```powershell
python -m venv venv
venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```powershell
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App Locally**
```powershell
streamlit run app.py
```
The app will be available at: **http://localhost:8501**

### **🐳 Running with Docker (Windows)**
#### **1️⃣ Build the Docker Image**
```powershell
docker build -t streamlit-chatbot .
```

#### **2️⃣ Run the Docker Container**
```powershell
docker run -p 8501:8501 streamlit-chatbot
```
The app will be available at: **http://localhost:8501**

---

## **🍏 Getting Started (Mac)**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App Locally**
```bash
streamlit run app.py
```
The app will be available at: **http://localhost:8501**

### **🐳 Running with Docker (Mac)**
#### **1️⃣ Build the Docker Image**
```bash
docker build -t streamlit-chatbot .
```

#### **2️⃣ Run the Docker Container**
```bash
docker run -p 8501:8501 streamlit-chatbot
```
The app will be available at: **http://localhost:8501**

---

## **📌 Notes**
✅ Make sure **Docker Desktop** is installed and running before using Docker.  
✅ If running locally, ensure **Python 3.9+** is installed.  
✅ Replace `"your-repo-name"` with the actual repository name.  

---

Now you're ready to **build & run** your Streamlit chatbot! 🚀 Let me know if you need any updates! 🎉