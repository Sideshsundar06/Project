def kmers(read,k):
    a = 0
    count = {}
    num_kmers = len(read) - k + 1
    for i in range(num_kmers):
        kmer = read[i:i+k]
        if kmer not in count:
            count[kmer] = 0
        count[kmer]+=1
        a=a+1
    print()
    print("No. of " , k ,"-mers ", a)
    l = list(count.keys())
    m = max(count.values())
    print()
    print(l)
    print("The most frequent ", k ,"-mers: ")
    if m == 1:
        print("No common kmers.")
    else:
        if count.get(l[i]) == a:
            print(l[i])
    return count

kmers("ATCTTCGAATGCTAGC",3)    
kmers("ATCTTCGAATGCTAGC",5)
kmers("ATTCGATTCATTTCGC",3)
kmers("ATTCGATTCATTTCGC",5)    
        