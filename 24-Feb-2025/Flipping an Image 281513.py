# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ln = len(image)
        new_image = []
        for row in image:
            for i in range(ln//2):
                row[i],row[ln-i-1] = row[ln-i-1],row[i]
        for row in image:
            new_image.append([0 if i == 1 else 1 for i in row])
            
        return new_image