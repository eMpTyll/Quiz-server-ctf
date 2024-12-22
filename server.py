import json


def check_answer(question, answer):
    if "alternatives" in question and answer.lower() in [
        alt.lower() for alt in question["alternatives"]
    ]:
        return True
    else:
        return question["answer"].lower() == answer.lower()


def main():
    with open("answers.json", "r") as f:
        data = json.load(f)

    questions = data["questions"]
    flag = data["flag"]
    correct_answers = 0

    for i, question in enumerate(questions, start=1):
        print(f"\nCâu hỏi {i}:")
        print(question["question"])
        user_answer = input("Câu trả lời: ").strip()

        if check_answer(question, user_answer):
            print("Chính xác. Good job, em!")
            correct_answers += 1
        else:
            print("Đáp án sai! Cố gắng thêm nhé :D")
            return

    if correct_answers == len(questions):
        print(f"\nChúc mừng! Flag của thầy: {flag}")
    else:
        print("\nXin lỗi, bạn không trả lời đúng tất cả câu hỏi.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nCó lỗi xảy ra: {e}")