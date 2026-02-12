# Studiova Bootstrap Template

Este proyecto es una plantilla web profesional, moderna y responsiva basada en Bootstrap 5.

## 🚀 Inicio Rápido

Para comenzar a editar y ver el proyecto en tu navegador:

1. **Instalar dependencias** (solo la primera vez):
   ```bash
   npm install
   ```

2. **Iniciar servidor de desarrollo**:
   ```bash
   npm start
   ```
   Esto abrirá el navegador y actualizará la página automáticamente con cada cambio.

## 📁 Estructura del Proyecto

*   `src/html/`: Páginas HTML del sitio (index.html, about-us.html, etc.).
*   `src/assets/scss/`: Archivos fuente de diseño (SASS/SCSS). **Edita aquí para cambiar colores y estilos.**
*   `src/assets/css/`: Archivos CSS compilados (generados automáticamente).
*   `src/assets/js/`: Scripts de JavaScript.
*   `src/assets/libs/`: Librerías externas (Bootstrap, AOS, Owl Carousel, etc.).

## 🛠️ Scripts Disponibles

*   `npm start`: Inicia el servidor local y el compilador de SCSS en tiempo real.
*   `npm run build:css`: Compila manualmente el archivo SCSS a CSS.

## ℹ️ Información Adicional

El proyecto utiliza un flujo de trabajo basado en **SASS**. No edites directamente los archivos en `src/assets/css/styles.css`, ya que se sobrescribirán al compilar el SCSS. Realiza tus cambios de estilo en `src/assets/scss/styles.scss` o sus parciales.