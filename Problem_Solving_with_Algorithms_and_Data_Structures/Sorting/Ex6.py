class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        count = 10
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                self.size += self.size
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                    if nextslot == hashvalue:
                        return
                    count += 1
            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace
        if count / self.size > 0.75:
            self.size += 11
            self.slots = [None] * self.size
            self.data = [None] * self.size

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                           not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __delitem__(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
                self.slots[position] = None

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True


    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __len__(self):
        return self.size 

    def __contains__(self, other):
        for i in self.data:
            if i == other:
                return True
                break
        return False




H = HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20] = 'duck'
H[21] = 'du2ck'
print(H[20])
print(H.data)
print(H[99])
print(len(H))
print('duck' in H)
print(H.data)
#del H[93]
print(H.slots)
H[111]="chisscken"
print(H.slots)
H[112]="chisscken"
print(H.slots)