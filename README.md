# string-calculator-kata
A mutation testing exercise based on the String Calculator Kata by Roy Osherove.

The code has already been written for you but we still have to kill the mutants!

The String Calculator Kata is:

---
1. int Add(string numbers)

- The method can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.
(for an empty string it will return 0) 
Hints:

 - Start with the simplest test case of an empty string and move to one and two numbers
 - Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
 - Remember to refactor after each passing test
---
2. Allow the Add method to handle an unknown amount of numbers

- Allow the Add method to handle new lines between numbers (instead of commas).
the following input is ok: “1\n2,3” (will equal 6)
the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
---
3. Support different delimiters

- To change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
---
4. Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. 

- if there are multiple negatives, show all of them in the exception message.
---
5. Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
---
6. Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6
---

## Continue in your language

-   [Python](python/README.md)
