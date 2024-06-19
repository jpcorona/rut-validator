# RUT Validator

A simple Python library to validate Chilean RUTs.

## Installation

```bash
pip install rut-validator

Manual de Implementación y Uso de rut_validator
1. Instalación
Para instalar la librería rut_validator, puedes usar pip. Asegúrate de tener instalado pip en tu sistema.

bash
Copy code
pip install rut-validator
2. Uso Básico
A continuación se muestra cómo usar la librería para validar un RUT chileno.

Ejemplo de Uso
python
Copy code
from rut_validator import valrut

# Ejemplos de RUTs válidos
print(valrut("12.345.678-5"))  # Debería retornar True
print(valrut("12345678-5"))    # Debería retornar True

# Ejemplos de RUTs inválidos
print(valrut("12.345.678-9"))  # Debería retornar False
print(valrut("12345678-9"))    # Debería retornar False
3. Detalles Técnicos
Función valrut
La función valrut es el núcleo de la librería y se utiliza para validar RUTs. Internamente, esta función realiza los siguientes pasos:

Limpieza del RUT: Se eliminan caracteres no numéricos, excepto la 'K'.
Cálculo del Dígito Verificador: Se calcula el dígito verificador utilizando el algoritmo estándar para RUTs chilenos.
Validación: Se compara el dígito verificador calculado con el proporcionado para determinar la validez del RUT.
4. Ejecución de Pruebas
Para asegurarte de que todo funcione correctamente, puedes ejecutar las pruebas unitarias incluidas en la librería.

Paso 1: Clona el repositorio
bash
Copy code
git clone https://github.com/tuusuario/rut_validator.git
cd rut_validator
Paso 2: Instala las dependencias de desarrollo
Si es necesario, crea un entorno virtual y activa el entorno.

bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
Paso 3: Ejecuta las pruebas
bash
Copy code
python -m unittest discover tests
5. Contribución
Si deseas contribuir a la librería, sigue estos pasos:

Clona el repositorio:

bash
Copy code
git clone https://github.com/tuusuario/rut_validator.git
cd rut_validator
Crea una rama nueva:

bash
Copy code
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y haz commit:

bash
Copy code
git add .
git commit -m "Agrega nueva funcionalidad"
Sube tus cambios y crea un pull request:

bash
Copy code
git push origin feature/nueva-funcionalidad
6. Licencia
Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, revisa el archivo LICENSE.

7. Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactar al autor:

Autor: Tu Nombre
Correo: tu.email@example.com
Repositorio GitHub: GitHub
