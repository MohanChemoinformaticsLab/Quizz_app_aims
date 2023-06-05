# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:53:23 2023

@author: RATUL BHOWMIK
"""

import streamlit as st
import base64


# Create title and subtitle
html_temp = """
		<div style="background-color:teal">
		<h1 style="font-family:arial;color:white;text-align:center;">Quizz App</h1>
		</div>
		<br>
		"""
st.markdown(html_temp, unsafe_allow_html=True)


# Define sidebar image paths
sidebar_image1 = "image1.jpg"  # Replace with the path to your first image file
sidebar_image2 = "image2.jpg"  # Replace with the path to your second image file

# Display first sidebar image
st.sidebar.image(sidebar_image1, use_column_width=True, width="100%")

# Display second sidebar image
st.sidebar.image(sidebar_image2, use_column_width=True, width="100%")



questions = (
    "Name the most common type of cancer that kills men in the world",
    "Name the cancer that occurs in the bone marrow and creates blood cells",
    "Name the cancer of connective tissues or cancer that occurs in the connective tissues in the body?",
    "Name the most common cancer in the world, due to which women die?",
    "You can get breast cancer even if it doesn't run in your family",
    "Men can get breast cancer",
    "Surgery and needle biopsies can cause breast cancer to spread",
    "Cancer is",
    "The following are Carcinogens i.e. cancer causing substances",
    "Which of the following is true?",
    "Cancer incidence may increase with use of _____",
    "Cancer can be treated by the following procedure?",
    "Which of the following is high risk group/ hereditary?",
    "Which of these particles are not used as a treatment for cancer?",
    "What common sleep aid, has been shown in a few studies to potentially increase survival time in lungs and other cancer patients when used in combination with chemotherapy?",
    "Which of these cancers causes more deaths worldwide than lung cancer?",
    "Which of the following biological pathways could be affected by aberrant miRNA expression?",
    "Presence of trace elements such as zinc in the bloodstream could contribute to growth of cancer cells",
    "Lung adenocarcinoma is the most diagnosed subtype of non-small cell lung cancer / NSCLC",
    "The following are carcinogens/ cancer causing substances",
    "Which of the following is true?",
    "Cancer incidence may increase with use of",
    "Which of these particles are not used as a treatment for cancer?",
    "Which of these cancers causes more deaths worldwide than lung cancer?",
    "Which of the following biological pathways could be affected by aberrant miRNA expression?",
    "Lung adenocarcinoma is the most diagnosed subtype of non-small cell lung cancer / NSCLC"
)

options = (
    ("A. Lung Cancer", "B. Prostate Cancer", "C. Liver Cancer", "D. Colon and Rectum Cancer"),
    ("A. Sacroma", "B. Myeloma", "C. Lymphoma", "D. Leukamia"),
    ("A. Lymphoma", "B. Sarcoma", "C. Carcinoid", "D. Medulloblastoma"),
    ("A. Breast Cancer", "B. Ovarian Cancer", "C. Rectal Cancer", "D. Vaginal Cancer"),
    ("A. Yes", "B. No", "C. Both A and B", "D. None"),
    ("A. True", "B. False", "C. Both A and B", "D. None"),
    ("A. True", "B. False", "C. Both A and B", "D. None"),
    ("A. Contagious disease", "B. Sometimes hereditary", "C. Infectious disease", "D. The curse of Nature for sin"),
    ("A. Tobacco", "B. Asbestos", "C. Benzene, Coal Tar, and Aniline Dyes", "D. All of the above"),
    ("A. All of the tumors turn into cancer", "B. Most cancers are tumors", "C. None", "D. Cancers are always malignant"),
    ("A. Colored polythene", "B. Artificially colored food items", "C. Excessive use of fast foods and preserved foods", "D. All of the above"),
    ("A. Surgery", "B. Chemotherapy", "C. Radiotherapy", "D. None of the above"),
    ("A. Breast Cancer", "B. Bone Cancer", "C. Blood Cancer", "D. None of the above"),
    ("A. Protons", "B. Neutrons", "C. Carbon ions", "D. Electrons"),
    ("A. Chamomile tea", "B. Melatonin", "C. ASMR", "D. Decaf Tea"),
    ("A. Breast Cancer", "B. Liver Cancer", "C. Colorectal Cancer", "D. Lung Cancer"),
    ("A. Proliferation", "B. Migration", "C. Apoptosis", "D. All of the above"),
    ("A. True", "B. False", "C. Invalid question", "D. None"),
    ("A. True", "B. False", "C. Invalid question", "D. None"),
    ("A. Tobacco", "B. Asbestos", "C. Benzene, coal tar, and aniline dyes", "D. All of the above"),
    ("A. All of the tumors turn into cancer", "B. Most cancers are tumors", "C. None of the above", "D. Cancer is always malignant"),
    ("A. Colored polythene", "B. Artificially colored food items", "C. Excessive use of fast foods and preserved foods", "D. All of the above"),
    ("A. Protons", "B. Neutrons", "C. Carbon ions", "D. Electrons"),
    ("A. Breast Cancer", "B. Liver Cancer", "C. Colorectal Cancer", "D. Lung Cancer"),
    ("A. Proliferation", "B. Migration", "C. Apoptosis", "D. All of the above"),
    ("A. True", "B. False", "C. Invalid question", "D. None of the above")
)

answers = ("A", "D", "B", "A", "A", "A", "B", "B", "D", "C", "D", "D", "A", "D", "B", "D", "A", "A", "A", "D", "C", "D", "D", "D", "A", "A")

def calculate_marks(user_answers):
    marks = 0
    for i, ans in enumerate(user_answers):
        if ans == answers[i]:
            marks += 1
    return marks

def display_quiz():
    user_answers = []

    for i, question in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        st.write(question)

        options_data = options[i]

        for option in options_data:
            st.write(option)

        selected_option = st.radio("Select your answer:", options_data, key=i)
        user_answers.append(selected_option[0])

    if st.button("Submit"):
        marks_obtained = calculate_marks(user_answers)
        st.write(f"You scored {marks_obtained} out of {len(questions)}.")

if __name__ == "__main__":
    display_quiz()
