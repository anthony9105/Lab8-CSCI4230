# src/services/quiz_service.py
from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")
        
        quiz = QuizModel(title=title, questions=questions)
        
        quiz.save()
        
        return quiz.id

    def get_quiz(self, quiz_id):
        return QuizModel.get_quiz(quiz_id=quiz_id)
    
    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = self.get_quiz(quiz_id=quiz_id)
        
        if quiz is None:
            return None, "Quiz not found"
        
        score = 0
        
        for i, question in enumerate(quiz.questions):
            if user_answers[i] == question['answer']:
                score += 1
        
        return score, "Quiz evaluated successfully"
