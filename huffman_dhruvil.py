import operator
import string
class HuffmanTree(object):
	
	def __init__(self, symbol='*', p=0, child0=None, child1=None,parent = None,v = None):
		
		self.symbol = symbol
		self.p = p
		self.child0 = []
		self.child1 = []
		self.parent = []
		self.v = v
		
		if child0 is not None:
			for child in child0:
				self.add_child(child0)
		if child1 is not None:
			for child in child1:
				self.add_child(child0)
		if parent is not None:
			for per in parent:
				self.add_parent(parent)
		
	def __repr__(self):
		return self.symbol
	def add_child0(self, node):
		assert isinstance(node, HuffmanTree)
		self.child0.append(node)
	def add_child1(self, node):
		assert isinstance(node, HuffmanTree)
		self.child1.append(node)
	def add_parent(self, node):
		assert isinstance(node, HuffmanTree)
		self.parent.append(node)
	
	
	
		
class Huffmancoding(HuffmanTree):
	file_path = "D:/read_file.txt"
	root_tree = 100
	encoded = []
	
	def __init__(self, p1, nodes = None, level = None, level1 = None):
		
		self.p1 = p1
		self.nodes = []
		self.level = level
		self.level1 = level1
		if nodes is not None:
			for nod in nodes:
				self.new_nodes(nodes)
        def new_nodes(self,node):
                assert isinstance(node, HuffmanTree)
                self.nodes = Huffmancoding(node)
	def add_nodes(self,node):
		
                list12 = []
              
                print node
                for i in range(0,len(T.p1)):
                                   
                        if T.p1[i] in node:
                                list12.append(T.p1[i])     
                              
                       
                #print list12
                
                binary = lambda n: '' if n==0 else binary(n/2) + str(n%2)
                print list12
                list15 = []
		for i in range(0,len(list12)):
			a = list12[i]
			b = 0
			list13 = []
			
			while (a.p < 100):
				list13.append(a.v)
				
				b = b + 1
				a = a.parent[0]
			#print list13
			
			L = Huffmancoding(i)
			k = ''
			for f in list13:
                                k = k + f
                        L.level = k
                        
                        L.level1 = list12[i]
                        
                        list15.append(L)
                        if i != len(list12)-1:
                                print list15[i].level1,"=",int(list15[i].level,2),",", len(list15[i].level),",",list15[i].level
                        else:
                                print "space=",int(list15[i].level,2),",", len(list15[i].level)
                                
                        #print list15[i].level1        
                        
                
                a = L.read_file()
                
                count = 1
                for k in range(0,len(a)):
                        
                        if count == 1:
                                for j in range(0,len(list15)):
                                         if a[k] == list12[j].symbol:
                                                q = int(list15[j].level,2)
                                                for j in range(0,len(list15)):
                                                        if a[k+1] == list12[j].symbol:
                                                                q = q * 2** len(list15[j].level)
                                                                q = q + int(list15[j].level,2)
                                                count = count + 1
                        else:
                                for j in range(0,len(list15)):
                                         if a[k] == list12[j].symbol:
                                                q = q * 2** len(list15[j].level)
                                                q = q + int(list15[j].level,2)                                                
                #print q
                #print bin(q)
                return q
               
                #print "length of encoded binary of whole file",len(bin(q))
                
		
	def read_file(self):
                #print 1
		myfile = open(Huffmancoding.file_path)
		#print 2
		mytxt = myfile.read()
		
		return mytxt
		
																																																																																																																	
# Need to finish the same process for all letters: c, d, ..., z
                


a = HuffmanTree(symbol='a', p=6.51738)
print 'p(' + a.symbol + ') = ' + str(a.p)
b = HuffmanTree(symbol='b', p=1.24248)
print 'p(' + b.symbol + ') = ' + str(b.p)
c = HuffmanTree(symbol='c', p=2.17339)
print 'p(' + c.symbol + ') = ' + str(c.p)
d = HuffmanTree(symbol='d', p=3.49835)
print 'p(' + d.symbol + ') = ' + str(d.p)
e = HuffmanTree(symbol='e', p=10.41442)
print 'p(' + e.symbol + ') = ' + str(e.p)
f = HuffmanTree(symbol='f', p=1.97881)
print 'p(' + f.symbol + ') = ' + str(f.p)
g = HuffmanTree(symbol='g', p=1.58610)
print 'p(' + g.symbol + ') = ' + str(g.p)
h = HuffmanTree(symbol='h', p=4.92888)
print 'p(' + h.symbol + ') = ' + str(h.p)
i = HuffmanTree(symbol='i', p=5.58094)
print 'p(' + i.symbol + ') = ' + str(i.p)
j = HuffmanTree(symbol='j', p=0.09033)
print 'p(' + j.symbol + ') = ' + str(j.p)
k = HuffmanTree(symbol='k', p=0.50529)
print 'p(' + k.symbol + ') = ' + str(k.p)
l = HuffmanTree(symbol='l', p=3.31490)
print 'p(' + l.symbol + ') = ' + str(l.p)
m = HuffmanTree(symbol='m', p=2.02124)
print 'p(' + m.symbol + ') = ' + str(m.p)
n = HuffmanTree(symbol='n', p=5.64513)
print 'p(' + n.symbol + ') = ' + str(n.p)
o = HuffmanTree(symbol='o', p=5.96302)
print 'p(' + o.symbol + ') = ' + str(o.p)
p = HuffmanTree(symbol='p', p=1.37645)
print 'p(' + p.symbol + ') = ' + str(p.p)
q = HuffmanTree(symbol='q', p=0.08606)
print 'p(' + q.symbol + ') = ' + str(q.p)
r = HuffmanTree(symbol='r', p=4.97563)
print 'p(' + r.symbol + ') = ' + str(r.p)
s = HuffmanTree(symbol='s', p=5.15760)
print 'p(' + s.symbol + ') = ' + str(s.p)	       
t = HuffmanTree(symbol='t', p=7.29357)
print 'p(' + t.symbol + ') = ' + str(t.p)
u = HuffmanTree(symbol='u', p=2.25134)
print 'p(' + u.symbol + ') = ' + str(u.p)
v = HuffmanTree(symbol='v', p=0.82903)
print 'p(' + v.symbol + ') = ' + str(v.p)
w = HuffmanTree(symbol='w', p=1.71272)
print 'p(' + w.symbol + ') = ' + str(w.p)
x = HuffmanTree(symbol='x', p=0.13692)
print 'p(' + x.symbol + ') = ' + str(x.p)
y = HuffmanTree(symbol='y', p=1.45984)
print 'p(' + y.symbol + ') = ' + str(y.p)
z = HuffmanTree(symbol='z', p=0.07836)
print 'p(' + z.symbol + ') = ' + str(z.p)
space = HuffmanTree(symbol=' ', p=19.18182)
print 'p(' + space.symbol + ') = ' + str(space.p)

# Need to include all letters in your tree below
MyTree = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space]


MyTree1 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space]

# Need to finish the funcition below that sorts the list MyTree in ascending order of probabilities.
def sort_mytree(tree=None):
	if tree is None:
		tree = []
# Write your code here to sort the tree
	tree = sorted(tree, key = operator.attrgetter('p')) 
	return tree
# Don't need to do anything here. The print below is to verify that your code sorts your tree correctly in ascending order of probabilities.
MyTree = sort_mytree(MyTree)
#print MyTree
list1 = []
list2 = []
count = 1

for i in range(0,26):
	MyTree = sort_mytree(MyTree)
	
	A = MyTree[0].p + MyTree[1].p

	top = HuffmanTree(p = A)
	
	top.add_child0(MyTree[0]) 
	top.add_child1(MyTree[1])
	MyTree[0].add_parent(top)
	MyTree[1].add_parent(top)
	MyTree[0].v = '0'
	MyTree[1].v = '1'
	list1.append(MyTree[0])
	list1.append(MyTree[1])
        print "parent"
	print MyTree[0].parent[0].p
        print "children"
        print top.child0[0].p
        print top.child1[0].p
	MyTree[0] = top
	del MyTree[1]

T = Huffmancoding(list1)
q = T.add_nodes(MyTree1)
print "encoded file =",int(bin(q),2),",",len(bin(q))
A = Huffmancoding(A)
print "read content of file = ",A.read_file()
