What is match statement?
-----

Before discussing this new feature in python 3.10, we will first see what is switch statement
in other language.

In the first example `switch_in_c` in C lang, the switch takes the particular value and
matches with the **exact value** defined in case expression.
Depending on the language we either have implicit continuation or explicet continuation.
In C, we have implicit conitnuation meaning that if we don't have the break statement
inside the case statement then it will execute all the case statement following it.

For long time python does not have any similar feature close to switch.
So in python 3.10, the new feature was introduced called `match`.
It is similar to the switch statement but not exactly same.
