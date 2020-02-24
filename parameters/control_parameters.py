import sys
sys.path.append('..')
import numpy as np
import chap5.transfer_function_coef as TF
import parameters.aerosonde_parameters as MAV

gravity = 9.81
sigma = 5
Va0 = 20
Va = 20
Vg = MAV.Va0

#----------roll loop-------------
wn_roll = 10
zeta_roll = 0.707

roll_kp = delta_a_max / roll_e_max
roll_kd = (2*zeta_roll*wn_roll - TF.aphi1)/(TF.aphi2)

#----------course loop-------------
Wx = 7
wn_course = 1/Wx*wn_roll
zeta_course = 2

course_kp = 2*zeta_course*wn_course*Vg/MAV.gravity
course_ki = wn_course**2*Vg/MAV.gravity

#----------sideslip loop-------------
# How to tune emaxbeta?
e_max_beta = 0.2
zeta_beta = 0.707

sideslip_kp = delta_r_max/e_max_beta
wn_beta = (TF.abeta1 + TF.abeta2*sideslip_kp)/2*zeta_beta

sideslip_ki = wn_beta**2/TF.abeta2

#----------yaw damper-------------
# How do you tune this one??

yaw_damper_tau_r = 0.5
yaw_damper_kp = 0.5

#----------pitch loop-------------
wn_pitch = delta_e_max/e_max_pitch
zeta_pitch = 0.707

pitch_kp = (wn_pitch**2 - TF.atheta2)/TF.atheta3
pitch_kd = (2*zeta_pitch*wn_pitch - TF.atheta1)/TF.atheta3
K_theta_DC = (pitch_kp*TF.atheta3)/wn_pitch**2

#----------altitude loop-------------
Wh = 7
wn_altitude = 1/Wh*wn_pitch
zeta_altitude = 0.707
altitude_kp = 2*zeta_altitude*wn_altitude/(K_theta_DC*Va)
altitude_ki = wn_altitude**2/(K_theta_DC*Va)
altitude_zone = 10

#---------airspeed hold using throttle---------------
wn_throttle = 10
zeta_throttle = 0.707
airspeed_throttle_kp = wn_throttle**2/TF.aV2
airspeed_throttle_ki = (2*zeta_throttle*wn_throttle - TF.aV1)/TF.aV2
