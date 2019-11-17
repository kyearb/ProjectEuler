import pdb

def triNum(num):
    return int(0.5*num*(num+1))

def main():

    letters = 'abcdefghijklmnopqrstuvwxyz'
    letterDict = {let: i+1 for (let,i) in zip(letters.upper(), range(26))}

    with open('words.txt', 'r') as f:
        line = f.read()

    words = line.replace('\"', '').replace('\n', '').split(',')

    sumList = []
    for word in words:
        tot = 0
        for letter in word:
            tot += letterDict[letter]
        sumList.append(tot)

    maxNum = 1
    count = 0
    i = 1
    while maxNum < max(sumList):
        maxNum = triNum(i)
        count += sum([x==maxNum for x in sumList])
        i += 1

    print(count)

if __name__=='__main__':
    pdb.run('main()')
