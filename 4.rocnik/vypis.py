import os

def folders(path,depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path+"\\"+item) and item[0] not in ".$":
            #ak nie si prazdny tak do teba skocim a zvacsim hlbku
            if len(os.listdir(path+"\\"+item)) == 0:
                #ci ma podadresare a nie subory
                print("-" * depth, item)
            else:
                folders(path+"\\"+item,depth+1)
    #print(os.listdir(path))


folders("D:\\škola")
