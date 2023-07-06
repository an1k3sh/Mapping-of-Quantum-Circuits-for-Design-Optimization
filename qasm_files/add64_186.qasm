OPENQASM 2.0;
include "qelib1.inc";
gate cv q0,q1 { cu(pi/2,-pi/2,pi/2,0) q0,q1; p(pi/4) q0; }
gate cv_dg q0,q1 { cu(pi/2,pi/2,-pi/2,0) q0,q1; p(7*pi/4) q0; }
qreg x192[1];
qreg x191[1];
qreg x190[1];
qreg x189[1];
qreg x188[1];
qreg x187[1];
qreg x186[1];
qreg x185[1];
qreg x184[1];
qreg x183[1];
qreg x182[1];
qreg x181[1];
qreg x180[1];
qreg x179[1];
qreg x178[1];
qreg x177[1];
qreg x176[1];
qreg x175[1];
qreg x174[1];
qreg x173[1];
qreg x172[1];
qreg x171[1];
qreg x170[1];
qreg x169[1];
qreg x168[1];
qreg x167[1];
qreg x166[1];
qreg x165[1];
qreg x164[1];
qreg x163[1];
qreg x162[1];
qreg x161[1];
qreg x160[1];
qreg x159[1];
qreg x158[1];
qreg x157[1];
qreg x156[1];
qreg x155[1];
qreg x154[1];
qreg x153[1];
qreg x152[1];
qreg x151[1];
qreg x150[1];
qreg x149[1];
qreg x148[1];
qreg x147[1];
qreg x146[1];
qreg x145[1];
qreg x144[1];
qreg x143[1];
qreg x142[1];
qreg x141[1];
qreg x140[1];
qreg x139[1];
qreg x138[1];
qreg x137[1];
qreg x136[1];
qreg x135[1];
qreg x134[1];
qreg x133[1];
qreg x132[1];
qreg x131[1];
qreg x130[1];
qreg x129[1];
qreg x128[1];
qreg x127[1];
qreg x126[1];
qreg x125[1];
qreg x124[1];
qreg x123[1];
qreg x122[1];
qreg x121[1];
qreg x120[1];
qreg x119[1];
qreg x118[1];
qreg x117[1];
qreg x116[1];
qreg x115[1];
qreg x114[1];
qreg x113[1];
qreg x112[1];
qreg x111[1];
qreg x110[1];
qreg x109[1];
qreg x108[1];
qreg x107[1];
qreg x106[1];
qreg x105[1];
qreg x104[1];
qreg x103[1];
qreg x102[1];
qreg x101[1];
qreg x100[1];
qreg x99[1];
qreg x98[1];
qreg x97[1];
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
cv x97[0],x99[0];
cv x98[0],x99[0];
cv x96[0],x99[0];
cx x97[0],x98[0];
cx x98[0],x96[0];
cv_dg x96[0],x99[0];
cv x100[0],x102[0];
cv x101[0],x102[0];
cv x99[0],x102[0];
cx x100[0],x101[0];
cx x101[0],x99[0];
cv_dg x99[0],x102[0];
cv x103[0],x105[0];
cv x104[0],x105[0];
cv x102[0],x105[0];
cx x103[0],x104[0];
cx x104[0],x102[0];
cv_dg x102[0],x105[0];
cv x106[0],x108[0];
cv x107[0],x108[0];
cv x105[0],x108[0];
cx x106[0],x107[0];
cx x107[0],x105[0];
cv_dg x105[0],x108[0];
cv x109[0],x111[0];
cv x110[0],x111[0];
cv x108[0],x111[0];
cx x109[0],x110[0];
cx x110[0],x108[0];
cv_dg x108[0],x111[0];
cv x112[0],x114[0];
cv x113[0],x114[0];
cv x111[0],x114[0];
cx x112[0],x113[0];
cx x113[0],x111[0];
cv_dg x111[0],x114[0];
cv x115[0],x117[0];
cv x116[0],x117[0];
cv x114[0],x117[0];
cx x115[0],x116[0];
cx x116[0],x114[0];
cv_dg x114[0],x117[0];
cv x118[0],x120[0];
cv x119[0],x120[0];
cv x117[0],x120[0];
cx x118[0],x119[0];
cx x119[0],x117[0];
cv_dg x117[0],x120[0];
cv x121[0],x123[0];
cv x122[0],x123[0];
cv x120[0],x123[0];
cx x121[0],x122[0];
cx x122[0],x120[0];
cv_dg x120[0],x123[0];
cv x124[0],x126[0];
cv x125[0],x126[0];
cv x123[0],x126[0];
cx x124[0],x125[0];
cx x125[0],x123[0];
cv_dg x123[0],x126[0];
cv x127[0],x129[0];
cv x128[0],x129[0];
cv x126[0],x129[0];
cx x127[0],x128[0];
cx x128[0],x126[0];
cv_dg x126[0],x129[0];
cv x130[0],x132[0];
cv x131[0],x132[0];
cv x129[0],x132[0];
cx x130[0],x131[0];
cx x131[0],x129[0];
cv_dg x129[0],x132[0];
cv x133[0],x135[0];
cv x134[0],x135[0];
cv x132[0],x135[0];
cx x133[0],x134[0];
cx x134[0],x132[0];
cv_dg x132[0],x135[0];
cv x136[0],x138[0];
cv x137[0],x138[0];
cv x135[0],x138[0];
cx x136[0],x137[0];
cx x137[0],x135[0];
cv_dg x135[0],x138[0];
cv x139[0],x141[0];
cv x140[0],x141[0];
cv x138[0],x141[0];
cx x139[0],x140[0];
cx x140[0],x138[0];
cv_dg x138[0],x141[0];
cv x142[0],x144[0];
cv x143[0],x144[0];
cv x141[0],x144[0];
cx x142[0],x143[0];
cx x143[0],x141[0];
cv_dg x141[0],x144[0];
cv x145[0],x147[0];
cv x146[0],x147[0];
cv x144[0],x147[0];
cx x145[0],x146[0];
cx x146[0],x144[0];
cv_dg x144[0],x147[0];
cv x148[0],x150[0];
cv x149[0],x150[0];
cv x147[0],x150[0];
cx x148[0],x149[0];
cx x149[0],x147[0];
cv_dg x147[0],x150[0];
cv x151[0],x153[0];
cv x152[0],x153[0];
cv x150[0],x153[0];
cx x151[0],x152[0];
cx x152[0],x150[0];
cv_dg x150[0],x153[0];
cv x154[0],x156[0];
cv x155[0],x156[0];
cv x153[0],x156[0];
cx x154[0],x155[0];
cx x155[0],x153[0];
cv_dg x153[0],x156[0];
cv x157[0],x159[0];
cv x158[0],x159[0];
cv x156[0],x159[0];
cx x157[0],x158[0];
cx x158[0],x156[0];
cv_dg x156[0],x159[0];
cv x160[0],x162[0];
cv x161[0],x162[0];
cv x159[0],x162[0];
cx x160[0],x161[0];
cx x161[0],x159[0];
cv_dg x159[0],x162[0];
cv x163[0],x165[0];
cv x164[0],x165[0];
cv x162[0],x165[0];
cx x163[0],x164[0];
cx x164[0],x162[0];
cv_dg x162[0],x165[0];
cv x166[0],x168[0];
cv x167[0],x168[0];
cv x165[0],x168[0];
cx x166[0],x167[0];
cx x167[0],x165[0];
cv_dg x165[0],x168[0];
cv x169[0],x171[0];
cv x170[0],x171[0];
cv x168[0],x171[0];
cx x169[0],x170[0];
cx x170[0],x168[0];
cv_dg x168[0],x171[0];
cv x172[0],x174[0];
cv x173[0],x174[0];
cv x171[0],x174[0];
cx x172[0],x173[0];
cx x173[0],x171[0];
cv_dg x171[0],x174[0];
cv x175[0],x177[0];
cv x176[0],x177[0];
cv x174[0],x177[0];
cx x175[0],x176[0];
cx x176[0],x174[0];
cv_dg x174[0],x177[0];
cv x178[0],x180[0];
cv x179[0],x180[0];
cv x177[0],x180[0];
cx x178[0],x179[0];
cx x179[0],x177[0];
cv_dg x177[0],x180[0];
cv x181[0],x183[0];
cv x182[0],x183[0];
cv x180[0],x183[0];
cx x181[0],x182[0];
cx x182[0],x180[0];
cv_dg x180[0],x183[0];
cv x184[0],x186[0];
cv x185[0],x186[0];
cv x183[0],x186[0];
cx x184[0],x185[0];
cx x185[0],x183[0];
cv_dg x183[0],x186[0];
cv x187[0],x189[0];
cv x188[0],x189[0];
cv x186[0],x189[0];
cx x187[0],x188[0];
cx x188[0],x186[0];
cv_dg x186[0],x189[0];
cv x190[0],x192[0];
cv x191[0],x192[0];
cv x189[0],x192[0];
cx x190[0],x191[0];
cx x191[0],x189[0];
cv_dg x189[0],x192[0];
