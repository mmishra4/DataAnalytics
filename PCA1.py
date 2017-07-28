import numpy as np

print(np.__version__)
migration_matrix = np.array([[0.8, 0.05],[0.02, 0.95]])
before_population = np.array([[400],[200]])
for i in list(range(1,100,1)):
    after_population = migration_matrix.dot(before_population)
    print("after" , i , ":" , after_population)
    before_population = after_population
np.linalg.eig(migration_matrix)

m1= np.array([[1,2],[2,1]])
np.linalg.eig(m1)