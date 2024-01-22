import os
from PIL import Image
import shutil
import torch
from torchvision.transforms import v2

import numpy as np

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def change_cmyk_rgb(    
    change_img_path: str, 
    file_path: str,) -> None:
    '''Смена цвета поступающих изображений'''
    
    if os.listdir(change_img_path):
        try:
            basedir = os.path.dirname(change_img_path)
            src = basedir + "/"
            file_to_copy = os.listdir(change_img_path)[0]
            image_path = basedir + "/" + os.listdir(change_img_path)[0]
            image = Image.open(image_path)
            if image.mode == "CMYK" or image.mode == "RGB":
                image = image.convert("RGB")
                image.save(image_path)
                recolored_pic = shutil.move(
                    os.path.join(src, file_to_copy),
                    os.path.join(file_path, file_to_copy),
                )
        except IndexError:
            pass
    else:
        pass

def prediction(
    data: str,
    file_path: str,
    model_path: str,
    result_path_ok: str,
    result_path_defect: str,
    path_for_tg: str,) -> None:
    '''Основная функция получения инференса из модели и преобразования его в сигнал'''
    

    model = torch.load(model_path + "/" + str(data)) # map_location=torch.device('cpu')
    model_ft = model.to(device)
    data_transforms_test = {
        "pipes": v2.Compose(
            [
                v2.ToImage(),
                v2.Resize(528, antialias=True),
                v2.ToDtype(torch.float32, scale=True),
                v2.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            ]
        )
    }
    class_names = ["def_front", "ok_front"]
    was_training = model_ft.training
    model_ft.eval()
    if os.listdir(file_path):
        try:
            basedir = os.path.dirname(file_path)
            src = basedir + "/"
            file_to_copy = os.listdir(file_path)[0]
            img_path = basedir + "/" + os.listdir(file_path)[0]
            img = Image.open(img_path)
            img = data_transforms_test["pipes"](img)
            img = img.unsqueeze(0)
            img = img.to(device)
            
            with torch.no_grad():
                outputs = model_ft(img)

                # logits = outputs.detach().numpy()[0]
                # probs = np.exp(logits) / (np.exp(logits)).sum()
                # probs = np.round(probs, decimals=3)
                # print(probs)

                _, preds = torch.max(outputs, 1)
                if class_names[preds[0]] == "ok_front":
                    signal_var = 1
                else:
                    signal_var = 0
                model_ft.train(mode=was_training)

                if signal_var:
                    img_path_good = shutil.move(
                        os.path.join(src, file_to_copy),
                        os.path.join(
                            result_path_ok, file_to_copy
                        ),
                    )  # os.remove(img_path)
                    img_path_bad = None

                else:
                    img_path_bad = shutil.move(
                        os.path.join(src, file_to_copy),
                        os.path.join(
                            result_path_defect, file_to_copy
                        ),
                    )
                    img_path_good = None
                    try:
                        img_tg = shutil.copy(
                            os.path.join(
                                result_path_defect, file_to_copy
                            ),
                            os.path.join(
                                path_for_tg, file_to_copy
                            ),
                        )
                    except shutil.SameFileError:
                        pass                

                return signal_var, img_path_bad, img_path_good

        except IndexError:
            pass
    else:
        pass