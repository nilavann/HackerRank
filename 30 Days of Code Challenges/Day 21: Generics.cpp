/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template <typename t>
void printArray(vector<t> elements){
    for(int i = 0;i < elements.size();i++)
        cout<<elements[i]<<endl;
}
