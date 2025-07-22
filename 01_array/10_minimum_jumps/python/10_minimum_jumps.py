class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        
        # Base case: If array has 0 or 1 element, no jumps needed.
        if n <= 1:
            return 0 

        # If the first element is 0 and the array has more than one element,
        # it's impossible to move from the start.
        if arr[0] == 0 and n > 1:
            return -1

        jumps = 0
        current_jump_end = 0  # The end of the farthest reach with current jumps
        farthest_reach = 0    # The farthest index reachable from any point so far

        # Iterate through the array. We go up to n-1 because if we reach n-1,
        # we've already counted the jump to get there.
        for i in range(n - 1):
            # Update the farthest index we can reach from the current position 'i'
            farthest_reach = max(farthest_reach, i + arr[i])

            # If current index 'i' goes beyond what we could reach with previous jumps,
            # it means we are stuck. This covers cases like [0, 10, 20].
            if i > farthest_reach:
                return -1

            # If we've reached the end of the current jump's range
            if i == current_jump_end:
                # Increment jump count
                jumps += 1
                # Update the new end of the jump range to the farthest_reach we've found
                current_jump_end = farthest_reach
                
                # Optimization: If the farthest_reach is already beyond or at the last index,
                # we don't need further jumps.
                if current_jump_end >= n - 1:
                    return jumps
        
        # If the loop finishes, it means we've successfully reached or passed the end.
        # The 'jumps' variable holds the minimum jumps required.
        # This condition is typically implicitly handled by the `if current_jump_end >= n - 1:`
        # but serves as a final safety net.
        if current_jump_end >= n - 1:
            return jumps
        else:
            return -1 # Should only be hit if the initial `if arr[0] == 0` didn't catch it and `i > farthest_reach` wasn't enough.