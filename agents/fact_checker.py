from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)


def fact_checker_agent(topic, report):

    prompt = f"""
    Topic: {topic}

    Research Report:

    {report}

    Verify the report.

    1. Identify any doubtful claims.
    2. Point out missing information.
    3. Suggest corrections.
    4. Give an overall accuracy score out of 10.

    Return a clear fact-check summary.
    """

    response = llm.invoke(prompt)

    return response.content