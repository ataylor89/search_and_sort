# Quicksort

Hi everyone. It's Friday evening, and I wanted to write a blog post on the Quicksort algorithm.

Charles Antony Richard Hoare, also known as Tony Hoare or C. A. R. Hoare, wrote two important papers on this algorithm, in July 1961 and January 1962.

You can find the July 1961 publication here: [https://dl.acm.org/doi/epdf/10.1145/366622.366642](https://dl.acm.org/doi/epdf/10.1145/366622.366642).

You can find the January 1962 publication here: [https://www.cs.ox.ac.uk/files/6226/H2006%20-%20Historic%20Quicksort.pdf](https://www.cs.ox.ac.uk/files/6226/H2006%20-%20Historic%20Quicksort.pdf).

(Also, here: [https://academic.oup.com/comjnl/article/5/1/10/395338](https://academic.oup.com/comjnl/article/5/1/10/395338]).

I wrote an implementation of the algorithm and pushed it to one of my Github repositories.

You can find it in this repository: [https://github.com/ataylor89/search_and_sort](https://github.com/ataylor89/search_and_sort).

You can find it in this file: [https://github.com/ataylor89/search_and_sort/blob/main/sort.py](https://github.com/ataylor89/search_and_sort/blob/main/sort.py).

Now, I remember conducting an interview for a software engineering job, in which the interviewer asked me the question, "Can you name an algorithm that can be used to sort a list?" I promptly responded, "Quicksort".

The interviewer then asked me, "Can you implement the algorithm?"

I don't remember what happened afterward, but in all likelihood, I was probably unable to remember the full implementation of the algorithm. I may have tried my hand at implementing it, unsuccessfully. Or I may have implemented a simpler algorithm instead.

So recently I decided to sit down and work on the problem, "How do you remember the implementation of Quicksort?"

I realized that it helps to remember several key ideas.

If we can remember several key ideas, then perhaps we can remember the full implementation.

The key ideas are as follows:

1. The Quicksort algorithm consists of two methods, a recursive quicksort method and an iterative partition method
2. The first statement of the quicksort method is the recursion condition, "if low < high"
3. The first statement of the partition method is to initialize the variable i to low - 1, that is, i = low - 1
4. We choose arr[high] to be the pivot value
5. We use a variable called j to loop through the subarray
6. The swap condition is "if arr[j] <= pivot"
7. We always increment i (by one) before swapping
8. We swap arr[i] and arr[j] whenever the swap condition is satisfied
9. We return the new pivot index at the end of the partition method

I know that nine ideas is a lot... but honestly, to remember the implementation, I might have to remember 5-10 important ideas.

I think that these nine ideas give us a lot of traction in solving the problem, and writing the implementation.

Now, I wanted this blog post to be short, simple, and concise.

The "heavy lifting" is in the code and the papers that I linked to.

The thesis of my post is simple: If we want to remember the Quicksort implementation, it helps to remember several key ideas.

Hopefully, the next time I sit down to implement the Quicksort algorithm, I'll be able to do so, knowing these key ideas.

Now, it's late, and I'm planning to watch a new TV show called Star Wars: The Ninth Jedi.

I'm excited to watch episode 1.

Maybe later I'll let you know what I think... of the TV show... of episode 1.

I wish everyone a nice weekend.

Thanks for reading,  
Andrew
