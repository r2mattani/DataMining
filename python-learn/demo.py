from sklearn import tree

#[height, weight, shoe size]
X=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40]]
Y=['male','female','female','female','male','male','male','female']

clf=  tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

predection = clf.predict([[190,70,44],[150,50,24], [145,49,78]])

print predection
