#  Smart Medical Diagnosis System

##  Project Overview

Smart Medical Diagnosis System is an AI-based Python application that predicts diseases based on symptoms entered by the user. The system uses Artificial Intelligence concepts such as Bayesian Networks and Knowledge Representation to perform probability-based disease prediction and provide intelligent medical decision support.

The project is designed to analyze symptoms entered through a terminal-based interface and identify the most probable disease along with probability values. The main objective of this project is to demonstrate how Artificial Intelligence techniques can be applied in healthcare for preliminary disease diagnosis.

The system contains a medical knowledge base consisting of diseases and their related symptoms. When the user enters symptoms such as fever, cough, headache, fatigue, body pain, or breathing issues, the system processes the information and calculates the probability of possible diseases using Bayesian probability concepts.

The disease with the highest probability is displayed as the predicted disease, along with other possible diseases and their probability percentages. This helps in intelligent and structured diagnosis based on symptom analysis.

Knowledge Representation is used to organize diseases, symptoms, and probabilities in a structured format, allowing efficient reasoning and decision-making. Bayesian Networks help the system handle uncertain and overlapping symptoms logically and effectively.

The system allows users to enter either full symptom names or only the starting letters of symptoms for faster and easier diagnosis.

The project includes features such as symptom-based disease prediction, probability-based output, terminal-based interaction, and an expandable disease database where additional symptoms and diseases can be added easily. The system is lightweight, modular, and user-friendly.

This project demonstrates the practical implementation of Artificial Intelligence in healthcare applications. Although the system is developed for educational purposes and does not replace professional medical consultation, it effectively showcases intelligent disease prediction using symptom analysis.

---

#  Features

- Symptom-based disease prediction
- Probability-based diagnosis
- Bayesian Network implementation
- Knowledge Representation techniques
- Terminal-based interface
- Accepts full symptom names or starting letters
- Fast and intelligent prediction system
- Multiple disease probability results
- Expandable medical knowledge base
- User-friendly and modular design

---

#  Technologies Used

- Python
- Pandas
- NumPy
- pgmpy
- Bayesian Networks
- Artificial Intelligence
- Knowledge Representation

---

#  Project Structure

```bash
Smart-Medical-Diagnosis-System/
│── dataset.csv
│── main.py
│── model.py
│── inference.py
│── gui.py
│── README.md
│── requirements.txt
```

---

#  Installation

## 1️ Clone Repository

```bash
git clone https://github.com/your-username/Smart-Medical-Diagnosis-System.git
```

## 2️ Move to Project Directory

```bash
cd Smart-Medical-Diagnosis-System
```

## 3️ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

#  Run the Project

## Terminal Version

```bash
python main.py
```

## GUI Version

```bash
python gui.py
```

---

#  Example Input

```text
Enter Symptoms:
fev cou hea fat
```

OR

```text
Enter Symptoms:
fever cough headache fatigue
```

---

#  Example Output

```text
========== DIAGNOSIS RESULTS ==========

Predicted Disease : COVID19

Other Possible Diseases:
Flu            : 75.30%
Viral Fever    : 42.10%
Typhoid        : 30.50%
```

---

#  Diseases Included

- COVID-19
- Flu
- Dengue
- Malaria
- Typhoid
- Pneumonia
- Viral Fever
- Allergy
- Asthma
- Common Cold

---

#  Future Enhancements

- Web application integration
- Mobile application support
- Voice-based symptom input
- More disease datasets
- Advanced AI algorithms
- Real-time healthcare support

---

#  Author

Dipali Patil  
Second Year – Artificial Intelligence & Data Science  
Dr. D. Y. Patil College of Engineering, Akurdi

---

#  Disclaimer

This project is developed for educational purposes only. The system is not intended to replace professional medical advice or diagnosis.

---

#  Conclusion

The Smart Medical Diagnosis System demonstrates how Artificial Intelligence techniques such as Bayesian Networks and Knowledge Representation can be used for intelligent symptom-based disease prediction. The project provides fast, logical, and probability-based diagnosis, showcasing the practical application of AI in healthcare systems.
