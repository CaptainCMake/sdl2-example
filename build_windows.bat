@echo off
setlocal

set build_dir=build_windows

cd /d C:\
if not exist %build_dir% mkdir %build_dir%
cd %build_dir%

dir

conan install .. -s arch=x86 -s compiler.version=16 -s compiler.runtime=MT || goto :error

systeminfo

cmake -G "Visual Studio 16 2019" -A Win32 .. || goto :error

cmake --build . --config Release --target PACKAGE -- /m || goto :error

:error
exit /b %errorlevel%