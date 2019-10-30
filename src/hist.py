
import numpy as np
import matplotlib.pyplot as plt

fields=['Mean of Word Count','Mean of Body Text Ratio','Mean of Emphasized Text','Mean of Text Positional Changes','Mean of Text CLusters',\
		'Mean of Link Count','Mean of Page Size (kb)','Mean of Graphics Size Percent','Mean of Graphics Count','Mean of Colour Count',\
		'Mean of Font Count']

efields=['Standard Deviation of Word Count','Standard Deviation of Body Text Ratio','Standard Deviation of Emphasized Text',\
		'Standard Deviation of Text Positional Changes','Standard Deviation of Text CLusters','Standard Deviation of Link Count',\
		'Standard Deviation of Page Size (kb)','Standard Deviation of Graphics Size Percent','Standard Deviation of Graphics Count',\
		'Standard Deviation of Colour Count','Standard Deviation of Font Count']
ind=[	490.01477436968, 0.124501348964188, 0.271342155130882, 1.33145977196082, 58.476955195118, 44.9596916653284,\
		2923.75988167656, 84.4220031797013, 37.4881965633531, 11.2018628553075, 10.6650072265939]
eind=[	1207.35721835792, 0.933810357100132, 0.745291972954829, 3.87418306426826, 164.27071425647, 69.0802441289281,\
 		8678.44616464139, 22.3640534779479, 59.68863675176, 4.57842498331033, 53.112072630305]
usa=[	544.8088235294117, 0.1613031836106031, 0.168198305208443, 0.5245098039215687, 30.95098039215686, 62.28186274509804,\
		1898.0973785998774, 80.88276651931785, 25.730392156862745, 5.044117647058823, 5.0245098039215685]
eusa=[	372.5016551096119, 0.2240744236445323, 0.101846073397447, 1.4516343915623589, 50.6830070627344, 34.42128651223879,\
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
	ax.bar(X,list(dind.values()), width=0.3, color='g', align='center')
	ax.bar(X+0.2, list(dusa.values()), width=0.3, color='b', align='edge')
	ax.legend(('India','USA'))
	plt.xticks(X,[list(dind.keys())[0][:4],list(dind.keys())[1][:18]],fontsize=13)
	plt.title(fields[p][8:], fontsize=17)
	plt.savefig("img"+str(p)+".png")
	plt.show()
