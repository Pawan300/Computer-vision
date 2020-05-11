from collections import OrderedDict

import numpy as np
from scipy.spatial import distance


class CentroidTracker:
    def __init__(self, m):
        self.nextObjectId = 0
        self.objects = OrderedDict()
        self.rectangle = None  #
        self.disappeared = OrderedDict()
        self.max_Disapper = m

    def register_object(self, centroid):#, cordinates):  #
        self.objects[self.nextObjectId] = centroid
        #self.rectangle = cordinates  #
        self.disappeared[self.nextObjectId] = 0
        self.nextObjectId += 1

    def deregister_object(self, id):
        del self.objects[id]
        del self.disappeared[id]

    def update_object(self, rectangle):
        if len(rectangle) == 0:
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1

                if self.disappeared[object_id] > self.max_Disapper:
                    self.deregister_object(object_id)
            return self.objects
        else:

            centroid_cordinate = np.zeros((len(rectangle), 2), dtype="int")
            #print("rectangle: ", rectangle)  #
            for (i, (x, y, z, w)) in enumerate(rectangle):
                centroid_cordinate[i] = (int(x + z) / 2.0, int(y + w) / 2.0)

            if len(self.objects) == 0:

                for i in range(0, len(centroid_cordinate)):
                    self.register_object(centroid_cordinate[i])#, rectangle[i])  #
            else:
                object_id = list(self.objects.keys())
                object_centroid = list(self.objects.values())
                print("object ",object_centroid)

                D = distance.cdist(
                    np.array(object_centroid), np.array(centroid_cordinate), "euclidean"
                )

                rows = D.min(axis=1).argsort()
                cols = D.argmin(axis=1)[rows]

                used_row = set()
                used_col = set()

                for (row, col) in zip(rows, cols):
                    if row in used_row or col in used_col:
                        continue
                    obj_id = object_id[row]
                    self.objects[obj_id] = centroid_cordinate[col]
                    self.disappeared[obj_id] = 0

                    used_col.add(col)
                    used_row.add(row)

                unused_row = set(range(0, D.shape[0])).difference(used_row)
                unused_col = set(range(0, D.shape[1])).difference(used_col)

                if D.shape[0] >= D.shape[1]:
                    for row in unused_row:
                        obj_id = object_id[row]
                        self.disappeared[obj_id] += 1

                        if self.disappeared[obj_id] > self.max_Disapper:
                            self.deregister_object(obj_id)

                else:
                    for col in unused_col:
                        self.register_object(centroid_cordinate[col])

            return self.objects
