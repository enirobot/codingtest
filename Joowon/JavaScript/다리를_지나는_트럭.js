function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let cnt = 0;
    let bridgeWeight = 0;
    let bridgeQue = [];

    while (bridgeQue || truck_weights) {
        if (bridgeQue && cnt === bridgeQue[0].time) {
            const bridge = bridgeQue.shift();

            bridgeWeight -= bridge.weight;
        }

        if (weight >= bridgeWeight + truck_weights[0]) {
            const truck = truck_weights.shift();

            bridgeWeight += truck;
            bridgeQue.push({weight: truck, time: cnt+bridge_length+1});
        }
    }


    return answer;
}

console.log(solution(2, 10, [7,4,5,6])); // 답: 8
console.log(solution(100, 100, [10])); // 답: 101
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])); // 답: 110