from ultralytics import YOLO
import time
import streamlit as st
import cv2
import settings
import threading
import pygame 

pygame.init()
pygame.mixer.init()

alert_general = pygame.mixer.Sound("sons/alerta.mp3")
alert_cellphone = pygame.mixer.Sound("sons/celular.mp3")
channel_cellphone = pygame.mixer.Channel(0)
alert_bat_cellphone = pygame.mixer.Sound("sons/bateria_de_celular.mp3")
channel_bat_cellphone = pygame.mixer.Channel(1)
alert_battery = pygame.mixer.Sound("sons/bateria.mp3")
channel_battery = pygame.mixer.Channel(2)
alert_needle = pygame.mixer.Sound("sons/seringa.mp3")
channel_needle = pygame.mixer.Channel(3)
alert_syringe = pygame.mixer.Sound("sons/agulha.mp3")
channel_syringe = pygame.mixer.Channel(4)
alert_scorpion = pygame.mixer.Sound("sons/escorpiao.mp3")
channel_scorpion = pygame.mixer.Channel(5)

def sleep_and_clear_success():
    time.sleep(3)
    st.session_state['recyclable_placeholder'].empty()
    st.session_state['non_recyclable_placeholder'].empty()
    st.session_state['hazardous_placeholder'].empty()

def load_model(model_path):
    model = YOLO(model_path)
    return model

def classify_waste_type(detected_items):
    cellphone = set(detected_items) & set(settings.CELLPHONE)
    non_cellphone = set(detected_items) & set(settings.CELLPHONE_BATTERY)
    battery = set(detected_items) & set(settings.BATTERY)
    needle = set(detected_items) & set(settings.NEEDLE)
    syringe = set(detected_items) & set(settings.SYRINGE)
    scorpion = set(detected_items) & set(settings.SCORPION)
    
    return cellphone, non_cellphone, battery, needle, syringe, scorpion

def remove_dash_from_class_name(class_name):
    return class_name.replace("_", " ")

def _display_detected_frames(model, st_frame, image):
    image = cv2.resize(image, (640, int(640 * (9/16))))
    
    # Inicializa os placeholders e variáveis no session_state se ainda não existirem
    if 'unique_classes' not in st.session_state:
        st.session_state['unique_classes'] = set()

    if 'recyclable_placeholder' not in st.session_state:
        st.session_state['recyclable_placeholder'] = st.sidebar.empty()
    if 'non_recyclable_placeholder' not in st.session_state:
        st.session_state['non_recyclable_placeholder'] = st.sidebar.empty()
    if 'hazardous_placeholder' not in st.session_state:
        st.session_state['hazardous_placeholder'] = st.sidebar.empty()

    if 'last_detection_time' not in st.session_state:
        st.session_state['last_detection_time'] = time.time()
    
    # Verifica se já se passaram 3 segundos desde a última detecção para limpar os placeholders
    if time.time() - st.session_state['last_detection_time'] > 3:
        st.session_state['recyclable_placeholder'].empty()
        st.session_state['non_recyclable_placeholder'].empty()
        st.session_state['hazardous_placeholder'].empty()
    
    # Realiza a predição no frame atual
    res = model.predict(image, conf=0.6)
    names = model.names
    detected_items = set()

    for result in res:
        new_classes = set([names[int(c)] for c in result.boxes.cls])
        # Se houver uma alteração nas classes detectadas, atualize a interface
        if new_classes != st.session_state['unique_classes']:
            st.session_state['unique_classes'] = new_classes
            # Limpa os placeholders (pode ser também onde você exibe informações detalhadas)
            st.session_state['recyclable_placeholder'].markdown('')
            st.session_state['non_recyclable_placeholder'].markdown('')
            st.session_state['hazardous_placeholder'].markdown('')
            detected_items.update(st.session_state['unique_classes'])
            
            cellphone, cellphone_battery, battery, needle, syringe, scorpion = classify_waste_type(detected_items)
            print(cellphone, cellphone_battery, battery, needle, scorpion)
            # Reproduz os alertas sonoros conforme a classificação
            if cellphone:
                if not channel_cellphone.get_busy():
                    alert_cellphone.play()
            if cellphone_battery:
                if not channel_bat_cellphone.get_busy():
                    alert_bat_cellphone.play()
            if battery:
                if not channel_battery.get_busy():
                    alert_battery.play()
            if scorpion:
                if not channel_scorpion.get_busy():
                    alert_scorpion.play()
            if needle and syringe:
                if not channel_syringe.get_busy():
                    alert_syringe.play()
            elif needle:
                time.sleep(1)  # Aguarda 1 segundo antes de tocar o alerta de agulha
                if not channel_needle.get_busy():
                    alert_needle.play()
            elif syringe:
                if not channel_syringe.get_busy():
                    alert_syringe.play()
            
            # Atualiza o tempo da última detecção
            st.session_state['last_detection_time'] = time.time()

    res_plotted = res[0].plot()
    st_frame.image(res_plotted, channels="BGR")

def play_webcam(model):
    source_webcam = settings.WEBCAM_PATH
    if st.button('Detectar objetos'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(model,st_frame,image)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))