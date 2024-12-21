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
        print(f"\nQuestion {i}:")
        print(question["question"])
        user_answer = input("Your answer: ").strip()

        if check_answer(question, user_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect! Exiting...")
            return

    if correct_answers == len(questions):
        print(f"\nCongratulations! Here's your flag: {flag}")
    else:
        print("\nSorry, you didn't answer all questions correctly.")
# ... existing code ...
if __name__ == "__main__":
    try:
        # Thêm netcat để lắng nghe kết nối
        import socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 1337))
        server.listen(1)
        
        print("Server is listening on port 1337...")
        while True:
            client, addr = server.accept()
            try:
                # Redirect stdin/stdout to socket
                import sys
                sys.stdin = client.makefile('r')
                sys.stdout = client.makefile('w')
                main()
            except Exception as e:
                print(f"\nAn error occurred. Exiting...")
            finally:
                client.close()
    except KeyboardInterrupt:
        print("\nExiting...")
        server.close()
    except Exception as e:
        print(f"\nAn error occurred. Exiting...")