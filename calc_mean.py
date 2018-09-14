import csv
def sqrt(x):
	return x**0.50
def avg(s,l):
	return s*1.0/l
def diff(x,y):
	return (x-y)**2
def calc_mean_std(filename):
	fields	= []
	rows 	= []
	with open(filename, 'r') as csvfile:
	    # creating a csv reader object
		csvreader = csv.reader(csvfile)     
		fields = csvreader.next()
		for row in csvreader:
			rows.append(map(float,row[1:]))
		l=len(rows)
		s=map(sum,zip(*rows))
		mean=map(avg,s,[l]*11)
		print mean
		std=[0]*11
		for i in rows:
			std=map(sum,zip(std,map(diff,i,mean)))
		std=map(avg,std,[l]*11)
		std=map(sqrt,std)
		print std
		csvfile.close()
	return mean,std
def main():
	filename1 = "india.csv"
 	filename2 = "usa.csv"
 	filename3 = "comparison_ind_usa.csv"
 	mean1,std1=calc_mean_std(filename1)
 	mean2,std2=calc_mean_std(filename2)
 	india	=["INDIA"]+mean1+std1
 	usa		=["USA"]+mean2+std2
 	rows	=[india,usa]
 	fields = [	'Country', \
 				'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11',\
 				'p1e', 'p2e', 'p3e', 'p4e', 'p5e', 'p6e', 'p7e', 'p8e', 'p9e', 'p10e', 'p11e']
 	with open(filename3, 'w+') as csvf:
		csvw = csv.writer(csvf)
		csvw.writerow(fields)
		csvw.writerows(rows)
		csvf.close()

	
 
	# reading csv file

		
 
	    
 

if __name__=='__main__':
	main()
