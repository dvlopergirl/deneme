import yeni
def karsılastır(text):
    m=yeni.Dequeue()
    for x in text:
        m.add_rear(x)
    denge=True
    while m.size()>1 and denge:
        ilk=m.remove_front()
        son=m.remove_rear()
        ayni=[]
        farkli=[]
        if ilk!=son:
            farkli.append(ilk)
            farkli.append(son)
            print("farklı eleman sayısı:",len(farkli))
            denge=False
        elif ilk==son:
            ayni.append(ilk)
            ayni.append(son)
            print("aynı eleman sayısı:",len(ayni))
        return denge    
karsılastır("fatma")
        
        
