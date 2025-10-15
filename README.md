
<!-- QUESTION ONE
Write a function that returns the second-largest number in a given list of integers. -->

![Q1](/screenshots/Q1.png)
Convert the list to a set to remove duplicates.

Sort in descending order.

Return the second element.

<!-- QUESTION TWO
Explain how you would optimize a page that loads too slowly. Mention at least three causes and how you’d fix each. -->

Cause	                                Fix
Large image sizes                Compress and use optimized formats (WebP, lazy loading).
Too many HTTP requests           Combine files (CSS/JS bundling), use CDN, caching.
Unoptimized JavaScript           Minify scripts, defer non-critical JS, use async loading.



<!--QUESTION THREE: You are creating a simple profile page that fetches user data from an API (https://jsonplaceholder.typicode.com/users/1).
Explain or show code for:
Fetching and displaying the user’s name and email.
Handling the loading and error states. -->


print("Loading...") shows that data is being fetched.

requests.get() → sends a GET request to the API.

.json() → converts the response to a Python dictionary.

try...except → handles network or request errors.


<!-- QUESTION FOUR:  A small store wants to calculate total sales from this dataset:
[
  {"item": "Pen", "price": 20, "quantity": 3},
  {"item": "Book", "price": 200, "quantity": 2},
  {"item": "Bag", "price": 800, "quantity": 1}
]

Write a short function to calculate the total revenue -->

![Q4](/screenshots/Q4.png)


Loops through each item and multiply price by quantity.
sum() aggregates the total revenue efficiently.


<!-- QUESTION FIVE:You’ve been given this code snippet:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers) -->

 <!-- 1. What’s wrong? -->
The code incorrectly removes items using index values, not the actual numbers. This causes unexpected behavior.

<!-- 2. What will it output? -->
![Q5 a](/screenshots/Q5%20a.png)
Output of original code

<!-- 3. Corrected version: -->
To remove even numbers correctly,that is print only non-even numbers

![Q5 b](/screenshots/Q5%20b.png)

Using list comprehension avoids modifying a list while iterating, which prevents skipping elements.
Filters out even numbers correctly.


<!--QUESTION SIX: Explain how you would use Git to collaborate on a team project with other developers.
 Mention at least: -->

<!-- One common Git command you use often. -->
git add .  stages all changes.

git commit -m records a snapshot with a message.

git push uploads changes to the remote repository for team access.

<!-- One problem you’ve faced while using Git and how you solved it. -->
Problem: Merge conflicts occur when two developers modify the same file.

Solution: Pull latest changes (git pull), resolve conflicts manually,
 and then commit the resolved file before pushing.
