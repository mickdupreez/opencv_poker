import cv2 as cv
import numpy as np


def find(needle_img_path, haystack_img_path, threshold=0.9, debug_mode=None):
    

    haystack_img = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)


    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]


    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, method)


    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    
    


    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    points = []

    if len(rectangles):
        print("needle found")
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (125, 125, 0)
        marker_type = cv.MARKER_CROSS
        thickness = 1
        #looping over all the locations and drawing rectangle
        for (x, y, w, h) in rectangles:
            
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # determine box positions
            if debug_mode == "rectangles":
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # draw box
                cv.rectangle(haystack_img, top_left, bottom_right, line_color, thickness, line_type)

            elif debug_mode == "points":

                cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        if debug_mode:
            cv.imshow("Matches", haystack_img)
            cv.waitKey()

    return points


points = find("screenshots/needle.png", "screenshots/heysatck.png", debug_mode="rectangles")












































    ## get best match position 
    #min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    #print("best match loc is : %s" % str(max_loc))
    #print("best match confidence : %s" % max_val)
    #
    #threshold = 0.9
    #if max_val >= threshold:
    #    print("needle found")
    #    
    #    needle_w = needle_img.shape[1]
    #    needle_h = needle_img.shape[0]    
    #    top_left = max_loc
    #    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    #    
    #    cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    #    cv.imshow("Result", haystack_img)
    #    cv.waitKey()
    #else:
    #    print("needle not found")
    #
    ##cv.imshow("Result", result)
    ##cv.waitKey()
    #
    #
    #