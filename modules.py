from vars import *
import requests
import json
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import time
import subprocess
import datetime


def get_available_algo(url, params):
    try:
        algo_request = requests.get(url, params=params)
        algo_request_status = int(algo_request.status_code)
        if 200 == algo_request_status:
            results = json.loads(algo_request.text)
            available_algo = results['result']['current']
            available_algo_list = []
            for i in available_algo:
                available_algo_list.append(i['algo'])
            return available_algo_list
    except:
        pass

search_available_algo = get_available_algo(api_end_point, algo_parms)
def get_available_workers(url, params):
    workers = False
    if search_available_algo:
        # Check 2 times
        for z in range(1, 3):
            print("Check # {} at : {}".format(z, datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
            for algo in search_available_algo:
                params['algo'] = str(algo)
                try:
                    worker_request = requests.get(url, params=params)
                    worekr_request_status = int(worker_request.status_code)
                    if 200 == worekr_request_status:
                        results = json.loads(worker_request.text)
                        if len(results['result']['workers']):
                            workers = True
                except:
                    pass
            # Check again after 60 seconds to make sure the API is honest
            time.sleep(60)
        return workers


def send_mail(email_message_content):
    if wanna_send_email == 1:

        text_subtype = 'plain'
        try:
            msg = MIMEText(email_message_content, text_subtype)
            msg['Subject'] = email_message_subject
            msg['From'] = "NiceHash Monitor {}".format(sender)
            msg['To'] = destination[0]
            conn = SMTP_SSL(SMTPserver_SSL)
            conn.set_debuglevel(False)
            conn.login(USERNAME, PASSWORD)
            conn.sendmail(sender, destination, msg.as_string())
            conn.close()
        except EOFError:
            print("mail failed")

    else:
        pass


def send_telegram_message(url, params):
    if wanna_send_telegram == 1:
        try:
            telegram_request = requests.get(url, params=params)
        except:
            pass
    else:
        pass


def start_monitor(monitor_type):
    if monitor_type == "miner_end":
        print("Monitor will start in : {} seconds".format(check_interval_seconds))
        # Give it a while until windows boots everything
        time.sleep(check_interval_seconds)
        print("Start Monitoring.. - {}".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))

        while True:
            if not get_available_workers(api_end_point, worker_parms):
                print("Not Running - {}".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
                send_mail(email_miner_message_content)
                send_telegram_message(telegram_api_end_point, telegram_miner_params)
                if restart_miner_device_if_worker_down:
                    subprocess.call(["shutdown", "/r", "/f", "/t", "0"])
            else:
                print("Running - {}".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
                print("Next check interval {} seconds".format(check_interval_seconds))
                time.sleep(check_interval_seconds)
    elif monitor_type == "server_end":
        print("Start Monitoring.. - ".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
        while True:
            if not get_available_workers(api_end_point, worker_parms):
                print("Not Running - {}".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
                send_mail(email_server_message_content)
                send_telegram_message(telegram_api_end_point, telegram_server_params)
            else:
                print("Running - {}".format(datetime.datetime.now().strftime("%I:%M%p - %B %d, %Y")))
            print("Next check interval {} seconds".format(check_interval_seconds))
            time.sleep(check_interval_seconds)
    else:
        print("Selection not found")
