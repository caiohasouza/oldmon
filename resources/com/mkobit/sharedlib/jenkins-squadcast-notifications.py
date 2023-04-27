##!/usr/bin/env python3
#import os
#import json
#import requests
#import sys
#
#def form_payload(build_number, job_name, build_url, status, job_status, priority):
#    """Forms the python representation of the data payload to be sent from the passed configuration"""
#    message = "Job {} (#{}) - {}".format(job_name, build_number, job_status)
#    description = "Job: {}\nBuild Number: {}\nStatus: {}. \nBuild URL: {}".format(job_name, build_number, job_status, build_url)
#    payload_rep = {"message" : message , "description" : description,
#        "build_url":  build_url, "job_name":  job_name, "build_number":  build_number,
#        "status" : status, "event_id" : job_name, "priority": priority}
#    return payload_rep
#
#def post_to_url(url, payload):  
#    """Posts the formed payload as json to the passed url"""
#    try:
#        headers={
#        'User-Agent': 'squadcast',
#        "Content-Type": "application/json"
#        }
#        req = requests.post(url, data = bytes(json.dumps(payload).encode('utf-8')), headers = headers)
#        if req.status_code > 299:
#            print("Request failed with status code %s : %s" % (req.status_code, req.content))
#    except requests.exceptions.RequestException as e:
#            print("Unable to create an incident with Squadcast, ", e)
#            sys.exit(2)
#
#if __name__ == "__main__":
#    squadcast_url = os.environ['SQUADCAST_URL']
#    build_number = int(os.environ['BUILD_NUMBER'])
#    job_name = os.environ['JOB_NAME']
#    build_url = os.environ['BUILD_URL']
#    job_url = os.environ['JOB_URL']
#    #job_status = os.environ['CURRENT_BUILD_RESULT']
#    #job_status_previous = os.environ['PREVIOUS_BUILD_RESULT']
#    job_status = os.environ['BUILD_STATUS']
#    priority = os.environ.get('PRIORITY', "P3")
#
#    if (job_status == "FAILURE") or (job_status == "UNSTABLE") or (job_status == "ABORTED"):
#        post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "trigger", job_status, priority))
#    elif (job_status == "SUCCESS"):
#        post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "resolve", job_status, priority))
#    #if (job_status_previous == "SUCCESS") and ((job_status == "UNSTABLE") or (job_status == "ABORTED") or (job_status == "FAILURE")):
#    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "trigger", job_status, priority))
#    #    print ("Creating an incident in Squadcast!")
#    #elif ((job_status_previous == "UNSTABLE") or (job_status_previous == "ABORTED") or (job_status_previous == "FAILURE")) and (job_status == "SUCCESS"):
#    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "resolve", job_status, priority))
#    #    print ("Resolving an incident in Squadcast!")
#    #if ((job_status_previous == "UNSTABLE") or (job_status_previous == "ABORTED") or (job_status_previous == "FAILURE")) and (job_status == "SUCCESS"):
#    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "resolve", job_status, priority))
#    #    print ("Resolving an incident in Squadcast!")
#    #else:
#    ##    print ("Not required to create an incident..")
#    #    post_to_url(squadcast_url, form_payload(str(build_number), job_name, build_url, "trigger", job_status, priority))
#    #    print ("Creating an incident in Squadcast!")
#!/usr/bin/env python
print("Hello")