from ultralytics import YOLO
import time
import streamlit as st
import cv2
import settings
import threading
import pygame
import logging

logging.basicConfig(filename='sound_events.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


pygame.init()
pygame.mixer.init()

alert_cellphone = pygame.mixer.Sound("sons/celular.mp3")
channel_cellphone = pygame.mixer.Channel(0)
alert_bat_cellphone = pygame.mixer.Sound("sons/bateria_de_celular.mp3")
channel_bat_cellphone = pygame.mixer.Channel(1)
alert_battery = pygame.mixer.Sound("sons/bateria.mp3")
channel_battery = pygame.mixer.Channel(2)
alert_needle = pygame.mixer.Sound("sons/agulha.mp3")
channel_needle = pygame.mixer.Channel(3)
alert_syringe = pygame.mixer.Sound("sons/seringa.mp3")
channel_syringe = pygame.mixer.Channel(4)
alert_scorpion = pygame.mixer.Sound("sons/escorpiao.mp3")
channel_scorpion = pygame.mixer.Channel(5)
alert_pilha = pygame.mixer.Sound("sons/pilha.mp3")
channel_pilha = pygame.mixer.Channel(6)

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
    pilha = set(detected_items) & set(settings.PILHA)

    return cellphone, non_cellphone, battery, needle, syringe, scorpion, pilha

def remove_dash_from_class_name(class_name):
    return class_name.replace("_", " ")

def _display_detected_frames(model, st_frame, image):
    image = cv2.resize(image, (640, int(640 * (9/16))))

    if 'unique_classes' not in st.session_state:
        st.session_state['unique_classes'] = set()
    if 'recent_detections_list' not in st.session_state:
        st.session_state['recent_detections_list'] = []
    if 'recent_logs_placeholder' not in st.session_state:
        st.session_state['recent_logs_placeholder'] = st.sidebar.empty()
    if 'last_log_time' not in st.session_state:
        st.session_state['last_log_time'] = 0


    res = model.predict(image, conf=0.6)
    names = model.names
    detected_items = set()

    # Mostrar logs recentes no sidebar
    log_text = "<b>Últimos Objetos Detectados:</b>\n"
    for log in st.session_state['recent_detections_list']:
        log_text += f"- {log}\n"
    st.session_state['recent_logs_placeholder'].markdown(log_text, unsafe_allow_html=True)


    for result in res:
        new_classes = set([names[int(c)] for c in result.boxes.cls])

        if new_classes != st.session_state['unique_classes'] and time.time() - st.session_state['last_log_time'] >= 3:
            st.session_state['unique_classes'] = new_classes
            st.session_state['recent_logs_placeholder'].markdown('') # Limpar placeholder de logs recentes

            detected_items.update(st.session_state['unique_classes'])

            cellphone, cellphone_battery, battery, needle, syringe, scorpion, pilha = classify_waste_type(detected_items)

            # Verifica se passaram 5 segundos desde o último log
            if time.time() - st.session_state['last_log_time'] >= 5 and detected_items:
                logging.info(f"Classes detectadas neste frame: {detected_items}")
                st.session_state['last_log_time'] = time.time() # Atualiza o tempo do último log
                detection_string = ", ".join(detected_items) # Formatando para string
                log_entry = f"{time.strftime('%H:%M:%S')} - Objetos: {detection_string}" # Adicionar timestamp
                st.session_state['recent_detections_list'].insert(0, log_entry) # Adicionar no inicio da lista
                st.session_state['recent_detections_list'] = st.session_state['recent_detections_list'][:5] # Manter apenas os 5 mais recentes

            if cellphone:
                if not channel_cellphone.get_busy():
                    alert_cellphone.play()
            if cellphone_battery:
                if not channel_bat_cellphone.get_busy():
                    alert_bat_cellphone.play()
            if battery:
                if not channel_battery.get_busy():
                    alert_battery.play()
            if needle:
                if not channel_needle.get_busy():
                    alert_needle.play()
            if syringe:
                if not channel_syringe.get_busy():
                    alert_syringe.play()
            if scorpion:
                if not channel_scorpion.get_busy():
                    alert_scorpion.play()
            if pilha:
                if not channel_pilha.get_busy():
                    alert_pilha.play()

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
