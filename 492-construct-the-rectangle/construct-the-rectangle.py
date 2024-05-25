class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 0: return [0,0]
        import math
        result=[area,1]
        for width in range(2,int(math.sqrt(area)+1)):
            if area % width == 0  and width <= area // width :
                result=[area // width,width] if area//width -width < result[0]- result[1] else [0,0]

        return result
        