# 📊 CodeAlpha – Data Visualization (Task 3)

## 📌 Overview 
It focuses on **analyzing and visualizing screen time usage patterns** among children and teenagers using a dataset that includes demographic, device usage, and health-related details.

By leveraging **Python**, **Pandas**, **Matplotlib**, and **Seaborn**, the project produces insightful charts that make it easier to identify:
- How average screen time varies by age, gender, and location.
- Which devices are most commonly used.
- Whether exceeding recommended screen time is associated with specific health issues.
- The balance between educational and recreational screen time.
The goal is to **present raw data in an engaging and interpretable format** to support better understanding and informed decision-making.

---
## 📂 Dataset Structure
The dataset `screentime.xlsx` contains the following columns:
| Column Name                           | Description |
|---------------------------------------|-------------|
| **Age**                               | Age of the participant (in years). |
| **Gender**                            | Gender of the participant (Male/Female). |
| **Avg_Daily_Screen_Time_hr**          | Average daily screen time in hours. |
| **Primary_Device**                    | Main device used for screen time (e.g., Smartphone, Laptop, TV). |
| **Exceeded_Recommended_Limit**        | Boolean value indicating if the participant exceeded the daily recommended screen time. |
| **Educational_to_Recreational_Ratio** | Ratio of educational screen time to recreational screen time. |
| **Health_Impacts**                    | Reported health issues (e.g., Poor Sleep, Eye Strain). |
| **Urban_or_Rural**                    | Location category where the participant lives (Urban/Rural). |

---
## 📈 Visualizations
The script generates **six key visualizations**:

1. **Bar Chart – Average Screen Time by Age**  
   Displays how average daily screen time changes with age.

2. **Pie Chart – Primary Device Distribution**  
   Shows the percentage distribution of primary devices used.

3. **Box Plot – Screen Time by Gender**  
   Compares screen time distribution between male and female participants.

4. **Bar Chart – Screen Time by Urban vs Rural Kids**  
   Highlights differences in screen time between urban and rural participants.

5. **Stacked Bar Chart – Health Impacts vs Exceeded Screen Time Limit**  
   Illustrates how different health issues are related to exceeding recommended limits.

6. **Count Plot – Educational-to-Recreational Ratio Categories**  
   Groups participants into categories (Low, Medium, High) based on their educational vs recreational usage ratio.

---
## 🛠️ Technologies Used
- **Python** – Core programming language
- **Pandas** – Data loading and manipulation
- **Matplotlib** – Static plotting library
- **Seaborn** – Advanced statistical visualization
- **OpenPyXL** – For reading Excel files

---

## 🚀 How to Run the Project
1. **Clone the repository**  
    - git clone https://github.com/yourusername/codealpha-data-visualization-task3.git
   cd codealpha-data-visualization-task3

2. Install required dependencies
     - pip install pandas matplotlib seaborn openpyxl
       
3. Run the visualization script
   - python visualization.py
     
4. View the results
    - All charts will be saved in the visuals folder and also displayed on screen.

📂 Project Structure
.
├── screentime.xlsx                  
├── visualization.py                
├── visuals/                         
└── README.md      

📊 Example Outputs
1. Average Screen Time by Age
2. Primary Device Distribution
3. Screen Time by Gender
4. Screen Time by Urban vs Rural Kids
5. Health Impacts vs Exceeded Screen Time Limit
6. Educational-to-Recreational Ratio Categories


