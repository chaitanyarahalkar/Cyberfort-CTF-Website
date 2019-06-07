#include <iostream>

using std::cout;

using std::string;

using std::cin;

int f(int i){

	if(i == 0)
		return 0;
	if(i == 1)
		return 1;

	return f(i-1) + f(i-2);

}

string encrypt(string plain){

	for(int i=0;i<plain.length();i++){
		plain[i] = (plain[i]-'a' + f(i)%26) %26;
		plain[i]+='a';
	}
	
	return plain;
}

int main(int argc, char const *argv[])
{

	// program accepts only lower case alphabets.
	cout<<encrypt("teststring")<<"\n";
	
	return 0;
}