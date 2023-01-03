function solution(nums) {
    var answer = 0;
    const numLen = nums.length / 2;
    const uniqueNums = new Set(nums);
    
    answer = uniqueNums.size > numLen ? numLen : uniqueNums.size;
    
    
    return answer;
}