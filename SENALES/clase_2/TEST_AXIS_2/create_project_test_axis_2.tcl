# Set the reference directory for source file relative paths (by default the value is script directory path)
set origin_dir "."

# Set the project name
set _xil_proj_name_ "TEST_AXIS_2"

# Create project
create_project -force ${_xil_proj_name_} ./${_xil_proj_name_} -part xc7z010clg400-1

# Set the directory path for the new project
set proj_dir [get_property directory [current_project]]

# Set project properties
set obj [current_project]
set_property -name "enable_vhdl_2008" -value "1" -objects $obj



######################## SOURCE FILES ########################
# Set 'sources_1' fileset object
source block_design_AXIS.tcl

update_compile_order -fileset sources_1
make_wrapper -files [get_files */design_1.bd] -top
add_files -norecurse "${origin_dir}/TEST_AXIS_2/TEST_AXIS_2.gen/sources_1/bd/design_1/hdl/design_1_wrapper.v"


######################## SIM FILES ########################
# Create 'sim_1' fileset (if not found)
if {[string equal [get_filesets -quiet sim_1] ""]} {
  create_fileset -simset sim_1
}

# Set 'sim_1' fileset object
set obj [get_filesets sim_1]
set files [list \
 [file normalize "${origin_dir}/sample_tb.vhd"] \
]
add_files -norecurse -fileset $obj $files