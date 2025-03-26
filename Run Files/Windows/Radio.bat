cd ../..
cd "Internet Radio"
set cwd=%cd%

python radio.py

mklink "%cwd%\Radio.lnk" "%cwd%\Radio.bat"