# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.31

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/user/Desktop/projects/data_storage/backend/microservices/crypto

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug

# Include any dependencies generated for this target.
include CMakeFiles/crypto.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/crypto.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/crypto.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/crypto.dir/flags.make

CMakeFiles/crypto.dir/codegen:
.PHONY : CMakeFiles/crypto.dir/codegen

CMakeFiles/crypto.dir/main.cpp.o: CMakeFiles/crypto.dir/flags.make
CMakeFiles/crypto.dir/main.cpp.o: /home/user/Desktop/projects/data_storage/backend/microservices/crypto/main.cpp
CMakeFiles/crypto.dir/main.cpp.o: CMakeFiles/crypto.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/crypto.dir/main.cpp.o"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/crypto.dir/main.cpp.o -MF CMakeFiles/crypto.dir/main.cpp.o.d -o CMakeFiles/crypto.dir/main.cpp.o -c /home/user/Desktop/projects/data_storage/backend/microservices/crypto/main.cpp

CMakeFiles/crypto.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/crypto.dir/main.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/Desktop/projects/data_storage/backend/microservices/crypto/main.cpp > CMakeFiles/crypto.dir/main.cpp.i

CMakeFiles/crypto.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/crypto.dir/main.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/Desktop/projects/data_storage/backend/microservices/crypto/main.cpp -o CMakeFiles/crypto.dir/main.cpp.s

# Object files for target crypto
crypto_OBJECTS = \
"CMakeFiles/crypto.dir/main.cpp.o"

# External object files for target crypto
crypto_EXTERNAL_OBJECTS =

crypto: CMakeFiles/crypto.dir/main.cpp.o
crypto: CMakeFiles/crypto.dir/build.make
crypto: CMakeFiles/crypto.dir/compiler_depend.ts
crypto: /usr/lib/libssl.so
crypto: /usr/lib/libcrypto.so
crypto: CMakeFiles/crypto.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable crypto"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/crypto.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/crypto.dir/build: crypto
.PHONY : CMakeFiles/crypto.dir/build

CMakeFiles/crypto.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/crypto.dir/cmake_clean.cmake
.PHONY : CMakeFiles/crypto.dir/clean

CMakeFiles/crypto.dir/depend:
	cd /home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/user/Desktop/projects/data_storage/backend/microservices/crypto /home/user/Desktop/projects/data_storage/backend/microservices/crypto /home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug /home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug /home/user/Desktop/projects/data_storage/backend/microservices/crypto/build/C-Debug/CMakeFiles/crypto.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/crypto.dir/depend

