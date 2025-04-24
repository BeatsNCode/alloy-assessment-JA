# Alloy Tech Assessment

## BACKGROUND
You’ve been tasked as the tech lead at a bank to build out the integration with Alloy’s
API in order to minimize fraudulent applications from getting approved and cutting down
on any manual reviews from the compliance team.

## TASK
What better way to learn more about our API than to build a working integration with
Alloy? We’ll provide everything you need on the Alloy side to get this working -
instructions, API docs and credentials - and all you need to do is build a simple script
that interacts with an API, processes its response, and makes a decision based on
predefined rules. Don’t worry: You’ll be using sandbox mode, so everything will be
simulated.

## INSTRUCTIONS
1. Watch our demo video to get acquainted with the basics of how Alloy works. You
won’t need access to the Alloy dashboard to write your script, since the API
response will provide everything you need - but this should provide helpful
context for what happens when you submit your API call to Alloy

2. Using a language of your choice, write a script that:
  a. Collects applicant details (these can be hardcoded into your script or done via a simple console input)
  b. Submits the details to Alloy’s sandbox API
c. Processes the API response and prints an appropriate message

3. Collect the following applicant details:
a. First Name
b. Last Name
c. Date of Birth (ISO-8601 format: YYYY-MM-DD)
d. SSN (9 digits, no dashes)
e. Email Address (valid format)
f. Address
  i. Line 1
  ii. Line 2
  iii. City
  iv. State (must be a two-letter code, ex. NY, CA, etc.)
  v. Zip/Postal Code
  vi. Country (must be “US” for sake of this assignment)

4. Submit to our API
a. Send the above details as a JSON payload via an HTTP POST request.
b. Process the API Response
i. If the response is `{"summary": {"outcome": "Approved"}}`
```
→ Print: "Congratulations! You are approved."
```
ii. If the response is `{"summary": {"outcome": "Manual
Review"}}` 
```
→ Print: "Your application is under review. Please wait
for further updates."
```
iii. If the response is `{"summary": {"outcome": "Deny"}}`
```
→ Print: "Unfortunately, we cannot approve your application at this
time."
```

6. Refer to our API documentation to see how to submit the applicant’s details to
Alloy:
  a. To get the exact format of the required fields (ex. name_first, name_last, etc.), you can utilize the GET endpoint
  b. For submitting the evaluation, you’ll utilize the POST endpoint
7. For authentication, we will provide a token and secret via secure email. We
recommend using Basic authentication for this assignment
8. Our API provides informative error handling, so any errors you receive should
help you to identify the problem with the integration, but please reach out if you
have questions or get stuck
9. By default, in Sandbox mode, a successful API request will return a response
including the JSON {"summary":{"outcome":"Approved"}}
10. To fully complete the assignment, use a test method we refer to as Sandbox

### Personas to coerce a different response from the API
a. Submitting an application with the last name Review (so you’d submit an
applicant with the name Jessica Review) will result in an “outcome” of
“Manual Review”, and the last name Deny will result in an “outcome” of
“Deny”.
