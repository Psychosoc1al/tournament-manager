import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "--noconfirm",
        "--onefile",
        "--distpath=./release",
        "--workpath=./release/build",
        "--add-data=icon/icon.ico:icon",
        "--windowed",
        "--splash=./icon/splash.png",
        "--name=TourMan",
        "main.py",
    ]
)
