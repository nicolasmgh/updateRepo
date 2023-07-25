# updateRepo

Aplicación basada en Python que permite actualizar repositorios con un click!

# Nota de versión

¡Advertencia!

Esta aplicación se encuentra en una versión muy temprana y está en desarrollo activo. Puede contener errores y limitaciones. En un principio, fue creada únicamente para uso personal, pero decidí compartirla en su estado actual para aquellos que puedan encontrarla útil o deseen contribuir a su mejora.

**Aviso:** No se recomienda utilizar esta versión en producción o para proyectos críticos.

## Requisitos

Tener instalado Git

## Instalación

Clona este repositorio en tu máquina local o descarga la última release.
El .exe debe encontrarse entre los archivos del repositorio que estés queriendo actualizar.

# Uso

Ejecuta el script haciendo doble click en el updateRepo.exe
La aplicación automáticamente ejecutará los siguientes comandos.

git pull
git add .
git commit -m "updated via updateRepo"
git push origin main

Si todo se realizó normalmente, se cerrará la ventana del cmd.
De lo contrario, se mantendrá abierta con los errores que hayan.

# Contribuciones

¡Toda ayuda es bienvenida! Si encuentras algún problema, tienes una idea para una mejora o deseas colaborar, no dudes en hacerlo. Puedes abrir un issue o enviar una pull request, y estaré encantado de revisarlo y trabajar juntos para hacer que esta aplicación sea aún mejor.
