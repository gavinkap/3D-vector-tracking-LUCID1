#3D Vector Tracking v0.1.7/0.2
#By Matthew Dickers and Gavin Kapuscinski with help from Owen Watts
#Pretty much all by Matt though...
#Some parts are not used but have been left in as may be needed later.
import random
import math
detector1 = []
detector2 = []
data = []
blob_num = 0
blob_size = 0
blobX = 0
blobY = 0
energy= 0
count = 0
are_same = []
true = []
lens = []
lenX = 0
lenY = 0
##gradient = 0
##gradients = []
##len_hyp = 0
##hyps = []
tan = 0
atan = 0
angle = 0
angles = []
sames = []


#Particle Analysis
    #Will be replaced with data from the Blobbing Algorithm
for i in range(0,100):
    blob_num = i
    blob_size = random.randint(1,25)
    blobX = random.randint(1,255)
    blobY = random.randint(1,255)
    energy = random.randint(1,25)
    data.append(blob_num)
    data.append(blob_size)
    data.append(blobX)
    data.append(blobY)
    data.append(energy)
    detector1.append(data)
    data = []

print("Randomly Generated Data Sets:")
print("Detector 1")
print(detector1)
print()

for i in range(0,100):
    blob_num = i
    blob_size = random.randint(1,25)
    blobX = random.randint(1,255)
    blobY = random.randint(1,255)
    energy = random.randint(1,25)
    data.append(blob_num)
    data.append(blob_size)
    data.append(blobX)
    data.append(blobY)
    data.append(energy)
    detector2.append(data)
    data = []
print("Detector 2")
print(detector2)
    #Will be replaced with data from the Blobbing Algorithm

#Identifying if particles are the same:
x = 0
while x != len(detector1):
    y = 0
    while y != len(detector2):
        if detector1[x][1] == detector2[y][1]:
            if detector1[x][4] == detector2[y][4]:
                count+=1
                true.append(x)
                true.append(y)
                are_same.append(true)
                true = []
            else:
                count+=1
        else:
            count+=1
        y+=1
    x+=1

#Pythagoras:
    #Calculating the length of X:
data = []
for i in range(len(are_same)):
    lenX = (detector1[are_same[i][0]][2]) - (detector2[are_same[i][1]][2])
    if lenX < 0:
        lenX = lenX*-1


    lenY = (detector1[are_same[i][0]][3]) - (detector2[are_same[i][1]][3])
    if lenY < 0:
        lenY = lenY*-1

    data.append(i)
    data.append(lenX)
    data.append(lenY)
    lens.append(data)
    data = []

##    #Pythagoras
##data = []
##for i in range(len(lens)):
##    len_hyp = lens[i][0]**2 + lens[i][1]**2
##    len_hyp = math.sqrt(len_hyp)
##    len_hyp = round(len_hyp,3)
##    data.append(i)
##    data.append(len_hyp)
##    hyps.append(data)
##    data = []
##print()
##print("Hyps for each same particle:")
##print(hyps))


###Calculating Gradient:
##data = []
##for i in range(len(lens)):
##    gradient = lens[i][2]/lens[i][1]
##    gradient = round(gradient,1)
##    data.append(i)
##    data.append(gradient)
##    gradients.append(data)
##    data = []

#Calculating Angle using Trig:
    #Uses Tan, Opposite/Adjascent
data = []
for i in range(len(lens)):
    tan = lens[i][2] / lens[i][1]
    atan = math.atan(tan)
    angle = math.degrees(atan)
    angle = round(angle,0)
    data.append(i)
    data.append(angle)
    angles.append(data)
    data = []
    
    #Data of all similar Particles
data = []
for i in range(len(are_same)):
    data.append(i)
    data.append(are_same[i][0])
    data.append(are_same[i][1])
    data.append(detector1[are_same[i][0]][1])
    data.append(detector2[are_same[i][1]][4])
    data.append(angles[i][1])
    sames.append(data)
    data = []

print()
print()
print("Data about similar particles:")
print(sames)
print()
print("The first value represents the similar particles number.")
print("The second value represents the particle from detector 1.")
print("The third value represents the particle from detector 2.")
print("The fourth value representes the size of each particle.")
print("The fith value representes the energy of the particle.")
print("The sixth value repsentes the angle at which the particle enters the detector.")





