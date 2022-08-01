class HashTable(object):
    def __init__(self):
        self.table = dict()
        #alternatively a list/array can be used, where enough empty spaces are inserted beforehand, to let the has value be the index, example, if the hash value is 5000, 
        #then 5000 is the index of the list, if the list is created big enough
        #here dict is used to save memory space instaed

    def store(self, string):
        key = self.calculate_hash_value(string)
        if key != -1:
            self.table[key] = string

    def lookup(self, string):
        key = self.calculate_hash_value(string)
        if key in self.table.keys():
            return key
        return -1

    #using the s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1] function, with n being the length of the string
    def calculate_hash_value(self, string):
        if len(string) >= 2:
            a = ord(string[0])
            b = ord(string[1])
            return a*31 + b 
        return -1

