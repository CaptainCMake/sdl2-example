@echo off
setlocal

set build_dir=build_windows
set build_path=C:\%build_dir%

cd /d %build_path%
if not exist %build_dir% mkdir %build_dir%
cd %build_dir%

set

conan install %CI_PROJECT_DIR% -s arch=x86 -s compiler.version=16 -s compiler.runtime=MT || goto :error

systeminfo

dir

cmake -G "Visual Studio 16 2019" -A Win32 %CI_PROJECT_DIR% || goto :error

cmake --build %build_path% --config Release --target PACKAGE -- /m || goto :error

:error
exit /b %errorlevel%