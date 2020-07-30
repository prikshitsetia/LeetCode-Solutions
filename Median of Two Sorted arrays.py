class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1=0
        p2=0
        m=len(nums1)
        n=len(nums2)
        li=[]
        while p1<=m-1 and p2<=n-1:
            if nums1[p1]<nums2[p2]:
                li.append(nums1[p1])
                p1+=1
            else:
                li.append(nums2[p2])
                p2+=1
        if p1==m and p2<=n-1:
            while p2<=n-1:
                li.append(nums2[p2])
                p2+=1
        elif p2==n and p1<=m-1:
            while p1<=m-1:
                li.append(nums1[p1])
                p1+=1
        ans=0
        l=len(li)
        if l%2==0:
            ans=(li[int(l/2)]+li[int(l/2)-1])/2
        else:
            ans=li[int(l/2)]
        return round(float(ans),1)
                
                
        