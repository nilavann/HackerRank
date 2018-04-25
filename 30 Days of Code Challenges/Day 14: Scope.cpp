	// Add your code here
    Difference(vector<int> ele){
        this->elements = ele;
    }
    void computeDifference(){
        int s = elements.size();
        this->maximumDifference = abs(elements[0] - elements[1]);
        for( int i = 0; i < s; i++){
            int res=0;
            for( int j = 0; j < s; j++){
                //printf("i=%d j=%d r=%d\n",elements[i],elements[j],abs(elements[i] - elements[j]));
                if( abs(elements[i] - elements[j]) > maximumDifference)
                    this->maximumDifference = abs(elements[i] - elements[j]);
            } 
        }
    }
    