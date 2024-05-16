import json
import re


def parse_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    # Split the content into questions using a regular expression
    questions = re.split(r'(Question #\d+)', content)
    questions = [q.strip() for q in questions if q.strip()]

    parsed_questions = []

    for i in range(1, len(questions), 2):
        question_data = {}

        # Extract question number
        question_number_match = re.search(r'Question #(\d+)', questions[i-1])
        if question_number_match:
            question_number = question_number_match.group(1)
            question_data['question_number'] = question_number

        # Combine question number and content
        question = questions[i-1] + " " + questions[i]

        # Extract topic
        topic_match = re.search(r'Topic (\d+)', question)
        if topic_match:
            question_data['topic'] = f"Topic {topic_match.group(1)}"

        # Extract question text
        question_text_match = re.search(r'(.*?)(?=A\.)', question, re.DOTALL)
        if question_text_match:
            question_data['question_text'] = question_text_match.group(
                1).strip()

        # Extract options
        options = re.findall(
            r'([A-D])\.\s(.*?)(?=[A-D]\.|Correct Answer:)', question, re.DOTALL)
        question_data['options'] = {opt[0]: opt[1].strip() for opt in options}

        # Extract correct answer
        correct_answer_match = re.search(
            r'Correct Answer:\s([A-D]+)', question)
        if correct_answer_match:
            correct_answer = correct_answer_match.group(1).strip()
            if len(correct_answer) > 1:
                question_data['correct_answer'] = list(correct_answer)
            else:
                question_data['correct_answer'] = correct_answer

        # Extract community vote distribution
        community_vote_match = re.search(
            r'Community vote distribution\s*(.*?)\s*(?=Question|$)', question, re.DOTALL)
        if community_vote_match:
            votes = re.findall(r'([A-D]+)\s*\((\d+)%\)',
                               community_vote_match.group(1))
            question_data['community_vote_distribution'] = {
                vote[0]: f"{vote[1]}%" for vote in votes}

        parsed_questions.append(question_data)

    return parsed_questions


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    # input_file = '1-100_OCR.txt'  # Replace with your file path
    input_file = 'data/text-files/devnet/200-383_OCR.txt'  # Replace with your file path
    output_file = 'data/question-files/devnet/100-200_test2.json'

    parsed_data = parse_text_file(input_file)
    save_to_json(parsed_data, output_file)
    print(f"Data has been successfully converted to {output_file}")
