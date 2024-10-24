#ifndef VAR_H
#define VAR_H

#include <iostream>
#include <vector>
#include <set>
#include <optional>

using namespace std;

class Var {
private:
    string name;        // Nombre de la variable
    set<int> values;    // Conjunto de valores que representan un evento
    optional<int> event; // Evento actual (usamos optional para manejar el "None" de Python)

public:
    // Constructor
    Var(const string& name, const set<int>& values)
        : name(name), values(values), event(nullopt) {}

    // Método para obtener los valores de la variable
    vector<int> getValues() const;

    // Método para resetear el evento
    void reset();

    // Método para establecer el evento
    void setEvent(int newEvent);

    // Método para obtener el valor del evento
    int getEvent();

    // Método para obtener el nombre de la variable (opcional)
    string getName() const;
};

#endif