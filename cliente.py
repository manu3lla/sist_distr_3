import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

def menu():
    print("\n1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        mensagem = {"comando": "adicionar", "tarefa": tarefa}
        socket.send_json(mensagem)
        resposta = socket.recv_json()
        print(resposta["msg"])

    elif opcao == "2":
        tarefa = input("Digite a tarefa a remover: ")
        mensagem = {"comando": "remover", "tarefa": tarefa}
        socket.send_json(mensagem)
        resposta = socket.recv_json()
        print(resposta["msg"])

    elif opcao == "3":
        mensagem = {"comando": "listar"}
        socket.send_json(mensagem)
        resposta = socket.recv_json()

        print("\nTarefas:")
        for t in resposta["tarefas"]:
            print("-", t)

    elif opcao == "4":
        break
