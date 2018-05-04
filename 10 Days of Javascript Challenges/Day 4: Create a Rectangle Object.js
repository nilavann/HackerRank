/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    var rec = new Object();
    rec.length = a;
    rec.width = b;
    rec.perimeter = (2 * a) + (2 * b);
    rec.area = a * b;
    return rec;
}