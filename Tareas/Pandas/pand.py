import pandas as pd
import numpy as np


def pandas(df):
    try:
        # LIMPIAR DATOS
        #
        #
        # Aqui vamos a eliminar los valores repetidos
        df = df.drop_duplicates()
        #

        #
        # Vamos a unificar los valores de los departamentos en mayusculas, para que Armenia, armenia sean ARMENIA

        df["Nombre departamento"] = df["Nombre departamento"].str.upper()
        #

        # VAMOS A PASAR TODOS LOS DATOS STRING A MAYUSUCULAS PARA FACILITAR EL ANALISIS
        df["Nombre municipio"] = df["Nombre municipio"].str.upper()
        df["Ubicación del caso"] = df["Ubicación del caso"].str.upper()
        df["Estado"] = df["Estado"].str.upper()
        df["Recuperado"] = df["Recuperado"].str.upper()
        #

        #

        # Tambien vamos a hacer que solo haya 2 sexos
        mapeo_sexo = {"f": "F", "F": "F", "m": "M", "M": "M"}
        df["Sexo"] = df["Sexo"].map(mapeo_sexo)
        #
        #

        # Cambiar valores nulos por 0 en algunas columnas
        valor_predefinido_para_nulos = 0
        df["Código DIVIPOLA municipio"].fillna(valor_predefinido_para_nulos)
        df["Código DIVIPOLA departamento"].fillna(valor_predefinido_para_nulos)
        #

        #

        # Pasar todas las fechas al formato de fechas de pandas
        df["fecha reporte web"] = pd.to_datetime(df["fecha reporte web"])
        df["Fecha de notificación"] = pd.to_datetime(df["Fecha de notificación"])
        df["Fecha de inicio de síntomas"] = pd.to_datetime(df["Fecha de inicio de síntomas"])
        df["Fecha de muerte"] = pd.to_datetime(df["Fecha de muerte"])
        df["Fecha de diagnóstico"] = pd.to_datetime(df["Fecha de diagnóstico"])
        df["Fecha de recuperación"] = pd.to_datetime(df["Fecha de recuperación"])
        #

        #

        # agregar columnas de dia,mes,año al nuevo df
        df["Dia"] = df["Fecha de notificación"].dt.day
        df["Mes"] = df["Fecha de notificación"].dt.month
        df["Año"] = df["Fecha de notificación"].dt.year
        #

        # Voy a ordenar en df en orden alfabetico de departamentos
        df = df.sort_values(by="Nombre departamento")
        #

        #
        # Extraer en vectores NUMPY los fallecidos, graver, leves por cada ciudad del departamento(Nariño en este caso)
        # Como ya pasamos todos los departamentos a mayusculas no deberiamos de tener problema

        df_nar = df[df["Nombre departamento"] == "NARIÑO"]# Aqui estamos sacando un nuevo df, con los datos de NARIÑO
        print(df_nar)
        #
        municipios =df_nar["Nombre municipio"].unique()
        for municipio in municipios:
            contador_leve = (df_nar[(df_nar["Nombre municipio"] == municipio) and (df_nar["Estado"] == "LEVE")]).shape[0]
            contador_fallecido = (df_nar[(df_nar["Nombre municipio"] == municipio) and (df_nar["Estado"] == "FALLECIDO")]).shape[0]
            contador_grave = (df_nar[(df_nar["Nombre municipio"] == municipio) and (df_nar["Estado"] == "GRAVE")]).shape[0]
            print(f"Del municipio {municipio}, los pacientes leves son {contador_leve}")
            print(f"Del municipio {municipio}, los pacientes fallecidos son {contador_fallecido}")
            print(f"Del municipio {municipio}, los pacientes graves son {contador_grave}")
        #

        #
        #Mirar los dias transcurridos que han pasado entre la primera fecha y la ultima
            #Primero eliminamos las filas donde hayan fehas repetidas nulas
        sin_fechas_rep = df["Fecha de notificación"].dropna() #Aqui hacemos un nuevo df con solo la columna de "Fecha de notificacion"
        primera_fecha = sin_fechas_rep.max()
        ultima_fecha = sin_fechas_rep.min()
        dias_transcurridos = primera_fecha - ultima_fecha
        print(f"Los dias trasncurridos en de la primera a la ultima fecha es {dias_transcurridos}")

        #Muertes de hombres y mujeres para las fechas de la anterior columna(Me supongo que es para la columna de fechas de notificacion)
        muertes_hombres = df[df["Sexo"]=="M"] & df[df["Recuperado"]=="FALLECIDO"]
        numero_muertes_h = muertes_hombres.shape[0]
        muertes_mujeres = df[df["Sexo"]=="F"] & df[df["Recuperado"]=="FALLECIDO"]
        nu_muertes_f = muertes_mujeres.shape[0]

        #Recuperados de hombres y mujeres
        muertes_hombres = df[df["Sexo"]=="M"] & df[df["Recuperado"]=="RECUPERADO"]
        numero_recuperados_h = muertes_hombres.shape[0]
        muertes_mujeres = df[df["Sexo"]=="F"] & df[df["Recuperado"]=="RECUPERADO"]
        numero_recuperados_f = muertes_mujeres.shape[0]
        #
        
        #Con esto podemos armar la matriz de [[muertes hombres, muertes mujeres][recuperados hombres, recuperado mujeres]]
        matriz = np.array([[numero_muertes_h, nu_muertes_f][numero_recuperados_h, numero_recuperados_f]])
        print(matriz)


        # 
        #Exportar una nueva tabla donde solo aparezca el dataframe de un deaprtamento
        desktop_path = ("C:/Users/HP/OneDrive - uqvirtual.edu.co/Escritorio/progra/")

        # Nombre del archivo CSV de salida
        output_file = "Nariño.csv"

        # Ruta completa del archivo de salida
        output_path = desktop_path + output_file

        # Guarda el DataFrame limpio como un archivo CSV en el escritorio
        df_nar.to_csv(output_path, index=False)
        print("El archivo se exporto con exito")

    except Exception as e:
        print("Error:", str(e))


def inicializar_funcion():
    try:
        df = pd.read_csv("repaso_extra/Analisis de datos/Casos_positivos_de_COVID-19_en_Colombia._20231026.csv",sep=",",header=0)
        # Visualizar las primeras 5 columnas----> df.iloc[filas,columnas]
        encabezado = df.iloc[:, :5]  # df.iloc[desde:hasta , desde:hasta]
        print(encabezado)
        #pandas(df)

    except Exception as e:
        print("Error:", str(e))

inicializar_funcion()
