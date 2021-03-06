#!/usr/bin/python3

import sys
import queue
import math
#from time import perf_counter

"""
Failed case #2/6: (Wrong answer)

Input:
18 36
-74258291 40695601
-74259991 40694901
-74257543 40695865
-74260991 40694301
-74256591 40696201
-74261991 40694501
-74261391 40694201
-74259891 40694101
-74254991 40696501
-74262191 40694601
-74263591 40693401
-74259091 40695901
-74262491 40693501
-74258091 40693501
-74254887 40696033
-74254891 40697301
-74253490 40697001
-74262591 40694701
1 2 1839
1 3 794
2 4 1167
2 1 1839
3 1 794
3 5 1010
4 6 1020
4 2 1167
4 7 413
4 8 1119
5 9 1628
5 3 1010
6 10 224
6 11 1942
6 4 1020
6 12 3221
7 4 413
7 13 1304
8 4 1119
8 14 1898
9 15 480
9 16 807
9 5 1628
9 17 1583
10 18 413
10 6 224
10 12 3362
11 6 1942
12 10 3362
12 6 3221
13 7 1304
14 8 1898
15 9 480
16 9 807
17 9 1583
18 10 413
10
2 17
10 8
6 8
11 13
16 2
15 14
15 8
6 5
7 1
17 11

Your output:
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1

Correct output:
6854
2363
2139
4679
6078
9935
8037
5830
3419
10983

 (Time used: 0.02/50.00, memory used: 10317824/2147483648.)
"""


"""
Warning, long feedback: only the beginning and the end of the feedback message is shown, and the middle was replaced by " ... ". 
Failed case #3/6: (Wrong answer)

Input:
100 1000
3097 9733
4950 275
2506 1855
3995 6281
6802 7863
9181 5848
5707 6125
4493 2397
218 7209
5206 2527
2597 7107
9572 8034
2438 3445
8528 5749
4509 1633
5903 1120
4911 7401
9006 9354
9610 6301
5159 3943
6608 4014
983 6970
7933 3377
4504 9327
2598 3013
9854 5588
9425 5619
3829 8108
5363 5695
2848 5596
6671 6205
2703 52
9240 2787
5142 2211
4463 2330
2704 5165
9929 7205
7253 9617
8609 6978
9616 1464
385 6742
8784 2932
4449 8303
4697 5851
114 2124
1158 6795
9479 7280
1309 9994
7041 9403
6124 1365
717 955
3397 3039
5203 5855
6835 6922
3659 1121
998 7977
5482 3239
5046 6053
572 9390
1477 2709
5169 9837
6205 3776
4447 3508
3808 9664
4414 4073
142 330
7805 7488
5744 1639
7449 7145
3256 2731
5279 5058
646 1988
1626 276
1074 7382
5546 5971
5595 1644
6951 2968
812 5793
5234 3229
111 1757
9472 8058
7864 4104
2697 8600
2593 9010
4426 5205
8315 7664
7162 4601
4242 9832
6825 2201
2695 412
4430 1218
3962 2050
858 6355
9624 6037
8941 9204
4551 6734
8304 2244
6742 5592
4825 678
6034 813
95 6 3366
7 33 4862
44 73 6366
36 91 4309
6 50 5428
48 37 9061
61 29 4148
34 36 3832
73 58 6715
23 19 3372
21 42 2432
18 92 8878
51 72 1037
77 14 3199
29 27 4064
7 32 6777
63 55 2515
80 77 6948
85 93 3750
6 29 3823
37 3 9152
74 70 5139
26 28 6532
31 34 4278
85 91 3989
94 20 4933
82 54 3001
63 44 2358
52 54 5188
68 89 1220
44 85 702
78 14 7718
46 63 4651
87 59 8148
9 8 6438
42 25 6188
38 28 3743
27 22 8551
36 39 6179
88 28 1774
25 60 1163
62 39 4006
64 48 2522
85 42 4917
34 14 4899
98 34 3742
98 22 5923
95 78 8817
36 46 2248
43 4 2074
92 93 5309
46 58 3960
67 34 5912
59 44 5437
90 15 2188
59 11 3053
20 54 3420
91 10 1523
87 57 2164
19 68 6058
27 42 2764
17 5 1948
16 50 331
80 81 11286
62 93 5938
64 92 7617
49 74 6301
70 15 1668
40 8 5209
48 55 9180
62 29 2097
24 66 10000
87 57 2164
18 93 8684
6 46 8080
98 55 5432
85 50 4200
41 100 8191
44 73 6366
88 52 6847
94 52 6913
97 36 6318
54 30 4203
87 54 2345
67 35 6148
93 94 8773
51 73 1136
71 73 6019
57 67 4844
65 16 3309
6 8 5823
94 10 5644
100 13 4458
96 14 4099
20 40 5102
28 87 4840
41 13 3885
62 68 2188
78 51 4840
96 15 5103
100 51 5320
29 91 4575
40 91 5193
62 75 2293
51 29 6639
5 31 1665
53 49 3997
24 8 6932
11 85 2640
74 87 6695
52 37 7749
59 53 5828
36 43 3592
66 61 10756
33 80 9188
11 83 1498
16 37 7298
11 76 6233
55 46 6202
86 92 7105
2 11 7227
40 34 4537
88 92 7789
29 89 3789
77 20 2042
3 18 9925
18 16 8801
5 18 2662
35 93 5405
 ... 8807
9794
5282
9020
6381
6730
10037
8160
12537
6972
1210
10626
8181
11174
9162
9150
6648
9662
9651
6252
7872
3470
10014
3102
6898
15054
5592
7676
5130
9979
6465
10666
2640
9266
5766
7849
6148
4202
6513
4963
1918
6472
8921
1550
4647
4394
0
11182
7424
8512
6015
8680
9267
10116
4919
9733
10122
10273
6920
9815
8789
5991
9411
7829
5915
10771
6908
8012
6118
9677
9528
6658
12566
4651
7169
3281
15024
6050
9402
10895
8813
5417
9679
6506
7825
5039
8388
9652
4914
8770
7854
6691
11134
7122
9416
9370
12930
10099
8107
8345
7816
10198
5506
8484
4776
8992
7854
5619
5249
5937
6779
1384
5610
7220
6789
9186
5692
7212
13800
8018
4965
9955
9815
2175
0
6135
13296
7475
5328
9305
5807
11425
7149
8003
8223
5987
9736
4339
11346
4877
7539
6286
12516
6357
9143
5246
11955
8460
8995
7964
5152
7895
5852
9386
9146
8058
6671
4044
4976
8911
11365
8876
2761
7333
6608
9168
9044
9202
9266
5898
11539
10324
11293
7402
8743
10047
9343
10106
14742
7809
7394
9983
8749
7629
3610
4044
8831
7440
5118
7822
7163
6044
4587
8128
4317
8435
5014
4704
7718
4387
9071
5480
6120
7569
9948
6698
11583
4452
9567
9166
4869
6716
10757
7205
11739
8435
8803
6389
10365
11285
10172
9307
8491
6815
7622
7173
12443
9170
8016
7778
8130
7333
8084
5807
10338
4917
8132
9440
6093
9147
4190
7534
7695
8671
14188
9843
9200
5255
3863
8831
7881
6081
10691
4414
6462
9401
6357
6096
4977
10604
9611
10477
7840
8092
7923
8371
9073
6690
8728
8851
4486
5407
6561
8277
5839
9371
6060
6626
7894
9507
9105
7647
7154
7880
10285
8698
10143
8681
7805
6462
4147
6972
7762
11044
9133
9624
5549
3704
3998
9439
8138
8566
6233
7545
3111
7677
9425
7212
6628
9285
9560
4526
5907
11385
4647
8528
10645
11747
9017
4212
9179
8492
8650
4934
9535
12478
5254
5497
10257
8073
5655
2396
5484
9671
5459
6093
11903
11806
2495
6924
12241
7466
6120
7473
4674
5160
8889
8935
4557
4237
5320
7515
9535
7896
11615
5171
3936
6807
7528
9235
8681
6548
7843
10507
11836
8332
8319
10068
10297
7702
8503
8136
4824
11955
4294
0
9384
11140
8382
8411
7866
7397
8127
2838
8411
4883
5847
11115
0
5825
10528
3565
7805
10107
8448
4543
2765
7938
9219
6205
5935
5853
6372
8012
7008
6413
2636
6096
11135
10466
8068
10249
9310
5983
10419
4974
6671
13515
5008
6883
6968
5827
8539
4545
10553
6918
4417
5666
7954
8659
9887
9266
10743
7098
9632
10764
10636
10357
6890
6857
9722
3690
4526
8977
10529
10153
13252
2386
6634
8317
4782
10324
5548
6263
6083
9569
9785
7217
10343
5566
7205

 (Time used: 1.24/50.00, memory used: 10317824/2147483648.)
"""


class BiAStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n; 
        self.inf = n*10**6
        self.clear()
        self.adj = adj
        self.cost = cost
        self.x = x
        self.y = y

    def clear(self):
        self.d = [[self.inf]*n, [self.inf]*n]
        self.visited = [False]*n
        self.workset = []

    def relax(self, q, side, v, dist, estimate):
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((estimate, v))

    def calc_dist(self):
        distance = self.inf
        for u in self.workset:
            if self.d[0][u] + self.d[1][u] < distance:
                distance = self.d[0][u] + self.d[1][u]
        if distance == self.inf:
            distance = -1
        return distance

    def process_min(self, q, side, s, t):
        finished = True
        distance = -1

        if not q[side].empty():
            v = q[side].get()[1]

            if not self.visited[v]:
                finished = False
                self.visited[v] = True
                self.workset.append(v)

                for u_i in range(len(self.adj[side][v])):
                    u = self.adj[side][v][u_i]
                    p = self.get_euclidian_bi_potential(u, s, t, side)
                    dist = self.d[side][v] + self.cost[side][v][u_i]
                    self.relax(q, side, u, dist, dist + p)

        if finished:
            distance = self.calc_dist()

        return finished, distance

    def query(self, s, t):
        self.clear()

        if s == t:
            return 0

        q = [queue.PriorityQueue(), queue.PriorityQueue()]

        self.relax(q, 0, s, 0, 0)
        self.relax(q, 1, t, 0, 0)

        while True:
            for side in [0, 1]:
                finished, distance = self.process_min(q, side, s, t)
                if finished:
                    return distance

        return -1
    
    def get_euclidian_bi_potential(self, u, s, t, side):
        if side == 1:
            s, t = t, s
        pi_f = math.sqrt( (self.x[u] - self.x[t])**2 + (self.y[u] - self.y[t])**2 )
        pi_r = math.sqrt( (self.x[u] - self.x[s])**2 + (self.y[u] - self.y[s])**2 )
        return (pi_f - pi_r) / 2.


class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n;
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.clear()
        self.x = x
        self.y = y

    def clear(self):
        self.d = [self.inf]*n
        self.visited = [False]*n
        self.workset = []
    
    def relax(self, q, v, dist, estimate):
        if self.d[v] > dist:
            self.d[v] = dist
            q.put((estimate, v))

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()

        if s == t:
            return 0
        
        q = queue.PriorityQueue()
        
        self.relax(q, s, 0, 0)

        while not q.empty():
            v = q.get()[1]
            
            if v == t:
                break

            if not self.visited[v]:
                self.visited[v] = True
                self.workset.append(v)

                if len(self.adj[v]) > 0:
                    for u_i in range(len(self.adj[v])):
                        u = self.adj[v][u_i]
                        p = self.get_euclidian_potential(u, t)                
                        dist = self.d[v] + self.cost[v][u_i]
                        self.relax(q, u, dist, dist + p)

        if self.d[t] == self.inf:
            return -1

        return self.d[t]

    def get_euclidian_potential(self, u, v):
        return math.sqrt( (self.x[u] - self.x[v])**2 + (self.y[u] - self.y[v])**2 )

def readl():
    return map(int, sys.stdin.readline().split())

"""
2 1
0 0
0 1
1 2 1
4
1 1
2 2
1 2
2 1

----------------
4 4
0 0
0 1
2 1
2 0
1 2 1
4 1 2
2 3 2
1 3 6
1
1 3

"""

if __name__ == '__main__':
    n,m = readl()

    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    # AStar:
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    # BiAStar:
    #adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    #cost = [[[] for _ in range(n)], [[] for _ in range(n)]]

    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b

    for e in range(m):
        u,v,c = readl()

        # AStar:
        adj[u-1].append(v-1)
        cost[u-1].append(c)
        
        # BiAStar:
        #adj[0][u-1].append(v-1)
        #cost[0][u-1].append(c)
        #adj[1][v-1].append(u-1)
        #cost[1][v-1].append(c)

    t, = readl()

    astar = AStar(n, adj, cost, x, y)
    #astar = BiAStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        #time = perf_counter()
        print(astar.query(s-1, t-1))
        #print(perf_counter() - time)


# Good job! (Max time used: 12.11/50.00, max memory used: 13213696/2147483648.)


