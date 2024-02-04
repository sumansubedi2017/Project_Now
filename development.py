import matplotlib.pyplot as plt
import datetime
import random

# Sample motivational quotes
motivational_quotes = [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
    "Strive not to be a success, but rather to be of value. -Albert Einstein",
]

def display_motivational_quote():
    print("\nMotivational Quote:")
    print(random.choice(motivational_quotes))

def track_progress(activities, progress):
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    plt.figure(figsize=(10, 6))
    plt.bar(activities, progress, color='skyblue')
    plt.title('Personal Development Progress Tracker')
    plt.xlabel('Activities')
    plt.ylabel('Progress (%)')
    plt.ylim(0, 100)
    
    for i, value in enumerate(progress):
        plt.text(i, value + 2, f'{value}%', ha='center', va='bottom')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig(f'progress_chart_{today}.png')
    plt.show()

if __name__ == "__main__":
    activities = ['Goal Setting', 'Learning', 'Exercise', 'Reading', 'Networking']
    
    # Get progress data from the user
    progress = []
    for activity in activities:
        while True:
            try:
                progress_value = int(input(f'Enter your progress for {activity} (%): '))
                if 0 <= progress_value <= 100:
                    progress.append(progress_value)
                    break
                else:
                    print("Progress should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    
    display_motivational_quote()
    track_progress(activities, progress)
