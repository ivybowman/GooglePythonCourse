#! /usr/bin/env python3
import os
import requests

# Setup
feedback_dir = 'feedback'
os.chdir(feedback_dir)
files = os.listdir()
url = 'http://192.168.1.241:8080/feedback'


def process_feedback():
    all_feedback = []
    for file in files:
        with open(file, 'r') as f:
            feedback = f.readlines()
            all_feedback.append({
                'title': feedback[0].strip(),
                'name': feedback[1].strip(),
                'date': feedback[2].strip(),
                'feedback': feedback[3].strip()
            })
    return all_feedback


def send_feedback(data):
    for x in data:
        r = requests.post(url, json=x)
        print(r.status_code)


if __name__ == "__main__":
    output = process_feedback()
    send_feedback(output)





