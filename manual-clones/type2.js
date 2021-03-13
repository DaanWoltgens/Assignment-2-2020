function pivotOrder(arr, pivot) {
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

function LowHighOrder(arr, pivot) {
     higher = [];
    lower = [];
    for ( let i = 0; i < arr.length; i++ ) {
        if ( arr[i] < pivot ) {
            lower.push( arr[i] );
        } else {
            higher.push( arr[i] );
        }
    }

    return lower.concat( higher );
}

function pivotOrder(arr, pivot) {
    largerThanPivot = [];
    smallerThanPivot = [];
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] < pivot) {
                smallerThanPivot.push(arr[i]);
            } else {
                largerThanPivot.push(arr[i]);
            }
        }

    return smallerThanPivot.concat(largerThanPivot);
}


function pivotOrder(inputList, limit) {
    higher = []; lower = [];
    for (let i = 0; i < inputList.length; i++) {
        if (inputList[i] < limit) { lower.push(inputList[i]); } 
        else { higher.push(inputList[i]); }
    }

    return lower.concat(higher);
}

function pivotOrder(arr, pivot) {
    /** Order an array based on a pivot
     * Input
     * Returns arr ordered such that all elements strictly smaller than pivot
     * occur first.
     */

    // initialize empty arrays
    higher = [];
    lower = [];
    // iterate over input array
    for (let index = 0; index < arr.length; index++) {
        // check whether the element belongs to the lower or higher list
        if (arr[index] < pivot) {
            lower.push(arr[index]);
        } else {
            higher.push(arr[index]);
        }
    }

    // concatenate and return
    return lower.concat(higher);
}

