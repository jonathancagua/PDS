# Set the reference directory for source file relative paths (by default the value is script directory path)
set origin_dir "."

# Set the project name
set _xil_proj_name_ "TEST_AXIS"

# Create project
create_project -force ${_xil_proj_name_} ./${_xil_proj_name_} -part xc7z010clg400-1

# Set the directory path for the new project
set proj_dir [get_property directory [current_project]]

# Set project properties
set obj [current_project]
set_property -name "enable_vhdl_2008" -value "1" -objects $obj



######################## SOURCE FILES ########################
# Set 'sources_1' fileset object
set obj [get_filesets sources_1]
set files [list \
 [file normalize "${origin_dir}/mult_by_constant.vhd"] \
]
add_files -norecurse -fileset $obj $files
set_property file_type {VHDL 2008} [get_files  "${origin_dir}/mult_by_constant.vhd"]

######################## SIM FILES ########################
# Create 'sim_1' fileset (if not found)
if {[string equal [get_filesets -quiet sim_1] ""]} {
  create_fileset -simset sim_1
}

# Set 'sim_1' fileset object
set obj [get_filesets sim_1]
set files [list \
 [file normalize "${origin_dir}/file_tb.vhd"] \
]
add_files -norecurse -fileset $obj $files

# Add local files from the original project (-no_copy_sources specified)
set files [list \
 [file normalize "${origin_dir}/file_tb_behav.wcfg" ]\
]
set added_files [add_files -fileset sim_1 $files]

# Set 'sim_1' fileset file properties for remote files
set file "$origin_dir/file_tb.vhd"
set file [file normalize $file]
set file_obj [get_files -of_objects [get_filesets sim_1] [list "*$file"]]
set_property -name "file_type" -value "VHDL 2008" -objects $file_obj
