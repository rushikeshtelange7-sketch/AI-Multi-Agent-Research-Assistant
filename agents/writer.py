from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def writer_agent(topic, analysis):

    prompt = f"""
    Create a professional research report.

    Topic:

    {topic}

    Analysis:

    {analysis}

    Include:

    1. Introduction

    2. Key Findings

    3. Conclusion

    Keep it concise and professional.
    """

    response = llm.invoke(prompt)

    return response.content