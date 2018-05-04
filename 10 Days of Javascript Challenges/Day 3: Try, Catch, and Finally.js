/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    let oldString = s;
    try{
        //convert string to list
        s = s.split("");
        //reverse the list
        s.reverse();
        //convert array to string
        s = s.join("");
    }
    catch(e){
        console.log(e.message);
    }
    finally{
        if( oldString === s)
            console.log(oldString);
        else
            console.log(s);
    }
}