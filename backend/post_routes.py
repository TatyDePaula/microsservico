# backend/post_routes.py
from flask import jsonify, request, Blueprint
from backend import database
from backend.models import Post
from sqlalchemy.exc import SQLAlchemyError

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        'id': p.id,
        'titulo': p.titulo,
        'corpo': p.corpo,
        'data_criacao': p.data_criacao,
        'id_usuario': p.id_usuario
    } for p in posts]), 200

@post_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
        'id': post.id,
        'titulo': post.titulo,
        'corpo': post.corpo,
        'data_criacao': post.data_criacao,
        'id_usuario': post.id_usuario
    }), 200

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    # Validação dos dados recebidos
    if not all(key in data for key in ('titulo', 'corpo', 'id_usuario')):
        return jsonify({'error': 'Dados incompletos'}), 400

    try:
        new_post = Post(
            titulo=data['titulo'],
            corpo=data['corpo'],
            id_usuario=data['id_usuario']
        )
        database.session.add(new_post)
        database.session.commit()
        return jsonify({'message': 'Post criado com sucesso!'}), 201
    except SQLAlchemyError as e:
        database.session.rollback()
        return jsonify({'error': str(e)}), 500

@post_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.titulo = data.get('titulo', post.titulo)
    post.corpo = data.get('corpo', post.corpo)

    try:
        database.session.commit()
        return jsonify({'message': 'Post atualizado com sucesso!'}), 200
    except SQLAlchemyError as e:
        database.session.rollback()
        return jsonify({'error': str(e)}), 500

@post_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    
    try:
        database.session.delete(post)
        database.session.commit()
        return jsonify({'message': 'Post excluído com sucesso!'}), 200
    except SQLAlchemyError as e:
        database.session.rollback()
        return jsonify({'error': str(e)}), 500



