import pandas as pd 
import joblib 

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

df = pd.read_csv("data/processed/career_dataset.csv")
print(df.shape)

x = df.drop("Career", axis=1)
y = df["Career"]

encoder = LabelEncoder ()
y = encoder.fit_transform (y) 

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 42
    )

model = RandomForestClassifier(
    n_estimators = 100,
    random_state = 42
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy:.2f}")
print(classification_report(y_test, y_pred))
print(x.shape)
print(y.shape)
print(x_train.shape)
print(y_test.shape)
print(df.shape)

joblib.dump(model, "models/career_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")
print("Model saved Successfully")
loaded_model = joblib.load("models/career_model.pkl")