from openai import OpenAI

# Connect to API (your key must be set in environment variables)
client = OpenAI()

# Function to classify an expense
def classify_expense(description):
    prompt = f"""
    You are an expense classifier. 
    Classify the following description into one of these categories:
    [Food, Transport, School Supplies, Utilities, Education, Others]

    Expense: "{description}"

    Only reply with the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # the model we're using
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# User input loop
if __name__ == "__main__":
    while True:
        description = input("Enter an expense description (or 'quit' to exit): ")
        amount = int(input("enter the amount you have spent: "))
        if description.lower() == "quit":
            break
        category = classify_expense(description)
        print(f"Expense: {description} → {amount} → Category: {category}\n")
