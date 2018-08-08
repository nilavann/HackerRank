/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    let l = nums.map(function(s) { 
        if( s % 2 == 0)
            return s * 2;
        else
            return s * 3;});
    return l
}