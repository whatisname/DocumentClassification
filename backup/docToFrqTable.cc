// Convert taged document into frequency table
// Author: XX
// Time: 1/10/2020

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
		// if (argc != 6)
	// {
	// 	cout << "usage: seedNumber dimX dimY blocksize ifStartNewLine" << endl;
	// 	exit(-1);
	// }
	// string newLine = argv[5]; // if start a new line in log file

	string inputname = "forum.data";
	ifstream inputfile;
  ofstream outputFile;
	
	// 1. open file
  inputfile.open(inputname.c_str(), ios::binary);
	if(!inputfile)
  {
    cout << "File not found!" << endl;
    exit(-1);
  }

  // 2. read file into stream
  stringstream ss;
  ss << inputfile.rdbuf();
  inputfile.close();

  // 3. read values into a 2D vector
  string line = "";
  string tag = "";
  string word = "";
  int line_index = 0;
	vector<vector<string>> docs;
	// vector<vector<int>> docs_count; //TODO
	vector<string> tags;

  while(getline(ss, line)) {
  	stringstream lines;
  	lines << line;
  	lines >> tag;
  	tags.push_back(tag);
  	docs.push_back(vector<int> );
  	for(!lines.eof()) {
  		lines >> word; // TODO
  	}
  	line_index ++;
  	if (i == 100) break;
  }
  cout << i;

	// file.open(name, fstream::app);

	// int repeat = 10;
	// for (int j=50; j <= 500; j += 50)
	// {
	// 	file << "./v " << j << " 5000 5000 500 y" << endl;
	// 	for (int i = 1; i < repeat; i++){
	// 	file << "./v " << j << " 5000 5000 500 n" << endl;
	// 	}
	// 	file << endl;
	// }

	// file.close();
	return 1;


}