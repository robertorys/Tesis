#include "Var.h"
#include <iostream>
#include <vector>
#include <set>
#include <optional>

using namespace std;

// Método para obtener los valores de la variable.
vector<int> Var::getValues() const {
    vector<int> result;
    if (event.has_value()) {
        result.push_back(event.value());
    } else {
        result.insert(result.end(), values.begin(), values.end());
    }
    return result;
}

// Método para resetear el evento.
void Var::reset() {
    event.reset();  
}

// Método opcional si se quiere establecer el evento manualmente.
void Var::setEvent(int newEvent) {
    event = newEvent;
}

// Método para obtener el valor del evento
int Var::getEvent() {
    return event.value();
}

// Método para obtener el nombre de la variable.
string Var::getName() const {
    return name;
}

