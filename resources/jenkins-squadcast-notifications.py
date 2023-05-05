#!/usr/bin/env python3
import os
import json
import requests
import sys
import argparse

def form_payload(build_number, job_name, build_url, status, job_status, priority):
    """Forms the python representation of the data payload to be sent from the passed configuration"""
    message = "Job {} (#{}) - {}".format(job_name, build_number, job_status)
    description = "Job: {}\nBuild Number: {}\nStatus: {}. \nBuild URL: {}".format(job_name, build_number, job_status, build_url)
    payload_rep = {"message" : message , "description" : description,
        "build_url":  build_url, "job_name":  job_name, "build_number":  build_number,
        "status" : status, "event_id" : job_name, "priority": priority}
    print ("1")
    return payload_rep

def post_to_url(url, payload):  
    """Posts the formed payload as json to the passed url"""
    print ("2")
    try:
        headers={
        'User-Agent': 'squadcast',
        "Content-Type": "application/json"
        }
        req = requests.post(url, data = bytes(json.dumps(payload).encode('utf-8')), headers = headers)
        if req.status_code > 299:
            print("Request failed with status code %s : %s" % (req.status_code, req.content))
    except requests.exceptions.RequestException as e:
            print("Unable to create an incident with Squadcast, ", e)
            sys.exit(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Passing build information.')
    parser.add_argument('--url', help='Squadcast API endpoint', default=os.environ['SQUADCAST_URL'])
    parser.add_argument('--build-number', help='Jenkins Build Number'default=int(os.environ['BUILD_NUMBER']))
    parser.add_argument('--job-name', help='Jenkins Job Name'default=os.environ['JOB_NAME'])
    parser.add_argument('--build-url', help='Jenkins Build URL'default=os.environ['BUILD_URL'])
    parser.add_argument('--job-url', help='Jenkins Job URL'default=os.environ['JOB_URL'])
    parser.add_argument('--build-status', help='Jenkins Build Status'default=os.environ['BUILD_STATUS'])
    parser.add_argument('--priority', help='Squadcast Priority', default="P3")
    args = parser.parse_args()    
    #squadcast_url = os.environ['SQUADCAST_URL']
    #build_number = int(os.environ['BUILD_NUMBER'])
    #job_name = os.environ['JOB_NAME']
    #build_url = os.environ['BUILD_URL']
    #job_url = os.environ['JOB_URL']
    ##job_status = os.environ['CURRENT_BUILD_RESULT']
    ##job_status_previous = os.environ['PREVIOUS_BUILD_RESULT']
    #job_status = os.environ['BUILD_STATUS']
    #priority = os.environ.get('PRIORITY', "P3")
    #args.build-status = args.build_status

    #print (args.build_status)
    if (args.build_status == "FAILURE") or (args.build_status == "UNSTABLE") or (args.build_status == "ABORTED"):
        post_to_url(args.url, form_payload(str(args.build_number), args.job_name, args.build_url, "trigger", args.build_status, args.priority))
    elif (args.build_status == "SUCCESS"):
        post_to_url(args.url, form_payload(str(args.build_number), args.job_name, args.build_url, "resolve", args.build_status, args.priority))
    #if (job_status_previous == "SUCCESS") and ((job_status == "UNSTABLE") or (job_status == "ABORTED") or (job_status == "FAILURE")):
    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "trigger", job_status, priority))
    #    print ("Creating an incident in Squadcast!")
    #elif ((job_status_previous == "UNSTABLE") or (job_status_previous == "ABORTED") or (job_status_previous == "FAILURE")) and (job_status == "SUCCESS"):
    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "resolve", job_status, priority))
    #    print ("Resolving an incident in Squadcast!")
    #if ((job_status_previous == "UNSTABLE") or (job_status_previous == "ABORTED") or (job_status_previous == "FAILURE")) and (job_status == "SUCCESS"):
    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "resolve", job_status, priority))
    #    print ("Resolving an incident in Squadcast!")
    else:
        print ("Build status not found..")
    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "trigger", job_status, priority))
    #    print ("Creating an incident in Squadcast!")