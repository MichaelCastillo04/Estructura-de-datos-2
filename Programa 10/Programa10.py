from flask import Flask, jsonify, request

app = Flask(__name__)

from fraces import fraces


@app.route('/fraces')
def getFraces():
    # return jsonify(fraces)
    return jsonify({'fraces': fraces})


@app.route('/fraces/<string:fraces_significado>')
def getFraces(fraces_significado):
    fracesFound = [
        fraces for fraces in fraces if fraces['fraces'] == fraces_significado.lower()]
    if (len(fracesFound) > 0):
        return jsonify({'fraces': fracesFound[0]})
    return jsonify({'message': ''})


@app.route('/fraces', methods=['POST'])
def addFraces():
    nueva_fraces = {
        'fraces': request.json['fraces'],
        'significado': request.json['significado'],
    }
    fraces.append(nueva_fraces)
    return jsonify({'fraces': fraces})


@app.route('/fraces/<string:fraces_significado>', methods=['PUT'])
def editarfraces(fraces_significado):
    fracesFound = [fraces for fraces in fraces if fraces['fraces'] == fraces_significado]
    if (len(fracesFound) > 0):
        fracesFound[0]['fraces'] = request.json['fraces']
        fracesFound[0]['significado'] = request.json['significado']
        return jsonify({
            'message': 'fraces Actualizada',
            'fraces': fracesFound[0]
        })
    return jsonify({'message': 'fraces no encontrada'})


@app.route('/fraces/<string:palabra_significado>', methods=['DELETE'])
def eliminarfraces(fraces_significado):
    fracesFound = [fraces for fraces in fraces if fraces['fraces'] == fraces_significado]
    if len(fracesFound) > 0:
        fraces.remove([fracesFound])
        return jsonify({
            'message': 'fraces Eliminada',
            'fraces': fraces
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)