function solution(s){
    var answer = true;
    let cnt = 0;
    
    for (let ele of s) {
        cnt += ele === '(' ? 1 : -1;
        
        if (cnt < 0) return false;
    }
    

    return cnt === 0 ? true : false;
}

console.log(solution("()()")); // 답: true
console.log(solution("(()(")); // 답: false