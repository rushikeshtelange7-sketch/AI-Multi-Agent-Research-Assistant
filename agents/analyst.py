from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def analyst_agent(topic, research):

    prompt = f"""
    Topic:

    {topic}

    Research Data:

    {research}

    Summarize the important insights in 5 bullet points.
    """

    response = llm.invoke(prompt)

    return response.content