from Stack import Stack
from BinaryTree import BinaryTree

def buildParseTree(fpexp):
	fplist = []
	while len(fpexp) != 0:
		ch = fpexp[0]
		if ch in '()+-*/':
			fplist.append(ch)
			fpexp = fpexp[1:]
		else:
			i = 0
			while (fpexp[i] not in '()+-*/andornot'):
				i += 1
			fplist.append(fpexp[:i])
			fpexp = fpexp[i:]
	print(fplist)
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+', '-', '*', '/', ')']:
			print(i)
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = pStack.pop()
		else:
			raise ValueError
	return eTree

def evaluate(parseTree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, 'and':operator.and_, 'or':operator.or_, 'not':operator.not_}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootVal()

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())

def postordereval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, 'and':operator.and_, 'or':operator.or_, 'not':operator.not_}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1,res2)
		else:
			return tree.getRootVal()

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def printexp(tree):
	sVal = ""
	if tree:
		sVal = '(' + printexp(tree.getLeftChild())
		sVal = sVal + str(tree.getRootVal())
		sVal = sVal + printexp(tree.getRightChild())+')'
	return sVal

pt = buildParseTree("((10+5)*3)")
printexp(pt)
ans = evaluate(buildParseTree('5and2'))
print(ans)
#pt.postorder()