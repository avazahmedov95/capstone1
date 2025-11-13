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

![Showing logs](https://github.com/user-attachments/assets/b60a1356-b524-4ece-9962-9168c11b3307)

![Connecting to Github](https://github.com/user-attachments/assets/0f06f2f5-b2db-4608-9399-ff305a71155c)

![Chat with DB 2](https://github.com/user-attachments/assets/2b4c117d-1ad9-4dcf-b97b-9792f320a287)

![Chat with DB](https://github.com/user-attachments/assets/580946ed-4f1e-410e-85b5-f60f1d702d44)

![Starting](https://github.com/user-attachments/assets/48364eb4-be18-4b97-89a4-7e7a848e37b1)

![Protection against unsafe operations](https://github.com/user-attachments/assets/bcd93611-4824-40db-9c91-d5f77750d9b0)


## 🧰 Tech Stack  
- 🐍 **Python 3.11+**  
- 🧠 **Semantic Kernel (1.37.1)**  
- 🌐 **Streamlit**  
- 🗄️ **SQLite / Local DB**  
- 🤖 **OpenAI API**  
- 💻 **GitHub REST API**  









