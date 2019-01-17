class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        N = len(gas)
        for start in range(0,N):
            res_gas = gas[start]-cost[start]
            cur = (start+1)%N
            #从当前位置向后走到出发位置之前
            while cur != start and res_gas>=0:
                res_gas += gas[cur]-cost[cur]
                cur = (cur+1)%N
            #最后一步，看是否可以走回当前位置，即判断当前油量是否>=0,是则可以循环继续，
            if res_gas>=0:
                return start
        return -1

    def canCompleteCircuitAdvance(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        N = len(gas)
        res_gas = [g-c for g,c in zip(gas,cost)]
        index_candidate = [i for i,res in enumerate(res_gas) if res>=0]
        
        for start in index_candidate:
            cur_gas = res_gas[start]
            cur = (start+1)%N
            
            while cur != start and cur_gas >= 0:
                cur_gas+= res_gas[cur]
                cur = (cur+1)%N
            
            if cur_gas>=0:
                return start
        return -1

               
            
                