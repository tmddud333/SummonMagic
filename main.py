import cv2
import pyautogui

print(pyautogui.position());
pyautogui.screenshot('confirm.png', region=(pyautogui.position().x,pyautogui.position().y, 60, 30))

im = cv2.imread('confirm.png')
cv2.imshow('im', im)