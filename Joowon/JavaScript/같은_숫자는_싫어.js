function solution(arr)
{
    var answer = [];

    answer = arr.filter((num, i) => {
        if (i === 0) return true;
        return arr[i-1] !== num;
    });
    
    return answer;
}

console.log(solution([1,1,3,3,0,1,1])); // 답: [1, 3, 0, 1]
console.log(solution([4,4,4,3,3])); // 답: [4, 3]