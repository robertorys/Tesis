#ifndef DISTRIB_H
#define DISTRIB_H

#include "Var.h"
#include <unordered_map>
#include <vector>
#include <optional>

using namespace std;

//  Definir una función de hash para vector<int>
struct VectorHash {
    size_t operator()(const vector<int>& v) const {
        size_t seed = v.size();
        for (int i : v) {
           // Combinar los hashes de los elementos individuales del vector
           seed ^= hash<int>{}(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

class Distrib {
    private:
        unordered_map<vector<int>,float, VectorHash> table;
        vector<Var*> vars;
        optional<vector<Var*>> parents;
        
    public:

    // Constructor
    Distrib(const unordered_map<vector<int>,float, VectorHash>& table, const vector<Var*>& vars)
        : table (table), vars (vars) {}

    // Establecer las variables padres.
    void setParents(optional<vector<Var*>> parents);

    float P();

    float cond_P();

    float joint_P();
};


#endif