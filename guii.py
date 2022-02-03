{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3d6ccbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bf16e3b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import filedialog"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d37c370e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9b058aad",
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image,ImageTk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "32d548ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9f55620d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8a1de8b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "#Loading the Model\n",
    "from keras.models import load_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c526d02a",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "Unable to open file (unable to open file: name = 'Age_Sex_Detection.hS', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\KANCHA~1\\AppData\\Local\\Temp/ipykernel_8392/872262293.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mmodel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mload_model\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Age_Sex_Detection.hS\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\u001b[0m in \u001b[0;36mload_wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    490\u001b[0m                 \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtmp_filepath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    491\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mres\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 492\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mload_function\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    493\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    494\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mload_wrapper\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\u001b[0m in \u001b[0;36mload_model\u001b[1;34m(filepath, custom_objects, compile)\u001b[0m\n\u001b[0;32m    581\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    582\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mH5Dict\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_supported_type\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 583\u001b[1;33m         \u001b[1;32mwith\u001b[0m \u001b[0mH5Dict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'r'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mh5dict\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    584\u001b[0m             \u001b[0mmodel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_deserialize_model\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mh5dict\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcustom_objects\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcompile\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    585\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'write'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mcallable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\utils\\io_utils.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, path, mode)\u001b[0m\n\u001b[0;32m    189\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_is_file\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mFalse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    190\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msix\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstring_types\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0m_is_path_instance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 191\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mh5py\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mFile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    192\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_is_file\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    193\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdict\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, name, mode, driver, libver, userblock_size, swmr, **kwds)\u001b[0m\n\u001b[0;32m    310\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mphil\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    311\u001b[0m                 \u001b[0mfapl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmake_fapl\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlibver\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 312\u001b[1;33m                 \u001b[0mfid\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmake_fid\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0muserblock_size\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mswmr\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mswmr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    313\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    314\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mswmr_support\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\u001b[0m in \u001b[0;36mmake_fid\u001b[1;34m(name, mode, userblock_size, fapl, fcpl, swmr)\u001b[0m\n\u001b[0;32m    140\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mswmr\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mswmr_support\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    141\u001b[0m             \u001b[0mflags\u001b[0m \u001b[1;33m|=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mACC_SWMR_READ\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 142\u001b[1;33m         \u001b[0mfid\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfapl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    143\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mmode\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'r+'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    144\u001b[0m         \u001b[0mfid\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mh5f\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mACC_RDWR\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfapl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mh5py\\_objects.pyx\u001b[0m in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mh5py\\_objects.pyx\u001b[0m in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mh5py\\h5f.pyx\u001b[0m in \u001b[0;36mh5py.h5f.open\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: Unable to open file (unable to open file: name = 'Age_Sex_Detection.hS', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)"
     ]
    }
   ],
   "source": [
    "model=load_model(\"Age_Sex_Detection.hS\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "2be52536",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialising the GUI\n",
    "top=tk.Tk()\n",
    "top.geometry('800x600')\n",
    "top.title('Age & Gender Detector')\n",
    "top.configure(background='#CDCDCD')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "98312a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialising the Labels (1 for age and 1 for Gender)\n",
    "label1=Label(top,background='#CDCDCD',font=('arial',15,\"bold\"))\n",
    "label2=Label(top,background='#CDCDCD',font=('arial',15,'bold'))\n",
    "sign_image=Label(top)\n",
    "\n",
    "#Defining Detect function which detects the age and gender of the person in image using the model\n",
    "def Detect(file_path):\n",
    "    global label_packed\n",
    "    image=Image.open(file_path)\n",
    "    image=image.resize((48,48))\n",
    "    image=numpy.expand_dims(image,axis=0)\n",
    "    image=np.array(image)\n",
    "    image=np.delete(image,0,1)\n",
    "    image=np.resize(image,(48,48,3))\n",
    "    print (image.shape)\n",
    "    sex_f=[\"Male\",\"Female\"]\n",
    "    image=np.array([image])/255\n",
    "    pred=model.predict(image)\n",
    "    age=int(np.round(pred[1][0]))\n",
    "    sex=int(np.round(pred[0][0]))\n",
    "    print(\"Predicted Age is \"+ str(age))\n",
    "    print(\"Predicted Gender is \"+sex_f[sex])\n",
    "    label1.configure(foreground=\"#011638\",text=age)\n",
    "    label2.configure(foreground=\"#011638\",text=sex_f[sex])\n",
    "\n",
    "#Defining Show_detect button function\n",
    "def show_Detect_button(file_path):\n",
    "    Detect_b=Button(top,text=\"Detect Image\",command=lambda: Detect(file_path),padx=10,pady=5)\n",
    "    Detect_b.configure(background=\"#364156\",foreground='white',font=('arial',10,'bold'))\n",
    "    Detect_b.place(relx=0.79,rely=0.46)\n",
    "    \n",
    "#Defining Upload Image Function\n",
    "def upload_image():\n",
    "    try:\n",
    "        file_path=filedialog.askopenfilename()\n",
    "        uploaded=Image.open(file_path)\n",
    "        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))\n",
    "        im=ImageTk.PhotoImage(uploaded)\n",
    "        \n",
    "        sign_image.configure(image=im)\n",
    "        sign_image.image=im\n",
    "        label1.configure(text='')\n",
    "        label2.configure(text='')\n",
    "        show_Detect_button(file_path)\n",
    "    except:\n",
    "        pass\n",
    "    \n",
    "upload=Button(top,text=\"Upload an Image\",command=upload_image,padx=10,pady=5)\n",
    "upload.configure(background='#364156',foreground='white',font=('arial',10,'bold'))\n",
    "upload.pack(side='bottom',pady=50)\n",
    "sign_image.pack(side='bottom',expand=True)\n",
    "\n",
    "label1.pack(side='bottom',expand=True)\n",
    "label2.pack(side=\"bottom\",expand=True)\n",
    "heading=Label(top,text=\"Age and Gender Detector\",pady=20,font=('arial',20,\"bold\"))\n",
    "heading.configure(background='#CDCDCD',foreground=\"#364156\")\n",
    "heading.pack()\n",
    "top.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "566c4fab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
