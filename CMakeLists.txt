cmake_minimum_required(VERSION 3.13)
cmake_policy(VERSION 3.13)
project(qpbo CXX)

include(GNUInstallDirs)

set(QPBO_VERSION_MAJOR 1)
set(QPBO_VERSION_MINOR 5)
set(QPBO_VERSION_PATCH 0)
set(QPBO_VERSION_STRING "${QPBO_VERSION_MAJOR}.${QPBO_VERSION_MINOR}.${QPBO_VERSION_PATCH}")

set(SRC_FILES qpbo.cpp qpbo_extra.cpp qpbo_maxflow.cpp qpbo_postprocessing.cpp)

add_library(${PROJECT_NAME} SHARED ${SRC_FILES})
add_library(${PROJECT_NAME}_static STATIC ${SRC_FILES})
set_target_properties(
	${PROJECT_NAME} ${PROJECT_NAME}_static
	PROPERTIES
		OUTPUT_NAME ${PROJECT_NAME}
		VERSION "${QPBO_VERSION_STRING}")

install(TARGETS ${PROJECT_NAME}
        EXPORT ${PROJECT_NAME}-targets
        DESTINATION "${CMAKE_INSTALL_LIBDIR}")

install(TARGETS ${PROJECT_NAME}_static
        EXPORT ${PROJECT_NAME}-static-targets
        DESTINATION "${CMAKE_INSTALL_LIBDIR}")
install(FILES block.h                   DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/qpbo")
install(FILES qpbo.h                    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/qpbo")

set(prefix     "${CMAKE_INSTALL_PREFIX}")
set(libdir     "${CMAKE_INSTALL_LIBDIR}")
set(includedir "${CMAKE_INSTALL_INCLUDEDIR}")
set(version    "${QPBO_VERSION_STRING}")

configure_file(${PROJECT_NAME}.pc.in ${PROJECT_NAME}.pc @ONLY)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.pc" DESTINATION "${CMAKE_INSTALL_LIBDIR}/pkgconfig")

install(EXPORT "${PROJECT_NAME}-targets"
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}"
        COMPONENT Development)

install(EXPORT "${PROJECT_NAME}-static-targets"
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}"
        COMPONENT Development)

configure_file("${PROJECT_NAME}-config.cmake.in"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-config.cmake"
        @ONLY)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-config.cmake"
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}"
        COMPONENT Development)
