# Polls System - Poll Service

## Description

The service is responsible for managing polls (both questions and choices) in the system:

- Create a new poll
- Update a poll
- Delete a poll
- Get a poll

## API Endpoints

### Questions

- **GET** `/questions` - Get all questions
- **GET** `/questions/{question_id}` - Get question by ID
- **POST** `/questions` - Create a new multiple choice question
- **PUT** `/questions/{question_id}` - Update question by ID
- **DELETE** `/questions/{question_id}` - Delete question by ID

### Answers

- **GET** `/answers` - Get all answers in the system
- **GET** `/answers/user/{user_id}` - Get all answers for a specific user
- **GET** `/answers/qustion/{qustion_id}` - Get all answers for a specific question
- **POST** `/answers` - Submit a new answer
- **PUT** `/answers/{answer_id}` - Update answer
- **DELETE** `/answers/user/{user_id}` - Delete all answers submitted by user
- **DELETE** `/answers/qustion/{qustion_id}` - Delete all answers related to question

### analytics

- **GET** `/analytics/questions/{question_id}/choices` - Get choices distribution for a question
- **GET** `/analytics/questions/{question_id}/total` - Get amount of answers for a question
- **GET** `/analytics/users/{user_id}/answers` - Get all answers submitted by user ID
- **GET** `/analytics/users/{user_id}/total_answers` - Get amount of questions answered by user
- **GET** `/analytics/questions` - Get global statistics overview

## Get Started

1. Clone the repository
2. run `pip install -r requirements.txt` to install dependencies
3. run `docker-compose up -d` to build the docker image for db and poll service
4. to run the service locally run `uvicorn app.main:app --reload --port 8010` command
