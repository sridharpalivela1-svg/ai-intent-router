from classifier import classify_intent
from router import route_and_respond


def main():

    print("AI Intent Router")
    print("Type 'exit' to quit\n")

    while True:

        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        # Step 1: classify intent
        intent_data = classify_intent(user_message)

        intent = intent_data["intent"]
        confidence = intent_data["confidence"]

        print(f"\nDetected Intent: {intent}")
        print(f"Confidence: {confidence}")

        # Step 2: route to expert
        response = route_and_respond(user_message, intent_data)

        print("\nAI Response:")
        print(response)
        print("\n-----------------------------\n")


if __name__ == "__main__":
    main()
