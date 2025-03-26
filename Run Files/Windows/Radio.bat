cd ../..
cd "Internet Radio"
set cwd=%cd%

mklink "%cwd%\Radio.lnk" "%cwd%\Radio.bat"

python radio.py