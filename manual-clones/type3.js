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

function lowHighSplit(arr, pivot, counter) {
     higher = [];
    lower = [];
    for (let i = 0; i < arr.length; i++) {
        counter++;
            if (arr[i] < pivot) {
                lower.push(arr[i]);
            } else {
                higher.push(arr[i]);
            }
    }

    return lower.concat(higher);
}


function pivotSplit(arr, pivot) {
    largerThanPivot = []; smallerThanPivot = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) { smallerThanPivot.push(arr[i]); } 
        else { largerThanPivot.push(arr[i]); }
    }

    result = smallerThanPivot.concat(largerThanPivot);
    return result;
}

function pivotSplit(inputList, splittingValue) {
    // initialize empty arrays
    higher = [];
    lower = [];
    // iterate over input array
    for (let i = 0; i < inputList.length; i++) {
        // check whether the element belongs to the lower or higher list
        if (inputList[i] < splittingValue) {
            lower.push(arr[i]);
        } else if (inputList[i] >= splittingValue) {
            higher.push(arr[i]);
        } else {
            print("Something went wrong...")
        }
    }

    // concatenate and return
    return lower.concat(higher);
}

