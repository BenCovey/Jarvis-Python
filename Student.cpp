#include <conio.h>
#include <iostream>
#include <string>
#include "Header.h"

using namespace std;
//Prototypes




string Name = "Test";
int numCourses;
string * courseList = new string[5];


void setName(string name) {
	Name = name;
	cout << Name;
};

string getName() {
	return Name;
};




