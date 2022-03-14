The solution can be obtained by creating a subarray of the original array and then checking whether the subarray forms an aesthetically pleasing garden. 

Firstly, create a function, isAesthetic() that checks whether the garden is aesthetically pleasing, i.e., if the trees are alternating between increasing and decreasing in height.

Subsequently, in the main function, the original array is passed into the isAesthetic() function to check whether the garden is already pleasing to look at, if yes the function will return 0 ways to cut the tree. Else, the function continues.

In a for loop running at the length of the array, a subarray is created for each iteraton to check if the garden would be aesthetically pleasing if the current iteration tree was chopped down. If so, increment the waysToCut variable. Else, continue on the for loop. Should the for loop end with 0 ways to cut the tree, the function will return -1, else it will return the appropriate number of ways to cut the trees.
