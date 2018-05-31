#Equation of plane
#Created by Danny Ceron
#Demonstras the equation of the line from calculus 3

class EquationOfPlane(object):
    """Calculating Plane equation"""

    def __init__(self, eqType,pointA, pointB,
                       pointC,pointD,pointE,pointF,
                       pointG,pointH,pointI):
        self.eqType = eqType
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        self.pointD = pointD
        self.pointE = pointE
        self.pointF = pointF
        self.pointG = pointG
        self.pointH = pointH
        self.pointI = pointI

    def __str__(self):
        """retrn the composed equation"""
        answer = NULL 
        return answer
    #calculats two vectors between 3 points in 3d spance
    #param a1, b1, c1,a2, b2, c2,a3, b3, c3
    #return v1A, v1B, v1C, v2A, v2B, v2C
    def choice(self):
        print("""

a) Find Eq of plane with given points
b) Find Eq of plane with given vectors
            """)
        choice = input("\nEnter your choice: ")
        return choice
        
    def difVectors(self,a1, b1, c1,
                        a2, b2, c2,
                        a3, b3, c3):
        v1A = a1-a2
        v1B = b1-b2
        v1C = c1-c2

        v2A = a3-a2
        v2B = b3-b2
        v2C = c3-c2

        return v1A, v1B, v1C, v2A, v2B, v2C
    
    def crossPro(self, v1a, v1b, v1c,
                       v2a, v2b, v2c):
        nA = ((v1b*v2c)-(v1c*v2b))
        nB = ((v1a*v2c)-(v1c*v2a))*-1
        nC = ((v1a*v2b)-(v1b*v2a))

        return nA, nB, nC
    
    def finalEq(self , nA, nB,nC,
                       p1, p2, p3):
        pa = (p1*nA)
        pb = (p2*nB)
        pc = (p3*nC)

        print(str(nA)+"x-("+str(pa)+")+"+str(nB)+"y-("+str(pb)+")+"+str(nC)+"z-("+str(pc)+") = 0")
        return None
    def find_plane_eq(self):
        vec1A,vec1B,vec1C,vec2A,vec2B,vec2C = self.difVectors(a1 = self.pointA, b1 = self.pointB, c1 = self.pointC,
                                                         a2 = self.pointD, b2 = self.pointE, c2 = self.pointF,
                                                         a3 = self.pointG, b3 = self.pointH, c3 = self.pointI)
        normX, normY, normZ = self.crossPro(v1a = vec1A, v1b = vec1B, v1c = vec1C,
                                       v2a = vec2A, v2b = vec2B, v2c = vec2C)
        self.finalEq(nA = normX, nB = normY, nC = normZ,
                   p1 =self.pointD, p2 =self.pointE, p3 =self.pointF)
    
#main

test1 = EquationOfPlane(eqType = 0 ,pointA =10, pointB =1,pointC =13,
                       pointD =5,pointE= 8,pointF =7,
                       pointG = 6,pointH =4,pointI =9)
"""
print(test1.difVectors(a1 = 3, b1 = 4, c1 = 8,
                        a2 = 1, b2 = 1, c2 = 1,
                        a3 = 6, b3 = 2, c3 = 0))
print(test1.crossPro(v1a =1, v1b = 1, v1c =1,
                     v2a =1, v2b =-1, v2c =1))
test1.finalEq(nA =2, nB =1, nC =-4,
                   p1 =3, p2 =5, p3 =8)
"""
test1.find_plane_eq()

