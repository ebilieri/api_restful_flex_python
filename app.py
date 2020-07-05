from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0',
     'nome': 'Emerson',
     'hablidades': ['Python', 'Flask', 'Django', 'C#']
     },
    {'id': '1',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']
     }
]

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    response = None
    try:
        response = desenvolvedores[id]
    except IndexError:
        mensagem = 'Desenvolvedor de id {} não existe'.format(id)
        response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    except Exception:
        mensagem = 'Erro desconhecido'
        response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    if request.method == 'GET':
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluído'})


@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
