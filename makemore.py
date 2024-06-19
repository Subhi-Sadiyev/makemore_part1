import matplotlib_inline as mplt
import torch

### loading dataset

words = open('names.txt', 'r').read().splitlines() 

#print(words[:10])

#print(max(len(w) for w in words))


### manualy sorting through characters and 
###creating start(S) and end(E) identifiers for starting or ending characters

#b = {}
#for w in words:
#    chs = ['<S>'] + list(w) + ['<E>']
#    for ch1, ch2 in zip(chs, chs[1:]):
#        bigram = (ch1, ch2)
#        b[bigram] = b.get(bigram, 0) + 1
#        #print(ch1, ch2)


#print(sorted(b.items(), key = lambda kv: -kv[1]))


### putting word occurence frequency dictionary into 2D arrays

N = torch.zeros((28,28), dtype=torch.int32)

chars = sorted(list(set(''.join(words))))
stoi = {s:i for i,s in enumerate(chars)}

stoi['<S>'] = 26
stoi['<E>'] = 27


for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

mplt.imshow(N)

