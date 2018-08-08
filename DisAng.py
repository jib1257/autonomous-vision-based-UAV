import math
def pix2DisAng(camheight, camwidth, ptA, ptB, SIZE1m, pix_off_1m_arctanhalf):
    mid = ((ptA[0]+ptB[0])/2,(ptA[1]+ptB[1])/2)
    size = abs(ptB[0]-ptA[0])
    dist = C*size
    yaw = mid[1] - camwidth/2.0
    disAng = [dist,yaw]
    return disAng

    