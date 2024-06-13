class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        b = []
        for i in range(len(students)):
            if students[i] in seats:
                seats.remove(students[i])
            else:
                b.append(students[i])
        seats.sort()
        b.sort()
        moves = 0
        for i in b:
            min_seat = seats[0]
            while min_seat != i:
                moves += 1
                min_seat = min_seat -1 if min_seat > i else min_seat + 1
            seats.pop(0)
        
        return moves