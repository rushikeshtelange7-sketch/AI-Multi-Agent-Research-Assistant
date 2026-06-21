from datetime import datetime
import streamlit as st

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent
from agents.fact_checker import fact_checker_agent
from utils.pdf_generator import create_pdf


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AI-Powered Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- SIDEBAR ----------------

st.sidebar.title("🤖 Project Info")

st.sidebar.write(
    "AI-Powered Multi-Agent Research Assistant"
)

st.sidebar.write("Built by Rushi")

st.sidebar.write("Version 1.0")


# ---------------- TITLE ----------------

st.title("🤖 AI-Powered Multi-Agent Research Assistant")

st.caption(
    "Planner • Researcher • Analyst • Writer • Fact Checker"
)


# ---------------- INPUT ----------------

topic = st.text_input(
    "Enter a research topic"
)


# ---------------- GENERATE REPORT ----------------

if st.button("Generate Report"):

    if topic.strip() == "":

        st.warning(
            "⚠️ Please enter a research topic."
        )

    else:

        with st.spinner(
            "🤖 AI agents are researching..."
        ):

            # Planner Agent
            plan = planner_agent(topic)

            # Researcher Agent
            research = researcher_agent(topic)

            # Analyst Agent
            analysis = analyst_agent(
                topic,
                research
            )

            # Writer Agent
            report = writer_agent(
                topic,
                analysis
            )

            # Fact Checker Agent
            fact_check = fact_checker_agent(
                topic,
                report
            )

        # Success Message

        st.success(
            "✅ Report generated successfully!"
        )

        # Time

        st.write(
            "🕒 Generated on:",
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        )

        st.divider()

        # Research Plan

        st.subheader(
            "📋 Research Plan"
        )

        st.write(plan)

        st.divider()

        # Web Results

        st.subheader(
            "🌐 Web Results"
        )

        for item in research:

            st.write(
                "•",
                item
            )

        st.divider()

        # AI Analysis

        st.subheader(
            "🧠 AI Analysis"
        )

        st.write(
            analysis
        )

        st.divider()

        # Final Report

        st.subheader(
            "📄 Final Report"
        )

        st.write(
            report
        )

        st.divider()

        # Fact Check

        st.subheader(
            "✅ Fact Check"
        )

        st.write(
            fact_check
        )

        st.divider()

        # Download Text Report

        st.download_button(

            label="📄 Download Text Report",

            data=report,

            file_name="research_report.md",

            mime="text/markdown"
        )

        # Download PDF

        pdf_file = create_pdf(
            topic,
            report
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(

                label="📄 Download PDF Report",

                data=file,

                file_name=pdf_file,

                mime="application/pdf"
            )