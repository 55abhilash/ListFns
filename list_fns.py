import linecache

class line :
	def no_of_lines(self, file_name) :
		with open(file_name) as f :
			for i, l in enumerate(f) :
				pass
		return i + 1
	def list_of_lines(self, file_name) :
		total_lines = self.no_of_lines(file_name)
		lines_list = list()
		for i in range(total_lines) :
			lines_list.append(linecache.getline(file_name, i))
		return lines_list
	def print_fn_lines(self, file_name) :
		llist = self.list_of_lines(file_name)
		print len(llist)
		str_ = '{' + '\n'
		i = 0
		j = 1
		while(i < len(llist)) :
			if llist[i] == str_ :
				print "Function no. : " + str(j)
				print llist[i - 2]
				print llist[i - 1]
				j = j + 1
			i = i + 1
buff = raw_input("Enter the filename")
lin = line()
lin.print_fn_lines(buff)
	
