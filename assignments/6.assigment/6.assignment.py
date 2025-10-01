import os
import re

# Define positive and negative word lists for Amazon project reviews
POSITIVE_WORDS = {
    "reliable","professional", "efficient", "trustworthy", "supportive",
"timely", "accurate", "user-friendly", "innovative", "responsive",
"flexible", "scalable", "smooth", "transparent", "well-organized",
"secure", "consistent", "excellent", "valuable", "high-quality",
"outstanding", "dependable", "collaborative", "knowledgeable",
"proactive", "seamless", "effective", "satisfactory"

}

NEGATIVE_WORDS = {
    "unreliable", "unprofessional", "inefficient", "careless", "slow",
"delayed", "inaccurate", "unfriendly", "complicated", "rigid",
"inflexible", "insecure", "inconsistent", "poor", "low-quality",
"unsatisfactory", "disappointing", "weak", "unhelpful", "unresponsive",
"messy", "confusing", "buggy", "frustrating", "untrustworthy", "limited",
"problematic", "unstable","bad"

}

# ✅ Directory where Amazon review .txt files are stored
amazon_reviews_dir = r"C:\Users\chala\OneDrive\Desktop\python_class\assignments\6.assigment\amazon_review"

print("Looking for Amazon reviews in:", os.path.abspath(amazon_reviews_dir))

# Ensure the directory exists
os.makedirs(amazon_reviews_dir, exist_ok=True)

def sanitize_filename(filename):
    """Clean filename: strip spaces and ensure .txt extension."""
    filename = filename.strip()
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

def analyze_sentiment(content):
    """Analyze Amazon review content and determine sentiment."""
    positive_count = len(re.findall(r'\b(?:' + '|'.join(POSITIVE_WORDS) + r')\b', content, re.IGNORECASE))
    negative_count = len(re.findall(r'\b(?:' + '|'.join(NEGATIVE_WORDS) + r')\b', content, re.IGNORECASE))

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

def read_and_analyze_review():
    """Read and analyze a specific Amazon review or all reviews."""
    choice = input("Do you want to analyze:\n1. A specific review\n2. All reviews\nEnter your choice: ").strip()

    if choice == "1":
        filename = input("Enter the file name: ")
        filename = sanitize_filename(filename)
        file_path = os.path.join(amazon_reviews_dir, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                sentiment = analyze_sentiment(content)
                print(f"\nAnalyzing file: {filename}\nDetected Sentiment: {sentiment}\n")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in {amazon_reviews_dir}.")
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")

    elif choice == "2":
        sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        files = os.listdir(amazon_reviews_dir)

        if not files:
            print("No Amazon reviews found.")
            return

        for filename in files:
            file_path = os.path.join(amazon_reviews_dir, filename)

            # ✅ Skip directories
            if not os.path.isfile(file_path):
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    sentiment = analyze_sentiment(content)
                    sentiment_counts[sentiment] += 1
            except Exception as e:
                print(f"Error reading file '{filename}': {e}")

        print("\n📊 Overall Amazon Review Sentiment Analysis:")
        for sentiment, count in sentiment_counts.items():
            print(f"{sentiment}: {count} review(s)")

    else:
        print("Invalid choice. Please enter 1 or 2.")

def create_review():
    """Create a new Amazon review note."""
    filename = input("Enter the name of the new Amazon review: ")
    filename = sanitize_filename(filename)
    file_path = os.path.join(amazon_reviews_dir, filename)

    content = input("Enter your Amazon review content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"✅ Amazon review '{filename}' saved successfully.")

def modify_review():
    """Modify an existing Amazon review note."""
    files = os.listdir(amazon_reviews_dir)
    files = [f for f in files if os.path.isfile(os.path.join(amazon_reviews_dir, f))]

    if not files:
        print("No Amazon reviews available to modify.")
        return

    print("Existing Amazon reviews:", ", ".join(files))
    filename = input("Enter the file name to modify: ")
    filename = sanitize_filename(filename)
    file_path = os.path.join(amazon_reviews_dir, filename)

    if not os.path.exists(file_path):
        print(f"Error: File '{filename}' not found in {amazon_reviews_dir}.")
        return

    new_content = input("Enter new Amazon review content:\n")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"✅ Amazon review '{filename}' updated successfully.")

def main():
    """Main function to run the Amazon Review Notes Management System."""
    while True:
        print("\n🛒 Amazon Review System")
        print("1. Read & Analyze Reviews")
        print("2. Create a New Review")
        print("3. Modify an Existing Review")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            read_and_analyze_review()
        elif choice == "2":
            create_review()
        elif choice == "3":
            modify_review()
        elif choice == "4":
            print("Exiting program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
