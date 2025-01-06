#def main():
    #with open("books/frankenstein.txt") as f:
       # book_text=f.read()

    #print (book_text)

#main()



letter_count = []



def countText():
    with open("books/frankenstein.txt") as f:
        book_text=f.read()

    words=book_text.split()
    wordTotal=len(words)

    a = 0
    b =0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    letp = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0 
    
    lowerCase= book_text.lower()
        
    for case in lowerCase:
        letter_count.append(case)

    for let in letter_count:
        if let == 'a':
            a += 1
        if let == 'b':
            b += 1
        if let == 'c':
            c += 1
        if let == 'd':
            d += 1
        if let == 'e':
            e += 1
        if let == 'f':
            f += 1
        if let == 'g':
            g += 1
        if let == 'h':
            h += 1
        if let == 'i':
            i += 1
        if let == 'j':
            j += 1
        if let == 'k':
            k += 1
        if let == 'l':
            l += 1
        if let == 'm':
            m += 1
        if let == 'n':
            n += 1
        if let == 'o':
            o += 1
        if let == 'p':
            letp += 1
        if let == 'q':
            q += 1
        if let == 'r':
            r += 1
        if let == 's':
            s += 1
        if let == 't':
            t += 1
        if let == 'u':
            u += 1
        if let == 'v':
            v += 1
        if let == 'w':
            w += 1
        if let == 'x':
            x += 1
        if let == 'y':
            y+=1
        if let == 'z':
            z += 1
    letterTotals= {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h, 'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':letp, 'q':q, 'r':r, 's':s, 't':t, 'u':u, 'v':v, 'w':w, 'x':x, 'y':y, 'z':z} 
    letterTotalsList=list(letterTotals.items())

        #print(len(words))
        #print(lowerCase)
        #print(letter_count)
        #print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,letp,q,r,s,t,u,v,w,x,y,z)
    #print(type(letterTotals))
    #print(letterTotalsList)
    #return letterTotalsList

    def sortOn(letterTotalsList):
        return letterTotalsList[1]

    letterTotalsList.sort(reverse=True, key=sortOn)
    print(wordTotal," words found in the document")
    print("Total number of each letter found in document from highest occurance to lowest:",letterTotalsList)

countText()

#print(countText())





