
import numpy as np
import matplotlib.pyplot as plt

fields=['Mean of Word Count','Mean of Body Text Ratio','Mean of Emphasized Text','Mean of Text Positional Changes','Mean of Text CLusters',\
		'Mean of Link Count','Mean of Page Size (kb)','Mean of Graphics Size Percent','Mean of Graphics Count','Mean of Colour Count',\
		'Mean of Font Count']
		
efields=['Standard Deviation of Word Count','Standard Deviation of Body Text Ratio','Standard Deviation of Emphasized Text',\
		'Standard Deviation of Text Positional Changes','Standard Deviation of Text CLusters','Standard Deviation of Link Count',\
		'Standard Deviation of Page Size (kb)','Standard Deviation of Graphics Size Percent','Standard Deviation of Graphics Count',\
		'Standard Deviation of Colour Count','Standard Deviation of Font Count']
ind=[	304.50898203592817, 0.4166505339819531, 80.43413173652695, 0.9940119760479041, 48.23353293413174, 36.35329341317365, \
		1949.170328288735, 77.80262293254758, 26.823353293413174, 9.694610778443113, 7.772455089820359]
eind=[	319.0065110792251, 5.031748670822134, 134.64515408160548, 2.03265852285013, 75.23750387482818, 29.25872158100259, \
		5375.771923950075, 30.389389368997904, 34.098157791929566, 4.713609515951212, 14.16251975563747 ]
usa=[	544.8088235294117, 0.1613031836106031, 90.05882352941177, 0.5245098039215687, 30.95098039215686, 62.28186274509804,\
		1898.0973785998774, 80.88276651931785, 25.730392156862745, 5.044117647058823, 5.0245098039215685]
eusa=[	372.5016551096119, 0.2240744236445323, 97.96506215247095, 1.4516343915623589, 50.6830070627344, 34.42128651223879,\
		3000.011082193864, 21.243980475197443, 23.810338375833794, 3.0715351443572847, 16.12920828974023]


for p in range(11):
	dind={}
	dusa={}
	for i in range(p,len(ind),11):
		dind[fields[i]]=ind[i]
		dind[efields[i]]=eind[i]
	for i in range(p,len(usa),11):
		dusa[fields[i]]=usa[i]
		dusa[efields[i]]=eusa[i]
	deind={}
	deusa={}
	for i in range(p,len(ind),11):
		deind[efields[i]]=eind[i]
	for i in range(p,len(eusa),11):
		deusa[efields[i]]=eusa[i]
	
	#fig, axe = plt.subplots(nrows=1, sharex=True)
	#axe.errorbar(list(dind.keys()), dind.values(), yerr=eind, fmt='o')
	#axe.errorbar(list(dind.keys()), dind.values(), yerr=eusa, fmt='o')
	
	X=np.arange(len(dind))
	print(X)
	print(dind)
	print(dusa)
	ax = plt.subplot(111)
	ax.bar(X,list(dind.values())[::-1], width=0.3, color='b', align='center')
	ax.bar(X+0.2, list(dusa.values())[::-1], width=0.3, color='g', align='edge')
	ax.legend(('India','USA'))
	plt.xticks(X,[list(dind.keys())[1][:4],list(dind.keys())[0][:18]],fontsize=13)
	plt.title(fields[p][8:], fontsize=17)
	plt.savefig("img"+str(p)*2+".png")
	plt.show()

