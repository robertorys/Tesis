#include "Var.h"
#include <iostream>
#include <vector>
#include <set>
#include <optional>

class Var {
private:
    std::string name;
    std::set<int> values;
    std::optional<int> event;
public:
    // Constructor
    Var(const std::string& name, const std::set<int>& values) 
        : name(name), values(values), event(std::nullopt) {}
    
    // Método para obtener los valores de la variable
    std::vector<int> getValues() const {
        std::vector<int> result;
        if (event.has_value()) {
            result.push_back(event.value());
        } else {
            result.insert(result.end(), values.begin(), values.end());
        }
        return result;
    }

    // Método para resetear el evento
    void reset() {
        event.reset();  
    }

    // Método opcional si se quiere establecer el evento manualmente
    void setEvent(int newEvent) {
        event = newEvent;
    }
};