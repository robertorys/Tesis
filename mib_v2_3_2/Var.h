#ifndef VAR_H
#define VAR_H

#include <iostream>
#include <vector>
#include <set>
#include <optional>

class Var {
private:
    std::string name;        // Nombre de la variable
    std::set<int> values;    // Conjunto de valores que representan un evento
    std::optional<int> event; // Evento actual (usamos std::optional para manejar el "None" de Python)

public:
    // Constructor
    Var(const std::string& name, const std::set<int>& values);

    // Método para obtener los valores de la variable
    std::vector<int> getValues() const;

    // Método para resetear el evento
    void reset();

    // Método opcional si se quiere establecer el evento manualmente
    void setEvent(int newEvent);

    // Método para obtener el nombre de la variable (opcional)
    std::string getName() const;
};

#endif