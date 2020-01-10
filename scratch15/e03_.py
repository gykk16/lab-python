import graphviz
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz

iris = load_iris()
X = iris.data
y = iris.target

# 의사 결정 나무(알고리즘) 객체 생성
decision_tree = DecisionTreeClassifier()

# 데이터를 모델에 fitting, 학습
decision_tree.fit(X, y)

# 예측 => 과제

# 의사 결정 나무 텍스트 출력
text_result = export_text(decision_tree, iris.feature_names)
print(text_result)

# 의사 결정 나무 그래프 출력
graph_data = export_graphviz(decision_tree,
                             feature_names = iris.feature_names,
                             class_names = iris.target_names,
                             filled = True)

graph = graphviz.Source(graph_data)
graph.render('iris')
