
# Malaria On‑Job Training — Bilingual App
# All Rights Reserved © Dr. Mohammedelnagi Mohammed

import streamlit as st

APP_TITLE_EN = "Malaria On‑Job Training (OJT) — Bilingual"
APP_TITLE_AR = "التدريب أثناء الخدمة على الملاريا — ثنائي اللغة"
COPYRIGHT = "All Rights Reserved © Dr. Mohammedelnagi Mohammed"

st.set_page_config(page_title=APP_TITLE_EN, page_icon="🦟", layout="wide")
lang = st.sidebar.toggle("Arabic / العربية", value=False)
L = "ar" if lang else "en"

st.title(APP_TITLE_AR if L=="ar" else APP_TITLE_EN)
st.caption(COPYRIGHT)

nav = [
    "Overview" if L=="en" else "نظرة عامة",
    "Case management" if L=="en" else "تدبير الحالات",
    "Diagnostics" if L=="en" else "التشخيص",
    "Surveillance" if L=="en" else "المراقبة الوبائية",
    "Vector control" if L=="en" else "مكافحة النواقل",
    "Pregnancy & special groups" if L=="en" else "الحمل والفئات الخاصة",
    "Pharmacovigilance" if L=="en" else "التيقظ الدوائي",
    "Training & Quiz" if L=="en" else "التدريب والاختبار",
    "References" if L=="en" else "المراجع",
]
page = st.sidebar.radio("Navigation", nav, index=0)

if page == nav[7]:
    st.subheader("Training — Quiz" if L=="en" else "التدريب — اختبار")
    quiz_data = []
    for i in range(1,31):
        quiz_data.append({
            "id": f"q{i}",
            "en": {
                "stem": f"Question {i}: What is the correct action in malaria case management step {i}?",
                "options": ["Option A","Option B","Option C","Option D","Option E"],
                "answer": i%5,
                "explain": "Refer to Saudi National Malaria Guideline."
            },
            "ar": {
                "stem": f"السؤال {i}: ما هو الإجراء الصحيح في خطوة تدبير الملاريا رقم {i}?",
                "options": ["الخيار أ","الخيار ب","الخيار ج","الخيار د","الخيار هـ"],
                "answer": i%5,
                "explain": "ارجع إلى الدليل الوطني للملاريا."
            }
        })
    score = 0
    for item in quiz_data:
        i = item[L]
        st.markdown(f"**{i['stem']}**")
        choice = st.radio(" ", i["options"], index=None, key=item["id"]+L)
        if choice is not None:
            idx = i["options"].index(choice)
            if idx == i["answer"]:
                st.success("Correct ✅" if L=="en" else "إجابة صحيحة ✅")
                score += 1
            else:
                st.error("Incorrect ❌" if L=="en" else "إجابة غير صحيحة ❌")
            st.caption(i["explain"])
    st.info((f"Score: {score}/{len(quiz_data)}") if L=="en" else f"النتيجة: {score}/{len(quiz_data)}")
else:
    st.markdown("Content sections as before (overview, case management, surveillance, etc.)")

st.divider()
st.caption(COPYRIGHT)
