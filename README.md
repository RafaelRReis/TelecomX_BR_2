# 📊 TelecomX BR – Análise de Churn / Churn Analysis & Interactive Dashboard

---
## 🇧🇷 Versão em Português

Este projeto tem como objetivo **analisar e monitorar a retenção de clientes** de uma empresa fictícia de telecomunicações, identificando padrões relacionados ao **Churn** (cancelamento de clientes) e gerando **insights acionáveis** para melhorar a retenção.  

Além da análise exploratória e modelagem realizadas em Python, o projeto inclui um **Dashboard Interativo** desenvolvido com **Dash + Plotly** para visualização dinâmica dos dados.  

### 🚀 Acesse o Dashboard
🔗 [**Clique aqui para abrir o Painel Interativo no Render**](https://telecomx-dashboard.onrender.com/)  
*(Certifique-se de que o servidor do Render esteja ativo, o carregamento inicial pode levar alguns segundos.)*

### 📂 Estrutura do Projeto
```
TelecomX_BR_2/
│
├── TelecomX_BR_2.ipynb                  # Notebook principal com EDA, modelagem e resultados
├── app.py                                # Código do dashboard (deploy no Render)
├── Dados_tratados_desafio_Telecom_X.csv  # Base de dados utilizada
├── requirements.txt                      # Bibliotecas necessárias
└── README.md                             # Documentação do projeto
```

### 📊 Principais Funcionalidades do Dashboard
- **Filtros Dinâmicos** por tipo de contrato e serviço de internet  
- **KPIs principais**: total de clientes, taxa de churn, taxa de retenção e tempo médio de permanência  
- **Visualizações interativas**:
  - Distribuição do churn
  - Perfil demográfico dos clientes
  - Análise dos serviços contratados
  - Insights financeiros (receita, métodos de pagamento, contratos)
  - Métricas avançadas como **CLV** (Customer Lifetime Value) e risco de churn
- **Tabela dinâmica** com clientes de maior valor e risco  
- 🔗 **Acesse diretamente o dashboard**: [https://telecomx-dashboard.onrender.com/](https://telecomx-dashboard.onrender.com/)

### 🛠 Tecnologias Utilizadas
- **Python** 3.x  
- **Pandas** – manipulação e limpeza de dados  
- **Plotly & Dash** – visualizações e dashboard interativo  
- **Dash Bootstrap Components** – estilização  
- **Jupyter Notebook** – análise exploratória e modelagem  
- **Render** – hospedagem do painel interativo  

### 📥 Como Executar Localmente
1️⃣ Clonar o repositório
```bash
git clone https://github.com/RafaelRReis/TelecomX_BR_2.git
cd TelecomX_BR_2
```

2️⃣ Criar ambiente virtual e instalar dependências
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

3️⃣ Executar o dashboard
```bash
python app.py
```
O dashboard ficará disponível em [http://localhost:8050](http://localhost:8050)

### 📑 Etapas da Análise (no Notebook)
1. Importação e inspeção inicial dos dados  
2. Tratamento de valores ausentes e ajustes de variáveis  
3. Análise exploratória (gráficos, correlações, distribuições)  
4. Engenharia de atributos  
5. Modelagem preditiva para estimar risco de churn  
6. Avaliação de métricas (matriz de confusão, classification report)  
7. Conclusões e recomendações  

### 📌 Observações
- A base de dados utilizada está disponível no próprio repositório (`Dados_tratados_desafio_Telecom_X.csv`).  
- O código do dashboard (`app.py`) foi adaptado para deploy no **Render**.  
- O notebook contém análises completas e geração de insights.  


---
## 🇺🇸 English Version

This project aims to **analyze and monitor customer retention** for a fictional telecommunications company, identifying patterns related to **Churn** (customer cancellations) and generating **actionable insights** to improve retention.  

In addition to exploratory data analysis and modeling in Python, the project includes an **Interactive Dashboard** built with **Dash + Plotly** for dynamic data visualization.  

### 🚀 Access the Dashboard
🔗 [**Click here to open the Interactive Dashboard on Render**](https://telecomx-dashboard.onrender.com/)  
*(Make sure the Render server is active. The initial load may take a few seconds.)*

### 📂 Project Structure
```
TelecomX_BR_2/
│
├── TelecomX_BR_2.ipynb                  # Main notebook with EDA, modeling, and results
├── app.py                                # Dashboard code (Render deployment)
├── Dados_tratados_desafio_Telecom_X.csv  # Dataset used in the project
├── requirements.txt                      # Required dependencies
└── README.md                             # Project documentation
```

### 📊 Key Dashboard Features
- **Dynamic Filters** for contract type and internet service  
- **Main KPIs**: total customers, churn rate, retention rate, and average tenure  
- **Interactive visualizations**:
  - Churn distribution
  - Customer demographic profile
  - Service usage analysis
  - Financial insights (revenue, payment methods, contracts)
  - Advanced metrics such as **CLV** (Customer Lifetime Value) and churn risk
- **Dynamic table** with high-value and at-risk customers  
- 🔗 **Direct access to the live dashboard**: [https://telecomx-dashboard.onrender.com/](https://telecomx-dashboard.onrender.com/)

### 🛠 Technologies Used
- **Python** 3.x  
- **Pandas** – data manipulation and cleaning  
- **Plotly & Dash** – visualizations and interactive dashboard  
- **Dash Bootstrap Components** – styling  
- **Jupyter Notebook** – exploratory analysis and modeling  
- **Render** – dashboard hosting  

### 📥 How to Run Locally
1️⃣ Clone the repository
```bash
git clone https://github.com/RafaelRReis/TelecomX_BR_2.git
cd TelecomX_BR_2
```

2️⃣ Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

3️⃣ Run the dashboard
```bash
python app.py
```
The dashboard will be available at [http://localhost:8050](http://localhost:8050)

### 📑 Analysis Steps (in the Notebook)
1. Data import and initial inspection  
2. Missing values handling and variable adjustments  
3. Exploratory Data Analysis (EDA) – charts, correlations, distributions  
4. Feature engineering  
5. Predictive modeling to estimate churn risk  
6. Performance evaluation – confusion matrix, classification report  
7. Conclusions and recommendations  

### 📌 Notes
- The dataset is available in the repository (`Dados_tratados_desafio_Telecom_X.csv`).  
- The dashboard code (`app.py`) is adapted for **Render** deployment.  
- The notebook contains the complete analysis and insights.  

