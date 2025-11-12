# 🔗 Configura un Enlace Troncal con VLANs en Cisco Packet Tracer

## 📘 Descripción del proyecto
En este laboratorio aprenderás a **configurar un enlace troncal (trunk)** entre switches Cisco utilizando **VLANs** en **Cisco Packet Tracer**.  
Este ejercicio te permitirá entender cómo se comunican múltiples VLANs entre diferentes switches y cómo se transporta la información a través de un único enlace físico.

🔗 **Video del laboratorio:**  
🎥 [Configura un Enlace Troncal con VLANs en Cisco Packet Tracer](https://youtu.be/OE97sHBV2EQ)  


---

## 🎯 Objetivos del proyecto

1. **Comprender el funcionamiento de los enlaces troncales (trunks):**  
   Analizar cómo los enlaces troncales permiten que múltiples VLANs viajen a través de un solo enlace entre switches.

2. **Configurar interfaces de switch como trunks:**  
   Utilizar los comandos CLI para activar el modo trunk y permitir el paso de varias VLANs.

3. **Verificar la propagación de VLANs entre switches:**  
   Observar cómo las VLANs definidas en un switch pueden comunicarse con las mismas VLANs en otro.

4. **Comprobar la conectividad entre hosts de distintas VLANs a través del trunk:**  
   Realizar pruebas de `ping` entre PCs pertenecientes a las mismas VLANs pero conectadas a diferentes switches.

---

## 🧰 Tecnologías y herramientas utilizadas

- Cisco Packet Tracer (versión 8.x o superior)  
- 2 Switches Cisco (modelo 2960 o equivalente)  
- PCs simuladas (para VLANs)  
- CLI (Command Line Interface)  
- Conocimientos básicos de VLANs y configuración de interfaces de red  

---

## 📂 Estructura del repositorio
TroncalVLANs_PacketTracer/
├── Configura un Enlace Troncal con VLANs en Cisco Packet Tracer.pkt ← Archivo del laboratorio (abrir con Packet Tracer)
├── Configura_un_Enlace_Troncal_con_VLANs_en_Cisco_Packet_Tracer.jpg ← Imagen de la topología del proyecto
└── README.md ← Documentación del laboratorio


---

## 🚀 Cómo usarlo

1. Descarga el archivo `.pkt` desde este repositorio.  
2. Ábrelo con **Cisco Packet Tracer 8.x o superior**.  
3. Observa la topología con dos switches y varios hosts.  
4. Ingresa a la CLI de cada switch y revisa las interfaces configuradas como trunks (`show interfaces trunk`).  
5. Prueba la conectividad entre dispositivos de la misma VLAN ubicados en switches diferentes.  

---

## 🌐 Topología visual

![Topología del laboratorio](Configura_un_Enlace_Troncal_con_VLANs_en_Cisco_Packet_Tracer.jpg)

---

## 📝 Notas adicionales

- Este laboratorio forma parte de la serie educativa de **El Networker TI**:  
  🎬 [Canal de YouTube - El Networker TI](https://www.youtube.com/@ElNetworkerTI)  
- Explora más proyectos y simulaciones de redes en mi repositorio principal:  
  💼 [GitHub - Packet Tracer Projects](https://github.com/TU_USUARIO/TU_REPO)

---


