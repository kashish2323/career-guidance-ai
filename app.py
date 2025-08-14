import streamlit as st

# Page settings
st.set_page_config(page_title="AI Career Guidance - By Kashish Fatima", page_icon="💡", layout="wide")

# Title & Intro
st.title("💡 AI Career Guidance System")
st.markdown("""
Hi, I'm **Kashish Fatima**, a Computer Science B.Tech (4th year) student passionate about **Data Science & AI**.  
I created this tool to help people discover the right career path based on their skills. 🚀
""")

# Sidebar - About Me
st.sidebar.title("👩‍💻 About the Creator")
st.sidebar.markdown("""
**Name:** Kashish Fatima  
**Skills:** Python, Excel, Prompt Engineering, SQL, Data Visualization, Tableau  
**Career Goal:** Data Scientist  
""")
st.sidebar.info("💬 Connect with me for AI/ML projects!")

# Step 1: User enters their skills
skills = st.multiselect(
    "Select your current skills:",
    [
        # Programming
        "Python", "Java", "C++", "R", "JavaScript", "SQL", "NoSQL",
        # Data Analysis & Visualization
        "Excel", "Data Visualization", "Tableau", "Power BI", "Matplotlib", "Seaborn",
        # AI/ML
        "Machine Learning", "Deep Learning", "Natural Language Processing", "Prompt Engineering",
        "Computer Vision", "Reinforcement Learning", "LLM Development",
        # Data Engineering
        "ETL", "Big Data", "Apache Spark", "Data Warehousing",
        # Cloud & DevOps
        "Cloud Computing", "Microsoft Azure AI", "AWS", "Google Cloud", "Docker", "Kubernetes",
        # Business & Product
        "Business Analysis", "Agile Methodology", "Scrum", "Product Management"
    ]
)

# Step 2: Career database
career_data = {
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Deep Learning", "Data Visualization", "Tableau"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "LLM Development", "Cloud Computing", "Prompt Engineering"],
    "Data Analyst": ["Python", "Excel", "SQL", "Data Visualization", "Tableau", "Power BI"],
    "NLP Engineer": ["Python", "Natural Language Processing", "Machine Learning", "Deep Learning", "LLM Development"],
    "ML Ops Engineer": ["Python", "Machine Learning", "Cloud Computing", "Docker", "Kubernetes", "Big Data"],
    "Business Intelligence Analyst": ["SQL", "Data Visualization", "Power BI", "Tableau", "Excel", "Business Analysis"],
    "Cloud AI Specialist": ["Python", "Cloud Computing", "Microsoft Azure AI", "AWS", "Google Cloud", "Machine Learning"],
    "Computer Vision Engineer": ["Python", "Computer Vision", "Machine Learning", "Deep Learning"],
    "Data Engineer": ["Python", "SQL", "ETL", "Apache Spark", "Big Data", "Data Warehousing", "Cloud Computing"],
    "AI Product Manager": ["Product Management", "Business Analysis", "Agile Methodology", "Prompt Engineering", "Cloud Computing", "Machine Learning"]
}

# Step 3: Recommend roles
if st.button("🔍 Recommend Roles"):
    if not skills:
        st.warning("Please select at least one skill.")
    else:
        recommendations = []
        for role, req_skills in career_data.items():
            matched = len(set(skills) & set(req_skills))
            total = len(req_skills)
            match_percent = (matched / total) * 100
            if match_percent > 0:
                recommendations.append((role, match_percent, list(set(req_skills) - set(skills))))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)

        if recommendations:
            for role, match, missing in recommendations:
                st.subheader(f"🎯 {role} - {match:.0f}% Match")
                if missing:
                    st.markdown(f"**Missing Skills:** {', '.join(missing)}")
                else:
                    st.markdown("✅ You have all the required skills!")
        else:
            st.error("No matching roles found. Try adding more skills.")

# Footer
st.markdown("---")
st.markdown("🖋 **Developed by Kashish Fatima** | Passionate about Data Science & AI")
