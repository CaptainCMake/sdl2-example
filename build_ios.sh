set -e

build_dir=build_ios

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan remote add bintray-stever https://api.bintray.com/conan/stever/conan --insert --force

conan install --update .. -s os=iOS -s arch=armv7 -s os.version=8.0 -s compiler.version=11.0

cmake -G Xcode -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_ARCHITECTURES="armv7 arm64" -DCMAKE_OSX_DEPLOYMENT_TARGET=8.0 -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY ..

cmake --build . --config Release

python3 ../add_xcode_folder_reference.py --project=/Users/steve/Code/sdl2-example/build_ios/Rectangles.xcodeproj/project.pbxproj --folderPath=Rectangles/Rectangles.xcassets --target=Rectangles
xcodebuild -workspace Rectangles.xcodeproj/project.xcworkspace -scheme Rectangles archive -archivePath Rectangles.xcarchive
xcodebuild -exportArchive -archivePath Rectangles.xcarchive -exportOptionsPlist ../exportOptions.plist -exportPath .
