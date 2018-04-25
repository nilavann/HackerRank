/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    for(var ch of s){
        if(ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u')
            console.log(ch);
    }
    for(var ch of s){
        if(ch !== 'a' && ch !== 'e' && ch !== 'i' && ch !== 'o' && ch !== 'u')
            console.log(ch);
    }
}