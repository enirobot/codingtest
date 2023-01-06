function solution(arr)
{
    var answer = [];
    const len = arr.length;

    answer = arr.filter((num, i) => {
        let check;

        if (i === 0) return true;

        if (arr[i-1] === num) {
            return false;
        } else {
            return true;
        }
    })
    
    return answer;
}

console.log(solution([1,1,3,3,0,1,1])); // 답: [1, 3, 0, 1]
console.log(solution([4,4,4,3,3])); // 답: [4, 3]