----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 09/05/2022 06:13:59 PM
-- Design Name: 
-- Module Name: sample_tb - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;
use ieee.std_logic_textio.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity sample_tb is
end sample_tb;

architecture Behavioral of sample_tb is
    --Clock and Reset
    signal clk,reset : std_logic;
    -- Other constants
    constant C_CLK_PERIOD : real := 10.0e-9; -- NS
    -- Testbench DUT generics
    constant DATA_IN_WIDTH : integer := 16; 

    --Declaramos las signal del tb para manejarnos con las señales AXIS.
    signal s_axis_tdata_tb     : std_logic_vector(DATA_IN_WIDTH-1 downto 0);
    signal s_axis_tvalid_tb    : std_logic;
    signal s_axis_tready_tb    : std_logic;
    
        
begin
    -----------------------------------------------------------
    -- Clocks and Reset
    -----------------------------------------------------------
    CLK_GEN : process
    begin
        clk <= '1';
        wait for C_CLK_PERIOD / 2.0 * (1 SEC);
        clk <= '0';
        wait for C_CLK_PERIOD / 2.0 * (1 SEC);
    end process CLK_GEN;

    RESET_GEN : process
    begin
        reset <= '0',
                 '1' after 20.0*C_CLK_PERIOD * (1 SEC);
        wait;
    end process RESET_GEN;
    
    process is
    begin 
        --Asignación por defecto.
        s_axis_tdata_tb     <= (others => '0');
        s_axis_tvalid_tb    <= '0';
        wait until (reset = '1');
        --Haemos un espera en ciclos de reloj
        delay_1 : for i in 0 to 10 loop
            wait until (clk'event and clk = '1');           
        end loop;
        --        
        send_data : for j in 0 to 20 loop
            --Generemos la señal AXI con el pulso en '1' cuando recibamos el tready. 
            if (s_axis_tready_tb = '1') then
                s_axis_tdata_tb  <= std_logic_vector(to_signed(j, DATA_IN_WIDTH));
                s_axis_tvalid_tb <= '1';                
            end if;
            wait until (clk'event and clk = '1');              
        end loop;
        s_axis_tvalid_tb <= '0';
        --Esperamos 10 ciclos de reloj a modo de prueba.
        delay_2 : for i in 0 to 10 loop
            wait until (clk'event and clk = '1');           
        end loop;
    end process; 

DUT : entity work.design_1_wrapper
    port map (
    M_AXIS_0_tdata => open,
    M_AXIS_0_tready => '1',
    M_AXIS_0_tuser => open,
    M_AXIS_0_tvalid => open,
    S_AXIS_0_tdata => s_axis_tdata_tb,
    S_AXIS_0_tready => s_axis_tready_tb,
    S_AXIS_0_tvalid => s_axis_tvalid_tb,
    aresetn_i => reset,
    clk_i => clk        
    );    


end Behavioral;
