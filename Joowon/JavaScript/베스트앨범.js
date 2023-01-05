function solution(genres, plays) {
    var answer = [];
    let map = new Map();
    let mapForSize = new Map();

    // 전체 재생횟수 카운팅
    genres.forEach((category, i) => {
        const num = plays[i];
        map.get(category) ? map.set(category, map.get(category) + num) : map.set(category, num);
    });

    answer = genres.map((category, i) => {
        return {
            category: category,
            num: plays[i],
            index: i
        };
    }).sort((a, b) => {
        if (a.category !== b.category) return map.get(b.category) - map.get(a.category);
        if (a.num !== b.num) return b.num - a.num;
        return a.index - b.index;
    }).filter(ele => {
        if (mapForSize.get(ele.category)) {
            if (mapForSize.get(ele.category) < 2) {
                mapForSize.set(ele.category, 2);

                return true;
            } else {
                return false;
            }
        } else {
            mapForSize.set(ele.category, 1);

            return true;
        }
    }).map(ele => ele.index);
    

    return answer;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])); // 답: [4, 1, 3, 0]
console.log(solution(["classic", "pop", "classic", "classic", "pop", "test"], [500, 600, 150, 800, 2500, 100])); // 답: [4, 1, 3, 0, 5]
console.log(solution(["classic", "pop", "classic", "classic", "pop", "test"], [500, 600, 150, 800, 600, 100])); // 답: [3, 0, 1, 4, 5]
console.log(solution(["classic", "classic", "classic", "classic", "classic"], [5, 5, 5, 5, 5])); // 답: [0, 1]
console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500])); // 답: [4, 1, 3, 0]
console.log(solution(["pop", "pop", "pop", "rap", "rap"], [45, 50, 40, 60, 70])); // 답: [1, 0, 4, 3]
console.log(solution(["classic"], [300])); // 답: [0]