OPENQASM 2.0;
include "qelib1.inc";
gate cv_dg q0,q1 { cu(pi/2,pi/2,-pi/2,0) q0,q1; p(7*pi/4) q0; }
gate cv q0,q1 { cu(pi/2,-pi/2,pi/2,0) q0,q1; p(pi/4) q0; }
qreg a[1];
qreg b[1];
qreg c[1];
cv_dg b[0],a[0];
cv_dg c[0],a[0];
cx c[0],b[0];
cv b[0],a[0];
