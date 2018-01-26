def convert_form(name):
    import os
    os.chdir(name+'/')
    os.system('mogrify -format jpeg *.png')
    os.system("rm *.png")
    os.system('mogrify -format jpeg *.jpg')
    os.system("rm *.jpg")