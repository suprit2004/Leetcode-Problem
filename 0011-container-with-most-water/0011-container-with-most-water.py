class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointers
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            shoter_height=min(height[left],height[right])
            area=width*shoter_height
            max_area=max(max_area,area)
            #moving the shoter pointer:
            if height[left]<height[right]:
                left +=1
            else:
                right-=1
        return max_area
        