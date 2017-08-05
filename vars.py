# API Vars
btc_addr = ''  # CHANGE ME - Get it from nicehash
fetch_algo_method = 'stats.provider.ex'
fetch_worker_method = 'stats.provider.workers'
api_end_point = 'https://api.nicehash.com/api'
algo_parms = {'method': fetch_algo_method, 'addr': btc_addr}
worker_parms = {'method': fetch_worker_method, 'addr': btc_addr}

# Telegram Notifications
wanna_send_telegram = 1  # CHANGE ME - 1 to enable and 0 to disable
telegram_token_key = ''  # CHANGE ME - Get it from Telegram
telegram_api_end_point = "https://api.telegram.org/bot{}/sendMessage".format(telegram_token_key)
telegram_miner_message_content = "Nicehash worker is down but windows is running.. Restarting windows if enabled."
telegram_chat_id = ''  # CHANGE ME - Get it from Telegram
telegram_miner_params = {'chat_id': telegram_chat_id, 'text': telegram_miner_message_content}
telegram_server_message_content = "Nicehash worker is down!"
telegram_server_params = {'chat_id': telegram_chat_id, 'text': telegram_server_message_content}

# Email Notifications
wanna_send_email = 1  # 1 to enable and 0 to disable
SMTPserver_SSL = 'HOSTNAMEorIP:465'  # CHANGE ME - SMTP server in the following format : IPorHostname:465
sender = ''  # CHANGE ME - SMTP Username
destination = ['acct1@domain.tld', 'acct2@domain.tld']  # CHANGE ME - Receiver address or addresses by a comma separated
USERNAME = ""  # CHANGE ME - SMTP Username
PASSWORD = ""  # CHANGE ME - SMTP Password
email_message_subject = "Mining Monitor"
email_server_message_content = telegram_server_message_content
email_miner_message_content = telegram_miner_message_content

# Tuning
check_interval_seconds = 600  # Time to wait before starting monitor, # useful for local monitor to give windows time to run miners

# Core
monitor_type = "server_end"  # "server_end" for remote monitor and "miner_end" for monitoring on mining device
restart_miner_device_if_worker_down = 1  # 1 to enable and 0 to disable
