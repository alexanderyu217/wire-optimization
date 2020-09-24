from classes import*

######################
#Tubes of the chassis#
######################
"""Left Side"""
fuf_a_l = Tube('FUF A(Left)', 14.3)
fuf_b_l = Tube('FUF B(Left)', 15.4)
fuf_c_l = Tube('FUF C(Left)', 10.9)
fuf_d_l = Tube('FUF D(Left)', 12.1)
fuf_e_l = Tube('FUF E(Left)', 11.4)
fuf_f_l = Tube('FUF F(Left)', 13.4)
f_upper_r_f_l = Tube('Front Upper Rails Front(Left)', 17.1)
f_upper_r_r_l = Tube('Front Upper Rails Rear(Left)', 8.1)
f_lower_r_l = Tube('Front Lower Rails(Left)', 22.3)
rear_front_bs_l = Tube('Rear Front Bulkhead Support(Left)', 35.3)
u_sis_l = Tube('Upper SIS(Left)', 34.0)
m_sis_front_l = Tube('Middle SIS Front(Left)', 18.4)
m_sis_rear_l = Tube('Middle SIS Rear(Left)', 21.9)
l_sis_front_l = Tube('Lower SIS Front(Left)', 16.4)
l_sis_rear_l = Tube('Lower SIS Rear(Left)', 18.3)
rr_upper_l = Tube('Rear Rails Upper(Left)', 19.4)
rr_middle_l = Tube('Rear Rails Middle(Left)', 24.0)
rr_lower_l = Tube('Rear Rails Lower(Left)', 21.2)
top_l = Tube('Top(Left)', 8.3)

"""Right Side"""
fuf_a_r = Tube('FUF A(Right)', 14.3)
fuf_b_r = Tube('FUF B(Right)', 15.4)
fuf_c_r = Tube('FUF C(Right)', 10.9)
fuf_d_r = Tube('FUF D(Right)', 12.1)
fuf_e_r = Tube('FUF E(Right)', 11.4)
fuf_f_r = Tube('FUF F(Right)', 13.4)
f_upper_r_f_r = Tube('Front Upper Rails Front(Right)', 17.1)
f_upper_r_r_r = Tube('Front Upper Rails Rear(Right)', 8.1)
f_lower_r_r = Tube('Front Lower Rails(Right)', 22.3)
rear_front_bs_r = Tube('Rear Front Bulkhead Support(Right)', 35.3)
u_sis_r = Tube('Upper SIS(Right)', 34.0)
m_sis_front_r = Tube('Middle SIS Front(Right)', 18.4)
m_sis_rear_r = Tube('Middle SIS Rear(Right)', 21.9)
l_sis_front_r = Tube('Lower SIS Front(Right)', 16.4)
l_sis_rear_r = Tube('Lower SIS Rear(Right)', 18.3)
rr_upper_r = Tube('Rear Rails Upper(Right)', 19.4)
rr_middle_r = Tube('Rear Rails Middle(Right)', 24.0)
rr_lower_r = Tube('Rear Rails Lower(Right)', 21.2)
top_r = Tube('Top(Right)', 8.3)

"""Crossing"""
c_d_cross = Tube('C-D Crossing(Plus or Minus 2 Inches)', 17.9)
z_cross = Tube('Z Crossing', 27.4)
k_cross = Tube('K Crossing', 13)

######################
#Nodes of the chassis#
######################

"""Left Side"""
a_l = Intersection('a_l')
b_l = Intersection('b_l')
c_l = Intersection('c_l', [n_t(a_l,rr_middle_l),n_t(b_l,rr_lower_l)])
d_l = Intersection('d_l', [n_t(a_l,rr_upper_l)])
e_l = Intersection('e_l', [n_t(d_l,m_sis_rear_l),n_t(c_l,l_sis_rear_l)])
f_l = Intersection('f_l', [n_t(e_l,l_sis_front_l)])
g_l = Intersection('g_l', [n_t(e_l,m_sis_front_l),n_t(d_l,u_sis_l)])
h_l = Intersection('h_l', [n_t(d_l,rear_front_bs_l)])
i_l = Intersection('i_l', [n_t(f_l,fuf_e_l),n_t(g_l,fuf_c_l)])
j_l = Intersection('j_l', [n_t(i_l,fuf_b_l)])
k_l = Intersection('k_l', [n_t(i_l,fuf_a_l),n_t(f_l,f_lower_r_l)])
l_l = Intersection('l_l', [n_t(j_l,f_upper_r_f_l),n_t(h_l, f_upper_r_r_l),n_t(i_l, fuf_f_l),n_t(g_l,fuf_d_l)])
z_l = Intersection('z_l', [(n_t(d_l, top_l))])

"""Right Side"""
a_r = Intersection('a_r')
b_r = Intersection('b_r')
c_r = Intersection('c_r', [n_t(a_r,rr_middle_r),n_t(b_r,rr_lower_r)])
d_r = Intersection('d_r', [n_t(a_r,rr_upper_r)])
e_r = Intersection('e_r', [n_t(d_r,m_sis_rear_r),n_t(c_r,l_sis_rear_r)])
f_r = Intersection('f_r', [n_t(e_r,l_sis_front_r)])
g_r = Intersection('g_r', [n_t(e_r,m_sis_front_r),n_t(d_r,u_sis_r)])
h_r = Intersection('h_r', [n_t(d_r,rear_front_bs_r)])
i_r = Intersection('i_r', [n_t(f_r,fuf_e_r),n_t(g_r,fuf_c_r)])
j_r = Intersection('j_r', [n_t(i_r,fuf_b_r)])
k_r = Intersection('k_r', [n_t(i_r,fuf_a_r),n_t(f_r,f_lower_r_r)])
l_r = Intersection('l_r', [n_t(j_r,f_upper_r_f_r),n_t(h_r, f_upper_r_r_r),n_t(i_r, fuf_f_r),n_t(g_r,fuf_d_r)])
z_r = Intersection('z_r', [(n_t(d_r, top_r))])







"""Left Side"""
a_l = Intersection('a_l')
b_l = Intersection('b_l')
c_l = Intersection('c_l', [n_t(a_l,rr_middle_l),n_t(b_l,rr_lower_l)])
d_l = Intersection('d_l', [n_t(a_l,rr_upper_l)])
e_l = Intersection('e_l', [n_t(d_l,m_sis_rear_l),n_t(c_l,l_sis_rear_l)])
f_l = Intersection('f_l', [n_t(e_l,l_sis_front_l)])
g_l = Intersection('g_l', [n_t(e_l,m_sis_front_l),n_t(d_l,u_sis_l)])
h_l = Intersection('h_l', [n_t(d_l,rear_front_bs_l)])
i_l = Intersection('i_l', [n_t(f_l,fuf_e_l),n_t(g_l,fuf_c_l)])
j_l = Intersection('j_l', [n_t(i_l,fuf_b_l)])
k_l = Intersection('k_l', [n_t(i_l,fuf_a_l),n_t(f_l,f_lower_r_l)])
l_l = Intersection('l_l', [n_t(j_l,f_upper_r_f_l),n_t(h_l, f_upper_r_r_l),n_t(i_l, fuf_f_l),n_t(g_l,fuf_d_l)])
z_l = Intersection('z_l', [(n_t(d_l, top_l))])

"""Right Side"""
a_r = Intersection('a_r')
b_r = Intersection('b_r')
c_r = Intersection('c_r', [n_t(a_r,rr_middle_r),n_t(b_r,rr_lower_r)])
d_r = Intersection('d_r', [n_t(a_r,rr_upper_r)])
e_r = Intersection('e_r', [n_t(d_r,m_sis_rear_r),n_t(c_r,l_sis_rear_r)])
f_r = Intersection('f_r', [n_t(e_r,l_sis_front_r)])
g_r = Intersection('g_r', [n_t(e_r,m_sis_front_r),n_t(d_r,u_sis_r)])
h_r = Intersection('h_r', [n_t(d_r,rear_front_bs_r)])
i_r = Intersection('i_r', [n_t(f_r,fuf_e_r),n_t(g_r,fuf_c_r)])
j_r = Intersection('j_r', [n_t(i_r,fuf_b_r)])
k_r = Intersection('k_r', [n_t(i_r,fuf_a_r),n_t(f_r,f_lower_r_r)])
l_r = Intersection('l_r', [n_t(j_r,f_upper_r_f_r),n_t(h_r, f_upper_r_r_r),n_t(i_r, fuf_f_r),n_t(g_r,fuf_d_r)])
z_r = Intersection('z_r', [(n_t(d_r, top_r))])

""""Crossing"""
node_connect(z_l, z_r, z_cross)
node_connect(k_l, k_r, k_cross)


#######
#Debug#
#######

