# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

from copy import deepcopy

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = deepcopy(img)
        rows = len(img)
        cols = len(img[0])
        for row in range(rows):
            for col in range(cols):
                av = [[row,col],[row+1,col+1],[row+1,col],[row,col+1],[row-1,col-1],[row-1,col],[row,col-1],[row+1,col-1],[row-1,col+1]]
                av = [[r,c] for r,c in av if 0<=r and r<=rows-1 and 0<=c and c<=cols-1]
                avg , count = 0,len(av)

                for r, c in av:
                    avg += img[r][c]
                avg //= count
                new_img[row][col] = avg
        return new_img


