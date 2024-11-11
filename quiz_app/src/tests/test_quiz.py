# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService

# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    # INCOMPLETE: Set up the mock return value
    # TODO: Set `mock_create_quiz.return_value` to 1 (a mock quiz ID)
    mock_create_quiz.return_value = 1
    
    # INCOMPLETE: Make a POST request to create a quiz
    # TODO: Use `client.post` to send a POST request to `/api/quizzes` with JSON data
    quiz_data = {
        'title': 'Sample Quiz',
        'questions': [{'question': 'What is 2+2?', 'answer': '4'}]
    }
    response = client.post(
        '/api/quizzes', 
        json=quiz_data
    )
    
    # INCOMPLETE: Write assertions to check the response
    # TODO: Assert that status code is 201, `quiz_id` in response is 1, and `mock_create_quiz` was called once
    assert response.status_code == 201
    
    assert response.get_json()['quiz_id'] == 1 
    
    mock_create_quiz.assert_called_once() 

# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    # INCOMPLETE: Set up the mock to simulate a QuizModel object
    # TODO: Create a MagicMock named `mock_quiz`, set `title` to "Sample Quiz", and `questions` to a sample list
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    mock_quiz.questions = [{'question': 'What is 2+2?', 'answer': '4'}]
    
    mock_quiz.to_dict.return_value = {
        'title': mock_quiz.title,
        'questions': mock_quiz.questions
    }
    
    # INCOMPLETE: Assign the mock quiz to `mock_get_quiz.return_value`
    # TODO: Set `mock_get_quiz.return_value` to `mock_quiz`
    mock_get_quiz.return_value = mock_quiz
    
    # INCOMPLETE: Make a GET request to retrieve the quiz
    # TODO: Use `client.get` to send a GET request to `/api/quizzes/1`
    response = client.get('/api/quizzes/1')
    
    # INCOMPLETE: Write assertions to check the response
    # TODO: Assert that status code is 200, `title` in response is "Sample Quiz", and `mock_get_quiz` was called once
    assert response.status_code == 200
    
    response_json = response.get_json()
    assert response_json['title'] == "Sample Quiz"
    assert response_json['questions'] == [{'question': 'What is 2+2?', 'answer': '4'}]  # Quiz questions should match
    
    mock_get_quiz.assert_called_once()

# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    # INCOMPLETE: Set up the mock to simulate score calculation
    # TODO: Set `mock_evaluate_quiz.return_value` to (1, "Quiz evaluated successfully")
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")
    
    # INCOMPLETE: Make a POST request to submit answers for a quiz
    # TODO: Use `client.post` to send a POST request to `/api/quizzes/1/submit` with JSON data containing answers
    answers = ["4", "Paris"]
    quiz_data = {'answers': answers}
    
    response = client.post('/api/quizzes/1/submit', json=quiz_data)
    
    # INCOMPLETE: Write assertions to check the response
    # TODO: Assert that status code is 200, `score` in response is 1, `message` is "Quiz evaluated successfully", and `mock_evaluate_quiz` was called once
    assert response.status_code == 200 
     
    response_json = response.get_json()
    assert response_json['score'] == 1 
    assert response_json['message'] == "Quiz evaluated successfully"
    
    mock_evaluate_quiz.assert_called_once()
