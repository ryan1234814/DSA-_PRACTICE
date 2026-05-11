class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maxArea=0
        while(left<=right):
            l=min(height[left],height[right])
            w=right-left
            area=l*w
            maxArea=max(maxArea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
