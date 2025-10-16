# Conversor e Consulta de Temperaturas 🌦️

![Python](https://imgshields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-library-orange?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

Programa que realiza a conversão de temperaturas entre diferentes escalas (Celsius, Fahrenheit, Kelvin) e a consulta da temperatura (em graus Celsius) atual de qualquer cidade do mundo em tempo real.

---

## ✨ Funcionalidades

* Navegação simples através de um menu no terminal.
* **Conversões de Temperatura:**
    * Celsius para Fahrenheit e vice-versa.
    * Celsius para Kelvin e vice-versa.
    * Kelvin para Fahrenheit e vice-versa.
* Insira o nome de uma cidade para obter a temperatura atual em graus Celsius.

---

## 🌐 APIs Utilizadas

Este projeto utiliza os serviços de código aberto da [Open-Meteo](https://open-meteo.com/) para obter os dados meteorológicos.

* **Geocoding API:** Usada para converter o nome de uma cidade nas suas coordenadas geográficas (latitude e longitude).
* **Weather Forecast API:** Usada para obter a temperatura atual com base nas coordenadas geográficas.

---

## 🛠️ Tecnologias

* **Python 3:** Linguagem principal do projeto.
* **Biblioteca `requests`:** Para realizar as chamadas HTTP às APIs da Open-Meteo de forma simples e eficiente.

---

## 🫵 Como Usar

Para executar este projeto localmente, irá precisar do Python 3 instalado. Siga os passos abaixo.

### **1. Pré-requisitos**

* Ter o [Python 3](https://www.python.org/downloads/) instalado na sua máquina.
* Ter o [Git](https://git-scm.com/) instalado para clonar o repositório.

### **2. Instalação e Execução**

Abra o seu terminal e siga estes passos:

```bash
git clone [https://github.com/Letrares/app-clima-python.git]https://github.com/Letrares/app-clima-python.git)


cd app-clima-python
