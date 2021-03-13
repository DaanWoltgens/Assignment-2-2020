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

function pivotOrder(arr, pivot) {
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


function pivotOrder(arr, pivot) {
    higher = []; lower = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) { lower.push(arr[i]); } 
        else { higher.push(arr[i]); }
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

