import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    'message': [
        'Congratulations you won a free iPhone',
        'Claim your prize now',
        'Get free recharge today',
        'Hi how are you',
        'Lets meet tomorrow',
        'Call me when you are free',
        'Win cash reward now',
        'Urgent! Your account has won money',
        'Good morning',
        'See you in class'
    ],
    'label': [
        'spam',
        'spam',
        'spam',
        'ham',
        'ham',
        'ham',
        'spam',
        'spam',
        'ham',
        'ham'
    ]
}

df = pd.DataFrame(data)

# Convert labels
df['label'] = df['label'].map({'ham':0,'spam':1})

# Features and Target
X = df['message']
y = df['label']

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# User Input
message = input("Enter Message: ")

message_vector = vectorizer.transform([message])

result = model.predict(message_vector)

if result[0] == 1:
    print("Spam Message")
else:
    print("Ham (Not Spam)")