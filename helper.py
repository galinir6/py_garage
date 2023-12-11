import json

def save_list(data_file , cars):
     json_string = json.dumps(cars)
     with open(data_file, 'w') as file:
      file.write(json_string)


def load_list(data_file , cars):
    try: 
        with open(data_file, 'r') as file:
         json_string = file.read()
         cars = json.loads(json_string)
         return cars
    except: pass