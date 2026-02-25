import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

tarefas = []

while True:
    mensagem = socket.recv_json()
    comando = mensagem.get("comando")

    if comando == "adicionar":
        tarefa = mensagem.get("tarefa")
        tarefas.append(tarefa)
        socket.send_json({
            "status": "ok",
            "msg": "Tarefa adicionada!"
        })

    elif comando == "remover":
        tarefa = mensagem.get("tarefa")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            socket.send_json({
                "status": "ok",
                "msg": "Tarefa removida!"
            })
        else:
            socket.send_json({
                "status": "erro",
                "msg": "Tarefa não encontrada."
            })

    elif comando == "listar":
        socket.send_json({
            "status": "ok",
            "tarefas": tarefas
        })

    else:
        socket.send_json({
            "status": "erro",
            "msg": "Comando inválido."
        })
