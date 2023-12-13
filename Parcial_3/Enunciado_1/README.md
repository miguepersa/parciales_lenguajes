En C++, la programación orientada a objetos (POO) permite la creación y manipulación de objetos.

### Clases y Objetos:

En C++, una clase es una plantilla que define la estructura y el comportamiento de un objeto. Un objeto es una instancia de una clase:

```cpp
class MiClase {
public:
    // Campos (variables miembro)
    int campo1;
    float campo2;

    // Constructor
    MiClase() {
        campo1 = 0;
        campo2 = 0.0f;
    }

    // Método
    void miMetodo() {
        // Código del método
    }
};
```

### Constructores:

Un constructor es un método especial que se llama automáticamente cuando se crea un objeto. Puedes tener varios constructores, incluido un constructor por defecto (sin parámetros) y constructores con parámetros:

```cpp
class Persona {
public:
    std::string nombre;
    int edad;

    // Constructor con parámetros
    Persona(std::string n, int e) {
        nombre = n;
        edad = e;
    }
};
```

### Métodos:

Los métodos son funciones que pertenecen a una clase y pueden manipular los datos de la clase. Pueden ser públicos, privados o protegidos. Un método público puede ser llamado desde fuera de la clase. Un método privado solo puede ser llamado desde dentro de la clase. Un método protegido es similar a uno privado, pero también puede ser accedido por clases derivadas:

```cpp
class Rectangulo {
private:
    int ancho;
    int altura;

public:
    // Constructor
    Rectangulo(int w, int h) : ancho(w), altura(h) {}

    // Método público
    int calcularArea() {
        return ancho * altura;
    }

private:
    // Método privado
    void metodoPrivado() {
        // Código del método privado
    }
};
```

### Acceso a Campos:

Los campos (variables miembro) pueden ser públicos, privados o protegidos. En general, se prefiere encapsular los campos y proporcionar métodos para acceder a ellos (Getters y setters):

```cpp
class Punto {
private:
    int x;
    int y;

public:
    // Constructor
    Punto(int x, int y) : x(x), y(y) {}

    // Métodos de acceso
    int obtenerX() const {
        return x;
    }

    int obtenerY() const {
        return y;
    }

    void establecerX(int nuevoX) {
        x = nuevoX;
    }

    void establecerY(int nuevoY) {
        y = nuevoY;
    }
};
```

En C++, el manejo de memoria es una parte crucial del desarrollo, y se puede realizar de manera explícita o implícita. Aquí se describen ambos enfoques:

### Manejo de Memoria Explícito (new/delete):

#### **Operadores `new` y `delete`:**
   - En C++, puedes asignar memoria dinámicamente usando el operador `new`. Este operador devuelve un apuntador al espacio de memoria asignado.

     ```cpp
     int *pEntero = new int; // Asigna memoria para un entero
     ```

   - Es responsabilidad del programador liberar la memoria asignada cuando ya no es necesaria utilizando el operador `delete`.

     ```cpp
     delete pEntero; // Libera la memoria asignada para el entero
     ```

   - Es importante evitar fugas de memoria (memory leaks) asegurándote de liberar toda la memoria asignada dinámicamente.

### Manejo de Memoria Implícito (Recolector de Basura):

En C++, no hay un recolector de basura (garbage collector) integrado como en algunos lenguajes de programación gestionados, como Java o C#. Sin embargo, puedes utilizar estrategias y librerias para gestionar automáticamente la memoria:

#### 1. **Smart Pointers:**
   - Los smart pointers son objetos que actúan como apuntadores, pero realizan un seguimiento automático de las referencias y liberan la memoria cuando ya no hay referencias.

     ```cpp
     #include <memory>

     std::unique_ptr<int> pEntero = std::make_unique<int>(); // Smart pointer único
     ```

   - `std::unique_ptr` y `std::shared_ptr` son tipos de smart pointers en la librería estándar de C++.

#### 2. **Contenedores de la STL:**
   - El uso de contenedores de la STL (Standard Template Library) como `std::vector`, `std::string`, etc., permite que la memoria se gestione automáticamente para los elementos que contienen.

     ```cpp
     #include <vector>

     std::vector<int> miVector; // El vector gestiona automáticamente la memoria
     ```

### Tipo de Asociacion en C++

C++ utiliza asociación estática de métodos. La resolución de métodos en C++ se realiza en tiempo de compilación y se basa en la firma (nombre y parámetros) de la función. Esto se conoce como enlace estático o vinculación estática. La elección de la función a llamar se realiza durante la fase de compilación.

La vinculación estática proporciona eficiencia en tiempo de ejecución, ya que no se necesita un mecanismo de búsqueda dinámica durante la ejecución del programa para determinar qué función debe llamarse.

En C++, la asociación dinámica se logra mediante el uso de funciones virtuales y clases base y derivadas. La palabra clave virtual se utiliza para marcar funciones en la clase base que pueden ser sobrescritas por las clases derivadas. El mecanismo de llamada a funciones virtuales utiliza apuntadores a funciones virtuales y una tabla de funciones virtuales (tabla vtable) para determinar qué función debe llamarse en tiempo de ejecución.

### Jerarquía de Tipos en C++:

#### 1. **Herencia:**
   - C++ admite herencia, lo que significa que puedes crear nuevas clases basadas en clases existentes. La herencia permite que una clase herede atributos y comportamientos de otra clase.

     ```cpp
     class Animal {
     public:
         void comer() { /* código para comer */ }
     };

     class Mamifero : public Animal {
     public:
         void amamantar() { /* código para amamantar */ }
     };
     ```

#### 2. **Herencia Múltiple:**
   - C++ permite la herencia múltiple, lo que significa que una clase puede heredar de múltiples clases base. Esto permite la combinación de características de varias clases en una nueva clase.

     ```cpp
     class Ave {
     public:
         void volar() { /* código para volar */ }
     };

     class AveMamifero : public Mamifero, public Ave {
     // ...
     };
     ```

#### 3. **Polimorfismo:**
   - C++ soporta el polimorfismo, que puede ser de dos tipos:
     - **Polimorfismo de tiempo de ejecución (dinámico):** Se logra mediante funciones virtuales y se activa usando apuntadores o referencias a la clase base.

       ```cpp
       class Forma {
       public:
           virtual void dibujar() { /* código para dibujar */ }
       };

       class Circulo : public Forma {
       public:
           void dibujar() override { /* código específico para dibujar un círculo */ }
       };
       ```

     - **Polimorfismo de tiempo de compilación (estático):** Se logra mediante sobrecarga de funciones y plantillas (si se considera el polimorfismo paramétrico).

#### 4. **Polimorfismo Paramétrico:**
   - C++ admite polimorfismo paramétrico a través de plantillas. Puedes crear funciones o clases que trabajen con tipos genéricos.

     ```cpp
     template <typename T>
     T suma(T a, T b) {
         return a + b;
     }

     int resultado = suma(5, 10);  // Llamada a la función con int
     float otroResultado = suma(3.14, 2.718);  // Llamada a la función con float
     ```

#### 5. **Manejo de Varianza:**
   - C++ admite covarianza y contravarianza en el contexto de apuntadores y referencias a clases base y derivadas.
     - **Covarianza:** 

       ```cpp
       class Base {};
       class Derivada : public Base {};

       Derivada objetoDerivado;
       Base* punteroBase = &objetoDerivado;  // Covarianza
       ```

     - **Contravarianza:** 

       ```cpp
       void funcion(Base* ptrBase) {}

       Derivada objetoDerivado;
       funcion(&objetoDerivado);  // Contravarianza
       ```