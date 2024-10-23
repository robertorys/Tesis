#include <iostream>
#include <unordered_map>
#include <vector>
#include <optional>
#include "Var.h"

//  Definir una función de hash para std::vector<int>
struct VectorHash {
    std::size_t operator()(const std::vector<int>& v) const {
        std::size_t seed = v.size();
        for (int i : v) {
           // Combinar los hashes de los elementos individuales del vector
           seed ^= std::hash<int>{}(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};



class Distrib {
    private:
        std::unordered_map<int,float> table;
        std::vector<Var> vars;
        std::optional<std::vector<Var>> parents;
        
    public:

    Distrib(const std::unordered_map<int,float>& table, const std::vector<Var>& vars,
        const std::optional<std::vector<Var>>& parents) :
        table(table), vars(vars), parents(parents) {}

    float P() {

    }

};
