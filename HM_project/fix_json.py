import json

class FixJson:
    def __init__(self, file: str):
        self.file = file

    def open_data(self) -> dict:
        try: 
            with open(self.file, 'r') as file: #open file
                return json.load(file)
        except:
            return {}

    def add_data(self, new_data: dict[str,str]) -> None:
        # get then add new data
        try:
            data = self.open_data()
            if data == None:
                data = {}
            data.update(new_data)
        except:
            data = self.open_data()
        with open(self.file, 'w') as file:
           json.dump(data, file, indent=2) # update file

    def delete_data(self, delete_key: str) -> None:

        # get then delete data
        data = self.open_data()
        if delete_key in data:
            del data[delete_key]

            # update file
            with open(self.file, 'w') as file:
                json.dump(data, file, indent=2)