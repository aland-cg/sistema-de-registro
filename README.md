# sistema-de-registro
Sistema Clínico Local Básico de Registro y Consulta de Pacientes


# Sistema Clínico Local

## Descripción general

El Sistema Clínico Local es una herramienta digital diseñada para facilitar el registro y consulta de información básica de pacientes durante actividades académicas, jornadas de salud y prácticas supervisadas.

Su objetivo principal es reducir errores de captura, mejorar la organización de los datos y permitir una consulta rápida de la información registrada.

## ¿Qué hace el sistema?

El sistema permite registrar:

* Nombre del paciente.
* Edad.
* Presión arterial.
* Frecuencia cardiaca.
* Saturación de oxígeno (SpO₂).
* Temperatura corporal.
* Glucosa capilar.

Además, cada registro almacena automáticamente:

* Fecha de captura.
* Hora de captura.

Toda la información queda almacenada localmente para su consulta posterior.

## ¿Cómo funciona?

1. El operador captura los datos del paciente.
2. El sistema verifica que los valores ingresados estén dentro de rangos razonables.
3. Si los datos son válidos, se almacenan automáticamente.
4. Los registros pueden consultarse posteriormente desde una tabla organizada.

## Beneficios

* Reduce errores de captura.
* Organiza la información de manera uniforme.
* Permite consultar registros anteriores.
* Facilita el seguimiento de la atención realizada.
* Ayuda a estudiantes y personal en formación a practicar el registro estructurado de información clínica.

## Alcance actual

Esta versión corresponde a un Producto Mínimo Viable (MVP).

Su propósito es validar el funcionamiento del sistema en un entorno controlado y recopilar retroalimentación de los usuarios antes de incorporar funciones más avanzadas.

## Tecnologías utilizadas

* Python
* Flask
* SQLite
* HTML

## Filosofía del proyecto

El sistema está diseñado bajo un enfoque de simplicidad, resiliencia y continuidad operativa.

Cada función incorporada debe aportar valor real al usuario, evitando complejidad innecesaria y priorizando la estabilidad, facilidad de uso y mantenimiento del sistema.

## Estado del proyecto

Versión: 0.2

Estado: MVP funcional

Funciones implementadas:

* Registro de pacientes.
* Validación básica de datos.
* Almacenamiento local.
* Consulta de registros.
* Registro automático de fecha y hora.
