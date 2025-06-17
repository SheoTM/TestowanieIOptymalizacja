# Raport projektu CNN – klasyfikacja kwiatów ze zbioru "TF Flowers"
# 1. Baza danych obrazów użyta do klasyfikacji

Podczas realizacji projektu wykorzystałem gotowy zbiór danych obrazów kwiatów udostępniony przez TensorFlow Datasets pod nazwą tf_flowers. Zbiór ten zawiera realistyczne zdjęcia różnych gatunków kwiatów, sklasyfikowanych do jednej z pięciu klas.

Całość danych została podzielona w następujących proporcjach:

80% – zbiór treningowy (2936 obrazów)

20% – zbiór walidacyjny (734 obrazy)

Zbiór tf_flowers zawiera 5 klas:
- daisy

- dandelion

- roses

- sunflowers

- tulips

Przykładowe dane ze zbioru:

![image.png](https://app.clear.ml/files//reports/6b8541564e464971bd8904c11585007c/image.png)

---

## 2. Model ResNet50 wytrenowany od zera na CPU

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&metrics=Training&variants=Accuracy&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_train" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&metrics=Validation&variants=Accuracy&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_val" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_time_cpu" width="100%" height="400"></iframe>

Czas treningu: 11 601 s  
Validation accuracy: 53.41%  
Validation loss: 1.3556

---

## 3. Optymalizacja szybkości treningu (GPU T4)

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_gpu_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_gpu_val_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=7b2eb2e4a00a46eb9b535f1a6c1fc9a1&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="resnet50_gpu_time" width="100%" height="400"></iframe>

**Wyniki:** accuracy wzrosła z 53% do 59%, czas uczenia skrócił się do 395 s.

---

## 4. Transfer learning

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=072a3ab9931d49d1815e7051488f151f&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="tl_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=072a3ab9931d49d1815e7051488f151f&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="tl_val_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=072a3ab9931d49d1815e7051488f151f&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="tl_time" width="100%" height="400"></iframe>

**Efekt:** accuracy ~90%, czas ~850 s.

---

## 5. Normalizacja

![normalziacja.png](https://app.clear.ml/files//reports/6b8541564e464971bd8904c11585007c/normalziacja.png)

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=46849e2607644b7a9cf282f845ae0b21&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Training&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="norm_train_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=46849e2607644b7a9cf282f845ae0b21&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Training&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="norm_train_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=46849e2607644b7a9cf282f845ae0b21&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="norm_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=46849e2607644b7a9cf282f845ae0b21&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="norm_val_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=46849e2607644b7a9cf282f845ae0b21&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="norm_time" width="100%" height="400"></iframe>

**Wynik:** accuracy spadła o ~10 pp, training time razy 2.

---

## 6. Augmentacja

![augmentacja.png](https://app.clear.ml/files//reports/6b8541564e464971bd8904c11585007c/augmentacja.png)

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=303f72adfc6545b0ad5b37829f60d924&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Training&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="aug_train_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=303f72adfc6545b0ad5b37829f60d924&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Training&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="aug_train_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=303f72adfc6545b0ad5b37829f60d924&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="aug_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=303f72adfc6545b0ad5b37829f60d924&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="aug_val_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=303f72adfc6545b0ad5b37829f60d924&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="aug_time" width="100%" height="400"></iframe>

**Wnioski:** brak dużej poprawy, ~3× dłuższe trenowanie.

---

## 7. Dropout

![Dropout.png](https://app.clear.ml/files//reports/6b8541564e464971bd8904c11585007c/Dropout.png)

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=935e98bada5848df8a88938299162e57&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Training&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="do_train_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=935e98bada5848df8a88938299162e57&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="do_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=935e98bada5848df8a88938299162e57&objects=9e9e8a88dafe46edb80ae036bc458212&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="do_time" width="100%" height="400"></iframe>

**Wnioski:** początkowy spadek, potem wyrównanie; czas *2×*.

---

## 8. Dokładanie danych

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=9e9e8a88dafe46edb80ae036bc458212&objects=c05bbbbba3204dfb899cba11c1528751&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="dup_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=9e9e8a88dafe46edb80ae036bc458212&objects=c05bbbbba3204dfb899cba11c1528751&metrics=Validation&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="dup_val_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=9e9e8a88dafe46edb80ae036bc458212&objects=c05bbbbba3204dfb899cba11c1528751&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="dup_time" width="100%" height="400"></iframe>

**Wnioski:** niewielki wzrost accuracy, ~3× wolniej, pojawia się overfitting.

---

## 9. Różne rozmiary wejściowe

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=5e57033545134a1a967fd9db547b06c5&objects=6534b4be32334a308a7fd135d8652d3f&objects=f4a1efeca1284273a502bc94e6e8331d&metrics=Training&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="size_train_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=5e57033545134a1a967fd9db547b06c5&objects=6534b4be32334a308a7fd135d8652d3f&objects=f4a1efeca1284273a502bc94e6e8331d&metrics=Training&variants=Loss&company=69f7cf3f0645ca9cf83920be8c3542" name="size_train_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=5e57033545134a1a967fd9db547b06c5&objects=6534b4be32334a308a7fd135d8652d3f&objects=f4a1efeca1284273a502bc94e6e8331d&metrics=Validation&variants=Loss&company=69f7f0645ca9cf83920be8c3542" name="size_val_loss" width="100%" height="400"></iframe>

Czasy trenowania:
- 96×96: 275 s
- 160×160: 429 s
- 224×224: 747 s

Dokładność:
- 96×96: 50.54%
- 160×160: 52.99%
- 224×224: 48%

**Wniosek:** najlepszy balans osiąga rozmiar **160×160**.

---

## 10. Batch size (porównanie 32, 64, 128)

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=15b498de37b642fc814b029be8861c9e&objects=5133936ca84743bca7e6e17f6612a117&objects=740b47f6634041c780e4452ccfdc4cd6&metrics=Training&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="bs_train_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=15b498de37b642fc814b029be8861c9e&objects=5133936ca84743bca7e6e17f6612a117&objects=740b47f6634041c780e4452ccfdc4cd6&metrics=Training&variants=Loss&company=69f7c32f3f0645ca9cf83920be8c3542" name="bs_train_loss" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=15b498de37b642fc814b029be8861c9e&objects=5133936ca84743bca7e6e17f6612a117&objects=740b47f6634041c780e4452ccfdc4cd6&metrics=Validation&variants=Accuracy&company=69f7c32f3f0645ca9cf83920be8c3542" name="bs_val_acc" width="100%" height="400"></iframe>

<iframe src="https://app.clear.ml/widgets/?type=scalar&objectType=task&xaxis=iter&objects=15b498de37b642fc814b029be8861c9e&objects=5133936ca84743bca7e6e17f6612a117&objects=740b47f6634041c780e4452ccfdc4cd6&metrics=Performance&variants=Training%20Time%20(s)&company=69f7c32f3f0645ca9cf83920be8c3542" name="bs_time" width="100%" height="400"></iframe>

**Wyniki:**
- Większy batch size → szybsze trenowanie
- Jednak przy zbyt dużym (`128`) model mógł się przeuczać szybciej

---

### Podsumowanie końcowe:

- **Najwyższa dokładność**: InceptionV3 ~90%  
- **Najszybszy model**: MobileNet (~296 s)  
- **Optymalny rozmiar**: 160×160  

---

