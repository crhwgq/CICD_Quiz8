# CI/CD Quiz 8

Add More Functionalities:

1. Basic operations: addition, subtraction, multiplication and division.

2. Advance operations: log, square, sin, cos, square root, percentage. Think of boundary conditions.


Testing:

1. Write test cases that cover each operations as well as boundary conditions. 

2. Achieve 100% test coverage.

3. Create html report.
   

CI/CD: 

1. When you implement the operations (basic/advance), do it on development branch. Write a .yml for that. This part is for only CI.

2. Do the CD (deployment) part on the main/master branch. Write a .yml for that. Only when development branch is merged, only then trigger .yml for CD.

3. The CI workflow should trigger only when you make changes in development branch.

4. The CD workflow should trigger only when you merge your development branch with master/main branch.
