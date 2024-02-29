import cv2
import numpy as np
import os
import shutil
def make_list(src_path, dest_path, count_result):
    '''Создание списка изображений'''
    image_list_dest = os.listdir(src_path)
    for count, f in enumerate(image_list_dest):
        f_name, f_ext = os.path.splitext(f)
        f_name = "pic_" + str(count + 1 + count_result)

        new_name = f'{f_name}{f_ext}'
        os.rename(os.path.join(src_path, f), os.path.join(src_path, new_name))

    image_list_src = os.listdir(src_path)
    for file_name in image_list_src:
        shutil.move(os.path.join(src_path, file_name), dest_path)

    result_list_sorted = sorted(os.listdir(dest_path), key=lambda x: int(x.rsplit('_', 1)[1].rsplit('.', 1)[0]))[::-1]
    return result_list_sorted

def calculate_lab_space(img_src, image_list, quantity):

    avg_img_1 = [np.asarray(cv2.mean(cv2.imread(img_src + f'{i}'))[0:3]) for i in image_list]
    avg_img_blue_list_1 = [avg_img_1[i][0] for i in range(quantity)]
    avg_img_green_list_1 = [avg_img_1[i][1] for i in range(quantity)]
    avg_img_red_list_1 = [avg_img_1[i][2] for i in range(quantity)]

    avg_channel_1 = sum(avg_img_blue_list_1)/len(avg_img_blue_list_1),\
                    sum(avg_img_green_list_1)/len(avg_img_green_list_1),\
                    sum(avg_img_red_list_1)/len(avg_img_red_list_1)

        # //sR, sG and sB (Standard RGB) input range = 0 ÷ 255
    # //X, Y and Z output refer to a D65/2° standard illuminant.
    # var_R = ( sR / 255 )
    # var_G = ( sG / 255 )
    # var_B = ( sB / 255 )

    var_R = ( avg_channel_1[2] / 255 )
    var_G = ( avg_channel_1[1] / 255 )
    var_B = ( avg_channel_1[0] / 255 )

    if (var_R > 0.04045):
        var_R = ((var_R + 0.055) / 1.055) ** 2.4
    else:
        var_R = var_R / 12.92
    if (var_G > 0.04045):
        var_G = ((var_G + 0.055) / 1.055) ** 2.4
    else:
        var_G = var_G / 12.92
    if (var_B > 0.04045):
        var_B = ((var_B + 0.055) / 1.055) ** 2.4
    else:
        var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
    Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
    Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

    # //Reference-X, Y and Z refer to specific illuminants and observers.
    #     Observer	2° (CIE 1931)	        10° (CIE 1964)	Note
    # Illuminant	X2	    Y2	    Z2	    X10	    Y10	    Z10	 
    # A	            109.850	100.000	35.585	111.144	100.000	35.200	Incandescent/tungsten
    # B	            99.0927	100.000	85.313	99.178;	100.000	84.3493	Old direct sunlight at noon
    # C	            98.074	100.000	118.232	97.285	100.000	116.145	Old daylight
    # D50	        96.422	100.000	82.521	96.720	100.000	81.427	ICC profile PCS
    # D55	        95.682	100.000	92.149	95.799	100.000	90.926	Mid-morning daylight
    # D65	        95.047	100.000	108.883	94.811	100.000	107.304	Daylight, sRGB, Adobe-RGB
    # D75	        94.972	100.000	122.638	94.416	100.000	120.641	North sky daylight
    # E	            100.000	100.000	100.000	100.000	100.000	100.000	Equal energy
    # F1	        92.834	100.000	103.665	94.791	100.000	103.191	Daylight Fluorescent
    # F2	        99.187	100.000	67.395	103.280	100.000	69.026	Cool fluorescent
    # F3	        103.754	100.000	49.861	108.968	100.000	51.965	White Fluorescent
    # F4	        109.147	100.000	38.813	114.961	100.000	40.963	Warm White Fluorescent
    # F5	        90.872	100.000	98.723	93.369	100.000	98.636	Daylight Fluorescent
    # F6	        97.309	100.000	60.191	102.148	100.000	62.074	Lite White Fluorescent
    # F7	        95.044	100.000	108.755	95.792	100.000	107.687	Daylight fluorescent, D65 simulator
    # F8	        96.413	100.000	82.333	97.115	100.000	81.135	Sylvania F40, D50 simulator
    # F9	        100.365	100.000	67.868	102.116	100.000	67.826	Cool White Fluorescent
    # F10	        96.174	100.000	81.712	99.001	100.000	83.134	Ultralume 50, Philips TL85
    # F11	        100.966	100.000	64.370	103.866	100.000	65.627	Ultralume 40, Philips TL84
    # F12	        108.046	100.000	39.228	111.428	100.000	40.353	Ultralume 30, Philips TL83

    Reference_X = 96.720	
    Reference_Y = 100.000
    Reference_Z = 81.427

    var_X = X / Reference_X
    var_Y = Y / Reference_Y
    var_Z = Z / Reference_Z

    if (var_X > 0.008856):
        var_X = var_X ** (1/3)
    else:
        var_X = (7.787 * var_X) + (16/116)
    if (var_Y > 0.008856):
        var_Y = var_Y ** (1/3)
    else:
        var_Y = (7.787 * var_Y) + (16/116)
    if (var_Z > 0.008856):
        var_Z = var_Z ** (1/3)
    else:
        var_Z = (7.787 * var_Z) + (16 / 116)

    space = str(((116 * var_Y) - 16).round(2)), str((500 * (var_X - var_Y)).round(2)), str((200 * (var_Y - var_Z)).round(2))

    num_list_1 = [float(num) for num in space]
    num_list = [str(num) for num in space]
    result = " : ".join(num_list)

    return result, num_list_1, avg_channel_1

normal_button_state = ("QPushButton {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #28495c, stop: 1 #5c7d90);"
                    "color: #efebef;"
                    "border-radius: 12px;"
                    "border: 1px solid #636173;"
                    "outline: 0px;}"
                    "QPushButton:hover, QPushButton:focus {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3c3b4b, stop: 1 #4b4875);;"
                    "border: 2px solid #636173;"
                    "color: #efebef}")

bg_signal_norm = ( "QLabel {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:"
                        "0 rgb(5, 103, 0), stop: 1 rgb(13, 236, 20));"
                        "color: white;"
                        "border: 1px;"
                        "border-radius: 15px;}")

bg_signal_defect = ("QLabel {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:"
                        "0 rgb(132, 0, 0), stop: 1 rgb(255, 0, 0));"
                        "color: white;"
                        "border: 1px;"
                        "border-radius: 15px;}")

green_button_state = ("QPushButton  {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:"
                    "0 rgb(5, 103, 0), stop: 1 rgb(13, 236, 20));"
                    "color: white;"
                    "border-radius: 12px;"
                    "border: 1px solid #636173}")

bg_signal_no_data = ("QLabel {background-color: #6c6a89;"
                    "border: 1px;"
                    "border-radius: 15px;}")

if __name__ == "__main__":
    make_list(src_path, dest_path, count_result)
    calculate_lab_space(img_src, image_list, quantity)