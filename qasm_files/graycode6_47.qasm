OPENQASM 2.0;
include "qelib1.inc";
qreg a[1];
qreg b[1];
qreg c[1];
qreg d[1];
qreg e[1];
qreg f[1];
cx b[0],a[0];
cx c[0],b[0];
cx d[0],c[0];
cx e[0],d[0];
cx f[0],e[0];
