OPENQASM 2.0;
include "qelib1.inc";
gate cv q0,q1 { cu(pi/2,-pi/2,pi/2,0) q0,q1; p(pi/4) q0; }
gate cv_dg q0,q1 { cu(pi/2,pi/2,-pi/2,0) q0,q1; p(7*pi/4) q0; }
qreg x0[1];
qreg x1[1];
qreg x2[1];
qreg x3[1];
qreg x4[1];
qreg x5[1];
qreg x6[1];
qreg x7[1];
qreg x8[1];
qreg x9[1];
qreg x10[1];
qreg x11[1];
qreg x12[1];
qreg x13[1];
cx x3[0],x2[0];
cx x4[0],x3[0];
cv x0[0],x2[0];
cx x0[0],x1[0];
cv_dg x1[0],x2[0];
cx x0[0],x1[0];
cv x1[0],x2[0];
cx x5[0],x4[0];
cx x6[0],x5[0];
cv x2[0],x4[0];
cx x3[0],x2[0];
cv_dg x3[0],x4[0];
cv_dg x2[0],x4[0];
cx x7[0],x6[0];
cx x8[0],x7[0];
cv x4[0],x6[0];
cx x5[0],x4[0];
cv_dg x5[0],x6[0];
cv_dg x4[0],x6[0];
cx x9[0],x8[0];
cx x10[0],x9[0];
cv x6[0],x8[0];
cx x7[0],x6[0];
cv_dg x7[0],x8[0];
cv_dg x6[0],x8[0];
cv x8[0],x10[0];
cx x9[0],x8[0];
cv_dg x9[0],x10[0];
cv_dg x8[0],x10[0];
cx x12[0],x13[0];
x x3[0];
x x5[0];
x x7[0];
x x9[0];
cx x10[0],x11[0];
cx x12[0],x10[0];
cv x11[0],x13[0];
cv_dg x10[0],x13[0];
cx x11[0],x10[0];
cv_dg x10[0],x13[0];
cv x8[0],x10[0];
cv_dg x9[0],x10[0];
cx x8[0],x9[0];
cv x9[0],x10[0];
cv x6[0],x8[0];
cv_dg x7[0],x8[0];
cx x6[0],x7[0];
cv x7[0],x8[0];
x x9[0];
cx x12[0],x11[0];
cx x11[0],x10[0];
cv x4[0],x6[0];
cv_dg x5[0],x6[0];
cx x4[0],x5[0];
cv x5[0],x6[0];
x x7[0];
cx x10[0],x8[0];
cv x2[0],x4[0];
cv_dg x3[0],x4[0];
cx x2[0],x3[0];
cv x3[0],x4[0];
x x5[0];
cx x8[0],x6[0];
cv x0[0],x2[0];
cx x1[0],x0[0];
cv_dg x0[0],x2[0];
cv x1[0],x2[0];
x x3[0];
cx x6[0],x4[0];
cx x4[0],x2[0];
cx x4[0],x3[0];
cx x6[0],x5[0];
cx x8[0],x7[0];
cx x10[0],x9[0];
