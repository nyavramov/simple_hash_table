import mmh3 

class Hash_Table:

    def __init__(self, table_size):

        self.table_size = table_size
        self.hash_table = [[] for i in range(table_size)]

    # Generate an index for the provided name using murmurhash3
    def get_table_index(self, name):

        return mmh3.hash128(name, signed = False) % self.table_size

    def insert_into_table(self, name, phone_number):

        index = self.get_table_index(name)

        # Check to see if the name, phone number have already been hashed into the table
        for entry in self.hash_table[index]:
            if entry.name == name and entry.phone_number == phone_number:
                print("Item is already in the database!")
                return

        # If the name, phone number has not yet been hashed
        new_entry = Table_Entry()
        new_entry.name = name
        new_entry.phone_number = phone_number

        self.hash_table[index].append(new_entry)

    # Given an input name, retrieve the matching phone number/s
    def get_phone_number(self, name):
        
        entries = self.hash_table[self.get_table_index(name)]

        # If we cannot locate a entry at the index we're looking at
        if len(entries) == 0:
            print("No person found with that name!")
            return None

        # If we have multiple entries for the index we're looking at, handle them using the principle of chaining
        elif len(entries) > 1:
            list_of_matching_names = []

            # If we have multiple items in our bucket, search them to see if there are 2 
            # or more identical names
            for entry in entries:
                if entry.name == name:
                    list_of_matching_names.append(entry)

            # If we have only one item in our matches, print it. Else, report multiple matches 
            # and print them all then return
            if len(list_of_matching_names) == 1:
                print(f"{list_of_matching_names[0].name}: {list_of_matching_names[0].phone_number}")
            elif len(list_of_matching_names) == 0:
                print("No person found with that name!")
            else:
                print("Multiple people found with that name: ")
                [print(f"{item.name}: {item.phone_number}") for item in list_of_matching_names]

            return entries

        # If we have only one match, print it out and return it
        else:
            if entries[0].name == name:
                print(f"{entries[0].name}: {entries[0].phone_number}")
                return entries
            else:
                print("No person found with that name!")
                return None

class Table_Entry:

    def __init__(self):
        self.name = None
        self.phone_number = None

def main():

    expected_entries = 3 # How many people we expect our hash table to store
    load_factor      = 1 # Ratio of the size of table to number of entries
    table_size       = load_factor * expected_entries

    hash_table = Hash_Table(table_size)

    hash_table.insert_into_table("Paul White", "201-887-1232")
    hash_table.insert_into_table("Jake Blue", "241-887-1219")
    hash_table.insert_into_table("Kate Green", "232-392-3289") 
    hash_table.insert_into_table("Jake Blue", "314-671-8492")  

    while True:
        print("Type a person's name to search for their phone number in the hash table or press enter to exit: ", end="")
        query = input()

        if query == "":
            break

        hash_table.get_phone_number(query)

if __name__ == '__main__':
    main()