startnum=1
spiral=[[startnum]]
centerrow=0

spiral[centerrow].append(startnum+1)

spiral.insert(0, list(range(spiral[centerrow][-1]+len(spiral[centerrow])+1,spiral[centerrow][-1],-1)))
centerrow+=1

spiral.insert(0,spiral[0])