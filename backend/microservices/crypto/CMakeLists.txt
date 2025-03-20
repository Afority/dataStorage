cmake_minimum_required(VERSION 3.16)

project(crypto LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(crypto main.cpp)

find_package(OpenSSL REQUIRED)
target_link_libraries(crypto OpenSSL::SSL)

include(GNUInstallDirs)
install(TARGETS crypto
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
