import os
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def eval():
    # Get the path to traces.out relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    traces_path = os.path.join(script_dir, "traces.out")

    print("Script directory:", script_dir)
    print("Looking for traces.out at:", traces_path)
    if not os.path.exists(traces_path):
        print("Error: traces.out not found!")
        print("Files in script directory:", os.listdir(script_dir))
        return

    # Load data
    with open(traces_path, "r") as f:
        data = json.load(f)

    # Extract features and labels
    X = np.array(data["traces"])
    y = np.array(data["labels"])

    y_pred_full, y_test_full = [], []

    # Re-train 10 times to reduce randomness
    for i in range(10):
        # 2. Split data into train/test (stratified)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            stratify=y,
            random_state=i
        )

        # 3. Train classifier
        clf = RandomForestClassifier(n_estimators=100, random_state=i)
        clf.fit(X_train, y_train)

        # 4. Predict on test set
        y_pred = clf.predict(X_test)

        # Collect predictions
        y_test_full.extend(y_test)
        y_pred_full.extend(y_pred)

    # 5. Print classification report
    print("\n=== Classification Report ===")
    print(classification_report(y_test_full, y_pred_full))


if __name__ == "__main__":
    eval()
