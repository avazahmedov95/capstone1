# 🤖 Capstone1 — Intelligent Assistant with Streamlit & Semantic Kernel  
This project is a **Streamlit-based intelligent assistant** powered by **OpenAI** and **Microsoft Semantic Kernel**. It integrates with **GitHub**, a local **database**, and supports extensions through modular plugins.  

## 🧠 Project Overview  
The assistant can:  
- 💬 communicate interactively via a Streamlit web interface,  
- 🧠 use OpenAI models for reasoning and text generation,  
- 🗃️ interact with a local SQL database,  
- 🔧 perform GitHub operations (issue creation, commit automation, etc.),  
- 🧩 support modular plugins for custom logic and tasks.  

## 🗄️ Database  
The database used in this project is based on a public dataset:  
👉 [Bike Store Sample Database — Kaggle](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database?utm_source=chatgpt.com&select=orders.csv)  

Please note that the database file (`db/sales`) is stored using **Git LFS** due to its size.  
To pull it locally, run the following commands in your terminal:  
```bash
git lfs install
git lfs pull
```

## 🔐 Environment Variables  
Before running the project, make sure to create a `.env` file in the root folder and add your own API keys and tokens:  
```bash
OPENAI_API_KEY=your_openai_key_here
GITHUB_TOKEN=your_github_token_here
GITHUB_API=github_url_here
GITHUB_REPO=github_repo_here
```  
Alternatively, you can set your keys as system environment variables directly on your computer.  

## 🚀 How to Run the App  
1️⃣ Clone the repository:  
```bash
git clone https://github.com/avazahmedov95/capstone1.git
cd capstone1
```  
2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```  
3️⃣ Pull database files via Git LFS:  
```bash
git lfs install
git lfs pull
```  
4️⃣ Run the Streamlit app:  
```bash
streamlit run app.py
```  
Then open your browser at 👉 [http://localhost:8501](http://localhost:8501)  

## 📸 Assistant in Action  
Below are screenshots showing how the assistant interacts with the user and performs tasks:

![Starting](https://github.com/user-attachments/assets/e5b84a3c-0c5c-479f-bbbd-ed4dfb0f5556?x=1)
```
![Chat with DB](https://github.com/user-attachments/assets/fac73d0b-95b9-471b-bbc8-5efcf0d35bbc?x=2)
```
![Chat with DB2](https://github.com/user-attachments/assets/f01f5f56-037b-4647-9200-0fcacdc409d9?x=3)
```
![Connecting to Github](https://github.com/user-attachments/assets/85703bf3-a12e-4b15-8e8b-d359915ffc07?x=4)
```
![Showing logs](https://github.com/user-attachments/assets/2ed62b36-d743-43e0-b34b-8f6dcb55b326?x=5)
```
![Protection against unsafe operations](https://github.com/user-attachments/assets/a93546f0-b928-45aa-97a2-cce62fe05a61?x=6)
```

## 🧰 Tech Stack  
- 🐍 **Python 3.11+**  
- 🧠 **Semantic Kernel (1.37.1)**  
- 🌐 **Streamlit**  
- 🗄️ **SQLite / Local DB**  
- 🤖 **OpenAI API**  
- 💻 **GitHub REST API**  









