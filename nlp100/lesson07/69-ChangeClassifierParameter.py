from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('./nlp100/lesson07/data/SST-2/train.tsv', sep = '\t')
valid_data = pd.read_csv('./nlp100/lesson07/data/SST-2/dev.tsv', sep = '\t')

# データの前処理
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['sentence'].to_list()).toarray()
y_train = train_data['label'].to_numpy()
X_valid = vectorizer.transform(valid_data['sentence'].to_list()).toarray()
y_valid = valid_data['label'].to_numpy()

C = np.linspace(0.001, 1, 5).tolist()
accuracies = []
for c in C:
    # モデルの学習
    classifier = LogisticRegression(penalty = 'l2', C = c, random_state = 42)
    classifier.fit(X_train, y_train)

    # 予測
    y_pred = classifier.predict(X_valid)

    # 正解率評価
    accuracies.append(accuracy_score(y_valid, y_pred))

plt.plot(pd.Series(C), pd.Series(accuracies))
plt.show()
