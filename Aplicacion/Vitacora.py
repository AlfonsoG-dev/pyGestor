"""
Crear la vitacora donde se almacena la informacion del desarrollo del proyecto
<pre> importar el modulo o complemento log
<post> crear la vitacora con sus especificaciones
"""
import logging as log
"configurar log con mensaje en fecha, nivel, archivo, linea, guardar en documentos"
log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s', 
                datefmt='%I:%M:%S:%S', handlers=[
                    log.FileHandler('Documentos\capaDatos.log'),
                    log.StreamHandler()
                ])
"Reglas de la vitacora"
if __name__ == '__main__':
    "verificacion para debug"
    log.debug("Mensaje para debugg")
    "verificacion para errores"
    log.info("Mensaje de Error")
    "verificacion de peligro"
    log.warning("Mensaje de alerta")
    "verificacion de error critico"
    log.critical("Mensaje critico")