#include <iostream>
#include <unordered_map>
#include <vector>
#include <optional>
#include "Var.h"
#include "Distrib.h"

using namespace std;

void Distrib::setParents(optional<vector<Var*>> parts) {
    parents = parts;
}

float Distrib::P() {
    if(parents.has_value()) {
        return Distrib::cond_P();
    } else {
        return Distrib::joint_P();
    }
}

float Distrib::joint_P() {
    vector<int> vars_key (vars.size());

    int i = 0;
    for (Var* v : vars) {
        vars_key[i] = v->getEvent();
        i ++;
    }
    return table[vars_key];
}

float Distrib::cond_P() {
    vector<int> vars_key (vars.size());
    vector<int> parents_key (parents.value().size());

    int i = 0;
    for (Var* v : vars) {
        vars_key[i] = v->getEvent();
        i ++;
    }
    i = 0;
    for (Var* v : parents.value()) {
        parents_key[i] = v->getEvent();
        i ++;
    }

    return table[vars_key];
}