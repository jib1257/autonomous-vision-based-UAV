import math

#def measure1m():

#Before using, measure the pixel width when object is at 1m, and measure the object width in meters

#Computes the distance and angle offset (in deg) using the camera inputs, object_length_at_1m_in_pixels and object_width_in_meters
def pix2DisAng(camwidth, ptA, ptB, LENGTH1m_pix, OBJECT_WIDTH_in_Meters):
    mid = ((ptA[0]+ptB[0])/2,(ptA[1]+ptB[1])/2)
    yawpix = mid[1] - camwidth/2.0

    len_pix = abs(ptB[0]-ptA[0])
    dist_in_m = LENGTH1m_pix/len_pix
    len_per_pix = OBJECT_WIDTH_in_Meters/len_pix
    offset_in_m = yawpix*len_per_pix
    yawRad = math.atan2(offset_in_m,dist_in_m)
    yawDeg = math.degrees(yawRad)

    return [dist_in_m, yawDeg]
