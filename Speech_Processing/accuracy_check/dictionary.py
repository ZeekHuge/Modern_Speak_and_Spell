import os
'''
f=open("a.txt", "r")
words=f.read().split("\n")
words.sort()
g=open("b.txt", "w+")
for i in range(len(words)):
	g.write(words[i]+"\n")
g.close()
f.close()
'''
f=open("a.txt", "r")
words=f.read().split("\n")
directory=os.listdir()
for word in words:
	os.system("touch "+word+".hyp")
	with open("test.fileids","w") as r:
		r.write(word)
	for d in directory:
		if os.path.isdir(d):
			os.chdir(d)
			files=os.listdir()
			for fi in files:
				filename, ext = os.path.splitext(fi)
				if ext==".wav" and filename==word:
					os.chdir("..")
					os.system("./run.sh "+word+".hyp "+word+" "+d)
					os.chdir(d)
			os.chdir("..")
f.close()
