from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from subprocess import check_call

iris = load_iris()
x = iris.data[:, 2:]
y = iris.target

tree_model = DecisionTreeClassifier(max_depth=3)
tree_model.fit(x,y)
export_graphviz(
    tree_model,
    out_file = './iris_tree_model_reg.dot',
    feature_names = iris.feature_names[2:],
    rounded = True,
    filled = True
)
check_call(['dot', '-Tpng', 'iris_tree_model_reg.dot', '-o', 'OutputFile.png'])
