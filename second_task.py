class ContactList(list):

    def __init__(self, list1 = list) -> None:
        self.list1 = list1

    def search_by_name(self, name):
        self.name = name
        list2 = []
        for i in self.list1:
            if self.name in i:
                list2.append(i)
        return list2
    
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya')) 
            