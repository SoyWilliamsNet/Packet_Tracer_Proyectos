# 🛰️ Proyecto: Mi Primera Red en Cisco Packet Tracer

Este repositorio corresponde al laboratorio explicado en el vídeo _“Aprende a crear tu PRIMERA RED en CISCO Packet Tracer”_.  
En él construiremos una topología básica de red con un router, un switch y dos PCs, siguiendo paso a paso la explicación y práctica para quienes están comenzando con redes.

## 📋 Objetivos del proyecto
- Crear una topología simple usando Cisco Packet Tracer.  
- Entender cómo conectar un router a un switch y luego a las PCs.  
- Configurar direccionamiento IPv4 básico (IP, máscara, gateway) en los dispositivos finales.  
- Verificar conectividad entre las PCs mediante `ping`.  
- Introducir conceptos fundamentales de redes: router, switch, cableado, subredes.

## ⚙️ Tecnologías y herramientas utilizadas
- Cisco Packet Tracer (versión 8.x o compatible)  
- Router Cisco (por ejemplo, modelo 2911)  
- Switch Cisco (por ejemplo, serie 2960)  
- PCs simuladas dentro de Packet Tracer  
- Tema orientado a preparación para la certificación Cisco DEVNET Associate (especialmente en la parte de redes básicas y topologías)

## 🧩 Estructura del repositorio
MiPrimeraRed_PacketTracer/

├── MiPrimeraRed.pkt

├── topologia.jpg

└── README.md

## 🚀 Cómo usarlo
1. Descarga o clona este repositorio en tu equipo.  
2. Abre el archivo `MiPrimeraRed.pkt` con Cisco Packet Tracer.  
3. En los dispositivos PC1 y PC2, asegúrate de que la dirección IP y gateway están correctamente configurados (tal como se muestra en el vídeo).  
4. En el router, verifica que la interfaz conectada al switch esté activada (`no shutdown`) y tenga la IP asignada correctamente.  
5. En una de las PCs, abre la terminal y ejecuta:
   ```bash
   ping <IP de la otra PC>
Si recibes respuestas, la configuración es correcta.
6. ¡Listo! Explora la topología, haz modificaciones (por ejemplo: cambia direcciones o añade un switch extra) para practicar.

🖼️ Visual de la topología

![Topología de Mi Primera Red](topologia.jpg)

📌 Notas adicionales

Ideal para principiantes que quieren entender los fundamentos de redes.

Puedes usar este proyecto como base para expandir: por ejemplo, añade VLANs, routers extra, segmentación de red, y así prepararte mejor para los temas de certificación.

Asegúrate de documentar tus cambios: cada vez que modifiques la topología, añade una breve descripción en este README o crea un nuevo archivo CHANGELOG.md
