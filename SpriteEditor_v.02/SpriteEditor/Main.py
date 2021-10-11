import ctypes  # An included library with Python install.
import pygame, sys, os, random
import pyautogui
import Make_Transparent as mt
import time as tm
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os

clock = pygame.time.Clock()

from pygame import *

pixel_animation = []

a = 0

pixels = []
load_sprite = False
print("do you want to load a sprite?")
action = input()
if action == "yes":
    print("what file do you want to load?")
    f_file = input()
    arr = os.listdir()
    if f_file in arr:
        f = open(f_file)
        load_data = []
        load_data.append(f.read())
        f.close()
        pixels.append(load_data[a])
        pixels = pixels[a]
        print(pixels)
        load_sprite = True
    else:
           
       ctypes.windll.user32.MessageBoxW(0,  "That File Does Not Exist!","Error!", 0x00001000)


         
pygame.init()

title = "Sprite Editor"
FPS = 60

pygame.display.set_caption(title)

WINDOW_SIZE = (600,600)
SPEED = 5
BLACK = (0,0,0)
WHITE = (255,255,255)
CYAN = (0,255,255)
RED = (255,0,0)



screen = pygame.display.set_mode(WINDOW_SIZE,32)


screen_division = 2
zoom = screen_division / 2
w1 = WINDOW_SIZE[0] / screen_division
w2 = WINDOW_SIZE[1] / screen_division

window_pixels = WINDOW_SIZE
#Scaling Resolution
display = pygame.Surface((w1, w2))

moving_right = False
moving_left = False


current_color = WHITE

can_paint = True

def createPixel(xpos, ypos, color):
    pixels.append([xpos,ypos,[color]])

random_colors = [WHITE, RED, CYAN, WHITE]

brush_type = "normal"


tag = 0

mouseX, mouseY = 10,10
mouse_down = False
while True:
    display = pygame.Surface((w1, w2))
    zoom = screen_division / 2
    w1 = WINDOW_SIZE[0] / screen_division
    w2 = WINDOW_SIZE[1] / screen_division
    display.fill(BLACK)
    #print(screen_division)
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX -= mouseX / screen_division * zoom
    mouseY -= mouseY / screen_division * zoom

    mouseX /= zoom
    mouseY /= zoom
    i = 0
    for pixel in pixels:
        if can_paint == True:
            if load_sprite == False:
                pygame.draw.rect(display, pixels[i][2][0], pygame.Rect(pixels[i][0],pixels[i][1], 1, 1))
            else:
                pygame.draw.rect(display, pixels[i][2][0], pygame.Rect(pixels[i][0],pixels[i][1], 1, 1))
        else:
            for p in pixel_animation[a]:
                pygame.draw.rect(display, pixels[i][2][0], pygame.Rect(pixels[i][0],pixels[i][1], 1, 1))
            #pygame.draw.rect(display, pixels[0][i][2][0], pygame.Rect(pixels[i][0][0],pixels[i][1][1], 1, 1))
            #pygame.draw.rect(display, pixels[0][i][2][0], pygame.Rect(pixels[0][i][0][0],pixels[0][i][0][1], pixels[0][i][1][0], pixels[0][i][1][1]))
        i+= 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_down = False
                print(pixels)
            if event.button == 3:
                screen_division += 2
            if event.button == 2:
                screen_division -= 2
        if event.type == pygame.KEYDOWN:
            
            print(event.key)
            if int(event.key)==27:
                wndw=Tk()
                
                wndw.eval("tk::PlaceWindow %s center" %wndw.winfo_toplevel())
                wndw.withdraw()
                screen.lock()       
                trigger = messagebox.askokcancel("Confirmation Required...","You pressed the ESC key! Do you want to exit the editor?\nYou will lose unsaved changes!")
                # wndw.winfo_depth=600
                # wndw.winfo_width=600
     
                
                
                if trigger==True:   
                        pygame.quit()
                        sys.exit()
                
                wndw.destroy()
                screen.unlock()
            if int(event.key)==1073742048:#enter the command mode
                 global startTime
                 startTime = tm.time()
            if int(event.key)==115:#if in command mode, save the current file [s key]
                uptime = str(datetime.timedelta(seconds=int(round(tm.time()-startTime))))
                if int(uptime.split(":")[2])<=1:
                    print("you are now saving your file.")
                wndw=Tk()
                
                wndw.eval("tk::PlaceWindow %s center" %wndw.winfo_toplevel())
                wndw.withdraw()    
                  
                wndw.filename=fd.asksaveasfilename(initialdir=os.getcwd(),title="Save your file...",filetypes=(("png file","*.png"),("We were forced to give you another choice but you don't get one haha","*.*")))
                label =Label(wndw,text=wndw.filename).pack()
                print(wndw.filename)
                f_file = open(f"{os.getcwd()}/{wndw.filename.split('/')[len(wndw.filename.split('/'))-1]}", "x")
                f_file.write(str(pixels))
                f_file.close()
                pygame.image.save(screen, f"{wndw.filename}.png")
                mt.transImage(f"{wndw.filename}.png" , f"{wndw.filename}.png")
                trigger = messagebox.askyesno("Question!","Do you want to save a screenshot of your file as a jpg?")
                
                if trigger == True:    
                    pygame.image.save(screen, f"{wndw.filename}.jpg")

                
            if event.key == pygame.K_KP0:
                print("you are now saving your file.")
                try: 
                 print("what name do you want to save the file as?")
                except FileExistsError:
                    print("File already exists...")
                save_file = input()
                f_file = open(save_file, "x")
                f_file.write(str(pixels))
                
                f_file.close()
            if event.key == pygame.K_KP1:
                brush_type = "normal"
                current_color = WHITE
            if event.key == pygame.K_KP2:
                brush_type = "normal"
                current_color = CYAN
            if event.key == pygame.K_KP3:
                brush_type = "normal"
                current_color = RED
            if event.key == pygame.K_KP4:
                print()
                print()
                print(pixel_animation[a])
            if event.key == pygame.K_KP5:
                brush_type = "random"
            if event.key == pygame.K_KP6:
                pygame.image.save(screen, "screenshot.png")

                mt.transImage("screenshot.png",str(tag) + ".png")
                tag += 1
            #New Frame of Animation
            if event.key == pygame.K_KP7:
                pixel_animation.append(pixels)
                pixels = []
            #Play Animation
            if event.key == pygame.K_KP9:
                can_paint = False
                a = 0
            if event.key == pygame.K_KP8:
                can_paint = True
                pixels = pixels[1:-1]
            if event.key == pygame.K_DELETE:
                pixels = []
                
        if can_paint == True:
            if mouse_down == True:
                if brush_type == "normal":
                    createPixel(mouseX,mouseY,current_color)
                else:
                    createPixel(mouseX,mouseY,random_colors[random.randint(0,3)])

    if can_paint == False:
        pixels = []
        p = 0
        while p != (len(pixel_animation[a][p]) - 1):
            createPixel(pixel_animation[a][p][0],pixel_animation[a][p][1],pixel_animation[a][p][2][0])
            p += 1
    a += 1
    if a > (len(pixel_animation) - 1):
        a = 0


        
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    try: 
     screen.blit(surf,(0, 0))
    except Exception as e:
               ctypes.windll.user32.MessageBoxW(0,  f"{e}\nWe're working hard to fix this... Please try again later","An Exception Has Occurred!", 0)
                
    pygame.display.update()

    clock.tick(FPS)
