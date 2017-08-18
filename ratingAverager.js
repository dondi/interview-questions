let ratingAverager = ratingInputList => {
    let total = 0;
    for (let i = 0; i < ratingInputList.length; i += 1) {
        total = ratingInputList[i].value + total;
    }

    return total / ratingInputList.length;
}
