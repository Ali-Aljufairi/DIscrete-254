from itcs254 import Relations

 
#U = {1, 6, 3, 9}
#def F(a, b): return a + b <= 10 and any((a + b) % x ** 2 == 0 for x in U)


#r = Relations(((a, b) for a in U for b in U if F(a, b) or F(b, a)), U)


r = Relations([(0,4),(1,1),(1,3),(2,2),(3,1),(4,0)], {0, 1,3,4})





print(r.relations())
