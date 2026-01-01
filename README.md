# 🏢 Smart Office IoT Project

Projet réalisé dans le cadre du module **Internet des Objets (IoT)** - ENSAM Meknès  
**Année académique :** 2025-2026  
**Encadrant :** Mr. Brahim BAKKAS

## 👥 Équipe
- **LAKLACH Badr**
- **RHAZOUANI Alae**
- **AIT BOUKDIR Imane**

## Description
Conception et simulation d'un environnement de bureau intelligent (Smart Office) utilisant Cisco Packet Tracer. Le projet intègre divers capteurs et actuateurs IoT pour automatiser l'éclairage, la climatisation, le contrôle d'accès et la sécurité incendie.

## Objectifs
1. **Automatisation** : Réduire l'intervention manuelle pour l'éclairage et le contrôle de température
2. **Sécurité** : Contrôle d'accès RFID pour les zones restreintes
3. **Sûreté** : Système de détection d'incendie avec activation automatique des sprinklers

## Technologies Utilisées
- **Outil de simulation :** Cisco Packet Tracer v8.2
- **Protocoles :** Wi-Fi (WPA2-PSK), TCP/IP
- **Capteurs :** RFID Reader, Fire Monitor, Motion Sensor, Temperature Sensor, Thermostat
- **Actuateurs :** Smart Door, Fire Sprinkler, LED Lights, Ceiling Fan, AC, Furnace
- **Programmation :** Python (pour MCU)
- **IA Générative :** Nano Banana (génération maquette 3D)

## Structure du Projet
```
├── Documentation/          # Rapport et fiche projet
├── Simulation/            # Fichier Packet Tracer (.pkt)
├── Images/                # Captures d'écran et diagrammes
└── Scripts/               # Scripts Python pour MCU
```

## Installation et Exécution

### Prérequis
- Cisco Packet Tracer v8.2 ou supérieur
- Système d'exploitation : Windows/Linux/macOS

### Étapes
1. Télécharger le fichier `Smart_Office.pkt` depuis le dossier `Simulation/`
2. Ouvrir le fichier avec Cisco Packet Tracer
3. Le réseau est préconfiguré avec :
   - **Router :** 192.168.1.1
   - **IoT Server :** 192.168.1.10
   - **Admin PC :** 192.168.1.100 (DHCP)
4. Accéder à l'interface IoT Server via le navigateur du Admin PC : `http://192.168.1.10`
   - Username : `admin`
   - Password : `admin`

## Architecture Réseau
```
Internet (Cloud) → Router → Switch → IoT Server
                              ↓
                    ┌─────────┼─────────┬─────────┐
                    │         │         │         │
              Director GW  Conf GW  Work GW  Break GW
                    │         │         │         │
              (Capteurs & Actuateurs par zone)
```

## Zones du Bureau
1. **Entrance** : Contrôle d'accès RFID
2. **Director's Office** : Sécurité renforcée, HVAC personnel
3. **Conference Rooms (x3)** : Climatisation et détection incendie
4. **Work Area** : HVAC intelligent, éclairage automatique
5. **Break Areas & Toilets** : Ventilation automatisée

## Fonctionnalités Testées
- ✅ Contrôle d'accès RFID (employés/directeur)
- ✅ Détection incendie et activation sprinklers
- ✅ HVAC intelligent (chauffage/climatisation)
- ✅ Éclairage activé par détection de mouvement
- ✅ Ventilation automatique (toilettes)

## Documentation
Le rapport complet est disponible dans `Documentation/BADR_ALAE_IMANE_IoT_Rapport.pdf`

## Remerciements
Nous remercions Mr. Brahim BAKKAS pour son encadrement et ses conseils tout au long de ce projet.