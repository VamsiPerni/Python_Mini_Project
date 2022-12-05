# Mini_project_python

NUMBER_OF_CUTS = int(input("NUMBER OF CUTS : "))
ANGLES_IN_LIST = list(map(int,input("ANGLES WITH SEPERATOR COMMA : ").split(",")))
K = []
for i in ANGLES_IN_LIST :
    if i not in K :
        K.append(i)
L = K  # STORING THE ANGLES WITHOUT REPETITON IN L VARIABLE
M = 0  # M IS TAKEN TO FIND OUT THE SUM OF ALL ANGLES IN LIST
for i in ANGLES_IN_LIST:
    M = M + i  # WE CA USE "SUM" FUNCTION TO GET SUM OF INTEGERS PRESENT IN THE LIST.
X = M  # STORING THE SUM OF ALL ANGLES GIVEN IN THE LIST IS STORED IN X VARIABLE
    # CASE 1 : CAKE SHOULD BE CUT INTO " N " EQUAL PARTS
    # CASE 2 : CAKE SHOULD BE CUT INTO " N " PARTS
    # CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL

if NUMBER_OF_CUTS == len(ANGLES_IN_LIST) and M ==360 :
        if len(L) == 1 and L[0] * NUMBER_OF_CUTS == 360 and len(ANGLES_IN_LIST) == NUMBER_OF_CUTS:
            print("FIRST CASE SATISFIED")
        else:
            print("FIRST CASE NOT SATISFIED")
        if X == 360 and len(ANGLES_IN_LIST) ==NUMBER_OF_CUTS: # SECOND CASE VERIFICATION
            print("SEOND CASE SATISFIED")
        else:
            print("SECOND CASE NOT SATISFIED")
        if K ==ANGLES_IN_LIST: # THIRD CASE VERIFICATION
             print("THIRD CASE SATISFIED")
        else:
            print("THIRD CASE NOT SATISFIED")
else:
    print("GIVE THE INPUT PROPERLY OR CHECK WHEATHER THE SUM OF ANGLES IS 360 ")
N = int(input("Number of cuts: "))
Angle = list(map(int,input("Enter angles seperated by comma: ").split(",")))
def Divide_the_cake(N,Angle):
    k = []
    for i in Angle:
        if i not in k:
            k.append(i)
    l = k
    sum1 = sum(Angle)
    x = sum1
    print(sum1)

    # CASE 1 : CAKE SHOULD BE CUT INTO 'N' EQUAL PARTS.
    # CASE 2 : CAKE SHOULD BE CUT INTO 'N' PARTS.
    # CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL.

    if N == len(Angle) and x==360:
        if len(l) == 1 and l[0] * 360 and len(Angle) == N:
            print("CASE 1 SATISFIED.")
        else:
            print("CASE 1 NOT SATISFIED.")
        if x == 360 and len(Angle) == N:
            print("CASE 2 SATISFIED.")
        else:
            print("CASE 2 NOT SATISFIED.")
        if k == Angle:
            print("CASE 3 SATISFIED.")
        else:
            print("CASE 3 NOT SATISFIED.")
    else:
        print("GIVE THE INPUT PROPERLY OR CHECK WEATHER THE SUM OF ANGLES IS 360.")
Divide_the_cake(N,Angle)
class Inputs :
    N = int(input("NUMBER_OF _CUTS: "))
    A = input("ANGLES_IN_LIST: ")
    B = A.split(",")
    for i in range(0,len(B)):
        B[i] = int(B[i])
    def fun(self,N,B):
        self.N = N
        self.B = B
class CASE(Inputs):
    def fun1(self):
        K = []
        for i in self.B:
            if i not in K:
                K.append(i)
        L = K # STORING THE ANGLES WITHOUT REPETITON IN L VARIABLE
        M = 0 # M IS TAKEN TO FIND OUT THE SUM OF ALL ANGLES IN LIST
        for i in self.B :
            M = M + i
        X = M # STORING THE SUM OF ALL ANGLES GIVEN IN THE LIST IS STORED IN X VARIABLE

    # CASE 1 : CAKE SHOULD BE CUT INTO " N " EQUAL PARTS
    # CASE 2 : CAKE SHOULD BE CUT INTO " N " PARTS
    # CASE 3 : CAKE SHOULD BE CUT AND NO TWO CAKE SLICES ARE EQUAL

        if self.N == len(self.B) and M == 360:
            if len(L) == 1 and L[0] * self.N == 360 and len(self.B) ==self.N: # FIRST CASE VERIFICATION
                print("FIRST CASE SATISFIED")
            else:
                print("FIRST CASE NOT SATISFIED")
            if X == 360 and len(self.B) == self.N:
                print("SEOND CASE SATISFIED")
            else: # SECOND CASE VERIFICATION
                print("SECOND CASE NOT SATISFIED")
            if K == self.B: # THIRD CASE VERIFICATION
                print("THIRD CASE SATISFIED")
            else:
                print("THIRD CASE NOT SATISFIED")
        else:
            print("GIVE THE INPUT PROPERLY OR CHECK WHEATHER THE SUM OF ANGLES IS 360")
C = CASE()
C.fun1()