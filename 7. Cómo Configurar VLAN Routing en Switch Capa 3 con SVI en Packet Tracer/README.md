# 🧩 Cómo Configurar VLAN Routing en Switch Capa 3 con SVI en Packet Tracer

## 📘 Descripción del proyecto
En este laboratorio aprenderás a configurar **VLAN Routing utilizando un switch de Capa 3 (Layer 3)** y **SVIs (Switch Virtual Interfaces)** en **Cisco Packet Tracer**.  
Esta práctica te permitirá comprender cómo un **switch de capa 3 puede enrutar tráfico entre VLANs**, eliminando la necesidad de un router externo.

🔗 **Video del laboratorio:**  
🎥 [Cómo Configurar VLAN Routing en Switch Capa 3 con SVI en Packet Tracer](https://youtu.be/-z5mDQ6zIHI)  


---

## 🎯 Objetivos del proyecto

1. **Comprender el enrutamiento entre VLANs con SVI:**  
   Analizar cómo los switches de Capa 3 permiten la comunicación entre VLANs mediante interfaces virtuales.

2. **Crear VLANs y asignarlas a puertos específicos:**  
   Configurar VLANs en el switch y vincularlas a diferentes grupos de hosts.

3. **Configurar interfaces virtuales SVI para cada VLAN:**  
   Asignar direcciones IP a las SVIs para que actúen como gateways de cada red VLAN.

4. **Verificar la comunicación entre VLANs sin usar un router externo:**  
   Realizar pruebas de conectividad (`ping`) entre PCs de distintas VLANs para confirmar el enrutamiento interno.

---

## 🧰 Tecnologías y herramientas utilizadas

- Cisco Packet Tracer (versión 8.x o superior)  
- Switch Cisco de Capa 3 (modelo 3560 o equivalente)  
- PCs simuladas conectadas a diferentes VLANs  
- CLI (Command Line Interface)  
- Conocimientos de VLANs, SVI y enrutamiento básico  

---

## 📂 Estructura del repositorio

VLANRouting_SVI_PacketTracer/
├── Cómo Configurar VLAN Routing en Switch Capa 3 con SVI en Packet Tracer .pkt ← Archivo del laboratorio (abrir con Packet Tracer)
├── Como_Configurar_VLAN_Routing_en_Switch_Capa_3_con_SVI_en_Packet_Tracer.jpg ← Imagen de la topología del proyecto
└── README.md ← Documentación del laboratorio


---

## 🚀 Cómo usarlo

1. Descarga el archivo `.pkt` desde este repositorio.  
2. Ábrelo con **Cisco Packet Tracer 8.x o superior**.  
3. Observa la topología con el switch de Capa 3 y las VLANs configuradas.  
4. Revisa las interfaces virtuales (`show ip interface brief`) y las rutas configuradas (`show ip route`).  
5. Ejecuta pruebas de `ping` entre PCs de distintas VLANs para confirmar la conectividad.  

---

## 🌐 Topología visual

![Topología del laboratorio](Como_Configurar_VLAN_Routing_en_Switch_Capa_3_con_SVI_en_Packet_Tracer.jpg)

---

## 📝 Notas adicionales

- Este laboratorio forma parte de la serie educativa de **El Networker TI**:  
  🎬 [Canal de YouTube - El Networker TI](https://www.youtube.com/@ElNetworkerTI)  
- Encuentra más proyectos y laboratorios en mi repositorio principal:  
  💼 [GitHub - Packet Tracer Projects](https://github.com/TU_USUARIO/TU_REPO)

---

