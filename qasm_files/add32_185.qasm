OPENQASM 2.0;
include "qelib1.inc";
gate cv q0,q1 { cu(pi/2,-pi/2,pi/2,0) q0,q1; p(pi/4) q0; }
gate cv_dg q0,q1 { cu(pi/2,pi/2,-pi/2,0) q0,q1; p(7*pi/4) q0; }
qreg x96[1];
qreg x95[1];
qreg x94[1];
qreg x93[1];
qreg x92[1];
qreg x91[1];
qreg x90[1];
qreg x89[1];
qreg x88[1];
qreg x87[1];
qreg x86[1];
qreg x85[1];
qreg x84[1];
qreg x83[1];
qreg x82[1];
qreg x81[1];
qreg x80[1];
qreg x79[1];
qreg x78[1];
qreg x77[1];
qreg x76[1];
qreg x75[1];
qreg x74[1];
qreg x73[1];
qreg x72[1];
qreg x71[1];
qreg x70[1];
qreg x69[1];
qreg x68[1];
qreg x67[1];
qreg x66[1];
qreg x65[1];
qreg x64[1];
qreg x63[1];
qreg x62[1];
qreg x61[1];
qreg x60[1];
qreg x59[1];
qreg x58[1];
qreg x57[1];
qreg x56[1];
qreg x55[1];
qreg x54[1];
qreg x53[1];
qreg x52[1];
qreg x51[1];
qreg x50[1];
qreg x49[1];
qreg x48[1];
qreg x47[1];
qreg x46[1];
qreg x45[1];
qreg x44[1];
qreg x43[1];
qreg x42[1];
qreg x41[1];
qreg x40[1];
qreg x39[1];
qreg x38[1];
qreg x37[1];
qreg x36[1];
qreg x35[1];
qreg x34[1];
qreg x33[1];
qreg x32[1];
qreg x31[1];
qreg x30[1];
qreg x29[1];
qreg x28[1];
qreg x27[1];
qreg x26[1];
qreg x25[1];
qreg x24[1];
qreg x23[1];
qreg x22[1];
qreg x21[1];
qreg x20[1];
qreg x19[1];
qreg x18[1];
qreg x17[1];
qreg x16[1];
qreg x15[1];
qreg x14[1];
qreg x13[1];
qreg x12[1];
qreg x11[1];
qreg x10[1];
qreg x9[1];
qreg x8[1];
qreg x7[1];
qreg x6[1];
qreg x5[1];
qreg x4[1];
qreg x3[1];
qreg x2[1];
qreg x1[1];
qreg x0[1];
cv x0[0],x3[0];
cv x1[0],x3[0];
cv x2[0],x3[0];
cx x0[0],x1[0];
cx x1[0],x2[0];
cv_dg x2[0],x3[0];
cv x4[0],x6[0];
cv x5[0],x6[0];
cv x3[0],x6[0];
cx x4[0],x5[0];
cx x5[0],x3[0];
cv_dg x3[0],x6[0];
cv x7[0],x9[0];
cv x8[0],x9[0];
cv x6[0],x9[0];
cx x7[0],x8[0];
cx x8[0],x6[0];
cv_dg x6[0],x9[0];
cv x10[0],x12[0];
cv x11[0],x12[0];
cv x9[0],x12[0];
cx x10[0],x11[0];
cx x11[0],x9[0];
cv_dg x9[0],x12[0];
cv x13[0],x15[0];
cv x14[0],x15[0];
cv x12[0],x15[0];
cx x13[0],x14[0];
cx x14[0],x12[0];
cv_dg x12[0],x15[0];
cv x16[0],x18[0];
cv x17[0],x18[0];
cv x15[0],x18[0];
cx x16[0],x17[0];
cx x17[0],x15[0];
cv_dg x15[0],x18[0];
cv x19[0],x21[0];
cv x20[0],x21[0];
cv x18[0],x21[0];
cx x19[0],x20[0];
cx x20[0],x18[0];
cv_dg x18[0],x21[0];
cv x22[0],x24[0];
cv x23[0],x24[0];
cv x21[0],x24[0];
cx x22[0],x23[0];
cx x23[0],x21[0];
cv_dg x21[0],x24[0];
cv x25[0],x27[0];
cv x26[0],x27[0];
cv x24[0],x27[0];
cx x25[0],x26[0];
cx x26[0],x24[0];
cv_dg x24[0],x27[0];
cv x28[0],x30[0];
cv x29[0],x30[0];
cv x27[0],x30[0];
cx x28[0],x29[0];
cx x29[0],x27[0];
cv_dg x27[0],x30[0];
cv x31[0],x33[0];
cv x32[0],x33[0];
cv x30[0],x33[0];
cx x31[0],x32[0];
cx x32[0],x30[0];
cv_dg x30[0],x33[0];
cv x34[0],x36[0];
cv x35[0],x36[0];
cv x33[0],x36[0];
cx x34[0],x35[0];
cx x35[0],x33[0];
cv_dg x33[0],x36[0];
cv x37[0],x39[0];
cv x38[0],x39[0];
cv x36[0],x39[0];
cx x37[0],x38[0];
cx x38[0],x36[0];
cv_dg x36[0],x39[0];
cv x40[0],x42[0];
cv x41[0],x42[0];
cv x39[0],x42[0];
cx x40[0],x41[0];
cx x41[0],x39[0];
cv_dg x39[0],x42[0];
cv x43[0],x45[0];
cv x44[0],x45[0];
cv x42[0],x45[0];
cx x43[0],x44[0];
cx x44[0],x42[0];
cv_dg x42[0],x45[0];
cv x46[0],x48[0];
cv x47[0],x48[0];
cv x45[0],x48[0];
cx x46[0],x47[0];
cx x47[0],x45[0];
cv_dg x45[0],x48[0];
cv x49[0],x51[0];
cv x50[0],x51[0];
cv x48[0],x51[0];
cx x49[0],x50[0];
cx x50[0],x48[0];
cv_dg x48[0],x51[0];
cv x52[0],x54[0];
cv x53[0],x54[0];
cv x51[0],x54[0];
cx x52[0],x53[0];
cx x53[0],x51[0];
cv_dg x51[0],x54[0];
cv x55[0],x57[0];
cv x56[0],x57[0];
cv x54[0],x57[0];
cx x55[0],x56[0];
cx x56[0],x54[0];
cv_dg x54[0],x57[0];
cv x58[0],x60[0];
cv x59[0],x60[0];
cv x57[0],x60[0];
cx x58[0],x59[0];
cx x59[0],x57[0];
cv_dg x57[0],x60[0];
cv x61[0],x63[0];
cv x62[0],x63[0];
cv x60[0],x63[0];
cx x61[0],x62[0];
cx x62[0],x60[0];
cv_dg x60[0],x63[0];
cv x64[0],x66[0];
cv x65[0],x66[0];
cv x63[0],x66[0];
cx x64[0],x65[0];
cx x65[0],x63[0];
cv_dg x63[0],x66[0];
cv x67[0],x69[0];
cv x68[0],x69[0];
cv x66[0],x69[0];
cx x67[0],x68[0];
cx x68[0],x66[0];
cv_dg x66[0],x69[0];
cv x70[0],x72[0];
cv x71[0],x72[0];
cv x69[0],x72[0];
cx x70[0],x71[0];
cx x71[0],x69[0];
cv_dg x69[0],x72[0];
cv x73[0],x75[0];
cv x74[0],x75[0];
cv x72[0],x75[0];
cx x73[0],x74[0];
cx x74[0],x72[0];
cv_dg x72[0],x75[0];
cv x76[0],x78[0];
cv x77[0],x78[0];
cv x75[0],x78[0];
cx x76[0],x77[0];
cx x77[0],x75[0];
cv_dg x75[0],x78[0];
cv x79[0],x81[0];
cv x80[0],x81[0];
cv x78[0],x81[0];
cx x79[0],x80[0];
cx x80[0],x78[0];
cv_dg x78[0],x81[0];
cv x82[0],x84[0];
cv x83[0],x84[0];
cv x81[0],x84[0];
cx x82[0],x83[0];
cx x83[0],x81[0];
cv_dg x81[0],x84[0];
cv x85[0],x87[0];
cv x86[0],x87[0];
cv x84[0],x87[0];
cx x85[0],x86[0];
cx x86[0],x84[0];
cv_dg x84[0],x87[0];
cv x88[0],x90[0];
cv x89[0],x90[0];
cv x87[0],x90[0];
cx x88[0],x89[0];
cx x89[0],x87[0];
cv_dg x87[0],x90[0];
cv x91[0],x93[0];
cv x92[0],x93[0];
cv x90[0],x93[0];
cx x91[0],x92[0];
cx x92[0],x90[0];
cv_dg x90[0],x93[0];
cv x94[0],x96[0];
cv x95[0],x96[0];
cv x93[0],x96[0];
cx x94[0],x95[0];
cx x95[0],x93[0];
cv_dg x93[0],x96[0];