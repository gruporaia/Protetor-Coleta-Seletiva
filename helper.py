from ultralytics import YOLO
import time
import streamlit as st
import cv2
import settings
import threading
import pygame 

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("alerta.mp3")
alert_cellphone = pygame.mixer.music.load("celular.mp3")
alert_bat_cellphone = pygame.mixer.music.load("Bateria_de_celular.mp3")
alert_battery = pygame.mixer.music.load("Bateria.mp3")
alert_needle = pygame.mixer.music.load("Seringa.mp3")
alert_scorpion = pygame.mixer.music.load("Escorpiao.mp3")


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
    scorpion = set(detected_items) & set(settings.SCORPION)
    
    return cellphone, non_cellphone, battery, needle, scorpion

def remove_dash_from_class_name(class_name):
    return class_name.replace("_", " ")

def _display_detected_frames(model, st_frame, image):
    image = cv2.resize(image, (640, int(640*(9/16))))
    
    if 'unique_classes' not in st.session_state:
        st.session_state['unique_classes'] = set()

    if 'recyclable_placeholder' not in st.session_state:
        st.session_state['recyclable_placeholder'] = st.sidebar.empty()
    if 'non_recyclable_placeholder' not in st.session_state:
        st.session_state['non_recyclable_placeholder'] = st.sidebar.empty()
    if 'hazardous_placeholder' not in st.session_state:
        st.session_state['hazardous_placeholder'] = st.sidebar.empty()

    if 'last_detection_time' not in st.session_state:
        st.session_state['last_detection_time'] = 0

    res = model.predict(image, conf=0.6)
    names = model.names
    detected_items = set()

    for result in res:
        new_classes = set([names[int(c)] for c in result.boxes.cls])
        if new_classes != st.session_state['unique_classes']:
            st.session_state['unique_classes'] = new_classes
            st.session_state['recyclable_placeholder'].markdown('')
            st.session_state['non_recyclable_placeholder'].markdown('')
            st.session_state['hazardous_placeholder'].markdown('')
            detected_items.update(st.session_state['unique_classes'])

            cellphone, cellphone_battery, battery, needle, scorpion = classify_waste_type(detected_items)


            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            if cellphone:
                if not pygame.mixer.music.get_busy():
                    alert_cellphone.play()
            if cellphone_battery:
                if not pygame.mixer.music.get_busy():
                    alert_bat_cellphone.play()
            if battery:
                if not pygame.mixer.music.get_busy():
                    alert_battery.play()
            if needle:
                if not pygame.mixer.music.get_busy():
                    alert_needle.play()
            if scorpion:
                if not pygame.mixer.music.get_busy():
                    alert_scorpion.play()
            threading.Thread(target=sleep_and_clear_success).start()
            st.session_state['last_detection_time'] = time.time()

    res_plotted = res[0].plot()
    st_frame.image(res_plotted, channels="BGR")


def play_webcam(model):
    source_webcam = settings.WEBCAM_PATH
    if st.button('Detect Objects'):
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