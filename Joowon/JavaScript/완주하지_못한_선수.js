function solution(participant, completion) {
    var answer = '';
    let map = new Map();
    
    completion.forEach((com, index) => {
        let par = participant[index];
        
        map.set(par, (map.get(par) || 0) + 1);
        map.set(com, (map.get(com) || 0) - 1);
    });
    map.set(participant.at(-1), (map.get(participant.at(-1)) || 0) + 1); // participant가 completion보다 1더 크니 마지막 요소는 따로 처리함
    
    for(let key of map.keys()) {
        if (map.get(key)) {
            
            return key;
        }
    }
}

console.log(solution(["leo", "kiki", "eden"], 	["eden", "kiki"])); // 답: "leo"