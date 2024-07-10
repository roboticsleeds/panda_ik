# assuming that eigen is installed via homebrew. You can get the path using
# brew --prefix eigen and update the paths below.

mkdir -p build

c++ -O3 -Wall -shared -std=c++11 \
    -arch arm64 \
    -I/opt/homebrew/opt/eigen/include/eigen3 \
    -fPIC \
    $(python3 -m pybind11 --includes) \
    panda_ik_pump.cpp \
    -o build/panda_ik_pump.so \
    -L$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
    -lpython$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")

c++ -O3 -Wall -shared -std=c++11 \
    -arch arm64 \
    -I/opt/homebrew/opt/eigen/include/eigen3 \
    -fPIC \
    $(python3 -m pybind11 --includes) \
    panda_ik_hand.cpp \
    -o build/panda_ik_hand.so \
    -L$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
    -lpython$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
