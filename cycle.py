import subprocess

PATH = "/Users/sanchez.hmsc/Documents/GitHub/neuralStyleTF_automate/"
PATH_OUT = PATH + "image_output/"
IMG_SIZE = 500


imagesDict = [
    {"img": "ecuador01.jpeg", "style": "g1.jpg", "iters": "100"},
    {"img": "ecuador03.jpeg", "style": "g5.jpg", "iters": "75"}
]

for params in imagesDict:
    # Create output folder
    (imgN, styN) = (params["img"].split(".")[0], params["style"].split(".")[0])
    outFolder = PATH_OUT + imgN + "_" + styN
    subprocess.Popen(['mkdir', outFolder])
    # Run python script
    cmd = [
        "python", "neural_style.py",
        "--content_img", params["img"],
        "--style_imgs", params["style"],
        "--img_output_dir", outFolder,
        "--max_size", str(IMG_SIZE),
        "--max_iterations", params["iters"],
        "--device", "/cpu:0",
        "--verbose",
        "--original_colors"
    ]
    subprocess.Popen(cmd)
