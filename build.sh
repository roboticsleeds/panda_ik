mkdir -p build
c++ -O3 -Wall -shared -std=c++11 -I/usr/include/eigen3 -I../franka_analytical_ik/Eigen -fPIC $(python3 -m pybind11 --includes) panda_ik_pump.cpp -o build/panda_ik_pump.so
c++ -O3 -Wall -shared -std=c++11 -I/usr/include/eigen3 -I../franka_analytical_ik/Eigen -fPIC $(python3 -m pybind11 --includes) panda_ik_hand.cpp -o build/panda_ik_hand.so
