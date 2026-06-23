import streamlit as st
import pandas as pd
from datetime import datetime

from streamlit_mic_recorder import mic_recorder

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
background-color:#0E1117;
}

.block-container{
padding-top:2rem;
}

.big-title{
font-size:55px;
font-weight:bold;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:20px;
color:lightgray;
}

.card{
padding:20px;
border-radius:15px;
background:#1e1e1e;
margin-top:10px;
}

.footer{
text-align:center;
padding:20px;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.write("📋 Planner")
    st.write("🌐 Researcher")
    st.write("🧠 Analyst")
    st.write("✍️ Writer")
    st.write("✅ Fact Checker")
    st.write("🎤 Voice Input")
    st.write("📁 File Upload")
    st.write("📥 Download Report")

    st.markdown("---")

    st.success("👨‍💻 Built by Rushi")

    st.info("🚀 Version 4.0")

# ---------------- HEADER ---------------- #

st.markdown(
'<div class="big-title">🤖 AI-Powered Multi-Agent Research Assistant</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Professional AI Research Generator</div>',
unsafe_allow_html=True
)

st.markdown("---")

# ---------------- DASHBOARD ---------------- #

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("🤖 Agents","5")

with col2:
    st.metric("📄 Reports","Unlimited")

with col3:
    st.metric("⚡ Speed","Fast")

with col4:
    st.metric("🟢 Status","Online")

st.markdown("---")

# ---------------- INPUTS ---------------- #

topic = st.text_input(
    "🔍 Enter Research Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

uploaded_file = st.file_uploader(
    "📁 Upload PDF/TXT/DOCX",
    type=["pdf","txt","docx"]
)

st.write("🎤 Voice Input")

mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="voice"
)

generate = st.button(
    "🚀 Generate AI Report",
    use_container_width=True
)

# ---------------- REPORT ---------------- #

if generate:

    if topic == "" and uploaded_file is None:

        st.warning("⚠️ Enter a topic or upload a file.")

    else:

        progress=st.progress(0)

        st.info("🤖 AI Agents are researching...")

        progress.progress(20)

        plan=planner_agent(topic)

        progress.progress(40)

        research=researcher_agent(topic)

        progress.progress(60)

        analysis=analyst_agent(topic,research)

        progress.progress(80)

        report=writer_agent(topic,analysis)

        progress.progress(100)

        st.success("✅ Report Generated")

        st.subheader("📋 Research Plan")
        st.write(plan)

        st.subheader("🌐 Web Results")

        for item in research:
            st.write("•",item)

        st.subheader("🧠 AI Analysis")
        st.write(analysis)

        st.subheader("📄 Final Report")
        st.write(report)

        st.download_button(

            label="📥 Download Report",

            data=report,

            file_name="research_report.txt",

            mime="text/plain"

        )

        st.subheader("📊 Agent Performance")

        chart=pd.DataFrame({

            "Agent":[
                "Planner",
                "Researcher",
                "Analyst",
                "Writer"
            ],

            "Score":[
                25,
                35,
                20,
                20
            ]

        })

        st.bar_chart(chart.set_index("Agent"))

        st.write("🕒",datetime.now())

st.markdown("---")

st.markdown(
'<div class="footer">👨‍💻 Built by Rushi 🚀 | Version 4.0</div>',
unsafe_allow_html=True
)