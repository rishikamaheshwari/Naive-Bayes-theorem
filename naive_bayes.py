from sklearn.naive_bayes import GaussianNB
f=[[100,1],[150,1],[180,0],[210,0]]
l=['orange','orange','apple','apple']
clf=GaussianNB()
trained=clf.fit(f,l)
for i in range(0,10):
    res=trained.predict([[150,1],[180,0],[160,1],[170,0],[100,0],[180,1]])
    print(res)
