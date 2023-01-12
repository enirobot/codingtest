function solution(priorities, location) {
    var answer = priorities.map((ele, i) => ({
        print: ele,
        myPrint: location === i
    }));
    let check = true;
    let cnt = 1;
    
    while (check) {
        const temp = answer.shift();
        
        if (answer.every(ele => temp.print >= ele.print)) {
            if (temp.myPrint) {
                check = false;
            } else {
                cnt += 1;
            }
        } else {
            answer.push(temp);
        }
    }
    
    
    return cnt;
}

console.log(solution([2, 1, 3, 2], 2)); // 답: 1
console.log(solution([1, 1, 9, 1, 1, 1], 0)); // 답: 5