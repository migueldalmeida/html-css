import json
import os
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, prioridade="Média"):
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = False
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__

class GerenciadorTarefas:
    def __init__(self, arquivo='tarefas.json'):
        self.arquivo = arquivo
        self.tarefas = self._carregar_dados()

    def _carregar_dados(self):
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Erro ao carregar: {e}")
        return []

    def salvar(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.tarefas, f, indent=4)

    def adicionar(self, titulo, prioridade):
        nova_tarefa = Tarefa(titulo, prioridade)
        self.tarefas.append(nova_tarefa.to_dict())
        self.salvar()
        print(f"✅ Tarefa '{titulo}' adicionada!")

    def listar(self, apenas_pendentes=False):
        print("\n--- LISTA DE TAREFAS ---")
        for i, t in enumerate(self.tarefas):
            status = "✔" if t['concluida'] else " "
            if apenas_pendentes and t['concluida']:
                continue
            print(f"{i}. [{status}] {t['titulo']} ({t['prioridade']}) - {t['data_criacao']}")

# Exemplo de execução
gerenciador = GerenciadorTarefas()

# Adicionando dados de teste
if not gerenciador.tarefas:
    gerenciador.adicionar("Estudar Python Avançado", "Alta")
    gerenciador.adicionar("Ir à academia", "Média")

gerenciador.listar()