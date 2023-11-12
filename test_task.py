import os
import json
import csv

data_dir = "test_task"
headers_flag = True

csv_file = open('logs.csv', 'w', newline='')
csv_order = ['room_number', 'qr', 'measured_temp', 'issue_heating', 'issue_motion', 'issue_temperature_sensor', 'issue_door', 'issue_window', 'issue_heating_switch', 'issue_kitchen_switch', 'issue_wifi', 'problem_description', 'solution', 'short_uuid', 'mac_address', 'timestamp', 'last_motion_time', 'last_motion_state', 'voltage_state', 'temp', 'broker_connection']
csv_writer = csv.DictWriter(csv_file, fieldnames=csv_order)
room_data = {}
duplicates = []
good = []


for i in range(2):
    for filename in os.listdir(data_dir):
        if (filename[-4:] == "json"):
            path_json = data_dir +'/'+filename
            data = open(path_json, encoding='utf-8')
            data_json = json.load(data)
            room_number = data_json.get("room_number")
            short_uuid = data_json.get("short_uuid")

            if (headers_flag == True):
                csv_writer.writeheader()
                headers_flag = False
            if (i == 0):
                if room_number:
                    if room_number in room_data:
                        room_data[room_number].append(data_json)
                    else:
                        room_data[room_number] = [data_json]
            if (i == 1):
                if not room_number:
                    for key, data_list in room_data.items():
                        for data in data_list:
                            if short_uuid == data['short_uuid']:
                                update_room = data['room_number']
                                room_data[update_room].append(data_json)
                                break

for key, data_list in room_data.items():
    if(len(data_list) == 1):
        if (data_list[0]['issue_heating'] == '' and data_list[0]['issue_motion'] == '' and data_list[0]['issue_temperature_sensor'] == '' and data_list[0]['issue_door'] == '' and data_list[0]['issue_window'] == ''and data_list[0]['issue_heating_switch'] == ''and data_list[0]['issue_kitchen_switch'] == ''and data_list[0]['issue_wifi'] == ''and data_list[0]['problem_description'] == ''):
            good.append(str(key))

    elif(len(data_list) > 1):
        duplicates.append(str(key))
    for data in data_list:
        csv_writer.writerow(data)

print("pokoje, w których jest parę logów i trzeba zweryfikować:")
print(duplicates)
print("---")
print("pokoje dobre - występuje jeden log i nie ma w nim opisanych żadnych problemów")
print(good)
