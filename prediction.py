import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

#读入+查看数据集
data=pd.read_csv('./static/mbti_1.csv')
#print(data[0:2])
#print(data['type'].value_counts())

#8：2划分训练集、测试集
X_train, X_test, y_train, y_test = train_test_split(data['posts'], data['type'], test_size=0.2, random_state=123)

#文本向量化
tfidf = TfidfVectorizer(stop_words='english')
X_train = tfidf.fit_transform(X_train)
X_test = tfidf.transform(X_test)

#机器学习-分类 多try几个分类模型 选个效果好的
#model1-逻辑回归 0.64
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report
# model1 = LogisticRegression(max_iter=3000)
# model1.fit(X_train, y_train)
# y_predicted = model1.predict(X_test)

#model2-决策树 0.47
# from sklearn import tree
# from sklearn.metrics import classification_report
# model2 = tree.DecisionTreeClassifier()
# model2.fit(X_train, y_train)
# y_predicted = model2.predict(X_test)

#model3-SGD 0.68
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
model3 = SGDClassifier()
model3.fit(X_train, y_train)
y_predicted = model3.predict(X_test)

#model4-SVM very very slow
# from sklearn import svm
# from sklearn.metrics import classification_report
# model4 = svm.SVC()
# model4.fit(X_train, y_train)
# y_predicted = model4.predict(X_test)

# #model5-KNeighbors very very slow
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import classification_report
# model4 = KNeighborsClassifier()
# model4.fit(X_train, y_train)
# y_predicted = model4.predict(X_test)

#分类结果
print('Score： ',model3.score(X_test, y_test))
print(classification_report(y_test, y_predicted))

#输入一个样本，进行预测，比如懒羊羊口吻说的话
input_data=["Remember, my woolly pals, relaxation is not a race. Take your time, listen to your heart, and find what truly brings you joy. Life is too short to be stressed, so let's embrace our inner calm and enjoy every fluffy moment!"]
input_data = tfidf.transform(input_data)
print(model3.predict(input_data))