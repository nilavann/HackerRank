class Student :  public Person{
	private:
		vector<int> testScores;  
	public:
        /*	
        *   Class Constructor
        *   
        *   Parameters:
        *   firstName - A string denoting the Person's first name.
        *   lastName - A string denoting the Person's last name.
        *   id - An integer denoting the Person's ID number.
        *   scores - An array of integers denoting the Person's test scores.
        */
        // Write your constructor here
        Student(string fN, string lN, int ident, vector<int> scores): Person(fN, lN, ident){
            this->testScores = scores;
        }
        /*	
        *   Function Name: calculate
        *   Return: A character denoting the grade.
        */
        char calculate(){
            int n = testScores.size();
            int sum = 0;
            for( int i = 0; i < n; i++)
                sum += testScores[i];
            int ave = sum/n;
            char g;
            if(ave >= 90)
                g = 'O';
            else if(ave >= 80)
                g = 'E';
            else if(ave >= 70)
                g = 'A';
            else if(ave >= 55)
                g = 'P';
            else if(ave >= 40)
                g = 'D';
            else
                g = 'T';
            return g;
        }
        
        // Write your function here
};