function solution(progresses, speeds) {
    var answer = [0];
    let cnt = 0;
    let time = Math.ceil((100 - progresses[0]) / speeds[0]);

    progresses.forEach((percent, index) => {
        const delay = Math.ceil((100 - percent) / speeds[index]);

        if (time < delay) {
            time = delay;
            cnt += 1;
            answer.push(1);
        } else {
            answer[cnt] += 1;
        }
    });


    return answer;
}

console.log(solution([93, 30, 55], 	[1, 30, 5])); // 답: [2, 1]
console.log(solution([95, 90, 99, 99, 80, 99] , [1, 1, 1, 1, 1, 1])); // 답: [1, 3, 2]