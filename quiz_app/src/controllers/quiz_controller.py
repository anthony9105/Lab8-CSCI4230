# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')


@quiz_bp.route('', methods=['POST'])
def create_quiz():
    quiz_service = QuizService()
    
    data = request.json
    
    quiz_id = quiz_service.create_quiz(quiz_data=data)
    
    return jsonify({
        'message': 'Quiz created successfully',
        'quiz_id': quiz_id
    }), 201


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz_service = QuizService()

    quiz = quiz_service.get_quiz(quiz_id=quiz_id)
    
    if quiz:
        return jsonify(quiz.to_dict()), 200
    
    return jsonify({
        'error': 'No quiz found with that id'
    }), 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):

    quiz_service = QuizService()
    
    user_answers = request.json.get('answers')
    
    if not user_answers:
        return jsonify({
            'message': 'No answers were provided'
        }), 404
    
    score, message = quiz_service.evaluate_quiz(
        quiz_id=quiz_id, 
        user_answers=user_answers
    )
    
    if score is None:
        return jsonify({
            'error': message
        }), 404
    
    return jsonify({
        'score': score,
        'message': message
    }), 200
    
