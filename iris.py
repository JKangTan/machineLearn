from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from IPython.display import Image
import pydotplus
import graphviz


iris = load_iris()

print("feature: ",iris.feature_names)
print("names: ",iris.target_names)

print(iris.data[0])
print(iris.target[0])


# iris.data 和iris.target 的50 100 0 分别记录一种花的开始

test_index = [0, 50, 100]
training_data = np.delete(iris.data, test_index, axis = 0)  # data是个二维数组 axis=0 表示删除对应整行
training_target = np.delete(iris.target, test_index)

testing_data = iris.data[test_index]
testing_target = iris.target[test_index]


clf = tree.DecisionTreeClassifier()
clf.fit(training_data, training_target)

print("testing_data" , testing_data)
print("testing_target" , testing_target)
print(clf.predict(testing_data))


dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
grap = pydotplus.graph_from_dot_data(dot_data)
grap.write_pdf("iris.pdf")
