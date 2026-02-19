from typing import TypedDict
from langgraph.graph import StateGraph,END

class GraphState(TypedDict):
    question: str
    answer: str

def ask_llm(state: GraphState):
    state["answer"] = "hello llm here"
    return state

builder = StateGraph(GraphState)
builder.add_node("llm",ask_llm)
builder.set_entry_point("llm")
builder.add_edge("llm",END)

graph = builder.compile()

result=graph.invoke({"question": "What is LangGraph?", "answer": ""})
print(result)
