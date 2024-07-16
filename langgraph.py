# -*- coding: utf-8 -*-
"""langgraph

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IfKxgprZAsblk3rQ0dhRZmbaHM6W3awX
"""

from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict

class Estado(TypedDict):
    parametro : str
    res_nodo1 : str
    res_nodo2 : str
    res_nodo3 : str
    res_nodo4 : str
    res_nodo5 : str
    res_final : str
    pasos : int

def nodo1(state):
  pasos = state['pasos']
  pasos += 1
  res_nodo = "ok" if isinstance(state['parametro'], int) else "no"
  print(f'---- pasaje por el nodo 1 ---- paso {pasos} ')
  return {"res_nodo1": res_nodo, "pasos": pasos}

def nodo2(state):
  pasos = state['pasos']
  pasos += 1
  res_nodo = "ok" if state['parametro'] % 2 ==0 else "no"
  print(f'---- pasaje por el nodo 2 ---- paso {pasos} ')
  return {"res_nodo2": res_nodo, "pasos": pasos}

def nodo3(state):
  pasos = state['pasos']
  pasos += 1
  res_nodo = "ok" if state['parametro'] % 3 ==0 else "no"
  print(f'---- pasaje por el nodo 3 ---- paso {pasos} ')
  return {"res_nodo3": res_nodo, "pasos": pasos}

def nodo4(state):
  pasos = state['pasos']
  pasos += 1
  res_nodo = "ok" if state['parametro'] % 4 ==0 else "no"
  print(f'---- pasaje por el nodo 4 ---- paso {pasos} ')
  return {"res_nodo4": res_nodo, "pasos": pasos}

def nodo5(state):
  pasos = state['pasos']
  pasos += 1
  res_nodo = "todos ok" if state['res_nodo1'] == "ok" and state['res_nodo2'] == "ok" and state['res_nodo3'] == "ok" and state['res_nodo4'] == "ok" else "no"
  print(f'---- pasaje por el nodo 5 ---- paso {pasos} ')
  return {"res_nodo5": res_nodo, "pasos": pasos}

def nodo6(state):
  print(f'resultado nodo 1: {state["res_nodo1"]}')
  print(f'resultado nodo 2: {state["res_nodo2"]}')
  print(f'resultado nodo 3: {state["res_nodo3"]}')
  print(f'resultado nodo 4: {state["res_nodo4"]}')
  print(f'resultado nodo 5: {state["res_nodo5"]}')
  return

#workflow secuencial
workflow = StateGraph(Estado)

workflow.add_node("nodo1", nodo1)
workflow.add_node("nodo2", nodo2)
workflow.add_node("nodo3", nodo3)
workflow.add_node("nodo4", nodo4)
workflow.add_node("nodo5", nodo5)
workflow.add_node("nodo6", nodo6)

workflow.set_entry_point("nodo1")
workflow.add_edge("nodo1", "nodo2")
workflow.add_edge("nodo2", "nodo3")
workflow.add_edge("nodo3", "nodo4")
workflow.add_edge("nodo4", "nodo5")
workflow.add_edge("nodo5", "nodo6")
workflow.add_edge("nodo6", END)

app = workflow.compile()

resultado = app.invoke({"parametro":12,"pasos":0})
from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))