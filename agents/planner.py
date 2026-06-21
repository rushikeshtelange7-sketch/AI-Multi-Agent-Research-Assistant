from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def planner_agent(topic):

    prompt = f"""
    Create a research plan for this topic:

    {topic}

    Give 5 main research sections.
    """

    response = llm.invoke(prompt)

    return response.content