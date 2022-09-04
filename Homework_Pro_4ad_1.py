
class TextStatistic:    
    
    def characters(f):
        n = 0
        for line in open(f):
            n += len(line.rstrip())
        return n

    def words(f):
        n = 0
        for line in open(f):
            list = line.split()
            for item in list:
                if item[0].isalpha():
                    n += 1
        return n

f = 'text'
print (TextStatistic.characters(f))

print (TextStatistic.words(f))


    


