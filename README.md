# Medical Appointment No-Shows Analysis

## Overview
This project investigates why patients miss their medical appointments using the **Medical Appointment No-Shows** dataset from Kaggle. The analysis aims to identify key factors that influence patient attendance, such as waiting times, SMS reminders, and demographic attributes.


---

## Workflow

### Phase 1: Data Cleaning
1. Load the dataset into a Pandas DataFrame.
2. Explore the data:
   - Check for null values
   - Identify duplicates
   - Verify column data types
3. Clean the data:
   - Correct data types (e.g., dates)
   - Remove duplicates
   - Handle missing values
4. Compare cleaned vs. original data to ensure improvements.

### Phase 2: Data Analysis
Key questions investigated:
1. **Does waiting time influence attendance?**  
   - Visualized with boxplots comparing `ScheduledDay` and `AppointmentDay` for `Show` vs `No-Show`.
2. **Do SMS reminders affect attendance?**  
   - Count plots comparing `No-Show` proportions for patients who received reminders vs those who did not.
3. **Does age influence attendance?**  
   - Histogram/KDE plots showing age distribution of attendees vs non-attendees.

Each visualization is accompanied by a concise conclusion describing the insights.

---
## Dashboard Preview

### Overview
![Dashboard](images/dashboard_overview.png)

---

## Key Insights
- Shorter waiting periods increase attendance.
- Gender alone doesn’t strongly affect attendance, but females are more numerous.
- Very young children attend more, older age groups attend less.
- Having chronic conditions (hypertension, diabetes, alcoholism, handicap) has minimal effect on attendance.
- Slightly higher non-attendance among patients with scholarships
- Surprisingly, patients who received SMS reminders have higher non-attendance (27%).

---
## Recommendations to Improve Patient Attendance

### 1️ Reduce Waiting Times

* Minimize the gap between appointment booking and the actual visit.
* Shorter waiting periods significantly increase patient attendance.

### 2️ Improve Reminder Systems

* Send timely reminders via SMS, email, or phone calls before appointments.
* Evaluate the most effective communication channels for different patient groups.

### 3️ Focus on Age-Specific Strategies

* Children generally attend with their families, while adolescents and older adults show lower attendance.
* Consider educational outreach for parents of adolescents and additional support for older patients.

### 4️ Support Vulnerable Groups

* Provide assistance such as transportation guidance or scheduling flexibility for patients with chronic conditions or mobility challenges.

### 5️ Monitor and Adjust Scheduling

* Regularly review attendance trends using dashboards.
* Adjust appointment schedules, reminder timing, and patient communication based on observed patterns.

### 6️ Simplify Appointment Access

* Make appointment booking easy through online platforms or phone systems.
* Reduce complexity to prevent missed appointments due to confusion or forgetfulness.

### 7️ Educate Patients

* Share clear messages about the importance of attending appointments and potential health consequences of missing them.



---
## Technologies
- Python 3.x
- Pandas & NumPy for data manipulation
- Matplotlib & Seaborn for visualization
- Jupyter Notebook for interactive analysis

---

## Author

Ahmed Sherif  
Data Analysis Student – Faculty of Engineering
