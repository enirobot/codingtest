function solution(progresses, speeds) {
    var answer = [0];
    let cnt = 0;
    let time = Math.ceil((100 - progresses[0]) / speeds[0]);
    const len = progresses.length;

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