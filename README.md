###

###

###

###

###



###
**# Cryptography Portfolio**

Mitchell Anderson

Table of Contents

| 1.Code Documentation |
| --- |
| a.Running the Program |
| b.Function Documentation |
| 2.Algorithm Descriptions |
| a.Affine Cipher |
| b.Vigenère Cipher |
| c.Frequency Calculation |
| d.Affine Cipher Attack |
| e.Vigenère Cipher Attack |
| f.Linear Feedback Shift Register Sequence |
| g.GCD (Greatest Common Denominator) |
| h.Extended GCD |
| i.Find Mod Inverse |
| j.Verify Primitive Roots |
| k.Miller-Rabin Primality Test |
| l.Generate Random Prime |
| m.Fermat&#39;s Factorization Method |
| n.Pollard Rho Factorization Method |
| o.Pollard p-1 Factorization Method |
| p.Wheel Factorization Method |
| |



1. 1.Code Documentation

1. a.Running the Program

The program was coded using Python 3.7, so it is recommended to run it using this version of Python. To run the program, you must have Python downloaded and installed.

Once you have Python installed, simply navigate to the directory with the code and use the py (or possibly python depending on your OS) command. For example, to run the affine cipher program, you would enter: py affine\_cipher.py and then the program will be run. None of the programs require command line input, although frequency\_calc.py can optionally take input from the command line.

1. b.Function Documentation

The documentation for each of the functions can be found in the program files themselves. I have written Pydocs for each of the functions in each of the files. The programs are split into separate files which must be run individually. The functionality of each file is self-explanatory based on the name (though you can read the code and documentation if you need more clarity).

1. 2.Algorithm Descriptions

1. a.Affine Cipher

An affine cipher is a basic cipher using multiplication and a shift to encrypt messages. It uses the following formula to encrypt a message:

Where  is the value of a letter of the plaintext,  is the corresponding ciphertext letter value, and  and  are the keys. The formula is evaluated mod 26 if you are using only letters.

An example of the cipher is as follows. Plaintext = &quot;hello&quot;, alpha = 3, beta = 11. If a =0, b = 1, and so on, then h = 7. So, to encrypt h, we would calculate the following:

The value 6 corresponds to the letter g, so h encrypts to g. Performing the same operation with the rest of the letters yields a ciphertext of gxssb. To decrypt, you must calculate the inverse of alpha (described in the mod inverse section) then use the formula:

In this case,  so  which is the value for h. It is important to not your alpha must be coprime with your mod for decryption to work properly. If you are using mod 26, then the following alpha values are acceptable:  1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

1. b.Vigenère Cipher

The Vigenère cipher is another relatively basic cipher system. This system requires a key word. For example, let&#39;s use the word &quot;lies&quot; for our key. This key is then placed in line with the plaintext and repeated as many times as needed to match the length of the plaintext. This is shown below (plaintext is &quot;schooliscool&quot;):

                                s c h o o l i s c o o l

                                l i e s l i e s l i e s

In this case, the key lined up nicely, but if it doesn&#39;t the key can simply be cut off at the end of the plaintext. To encrypt, simply add the values of each vertical pair of letters to receive the corresponding ciphertext. In this case, this leads to the ciphertext of: &quot;dklgztmknwsd&quot;.

In order to decrypt, the exact same procedure is performed except you subtract the key from the ciphertext, rather than add. This will yield the original plaintext.

1. c.Frequency Calculation

This algorithm is pretty straightforward. There&#39;s really not much of an algorithm to it at all. The program that I wrote simply reads in a file, iterates through it, and counts the number of occurrences of each character in the file.

In terms of how it is implemented more specifically, I perform the following steps. I iterate through the file, character-by-character, and check each character against the keys a Python dictionary. If the character already exists in the dictionary, I increment the corresponding value by one. If the character is not yet in the dictionary, I add it as a key and set the corresponding value to one. In this way, it only has a count for characters which appear in a text. (i.e. if a text has no letter b&#39;s in it, then b is never stored in the dictionary, rather than storing it with a value of 0).

1. d.Affine Cipher Attack

The most effective affine cipher attack is a known plaintext attack. This attack works most of the time as long as you have at least two letters of the plaintext and the corresponding letters of the ciphertext. Using these values, you can create a system of equations to attempt to solve for alpha and beta. For example, suppose you have the plaintext &quot;if&quot; corresponding to ciphertext &quot;pq&quot;. This means &quot;i&quot; produces &quot;p&quot; and &quot;f&quot; produces &quot;q&quot;. Using this information, you can create the following two equations:

By subtracting these two equations, you obtain the following result:

Thus, we have found that alpha equals 17.

If alpha had been equal to multiple values, then we would simply pick the value that is a valid alpha value (it must be coprime with the mod). In this instance, we only got 17, which is a valid value of alpha. All we need to do to find beta is to plug alpha back in to one of the equations above.

So, we have discovered that the key values for this affine cipher are alpha = 17 and beta = 9.

1. e.Vigenère Cipher Attack

The first step of a Vigenère cipher attack is to determine the key length. This can be decently accurately guessed using the following method. Take the ciphertext string and copy it. Shift the copied string once to the right and compare the two strings with each other (the original and the shifted ciphertexts). If our ciphertext is &quot;hghhg&quot; then the result should look like this:

                                        h g h h g

                                         h g h h g

                                             \*

You can see that there is one column where both characters match, marked with the asterisk. In this case, we have one such occurrence. We then shift the copied ciphertext string to the right once more and count the occurrences again. We repeat this procedure until the strings can no longer be compared. Here are the results of each shift:

| Shift | Occurrences |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 0 |

As you can see, the greatest number of occurrences happen at shift 3. Therefore, the key length is most likely three.

Now that we&#39;ve determined the key length, we can determine the key itself. The following is the method which I have used in my code.

First, take the ciphertext and trim it down to only contain every n

# th
 character, where n is the key length. In the example used above, that means we would look at only the 1
# st
, 4
# th
, 7
# th
, etc. characters. We count the frequencies of all 26 letters and store the results in a list. In the example above, that sums up to only two h&#39;s.

We then divide each value by the total number of letters counted. In this case just the two h&#39;s, so have the following result:

Typically, you will end with an array with many fractions in it, but the procedure remains the same. Now, you will need one more list, which contains the frequencies of English letters:

You must now compute freqDivided \* engFreq (dot product) 26 times. Each time it is computed, rotate engFreq once to the right. Keep track of which iteration each dot product is on. The iteration of the largest dot product correlates to the value of the character of the key. For instance, if the largest dot product is the fifth one, then the value of one of the key characters would be 5, which would correlate to &quot;f&quot;.

When you calculate this result for the first iteration of character frequencies (as in the 1

# st
, 4
# th
, etc. characters of the ciphertext), then the determined key character would be the first character of the key. This entire process is repeated through the entire the length of the key (in this case, the second iteration would be 2
# nd
, 5
# th
, etc. characters; this would yield the second character of the key). Thus, this process will yield the key. Feel free to play around with the code to help understand the process a bit better.

1. f.Linear Feedback Shift Register Sequence

An LFSR sequence is a method to generate a key using a basic recurrence relation. For example, we can use the following recurrence relation:

We will also need some initial values for the recurrence relation (specifically, we&#39;ll need three because that is the largest variable shift in the recurrence relation – from ):

Given these initial values and recurrence relation, we can generate any length key we want. Say we want a key to encrypt the plaintext:

We&#39;ll need a key of length three to encrypt this with an LFSR sequence. So, we&#39;ll generate the key using the following recurrence relation. The way it works is simple. The relation above essentially states the following:

So, from our initial values, the 4

# th
 bit would be equal to the 3
# rd
 bit (1) plus the 1
# st
 bit (0), which equals 1. In this way we can expand the key to match the length of the plaintext as follows:

Then, to encrypt the plaintext, we simply add the key to the plaintext bit-by-bit:

Thus, the ciphertext is 1101111. Decryption uses the exact same method, where adding the ciphertext to the key yields the plaintext.

1. g.GCD (Greatest Common Denominator)

To calculate the GCD of two numbers, you can use the simple Euclidean algorithm. To calculate the GCD you would use the following steps which follow this simple rule:

With an equation on the form of:

Example: gcd(27, 33):

This means gcd(27, 33) = 3 because 3 is the first divisor that perfectly divides its dividend.

1. h.Extended GCD

This is simply an extended version of the GCD above. It gives you solutions to the values x and y from the following equation (correlating to gcd(a, b) = d):

To compute extendedGCD(27, 33), we start with the same steps from above:

But rather than continuing to the final step, we rearrange the first two equations to solve for the remainder:

Then, we will replace the 6 in the second equation with the first equation:

Thus, we have found the values x and y. That is, x = -4 and y = 5.

1. i.Find Mod Inverse

Now that you know how to perform the extended GCD (assuming you&#39;ve read the previous section), finding the mod inverse is very easy. The extended GCD finds solutions to the equation:  where . Suppose you want to find the inverse of a number, n, under mod m. All you need to do is calculate extendedGCD(n, m) and the value of x will be the inverse of n under mod m.

1. j.Verify Primitive Roots

Another simple algorithm here. A primitive root is any number whose powers will generate all numbers under a mod. For example, 3 is a primitive root under mod 7 because

As you can see, the powers of 3 generate all numbers under mod 7. Therefore, 3 is a primitive root under mod 7.

A test to see if an integer can easily be performed by simply iterating through the powers of a number and ensuring that no numbers are missed under a given mod.

1. k.Miller-Rabin Primality Test

The Miller-Rabin test can determine if a number is prime relatively quickly with a relatively high level of certainty. If given a number, n, then the Miller-Rabin method goes as follows.

Find the largest power of 2, 2

# S
, that divides n-1 where  for some odd m. Compute . If  then n is probably prime. Otherwise, compute the following:

Repeat this process until you either find some  or you reach . If any b equals 1, then n is composite. If any b equals -1, then n is probably prime. If you reach  and it is equal to -1, then n is prime, otherwise it is composite.

1. l.Generate Random Prime

I performed this in a very simple way. I simply used the built-in Python random library to generate random numbers. Then, I used the Miller-Rabin primality test to determine if the number was a prime. If it was not, I&#39;d simply regenerate a number and test it, continuing until I found a prime number.

1. m.Fermat&#39;s Factorization Method

Fermat&#39;s factorization is built off the idea that an odd integer n can be represented as

If you rewrite the equation, you get:

The method essentially just tries values for a, in hopes that we find a square. Then, one factor of n would be .

1. n.Pollard Rho Factorization Method

This algorithm uses a polynomial (often ) to generate a pseudo-random sequence of numbers. You set  and . It works out that if               (where n is the number you wish to factorize), then you have found a factor of n. If it is equal to 1, then you can continue to loop the algorithm. If it is not equal 1, but is also equal to n, then the algorithm has failed and you must try again with new starting values for a and b or with a new polynomial.

1. o.Pollard p-1 Factorization Method

This algorithm stems off Fermat&#39;s little theorem that . The algorithm works as follows. Let , choose some bound B. Compute . Then, we set  and compute . If , then d is a factor of n, otherwise, we continue repeating the above algorithm.

1. p.Wheel Factorization Method

The wheel factorization method is an improvement upon the trial division method. In this algorithm, you start with a small list of numbers, for example [2, 3, 5]. You test n against this list of numbers, then you generate a new list of numbers that extends your first list. This list of numbers will contain only numbers that are coprime with each of the number previously in the list. Then, n is tested against those number as well. And the process is repeated until a factor of n is found.

In the case of an initial list of [2, 3, 5], the next list generated would be [7, 11, 13, 17, 19, 23, 29, 31], which are each coprime with 2, 3, and 5. In this way, the number of divisions required is reduced compared to the trial division method.