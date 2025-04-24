import requests
import json
import os
import base64
import argparse
from dotenv import load_dotenv

load_dotenv()

alloy_application_token = os.getenv('ALLOY_APPLICATION_TOKEN')
alloy_application_secret = os.getenv('ALLOY_APPLICATION_SECRET')

credentials = alloy_application_token + ":" + alloy_application_secret

encoded_credentials = base64.b64encode(credentials.encode('utf-8'))


def fetchOauthToken():
    url = "https://sandbox.alloy.co/v1/oauth/bearer"

    payload = {
        "grant_type": "client_credentials",
        "application_token": alloy_application_token,
        "application_secret": alloy_application_secret
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {encoded_credentials}'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    return response.text

oauth_response = json.loads(fetchOauthToken())
bearer_token = oauth_response['bearer_token']


def submitEvaluation(first_name, last_name, dob, ssn, email, address1, address2, city, state, zip, country):

    url = "https://sandbox.alloy.co/v1/evaluations"

    headers = {
        "accept": "application/json",
        'Authorization': f'Bearer {bearer_token}',
        "alloy-entity-type": "person",
        "content-type": "application/json"
    }

    payload = {
        "name_first": first_name,
        "name_last": last_name,
        "birth_date": dob,
        "document_ssn": ssn,
        "email_address": email,
        "address_line_1": address1,
        "address_line_2": address2,
        "address_city": city,
        "address_state": state,
        "address_postal_code": zip,
        "address_country_code": country
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    return response_json 
    

def main():
    parser = argparse.ArgumentParser(
        description="Submit an Alloy evaluation via the console"
    )
    parser.add_argument("first_name")
    parser.add_argument("last_name")
    parser.add_argument("dob", help="Birth date (YYYY-MM-DD)")
    parser.add_argument("ssn", help="SSN (e.g. 123-45-6789)")
    parser.add_argument("email")
    parser.add_argument("address1", help="Address line 1")
    parser.add_argument("--address2", default="", help="Address line 2")
    parser.add_argument("city")
    parser.add_argument("state")
    parser.add_argument("zip_code")
    parser.add_argument("country", help="Country code (e.g. US)")
    args = parser.parse_args()

    result = submitEvaluation(
        args.first_name, args.last_name, args.dob, args.ssn, args.email,
        args.address1, args.address2, args.city, args.state, args.zip_code, args.country
    )

    evaluationOutcome = result["summary"]["outcome"]
    if evaluationOutcome == "Approved":
        print("Congratulations! You are approved.")
    elif evaluationOutcome == "Manual Review":
        print("Your application is under review. Please wait for further updates.")
    elif evaluationOutcome == "Denied":
        print("Unfortunately, we cannot approve your application at this time.")

if __name__ == "__main__":
    main()