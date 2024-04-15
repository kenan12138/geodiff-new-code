The original geodiff code was modified, including the environment and corresponding code, and it ran successfully. The usage environment of this code is pyg 2.1.0 py37_torch_1.11.0_cu115. Execute the following command conda install pytorch-geometric= 2.1.0=py37_torch_1.11.0_cu115 -c rusty1s -c conda-forge. For other packages, see the env.yml file.You can compare it with the original geodiff code to find the modified parts. Most modifications are in dataset.py and gin.py or other files.






This is my first time uploading a file, so please forgive me for my mistakes. The code I uploaded corresponds to the contents of the models folder and utils folder of the original geodiff MinkaiXu. Please name them according to the folder naming method of the original geodiff. After my own experiments, it can be run on cuda11.5, pytorch 1.11.0 pyg 2.1.0, please see env.yml for the environment.



The original code address is as follows https://github.com/MinkaiXu/GeoDiff.




A new file called pdb.py has been added that can convert files with a .pkl extension to a .pdb extension, making it easier to open and view them in PyMOL 
