# PoC_paLANTENNA

**Prueba de Concepto -- Transmisión por Emisiones Electromagnéticas en
Cable Ethernet**\
Inspirado en investigaciones tipo LANtenna\ https://arxiv.org/pdf/2110.00104 (Mordechai Guri,Ben-Gurion - University of the Negev, Israel)
Cyber-Security Research Center
Autor: Jeremías Palazzesi

------------------------------------------------------------------------

## Descripción General

**PoC_paLANTENNA** es una prueba de concepto experimental que demuestra
cómo un cable Ethernet puede comportarse como un emisor
electromagnético no intencional, permitiendo la transmisión de datos a
muy baja tasa mediante actividad de red controlada.

Este proyecto recrea, de forma simplificada y con fines educativos, el
concepto de transmitir información modulando deliberadamente el tráfico
Ethernet y detectando las emisiones RF resultantes utilizando un
receptor RTL-SDR.

Este proyecto está destinado exclusivamente a fines educativos y de
laboratorio en entornos controlados.

------------------------------------------------------------------------

## Concepto

El sistema funciona mediante:

-   Generación de ráfagas controladas de tráfico UDP\
-   Uso de la actividad eléctrica del cable Ethernet para producir
    emisiones EM medibles\
-   Captura de dichas emisiones con un RTL-SDR\
-   Detección de presencia de señal mediante umbral de potencia\
-   Codificación y decodificación en Morse (`.` y `_`) utilizando OOK
    (On-Off Keying)

No es un método práctico de exfiltración, sino un experimento de
investigación de canal lateral.

------------------------------------------------------------------------

## Arquitectura

    [ PC Transmisor ]
            |
            |  Modulación por ráfagas UDP
            v
      Cable Ethernet (UTP)
            |
            |  Emisión electromagnética
            v
    [ RTL-SDR + Receptor Linux ]
            |
            |  Detección de potencia
            v
     Decodificación Morse (tiempo real)

------------------------------------------------------------------------

## Componentes

### 1. Transmisor

Archivo: `tx_morse_lan.py`

-   Envía símbolos Morse utilizando ráfagas de tráfico UDP\
-   `.` → ráfaga corta\
-   `_` → ráfaga larga\
-   Silencio → separación de símbolos

Uso:

    python tx_morse_lan.py ...___...

Funciona en:

-   Windows\
-   Linux\
-   Cualquier sistema con Python 3

------------------------------------------------------------------------

### 2. Receptor

Archivo: `rx_morse_lan.py`

-   Utiliza RTL-SDR para monitorear una frecuencia fija\
-   Mide potencia promedio de señal RF\
-   Detecta presencia de señal\
-   Clasifica punto o raya según duración\
-   Decodifica Morse a ASCII en tiempo real

------------------------------------------------------------------------

## Requisitos

### Hardware

-   2 computadoras (TX y RX)\
-   Cable Ethernet UTP (preferentemente sin blindaje)\
-   RTL-SDR (por ejemplo RTL-SDR Blog V4)\
-   Antena básica VHF

### Software (Receptor -- Ubuntu)

    sudo apt install rtl-sdr python3-numpy
    pip install pyrtlsdr

Verificación del RTL-SDR:

    rtl_test

------------------------------------------------------------------------

## Configuración Inicial

### 1. Encontrar una Frecuencia Adecuada

1.  Abrir GQRX u otro visor de espectro\
2.  Escanear entre 50--300 MHz\
3.  Ejecutar el transmisor\
4.  Identificar un pico de señal que aparezca solo durante la
    transmisión\
5.  Ajustar `CENTER_FREQ` en el script receptor

------------------------------------------------------------------------

### 2. Ajustar Parámetros Críticos

Receptor:

-   `CENTER_FREQ`\
-   `GAIN`\
-   `THRESHOLD`\
-   `DOT_THRESHOLD`\
-   `LETTER_GAP`

Transmisor:

-   `DOT_DURATION`\
-   `DASH_DURATION`\
-   `SYMBOL_GAP`

Se requiere calibración según el entorno.

------------------------------------------------------------------------

## Recomendaciones de Laboratorio

-   Utilizar cable UTP sin blindaje (evitar STP)\
-   Mayor longitud de cable mejora la radiación\
-   Probar forzar la NIC a 100 Mbps\
-   Ubicar el RTL-SDR a 20--50 cm del cable inicialmente\
-   Minimizar interferencias RF cercanas

------------------------------------------------------------------------

## Limitaciones

-   Tasa de transmisión extremadamente baja\
-   Alta sensibilidad al ruido\
-   Requiere calibración manual\
-   Solo prueba de concepto\
-   No apto para transferencia real de datos

------------------------------------------------------------------------

## Aviso Ético

Este repositorio está destinado a:

-   Estudio académico\
-   Experimentación de canales laterales RF\
-   Entornos controlados de laboratorio

No utilizar esta técnica contra sistemas sin autorización explícita.

El autor no asume responsabilidad por usos indebidos.

------------------------------------------------------------------------

## Contexto de Investigación

Este proyecto se inspira en investigaciones académicas sobre canales
laterales electromagnéticos en cables Ethernet y técnicas de
exfiltración en redes air-gapped.

Recrea el concepto de manera simplificada con fines educativos.

------------------------------------------------------------------------

## Licencia

Licencia MIT
