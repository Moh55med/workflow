from langgraph.graph import StateGraph, END, START
import random
from typing import TypedDict

class TourismState(TypedDict, total=False):
    total_tourists: int
    religious_tourists: int
    regular_tourists: int
    top_countries: list
    monthly_arrivals: dict

def get_total_tourists(state):
    total = 10000000  # Example static data
    return {"total_tourists": total}

def split_tourists(state):
    total = state["total_tourists"]
    religious = int(total * 0.6)
    regular = total - religious
    state.update({"religious_tourists": religious, "regular_tourists": regular})
    return state

def top_countries(state):
    countries = [
        {"country": "Egypt", "tourists": 2000000},
        {"country": "India", "tourists": 1500000},
        {"country": "Pakistan", "tourists": 1200000},
        {"country": "Indonesia", "tourists": 1000000},
        {"country": "Turkey", "tourists": 800000},
    ]
    state["top_countries"] = countries
    return state

def monthly_arrivals(state):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    arrivals = {month: random.randint(600000, 900000) for month in months}
    state["monthly_arrivals"] = arrivals
    return state

# Build the workflow graph
builder = StateGraph(TourismState)
builder.add_node("get_total_tourists", get_total_tourists)
builder.add_node("split_tourists", split_tourists)
builder.add_node("top_countries", top_countries)
builder.add_node("monthly_arrivals", monthly_arrivals)

builder.add_edge(START, "get_total_tourists")
builder.add_edge("get_total_tourists", "split_tourists")
builder.add_edge("split_tourists", "top_countries")
builder.add_edge("top_countries", "monthly_arrivals")
builder.add_edge("monthly_arrivals", END)

workflow = builder.compile()

def analyze_tourism_workflow():
    result = workflow.invoke({})
    return {"data": result}

if __name__ == "__main__":
    # Example: run the workflow for the year 2021
    result = analyze_tourism_workflow()
    print(result)
