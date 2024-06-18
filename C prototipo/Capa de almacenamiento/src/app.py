# Este el el ejemplo proporcionado (sobre un blog), debe ser adecuado a la estructura actual del desarrollo IoT y la respectiva base de datos.
""" Este es un código muy básico y podría necesitar mejoras para un entorno de producción, 
pero nos dará una idea de cómo funcionan las APIs RESTful con Flask."""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Esta línea permitirá las solucitudes de origen cruzado

posts = [
    {'id' : 1, 'contenido' : 'Primera publicacion'},
    {'id' : 2, 'contenido' : 'Segunda publicacion'}
]

@app.route('/blog', methods = ['GET'])
def get_posts():
        return jsonify(posts)

@app.route('/blog', methods = ['POST'])
def add_posts():
        new_post = {'id' : request.json['id'], 'contenido' : request.json['contenido']}
        posts.append(new_post)
        return jsonify(new_post), 201

@app.route('/blog/<int:post_id>', methods = ['PUT'])
def update_posts(post_id):
        post = [post for post in posts if post ['id'] == post_id]
        if not post:
                return jsonify({'error': 'No se encontro la publicacion'}), 404
        post[0]['contenido'] = request.json.get('contenido', post[0]['contenido'])
        return jsonify(post[0])

# Nueva línea: Implementación del PATCH

"""@app.route('/blog/<int:post_id>', methods=['PATCH'])
def patch_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if not post:
        return jsonify({'error': 'No se encontró la publicación'}), 404
    if 'contenido' in request.json:
        post[0]['contenido'] = request.json['contenido']
    return jsonify(post[0])"""

@app.route('/blog/<int:post_id>', methods = ['DELETE'])
def delete_posts(post_id):
        global posts # Nueva línea
        post = [post for post in posts if post ['id'] == post_id]
        if not post:
                return jsonify({'error': 'No se encontro la publicacion'}), 404
        posts = [p for p in posts if p['id'] != post_id] # Línea anterior: post.remove(post[0])
        return jsonify({'exito': 'Publicacion eliminada correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)