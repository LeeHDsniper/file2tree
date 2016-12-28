# -*- coding:utf-8 -*-

import os
import os.path
import sys
import getopt


def usage():
    print '[ * ] use like "python file2tree.py -r d:/tree"'
    print '[ * ] or use like "python file2tree.py --rootdir d:/tree"'


def get_tree(cur_path):
	stack=[]
	ret=[]
	stack.append(cur_path)
	while len(stack)>0:
		tmp=stack.pop(len(stack)-1)
		if os.path.isdir(tmp):
			ret.append(tmp)
			for item in os.listdir(tmp):
				stack.append(os.path.join(tmp,item))
			#print tmp
		elif os.path.isfile(tmp):
			ret.append(tmp)
			#print tmp
	return ret

def write_tree(rootdir):
	file_tree=open(os.path.join(rootdir,"/file2tree.txt"),"w")
	path_list=get_tree(rootdir)
	length=len(path_list)
	#file_tree.write("©À©¤"+os.path.split(rootdir)[1]+"\n")
	for index in range(1,length):
		tmp=os.path.normcase(path_list[index].split(rootdir)[1])
		tmp=tmp.strip("\\")
		deepth=tmp.count("\\")+1
		path_name=os.path.split(tmp)[1]
		if(index<length-1):
			tmp_next=os.path.normcase(path_list[index+1].split(rootdir)[1])
			tmp_next=tmp_next.strip("\\")
			deepth_next=tmp_next.count("\\")+1
		else:
			deepth_next=-1#©¦
		if deepth_next==deepth or deepth_next>deepth:
			space=""
			for sp in range(0,deepth-1):
				space+="©¦  "
			file_tree.write(space+"©À©¤"+path_name+"\n")
	
		elif deepth_next!=deepth :
			space=""
			for sp in range(0,deepth-1):
				space+="©¦  "
			file_tree.write(space+"©¸©¤"+path_name+"\n")
		#print os.path.split(i)[1]
	file_tree.close()
	
	
opts, args = getopt.getopt(sys.argv[1:], "hr:", ["help", "rootdir="])
if not opts:
	usage()
for op, value in opts:
	if op == "-r" or op == "--rootdir":
		rootdir = value
		if not os.path.exists(rootdir):
			print '[ * ] path "%s" does not exist,please check the param "-r"' % (rootdir)
			sys.exit()
		else:
			write_tree(rootdir.rstrip("\\"))	
	else:
		usage()
		sys.exit()
