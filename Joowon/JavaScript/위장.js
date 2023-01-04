function solution(clothes) {
    var answer = 1;
    let clothMap = new Map();
    
    clothes.forEach(cloth => {
        clothMap.get(cloth[1]) ? clothMap.set(cloth[1], clothMap.get(cloth[1]) + 1) : clothMap.set(cloth[1], 2);
    });
    clothMap.forEach((num, cloth) => {
        answer *= num;
    });
    answer -= 1; // 모든 옷을 입지 않은 경우를 빼줘야함
    
    
    return answer;
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])); // 답: 5