import os
import json
import csv

data_dir = "test_task"
headers_flag = True

csv_file = open('logs.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

for filename in os.listdir(data_dir):
    if (filename[-4:] == "json"):
        path_json = data_dir +'/'+filename
        data = open(path_json, encoding='utf-8')
        data_json = json.load(data)

        if (headers_flag == True):
            csv_writer.writerow((['room_number', 'qr', 'measured_temp', 'issue_heating', 'issue_motion', 'issue_temperature_sensor', 'issue_door', 'issue_window', 'issue_heating_switch', 'issue_kitchen_switch', 'issue_wifi', 'problem_description', 'solution', 'short_uuid', 'mac_address', 'timestamp', 'last_motion_time', 'last_motion_state', 'voltage_state', 'temp', 'broker_connection']))
            headers_flag = False

        csv_writer.writerow(data_json.values())
        data.close()