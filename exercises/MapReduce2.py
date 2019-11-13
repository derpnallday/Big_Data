from mrjob.job import MRJob

class MRWordCounter(MRJob):  

    def mapper(self, _, line):
    	yield "chars", len(line)

    	for words in line.split():
    		yield "words", 1

    	yield "lines", 1
    	

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRWordCounter.run()