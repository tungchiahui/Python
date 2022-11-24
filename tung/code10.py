#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
#已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
n=len(['x','y','z'])
for x in range(n):
    for y in range(n):
        for z in range(n):
            if x!=y and y!=z and x!=z and x not in [0] and z not in [0,2]:
                print('比赛对手名单为：a - {}, b - {}, c - {}'.format('xyz'[x],'xyz'[y],'xyz'[z]))