from time import sleep

import pygame
import random
import stack
from tkinter import *

# Constants
BAR_COLOR = (165, 42, 42)
SCREEN_BG = (135, 206, 235)
TEXT_COLOR = (255, 255, 255)
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000
X_ASPECT_RATIO = SCREEN_WIDTH / 1000
Y_ASPECT_RATIO = SCREEN_HEIGHT / 650
# ideally X_ASPECT_RATIO must be equal to Y_ASPECT RATIO for stable display
MAX_BAR_HEIGHT = 500 * SCREEN_HEIGHT / 650
SELECTION = 1
BUBBLE = 2
INSERTION = 3
QUICK = 4
MERGE = 5
HEAP = 6
close_application = False
# clock = pygame.time.Clock()

##########################
# Global array utilities

ARRAY_SIZE = 200

arr = [random.randint(1, int(MAX_BAR_HEIGHT)) for i in range(ARRAY_SIZE)]


def display_array(screen):
    bar_width = SCREEN_WIDTH / ARRAY_SIZE
    pygame.draw.rect(screen, SCREEN_BG,
                     (0, 150 * SCREEN_HEIGHT / 650, 1000 * SCREEN_WIDTH / 1000, 500 * SCREEN_HEIGHT / 650))
    for i in range(ARRAY_SIZE):
        pygame.draw.rect(screen, BAR_COLOR, (bar_width * i, SCREEN_HEIGHT - arr[i], bar_width, arr[i]))


###########################
###########################
###########################
# Displaying text
TIME_SCALE = 1
def display_msg(screen, msg, loc):
    screen.blit(msg, loc)


def display_mili_t(screen, mili_t, loc, font):
    time_info = font.render(f"Time : {mili_t} ms", True, TEXT_COLOR)
    screen.blit(time_info, loc)


def display_array_size(screen, font, loc):
    arr_size = font.render(f"Array size : {ARRAY_SIZE}", True, TEXT_COLOR)
    screen.blit(arr_size, loc)


def display_time_complexity(screen, font, text, loc):
    time_compl = font.render(text, True, TEXT_COLOR)
    screen.blit(time_compl, loc)


###########################


option = 7


# Getting option from the user

def get_option():
    global option
    option = 7

    def choose_opt(opt):
        global option
        option = opt
        root.destroy()

    def reset_quit():
        global option
        option = 7
        root.destroy()

    root = Tk()
    root.geometry("800x600")
    root.config(bg="sky blue")
    root.title("Simsort")
    ask_option_Lable = Label(root, text="Select what you wanna simulate?", font="helvetica 16 italic bold",
                             bg="sky blue")
    selection_button = Button(root, text="Selection Sort", font="Roman 18 bold", command=lambda: choose_opt(1))
    bubble_button = Button(root, text="Bubble Sort", font="Roman 18 bold", command=lambda: choose_opt(2))
    insertion_button = Button(root, text="Insertion Sort", font="Roman 18 bold", command=lambda: choose_opt(3))
    quick_button = Button(root, text="Quick Sort", font="Roman 18 bold", command=lambda: choose_opt(4))
    merge_button = Button(root, text="Merge Sort", font="Roman 18 bold", command=lambda: choose_opt(5))
    heap_button = Button(root, text="Heap Sort", font="Roman 18 bold", command=lambda: choose_opt(6))
    quit_button = Button(root, text="Quit", font="Roman 18 bold", command=reset_quit)
    ask_option_Lable.place(relx=0.20, rely=0, relheight=0.10, relwidth=0.60)
    selection_button.place(relx=0.30, rely=0.13, relheight=0.10, relwidth=0.40)
    bubble_button.place(relx=0.30, rely=0.26, relheight=0.10, relwidth=0.40)
    insertion_button.place(relx=0.30, rely=0.39, relheight=0.10, relwidth=0.40)
    quick_button.place(relx=0.30, rely=0.52, relheight=0.10, relwidth=0.40)
    merge_button.place(relx=0.30, rely=0.65, relheight=0.10, relwidth=0.40)
    heap_button.place(relx=0.30, rely=0.78, relheight=0.10, relwidth=0.40)
    quit_button.place(relx=0.30, rely=0.89, relheight=0.10, relwidth=0.40)
    root.mainloop()
    return option
cont = False
def get_preferences():
    root = Tk()
    root.geometry('800x600')
    root.configure(bg="sky blue")
    root.title("Simsort")
    size_preference = Label(root, text="Enter size of the array", font="Helvetica 12 bold",bg = "sky blue")
    size_entry = Entry(root, justify=CENTER, font="Helvetica 12 bold")
    ask_array_preference = Label(root, text="Initially,array to be -\n1.Sorted(Ascending) "
                                            "2.Sorted(Descending)\n3.Randomly Generated\nEnter your option:",
                                 font="Helvetica 12 bold",bg = 'sky blue')
    array_preference_entry = Entry(root, justify=CENTER, font="Helvetica 12 bold")
    error_message = Label(root,text = 'Please Enter valid input.',font = "Helvetica 8",bg = "sky blue",fg = "red")
    def set_preferences():
        global ARRAY_SIZE
        global arr
        global cont
        destroy = False
        try:
            size = int(size_entry.get())
            array_type = int(array_preference_entry.get())
            if size > 0  and array_type in range(1,4):
                ARRAY_SIZE = size
                arr = [random.randint(1,MAX_BAR_HEIGHT) for _ in range(ARRAY_SIZE)]
                if(array_type == 1):
                    arr.sort()
                elif(array_type == 2):
                    arr.sort()
                    arr = arr[::-1]
                destroy = True
            else:
                error_message.place(relx=0.20, rely=0.74, relheight=0.04, relwidth=0.60)
        except:
            print("in ex")
            error_message.place(relx = 0.20,rely = 0.74,relheight = 0.04,relwidth = 0.60)
        finally:
            if destroy:
                cont = True
                root.destroy()

    submit = Button(root, text="Submit", font="Helvetica 12 bold",command = set_preferences)

    size_preference.place(relx = 0.20,rely = 0,relheight = 0.15,relwidth = 0.60)
    size_entry.place(relx = 0.35,rely = 0.20,relheight = 0.05,relwidth = 0.30)
    ask_array_preference.place(relx = 0.20,rely = 0.30,relheight = 0.15,relwidth = 0.60)
    array_preference_entry.place(relx = 0.35,rely = 0.50,relheight = 0.05,relwidth = 0.30)
    submit.place(relx = 0.45,rely = 0.65,relheight = 0.04,relwidth = 0.10)

    root.mainloop()


###########################################################################

def selection_sort():
    global arr
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Selection Sort")
    screen.fill(SCREEN_BG)
    flag = True
    i = 0
    swaps = 0
    mili_t = 0
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        if i < ARRAY_SIZE - 1:
            min_ind = i
            min_ele = arr[i]
            for j in range(i + 1, ARRAY_SIZE):
                pygame.time.delay(TIME_SCALE)
                mili_t += TIME_SCALE
                if arr[j] < min_ele:
                    min_ind = j
                    min_ele = arr[j]
            if min_ind != i:
                temp = arr[min_ind]
                arr[min_ind] = arr[i]
                arr[i] = temp
                swaps += 1
            i += 1

        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N^2)", (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


def bubble_sort():
    global arr
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Bubble Sort")
    screen.set_alpha(None)
    screen.fill(SCREEN_BG)
    flag = True
    swaps = 0
    mili_t = 0
    i = 0
    is_sorted = False
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        if i < ARRAY_SIZE - 1 and not is_sorted:
            is_sorted = True
            for j in range(0, ARRAY_SIZE - i - 1):
                pygame.time.delay(TIME_SCALE)
                mili_t += TIME_SCALE
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swaps += 1
                    is_sorted = False
            i = i + 1
        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N^2)", (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


def insertion_sort():
    global arr
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Insertion Sort")
    screen.set_alpha(None)
    screen.fill(SCREEN_BG)
    flag = True
    shifts = 0
    mili_t = 0
    i = 1
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        if i < ARRAY_SIZE:
            key = arr[i]
            j = i - 1
            are_greater = True
            while j >= 0 and are_greater:
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    pygame.time.delay(TIME_SCALE)
                    shifts += 1
                    mili_t += TIME_SCALE
                    j -= 1
                else:
                    are_greater = False
            arr[j + 1] = key
        i += 1
        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N^2)", (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


swaps = 0
mili_t = 0


def partition(low, high):
    global arr
    global swaps
    global mili_t
    pivot_ele = arr[low]
    pivot = low
    i = low
    j = high
    while i <= j:
        mili_t += TIME_SCALE
        sleep(0.001*TIME_SCALE)
        if arr[i] <= pivot_ele:
            i += 1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            swaps += 1
            j -= 1
    temp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    return j


def quick_sort():
    global arr
    global mili_t
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Quick Sort")
    screen.set_alpha(None)
    screen.fill(SCREEN_BG)
    flag = True
    stck = stack.Stack()
    stck.push([0, ARRAY_SIZE - 1])
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                swaps = mili_t = 0
                flag = False
        if not stck.is_empty():
            cur_top = stck.top()
            low, high = cur_top
            if low < high:
                j = partition(low, high)
                stck.pop()
                stck.push([low, j - 1])
                stck.push([j + 1, high])
            else:
                stck.pop()
        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N * Log(N))", (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


def merge(low, mid, high):
    global arr
    global mili_t
    b = arr[low:mid + 1]
    c = arr[mid + 1:high + 1]
    i = 0
    j = 0
    n1 = mid - low + 1
    n2 = high - mid
    k = low
    while i < n1 and j < n2:
        if b[i] < c[j]:
            sleep(0.001*TIME_SCALE)
            mili_t += TIME_SCALE
            arr[k] = b[i]
            k += 1
            i += 1
        else:
            sleep(0.001*TIME_SCALE)
            mili_t += TIME_SCALE
            arr[k] = c[j]
            k += 1
            j += 1
    while i < n1:
        sleep(0.001*TIME_SCALE)
        mili_t += TIME_SCALE
        arr[k] = b[i]
        i += 1
        k += 1
    while j < n2:
        sleep(0.001*TIME_SCALE)
        mili_t += TIME_SCALE
        arr[k] = c[j]
        j += 1
        k += 1


def merge_sort():
    global arr
    global mili_t
    global swaps
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Merge Sort")
    screen.set_alpha(None)
    screen.fill(SCREEN_BG)
    flag = True
    cur_size = 1
    low = 0
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                swaps = mili_t = 0
                flag = False
        if cur_size <= ARRAY_SIZE - 1 and low < ARRAY_SIZE - 1:
            mid = min(ARRAY_SIZE - 1, low + cur_size - 1)
            high = min(ARRAY_SIZE - 1, low + 2 * cur_size - 1)
            merge(low, mid, high)
            low = low + 2 * cur_size
            if low >= ARRAY_SIZE - 1:
                low = 0
                cur_size *= 2
        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N * Log(N))",
                                (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


def heapify(i, n):
    global arr
    global swaps
    global mili_t
    largest_ind = i
    l_ind = 2 * i + 1
    r_ind = 2 * i + 2

    if l_ind < n and arr[l_ind] > arr[largest_ind]:
        largest_ind = l_ind
    if r_ind < n and arr[r_ind] > arr[largest_ind]:
        largest_ind = r_ind
    if largest_ind != i:
        sleep(0.001*TIME_SCALE)
        mili_t += TIME_SCALE
        temp = arr[i]
        arr[i] = arr[largest_ind]
        arr[largest_ind] = temp
        swaps += 1
        heapify(largest_ind, n)


def heap_sort():
    global arr
    global mili_t
    global swaps
    pygame.init()
    fnt_20 = pygame.font.Font("freesansbold.ttf", int(20 * X_ASPECT_RATIO))
    fnt_32 = pygame.font.Font("freesansbold.ttf", int(32 * X_ASPECT_RATIO))
    scale_info = fnt_20.render(f"Scale : O(1) = {TIME_SCALE} ms.", True, TEXT_COLOR)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simsort - Heap Sort")
    screen.set_alpha(None)
    screen.fill(SCREEN_BG)
    flag = True
    i = ARRAY_SIZE // 2 - 1
    heap_formed = False
    while flag:
        screen.fill(SCREEN_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                swaps = mili_t = 0
                flag = False
        if i >= 0 and not heap_formed:
            pygame.time.delay(TIME_SCALE)
            mili_t += TIME_SCALE
            heapify(i, ARRAY_SIZE)
            i -= 1
            if i == -1:
                i = ARRAY_SIZE - 1
                heap_formed = True
        if heap_formed and i > 0:
            pygame.time.delay(TIME_SCALE)
            mili_t += TIME_SCALE
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            swaps += 1
            heapify(0, i)
            i -= 1

        display_array(screen)
        display_msg(screen, scale_info, (0 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_mili_t(screen, mili_t, (0 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO), fnt_32)
        display_array_size(screen, fnt_32, (500 * X_ASPECT_RATIO, 0 * Y_ASPECT_RATIO))
        display_time_complexity(screen, fnt_32, "Time Complexity : O(N * Log(N))",
                                (500 * X_ASPECT_RATIO, 50 * Y_ASPECT_RATIO))

        pygame.display.update()
    if not flag:
        pygame.display.quit()


if __name__ == "__main__":
    option = 1
    while 1 <= option <= 6:
        option = get_option()
        if 1 <= option <= 6:
            get_preferences()
        if option == SELECTION and cont :
            selection_sort()
        elif option == BUBBLE and cont:
            bubble_sort()
        elif option == INSERTION and cont:
            insertion_sort()
        elif option == QUICK and cont :
            quick_sort()
        elif option == MERGE and cont:
            merge_sort()
        elif option == HEAP and cont:
            heap_sort()
        cont = False
