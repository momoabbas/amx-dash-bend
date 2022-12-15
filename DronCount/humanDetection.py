# import cv2
# import torch
# import math
#
#
# class Tracker:
#     def __init__(self):
#         # Store the center positions of the objects
#         self.center_points = {}
#         # Keep the count of the IDs
#         # each time a new object id detected, the count will increase by one
#         self.id_count = 0
#
#
#
#     def update(self, objects_rect):
#         # Objects boxes and ids
#         objects_bbs_ids = []
#
#         # Get center point of new object
#         for rect in objects_rect:
#             x, y, w, h = rect
#             cx = (x + x + w) // 2
#             cy = (y + y + h) // 2
#
#             # Find out if that object was detected already
#             same_object_detected = False
#             for id, pt in self.center_points.items():
#                 dist = math.hypot(cx - pt[0], cy - pt[1])
#
#                 if dist < 35:
#                     self.center_points[id] = (cx, cy)
# #                    print(self.center_points)
#                     objects_bbs_ids.append([x, y, w, h, id])
#                     same_object_detected = True
#                     break
#
#             # New object is detected we assign the ID to that object
#             if same_object_detected is False:
#                 self.center_points[self.id_count] = (cx, cy)
#                 objects_bbs_ids.append([x, y, w, h, self.id_count])
#                 self.id_count += 1
#
#         # Clean the dictionary by center points to remove IDS not used anymore
#         new_center_points = {}
#         for obj_bb_id in objects_bbs_ids:
#             _, _, _, _, object_id = obj_bb_id
#             center = self.center_points[object_id]
#             new_center_points[object_id] = center
#
#         # Update dictionary with IDs not used removed
#         self.center_points = new_center_points.copy()
#         return objects_bbs_ids
#
# # from tracker import *
# import numpy as np
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
#
# cap=cv2.VideoCapture("media/na.mp4")
#
#
# def POINTS(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE :
#         colorsBGR = [x, y]
#         print(colorsBGR)
#
#
# cv2.namedWindow('FRAME')
# cv2.setMouseCallback('FRAME', POINTS)
#
# tracker = Tracker()
# while True:
#     ret,frame=cap.read()
#     frame=cv2.resize(frame,(720,400))
#     results=model(frame)
# #     frame=np.squeeze(results.render())
#     count=0
#     for index,row in results.pandas().xyxy[0].iterrows():
# #         print(row)
#         x1=int(row['xmin'])
#         y1=int(row['ymin'])
#
#         x2=int(row['xmax'])
#         y2=int(row['ymax'])
#         b=str(row['name'])
#         if 'person' in b:
#             count=count+1
#             print(count)
#
#             cv2.rectangle(frame, (x1, y1),(x2, y2),(0, 0, 255), 2)
#
# #         list=list.append([x1,y1,x2,y2])
# #     boxes_id=tracker.update(list)
# #     cv2.rectangle(frame, (x1, y1),(x2, y2),(0, 0, 255), 2)
# #     cv2.putText(frame,b,(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0))
#
#
#     cv2.imshow('FRAME',frame)
#     if cv2.waitKey(1)&0xFF==27:
#         break
# cap.release()
# cv2.destroyAllWindows()
