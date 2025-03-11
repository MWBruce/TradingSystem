cmake_minimum_required(VERSION 3.10)
project(TradingSystem)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(yaml-cpp REQUIRED)

include_directories(${PROJECT_SOURCE_DIR}/src/config_manager)
include_directories(${PROJECT_SOURCE_DIR}/src/backend)

configure_file(${CMAKE_SOURCE_DIR}/config/global_config.yaml ${CMAKE_BINARY_DIR}/config/global_config.yaml COPYONLY)

set(SOURCES
    main.cpp
    src/backend/MainTradingSystemBackend.cpp
    src/config_manager/ConfigManager.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PRIVATE yaml-cpp)
