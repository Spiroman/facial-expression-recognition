## Faciel Emotion Recognition (FER) from obfuscated images
The purpose of this project is to try and asses which facial landmarks are more important for FER, the eyes or the mouth.  
There are 2 main parts in this project:
1. Obfuscating the mouth and eyes from faces
2. Classifying the emotion of the obfuscated face

The rest of the document specifies how to recreate the results of our project.  

### Obfuscating the mouth and eyes from faces
We used the JAFFE dataset, which is not publicly available, but access for academic and non commercial purposes could be request [here](https://zenodo.org/record/3451524#.YlC7jtNBxb8).  
The object of this step, is to take the original images, and make two new datasets from them. The first will have the eyes of the subjects obfuscated, and the other the mouth.  
To achieve this we used this [face regonition](https://github.com/ageitgey/face_recognition) library. Follow the installation instructions there have access the **face_recognition** package.  
After you've completed the installation, you can execute the `image_obfuscator.py` script that will create two new folders with obfuscated images.  
To run the script run the following in your terminal: `python3 image_obfuscator.py <path to original images>`  
And you're done. You should now have two new folders called eyes and mouth which hold your obfuscated images.

### Classifying the emotion of the obfuscated face
We used this amazing [facial expression recgnition project](https://github.com/ashishpatel26/Facial-Expression-Recognization-using-JAFFE) for our model, and introduced some changes to match new libraries, and added some additional analysis info.  
To reproduce our steps you'll need to run the previous step for the image obfuscation, after which you can use Google's Collab notebooks with the `FER_JAFFE_CNN.ipynb` notebook and simply run it (some additional, minor instructions are provided inside).  To extract extra insights do the same with the `results_analysis.ipynb` notebook, you'll have to upload your results from the last steps of the first notebook.