#include <iostream>
#include "Var.h"

using namespace std;

int main(void) {
    set<int> valores = {0,1,2};
    Var X("X", valores);

    vector<int> valores_var =   X.getValues();
    cout << "Valores: ";
    for (int valor : valores_var) {
        cout << valor << " ";
    }
    cout << endl;

    return 0;
}

