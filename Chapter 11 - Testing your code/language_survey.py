#creating languag based questionnaire for survey.py
from survey import AnonymousSurvey
# Define a question about programming languages
question = "What language did you first learn to speak?"
# Create a survey object
language_survey = AnonymousSurvey(question)
# Show the question and store responses
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    language_survey.store_response(response)
# Show the survey results
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()