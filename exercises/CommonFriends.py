from mrjob.job import MRJob

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


class MRWordCounter(MRJob):  

    def mapper(self, _, line):
    	for c in line.split():
    		yield "a",c

    def reducer(self, key, values):
        yield key, intersection(values)

if __name__ == '__main__':
    MRWordCounter.run()