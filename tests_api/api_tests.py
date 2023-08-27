import requests

head = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
root = "http://petstore.swagger.io/v2/"


def test_create_and_fetch_user_part1():
    # Create a user with hardcoded values
    create_response = create_default_user()
    print(f"\n *Results from create user")
    print(create_response.status_code)
    print(create_response.json())  # Sometimes it returns 405 error code, can't figure out why

    # Get the user with hardcoded values
    get_response = get_user(username="Miquel")
    print(f"\n *Results from get user")
    print(f"Status Code: {get_response.status_code}")
    print(f"Text: {get_response.json()}")


def test_find_by_status_part2_part3():
    # Fetch objects by status "sold"
    status = "sold"
    find_by_status_response = find_by_status(status)
    print(f"\n *Results from findByStatus {status}")
    print(f"Status Code: {find_by_status_response.status_code}")
    print(f"Text: {find_by_status_response.json()}")

    # From response, sort an array of Tuples that contains "id", "name"
    print(f"\n *Array of Tuples with id and name: \n {get_id_and_name_tuples(find_by_status_response.json())}")

    # From response, create an object called animal_list and
    # user internal class method to return the names and how many times are used
    animal_list = ObjectDataset(find_by_status_response.json())
    print(f"\n *Array of names and times repeated in the dataset: \n {animal_list.count_name_occurrences()}")


# region "Part 1 and 2"
def create_default_user():
    """
    creates a new user with hardcoded values
    :return: response from the post call
    """
    user = {
        "id": 6000,
        "username": "Miquel",
        "firstName": "Vidal",
        "lastName": "Bieto",
        "email": "mvbieto@hotmail.com",
        "password": "test20",
        "phone": "0000",
        "userStatus": 10
    }

    response = requests.post(f"{root}user", headers=head, json=user)
    return response


def get_user(username):
    """
    gets a hardcoded user
    :param username: "Miquel" string base
    :return: response
    """
    response = requests.get(f"{root}user/{username}", headers=head)
    return response


def find_by_status(status):
    """
    Gets the list of objects by status
    :param status: For this case, it has to be "sold"
    :return: response
    """
    response = requests.get(f"{root}pet/findByStatus?status={status}", headers=head)
    return response


def get_id_and_name_tuples(object_list):
    """
    From the response of Find By Status, sort and return id and name of the sold items
    :param object_list: response.json from find_by_status call
    :return: It returns an array of tuples with id and name
    """
    id_name_tuples = []
    for obj in object_list:
        if "id" in obj and "name" in obj:
            id_name_tuples.append((obj["id"], obj["name"]))
    return id_name_tuples


# endregion


# region "Part 3"
class ObjectDataset:
    def __init__(self, data_list):
        """
        Constructor of ObjectDataset
        :param data_list: response list of objects from findByStatus
        """
        self.objects = data_list

    def get_objects(self):
        return self.objects

    def get_object_names(self):
        names = []
        for obj in self.objects:
            if "name" in obj:
                names.append(obj["name"])
        return names

    def get_object_by_id(self, target_id):
        for obj in self.objects:
            if "id" in obj and obj["id"] == target_id:
                return obj
        return None

    def count_name_occurrences(self):
        name_count = {}
        for obj in self.objects:
            if "name" in obj:
                name = obj["name"]
                name_count[name] = name_count.get(name, 0) + 1
        return name_count
# endregion
