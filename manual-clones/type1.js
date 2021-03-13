function pivotSplit(arr, pivot) {
    higher = [];
    lower = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) {
            lower.push(arr[i]);
        } else {
            higher.push(arr[i]);
        }
    }

    return lower.concat(higher);
}

function pivotSplit(arr, pivot) {
     higher = [];
    lower = [];
    for (let i = 0; i < arr.length; i++) {
            if (arr[i] < pivot) {
                lower.push(arr[i]);
            } else {
                higher.push(arr[i]);
            }
    }

    return lower.concat(higher);
}


function pivotSplit(arr, pivot) {
    higher = []; lower = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) { lower.push(arr[i]); } 
        else { higher.push(arr[i]); }
    }

    return lower.concat(higher);
}

function pivotSplit(arr, pivot) {
    // initialize empty arrays
    higher = [];
    lower = [];
    // iterate over input array
    for (let i = 0; i < arr.length; i++) {
        // check whether the element belongs to the lower or higher list
        if (arr[i] < pivot) {
            lower.push(arr[i]);
        } else {
            higher.push(arr[i]);
        }
    }

    // concatenate and return
    return lower.concat(higher);
}

