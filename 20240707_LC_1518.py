class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        empty = numBottles
        numBottles = 0

        while empty >= numExchange:
            numBottles += empty//numExchange
            empty = empty%numExchange

            drink += numBottles
            empty += numBottles
            numBottles = 0
        return drink