# Approach

# You want to find the most common substring within two strings

You are given two strings for ex:

a = "ABAB"

b = "BABA"

By looking at these two strings we should be able to find the most common substring is ABA.

Things to take into account when answering this question:

1. What is the characset that we will be using... all uppercase or will there be lowercase?

2. What is the max length of this string? Is there any caps set on the string or will it need
to handle all strings thrown at it?

3. 

# Methods

1. You could run threw all variations of the string. This would not be the prefered approach but
it could get you down the right path when talking with your interviewer. 

2. You could print out all the variations into a dic or list. Then see what the most common occurence.
This isn't preferred as well but it would get the job done. Only concern you may want to have is mem
limits set.

3. Use a type of graph approach for ex:

   A  B  A  B
B [0  1  0  1]
A [1  0  2  0]
B [0  2  0  3]
A [1  0  3  0]