%%Start and configure
clc;clear;close all
%
model_params.fs = 100e6;
model_params.ts = 1/model_params.fs;
%Open simulink model
open('model');
hdlsetup('model'); 
%%
b = [1 0.75];
a = 1;
fvtool(b,a)

%% Design a filter
b1 = firpm(20,[0 0.4 0.5 1],[1 1 0 0]); 
b2 = firpm(40,[0 0.4 0.5 1],[1 1 0 0]); 
fvtool(b1,1,b2,1)

sine_generator = dsp.SineWave;
sine_generator.Frequency = 40e6;
sine_generator.SampleRate = 100e6;
sine_generator.PhaseOffset = 0;
sine_generator.ComplexOutput = false;
sine_generator.SamplesPerFrame = 1000;
sine_signal = sine_generator();

sine_output = filter(b2,1,sine_signal);




