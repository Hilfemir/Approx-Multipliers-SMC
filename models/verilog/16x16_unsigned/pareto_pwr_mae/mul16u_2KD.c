/***
* This code is a part of EvoApproxLib library (ehw.fit.vutbr.cz/approxlib) distributed under The MIT License.
* When used, please cite the following article(s): V. Mrazek, Z. Vasicek, L. Sekanina, H. Jiang and J. Han, "Scalable Construction of Approximate Multipliers With Formally Guaranteed Worst Case Error" in IEEE Transactions on Very Large Scale Integration (VLSI) Systems, vol. 26, no. 11, pp. 2572-2576, Nov. 2018. doi: 10.1109/TVLSI.2018.2856362 
* This file contains a circuit from a sub-set of pareto optimal circuits with respect to the pwr and mae parameters
***/
// MAE% = 0.000075 %
// MAE = 3230 
// WCE% = 0.00042 %
// WCE = 18075 
// WCRE% = 300.39 %
// EP% = 99.84 %
// MRE% = 0.0067 %
// MSE = 16238.254e3 
// PDK45_PWR = 1.648 mW
// PDK45_AREA = 2404.2 um2
// PDK45_DELAY = 2.44 ns
#include <stdint.h>
#include <stdlib.h>

uint16_t mul8_364(uint8_t a, uint8_t b)
{
  uint16_t c = 0;
  uint8_t n0 = (a >> 0) & 0x1;
  uint8_t n2 = (a >> 1) & 0x1;
  uint8_t n4 = (a >> 2) & 0x1;
  uint8_t n6 = (a >> 3) & 0x1;
  uint8_t n8 = (a >> 4) & 0x1;
  uint8_t n10 = (a >> 5) & 0x1;
  uint8_t n12 = (a >> 6) & 0x1;
  uint8_t n14 = (a >> 7) & 0x1;
  uint8_t n16 = (b >> 0) & 0x1;
  uint8_t n18 = (b >> 1) & 0x1;
  uint8_t n20 = (b >> 2) & 0x1;
  uint8_t n22 = (b >> 3) & 0x1;
  uint8_t n24 = (b >> 4) & 0x1;
  uint8_t n26 = (b >> 5) & 0x1;
  uint8_t n28 = (b >> 6) & 0x1;
  uint8_t n30 = (b >> 7) & 0x1;
  uint8_t n32;
  uint8_t n48;
  uint8_t n64;
  uint8_t n82;
  uint8_t n98;
  uint8_t n114;
  uint8_t n132;
  uint8_t n149;
  uint8_t n164;
  uint8_t n167;
  uint8_t n182;
  uint8_t n198;
  uint8_t n214;
  uint8_t n232;
  uint8_t n248;
  uint8_t n264;
  uint8_t n282;
  uint8_t n298;
  uint8_t n299;
  uint8_t n314;
  uint8_t n315;
  uint8_t n332;
  uint8_t n333;
  uint8_t n348;
  uint8_t n349;
  uint8_t n364;
  uint8_t n365;
  uint8_t n382;
  uint8_t n383;
  uint8_t n398;
  uint8_t n399;
  uint8_t n414;
  uint8_t n432;
  uint8_t n448;
  uint8_t n464;
  uint8_t n482;
  uint8_t n498;
  uint8_t n514;
  uint8_t n532;
  uint8_t n548;
  uint8_t n549;
  uint8_t n564;
  uint8_t n565;
  uint8_t n582;
  uint8_t n583;
  uint8_t n598;
  uint8_t n599;
  uint8_t n614;
  uint8_t n615;
  uint8_t n632;
  uint8_t n633;
  uint8_t n648;
  uint8_t n649;
  uint8_t n664;
  uint8_t n682;
  uint8_t n698;
  uint8_t n714;
  uint8_t n732;
  uint8_t n748;
  uint8_t n764;
  uint8_t n782;
  uint8_t n798;
  uint8_t n799;
  uint8_t n814;
  uint8_t n815;
  uint8_t n832;
  uint8_t n833;
  uint8_t n848;
  uint8_t n849;
  uint8_t n864;
  uint8_t n865;
  uint8_t n882;
  uint8_t n883;
  uint8_t n898;
  uint8_t n899;
  uint8_t n914;
  uint8_t n932;
  uint8_t n948;
  uint8_t n964;
  uint8_t n982;
  uint8_t n998;
  uint8_t n1014;
  uint8_t n1032;
  uint8_t n1048;
  uint8_t n1049;
  uint8_t n1064;
  uint8_t n1065;
  uint8_t n1082;
  uint8_t n1083;
  uint8_t n1098;
  uint8_t n1099;
  uint8_t n1114;
  uint8_t n1115;
  uint8_t n1132;
  uint8_t n1133;
  uint8_t n1148;
  uint8_t n1149;
  uint8_t n1164;
  uint8_t n1182;
  uint8_t n1198;
  uint8_t n1214;
  uint8_t n1232;
  uint8_t n1248;
  uint8_t n1264;
  uint8_t n1282;
  uint8_t n1298;
  uint8_t n1299;
  uint8_t n1314;
  uint8_t n1315;
  uint8_t n1332;
  uint8_t n1333;
  uint8_t n1348;
  uint8_t n1349;
  uint8_t n1364;
  uint8_t n1365;
  uint8_t n1382;
  uint8_t n1383;
  uint8_t n1398;
  uint8_t n1399;
  uint8_t n1414;
  uint8_t n1432;
  uint8_t n1448;
  uint8_t n1464;
  uint8_t n1482;
  uint8_t n1498;
  uint8_t n1514;
  uint8_t n1532;
  uint8_t n1548;
  uint8_t n1549;
  uint8_t n1564;
  uint8_t n1565;
  uint8_t n1582;
  uint8_t n1583;
  uint8_t n1598;
  uint8_t n1599;
  uint8_t n1614;
  uint8_t n1615;
  uint8_t n1632;
  uint8_t n1633;
  uint8_t n1648;
  uint8_t n1649;
  uint8_t n1664;
  uint8_t n1682;
  uint8_t n1698;
  uint8_t n1714;
  uint8_t n1732;
  uint8_t n1748;
  uint8_t n1764;
  uint8_t n1782;
  uint8_t n1798;
  uint8_t n1799;
  uint8_t n1814;
  uint8_t n1815;
  uint8_t n1832;
  uint8_t n1833;
  uint8_t n1848;
  uint8_t n1849;
  uint8_t n1864;
  uint8_t n1865;
  uint8_t n1882;
  uint8_t n1883;
  uint8_t n1898;
  uint8_t n1899;
  uint8_t n1914;
  uint8_t n1915;
  uint8_t n1932;
  uint8_t n1933;
  uint8_t n1948;
  uint8_t n1949;
  uint8_t n1964;
  uint8_t n1965;
  uint8_t n1982;
  uint8_t n1983;
  uint8_t n1998;
  uint8_t n1999;
  uint8_t n2014;
  uint8_t n2015;

  n32 = n0 & n16;
  n48 = n2 & n16;
  n64 = n4 & n16;
  n82 = n6 & n16;
  n98 = n8 & n16;
  n114 = n10 & n16;
  n132 = n12 & n16;
  n149 = n14 & n16;
  n164 = n0 & n18;
  n167 = n149;
  n182 = n2 & n18;
  n198 = n4 & n18;
  n214 = n6 & n18;
  n232 = n8 & n18;
  n248 = n10 & n18;
  n264 = n12 & n18;
  n282 = n14 & n18;
  n298 = n48 ^ n164;
  n299 = n48 & n164;
  n314 = n64 ^ n182;
  n315 = n64 & n182;
  n332 = n82 ^ n198;
  n333 = n82 & n198;
  n348 = n98 ^ n214;
  n349 = n98 & n214;
  n364 = n114 ^ n232;
  n365 = n114 & n232;
  n382 = n132 ^ n248;
  n383 = n132 & n248;
  n398 = n167 ^ n264;
  n399 = n167 & n264;
  n414 = n0 & n20;
  n432 = n2 & n20;
  n448 = n4 & n20;
  n464 = n6 & n20;
  n482 = n8 & n20;
  n498 = n10 & n20;
  n514 = n12 & n20;
  n532 = n14 & n20;
  n548 = (n314 ^ n414) ^ n299;
  n549 = (n314 & n414) | (n414 & n299) | (n314 & n299);
  n564 = (n332 ^ n432) ^ n315;
  n565 = (n332 & n432) | (n432 & n315) | (n332 & n315);
  n582 = (n348 ^ n448) ^ n333;
  n583 = (n348 & n448) | (n448 & n333) | (n348 & n333);
  n598 = (n364 ^ n464) ^ n349;
  n599 = (n364 & n464) | (n464 & n349) | (n364 & n349);
  n614 = (n382 ^ n482) ^ n365;
  n615 = (n382 & n482) | (n482 & n365) | (n382 & n365);
  n632 = (n398 ^ n498) ^ n383;
  n633 = (n398 & n498) | (n498 & n383) | (n398 & n383);
  n648 = (n282 ^ n514) ^ n399;
  n649 = (n282 & n514) | (n514 & n399) | (n282 & n399);
  n664 = n0 & n22;
  n682 = n2 & n22;
  n698 = n4 & n22;
  n714 = n6 & n22;
  n732 = n8 & n22;
  n748 = n10 & n22;
  n764 = n12 & n22;
  n782 = n14 & n22;
  n798 = (n564 ^ n664) ^ n549;
  n799 = (n564 & n664) | (n664 & n549) | (n564 & n549);
  n814 = (n582 ^ n682) ^ n565;
  n815 = (n582 & n682) | (n682 & n565) | (n582 & n565);
  n832 = (n598 ^ n698) ^ n583;
  n833 = (n598 & n698) | (n698 & n583) | (n598 & n583);
  n848 = (n614 ^ n714) ^ n599;
  n849 = (n614 & n714) | (n714 & n599) | (n614 & n599);
  n864 = (n632 ^ n732) ^ n615;
  n865 = (n632 & n732) | (n732 & n615) | (n632 & n615);
  n882 = (n648 ^ n748) ^ n633;
  n883 = (n648 & n748) | (n748 & n633) | (n648 & n633);
  n898 = (n532 ^ n764) ^ n649;
  n899 = (n532 & n764) | (n764 & n649) | (n532 & n649);
  n914 = n0 & n24;
  n932 = n2 & n24;
  n948 = n4 & n24;
  n964 = n6 & n24;
  n982 = n8 & n24;
  n998 = n10 & n24;
  n1014 = n12 & n24;
  n1032 = n14 & n24;
  n1048 = (n814 ^ n914) ^ n799;
  n1049 = (n814 & n914) | (n914 & n799) | (n814 & n799);
  n1064 = (n832 ^ n932) ^ n815;
  n1065 = (n832 & n932) | (n932 & n815) | (n832 & n815);
  n1082 = (n848 ^ n948) ^ n833;
  n1083 = (n848 & n948) | (n948 & n833) | (n848 & n833);
  n1098 = (n864 ^ n964) ^ n849;
  n1099 = (n864 & n964) | (n964 & n849) | (n864 & n849);
  n1114 = (n882 ^ n982) ^ n865;
  n1115 = (n882 & n982) | (n982 & n865) | (n882 & n865);
  n1132 = (n898 ^ n998) ^ n883;
  n1133 = (n898 & n998) | (n998 & n883) | (n898 & n883);
  n1148 = (n782 ^ n1014) ^ n899;
  n1149 = (n782 & n1014) | (n1014 & n899) | (n782 & n899);
  n1164 = n0 & n26;
  n1182 = n2 & n26;
  n1198 = n4 & n26;
  n1214 = n6 & n26;
  n1232 = n8 & n26;
  n1248 = n10 & n26;
  n1264 = n12 & n26;
  n1282 = n14 & n26;
  n1298 = (n1064 ^ n1164) ^ n1049;
  n1299 = (n1064 & n1164) | (n1164 & n1049) | (n1064 & n1049);
  n1314 = (n1082 ^ n1182) ^ n1065;
  n1315 = (n1082 & n1182) | (n1182 & n1065) | (n1082 & n1065);
  n1332 = (n1098 ^ n1198) ^ n1083;
  n1333 = (n1098 & n1198) | (n1198 & n1083) | (n1098 & n1083);
  n1348 = (n1114 ^ n1214) ^ n1099;
  n1349 = (n1114 & n1214) | (n1214 & n1099) | (n1114 & n1099);
  n1364 = (n1132 ^ n1232) ^ n1115;
  n1365 = (n1132 & n1232) | (n1232 & n1115) | (n1132 & n1115);
  n1382 = (n1148 ^ n1248) ^ n1133;
  n1383 = (n1148 & n1248) | (n1248 & n1133) | (n1148 & n1133);
  n1398 = (n1032 ^ n1264) ^ n1149;
  n1399 = (n1032 & n1264) | (n1264 & n1149) | (n1032 & n1149);
  n1414 = n0 & n28;
  n1432 = n2 & n28;
  n1448 = n4 & n28;
  n1464 = n6 & n28;
  n1482 = n8 & n28;
  n1498 = n10 & n28;
  n1514 = n12 & n28;
  n1532 = n14 & n28;
  n1548 = (n1314 ^ n1414) ^ n1299;
  n1549 = (n1314 & n1414) | (n1414 & n1299) | (n1314 & n1299);
  n1564 = (n1332 ^ n1432) ^ n1315;
  n1565 = (n1332 & n1432) | (n1432 & n1315) | (n1332 & n1315);
  n1582 = (n1348 ^ n1448) ^ n1333;
  n1583 = (n1348 & n1448) | (n1448 & n1333) | (n1348 & n1333);
  n1598 = (n1364 ^ n1464) ^ n1349;
  n1599 = (n1364 & n1464) | (n1464 & n1349) | (n1364 & n1349);
  n1614 = (n1382 ^ n1482) ^ n1365;
  n1615 = (n1382 & n1482) | (n1482 & n1365) | (n1382 & n1365);
  n1632 = (n1398 ^ n1498) ^ n1383;
  n1633 = (n1398 & n1498) | (n1498 & n1383) | (n1398 & n1383);
  n1648 = (n1282 ^ n1514) ^ n1399;
  n1649 = (n1282 & n1514) | (n1514 & n1399) | (n1282 & n1399);
  n1664 = n0 & n30;
  n1682 = n2 & n30;
  n1698 = n4 & n30;
  n1714 = n6 & n30;
  n1732 = n8 & n30;
  n1748 = n10 & n30;
  n1764 = n12 & n30;
  n1782 = n14 & n30;
  n1798 = (n1564 ^ n1664) ^ n1549;
  n1799 = (n1564 & n1664) | (n1664 & n1549) | (n1564 & n1549);
  n1814 = (n1582 ^ n1682) ^ n1565;
  n1815 = (n1582 & n1682) | (n1682 & n1565) | (n1582 & n1565);
  n1832 = (n1598 ^ n1698) ^ n1583;
  n1833 = (n1598 & n1698) | (n1698 & n1583) | (n1598 & n1583);
  n1848 = (n1614 ^ n1714) ^ n1599;
  n1849 = (n1614 & n1714) | (n1714 & n1599) | (n1614 & n1599);
  n1864 = (n1632 ^ n1732) ^ n1615;
  n1865 = (n1632 & n1732) | (n1732 & n1615) | (n1632 & n1615);
  n1882 = (n1648 ^ n1748) ^ n1633;
  n1883 = (n1648 & n1748) | (n1748 & n1633) | (n1648 & n1633);
  n1898 = (n1532 ^ n1764) ^ n1649;
  n1899 = (n1532 & n1764) | (n1764 & n1649) | (n1532 & n1649);
  n1914 = n1814 ^ n1799;
  n1915 = n1814 & n1799;
  n1932 = (n1832 ^ n1815) ^ n1915;
  n1933 = (n1832 & n1815) | (n1815 & n1915) | (n1832 & n1915);
  n1948 = (n1848 ^ n1833) ^ n1933;
  n1949 = (n1848 & n1833) | (n1833 & n1933) | (n1848 & n1933);
  n1964 = (n1864 ^ n1849) ^ n1949;
  n1965 = (n1864 & n1849) | (n1849 & n1949) | (n1864 & n1949);
  n1982 = (n1882 ^ n1865) ^ n1965;
  n1983 = (n1882 & n1865) | (n1865 & n1965) | (n1882 & n1965);
  n1998 = (n1898 ^ n1883) ^ n1983;
  n1999 = (n1898 & n1883) | (n1883 & n1983) | (n1898 & n1983);
  n2014 = (n1782 ^ n1899) ^ n1999;
  n2015 = (n1782 & n1899) | (n1899 & n1999) | (n1782 & n1999);

  c |= (n32 & 0x1) << 0;
  c |= (n298 & 0x1) << 1;
  c |= (n548 & 0x1) << 2;
  c |= (n798 & 0x1) << 3;
  c |= (n1048 & 0x1) << 4;
  c |= (n1298 & 0x1) << 5;
  c |= (n1548 & 0x1) << 6;
  c |= (n1798 & 0x1) << 7;
  c |= (n1914 & 0x1) << 8;
  c |= (n1932 & 0x1) << 9;
  c |= (n1948 & 0x1) << 10;
  c |= (n1964 & 0x1) << 11;
  c |= (n1982 & 0x1) << 12;
  c |= (n1998 & 0x1) << 13;
  c |= (n2014 & 0x1) << 14;
  c |= (n2015 & 0x1) << 15;

  return c;
}

uint64_t mult8_cgp14ep_ep64716_wc26_csamrca(const uint64_t B,const uint64_t A)
{
   uint64_t O, dout_20, dout_21, dout_22, dout_23, dout_27, dout_28, dout_29, dout_30, dout_31, dout_38, dout_39, dout_40, dout_41, dout_42, dout_43, dout_44, dout_45, dout_48, dout_49, dout_50, dout_51, dout_52, dout_53, dout_63, dout_64, dout_65, dout_69, dout_70, dout_71, dout_72, dout_73, dout_74, dout_75, dout_76, dout_77, dout_78, dout_79, dout_80, dout_81, dout_82, dout_83, dout_84, dout_85, dout_87, dout_88, dout_91, dout_92, dout_93, dout_94, dout_95, dout_96, dout_103, dout_105, dout_107, dout_108, dout_109, dout_110, dout_111, dout_112, dout_113, dout_114, dout_115, dout_116, dout_117, dout_118, dout_119, dout_120, dout_121, dout_122, dout_123, dout_124, dout_125, dout_126, dout_127, dout_128, dout_129, dout_130, dout_131, dout_132, dout_133, dout_134, dout_135, dout_136, dout_137, dout_138, dout_139, dout_140, dout_141, dout_145, dout_146, dout_147, dout_148, dout_149, dout_150, dout_151, dout_152, dout_153, dout_154, dout_155, dout_156, dout_157, dout_158, dout_159, dout_160, dout_161, dout_162, dout_163, dout_164, dout_165, dout_166, dout_167, dout_168, dout_169, dout_170, dout_171, dout_172, dout_173, dout_174, dout_175, dout_176, dout_177, dout_178, dout_179, dout_180, dout_181, dout_182, dout_183, dout_184, dout_185, dout_186, dout_187, dout_188, dout_189, dout_190, dout_191, dout_192, dout_193, dout_194, dout_195, dout_196, dout_197, dout_198, dout_199, dout_200, dout_201, dout_202, dout_203, dout_204, dout_205, dout_206, dout_207, dout_208, dout_209, dout_210, dout_211, dout_212, dout_213, dout_214, dout_215, dout_216, dout_217, dout_218, dout_219, dout_220, dout_221, dout_222, dout_223, dout_224, dout_225, dout_226, dout_227, dout_228, dout_229, dout_230, dout_231, dout_232, dout_233, dout_234, dout_235, dout_236, dout_237, dout_238, dout_239, dout_240, dout_241, dout_242, dout_243, dout_244, dout_245, dout_246, dout_247, dout_248, dout_249, dout_250, dout_251, dout_252, dout_253, dout_254, dout_255, dout_256, dout_257, dout_258, dout_259, dout_260, dout_261, dout_262, dout_263, dout_264, dout_265, dout_266, dout_267, dout_268, dout_269, dout_270, dout_271, dout_272, dout_273, dout_274, dout_275, dout_276, dout_277, dout_278, dout_279, dout_280, dout_281, dout_282, dout_283, dout_284, dout_285, dout_286, dout_287, dout_288, dout_289, dout_290, dout_291, dout_292, dout_293, dout_294, dout_295, dout_296, dout_297, dout_298, dout_299, dout_300, dout_301, dout_302, dout_303, dout_304, dout_305, dout_306, dout_307, dout_308, dout_309, dout_310, dout_311, dout_312, dout_313, dout_314, dout_315, dout_316, dout_317, dout_318, dout_319, dout_320, dout_321, dout_322, dout_323, dout_324, dout_325, dout_326, dout_327, dout_328, dout_329, dout_330, dout_331, dout_332, dout_333, dout_334, dout_335;   int avg=0;

   dout_20=((B >> 4)&1)&((A >> 0)&1);
   dout_21=((B >> 5)&1)&((A >> 0)&1);
   dout_22=((B >> 6)&1)&((A >> 0)&1);
   dout_23=((B >> 7)&1)&((A >> 0)&1);
   dout_27=((B >> 3)&1)&((A >> 1)&1);
   dout_28=((B >> 4)&1)&((A >> 1)&1);
   dout_29=((B >> 5)&1)&((A >> 1)&1);
   dout_30=((B >> 6)&1)&((A >> 1)&1);
   dout_31=((B >> 7)&1)&((A >> 1)&1);
   dout_38=dout_20|dout_27;
   dout_39=dout_20&dout_27;
   dout_40=dout_21^dout_28;
   dout_41=dout_21&dout_28;
   dout_42=dout_22^dout_29;
   dout_43=dout_22&dout_29;
   dout_44=dout_23^dout_30;
   dout_45=dout_23&dout_30;
   dout_48=((B >> 2)&1)&((A >> 2)&1);
   dout_49=((B >> 3)&1)&((A >> 2)&1);
   dout_50=((B >> 4)&1)&((A >> 2)&1);
   dout_51=((B >> 5)&1)&((A >> 2)&1);
   dout_52=((B >> 6)&1)&((A >> 2)&1);
   dout_53=((B >> 7)&1)&((A >> 2)&1);
   dout_63=((A >> 3)&1)&((B >> 1)&1);
   dout_64=dout_38|dout_48;
   dout_65=dout_38&dout_48;
   dout_69=dout_40^dout_49;
   dout_70=dout_40&dout_49;
   dout_71=dout_69&dout_39;
   dout_72=dout_69^dout_39;
   dout_73=dout_70|dout_71;
   dout_74=dout_42^dout_50;
   dout_75=dout_42&dout_50;
   dout_76=dout_74&dout_41;
   dout_77=dout_74^dout_41;
   dout_78=dout_75|dout_76;
   dout_79=dout_44^dout_51;
   dout_80=dout_44&dout_51;
   dout_81=dout_79&dout_43;
   dout_82=dout_79^dout_43;
   dout_83=dout_80|dout_81;
   dout_84=dout_31^dout_52;
   dout_85=dout_31&dout_52;
   dout_87=dout_84^dout_45;
   dout_88=dout_85|dout_45;
   dout_91=((B >> 2)&1)&((A >> 3)&1);
   dout_92=((B >> 3)&1)&((A >> 3)&1);
   dout_93=((B >> 4)&1)&((A >> 3)&1);
   dout_94=((B >> 5)&1)&((A >> 3)&1);
   dout_95=((B >> 6)&1)&((A >> 3)&1);
   dout_96=((B >> 7)&1)&((A >> 3)&1);
   dout_103=dout_64&dout_63;
   dout_105=dout_64|dout_63;
   dout_107=dout_72^dout_91;
   dout_108=dout_72&dout_91;
   dout_109=dout_107&dout_65;
   dout_110=dout_107^dout_65;
   dout_111=dout_108|dout_109;
   dout_112=dout_77^dout_92;
   dout_113=dout_77&dout_92;
   dout_114=dout_112&dout_73;
   dout_115=dout_112^dout_73;
   dout_116=dout_113|dout_114;
   dout_117=dout_82^dout_93;
   dout_118=dout_82&dout_93;
   dout_119=dout_117&dout_78;
   dout_120=dout_117^dout_78;
   dout_121=dout_118|dout_119;
   dout_122=dout_87^dout_94;
   dout_123=dout_87&dout_94;
   dout_124=dout_122&dout_83;
   dout_125=dout_122^dout_83;
   dout_126=dout_123|dout_124;
   dout_127=dout_53^dout_95;
   dout_128=dout_53&dout_95;
   dout_129=dout_127&dout_88;
   dout_130=dout_127^dout_88;
   dout_131=dout_128|dout_129;
   dout_132=((B >> 0)&1)&((A >> 4)&1);
   dout_133=((B >> 1)&1)&((A >> 4)&1);
   dout_134=((B >> 2)&1)&((A >> 4)&1);
   dout_135=((B >> 3)&1)&((A >> 4)&1);
   dout_136=((B >> 4)&1)&((A >> 4)&1);
   dout_137=((B >> 5)&1)&((A >> 4)&1);
   dout_138=((B >> 6)&1)&((A >> 4)&1);
   dout_139=((B >> 7)&1)&((A >> 4)&1);
   dout_140=dout_105^dout_132;
   dout_141=dout_105&dout_132;
   dout_145=dout_110^dout_133;
   dout_146=dout_110&dout_133;
   dout_147=dout_145&dout_103;
   dout_148=dout_145^dout_103;
   dout_149=dout_146|dout_147;
   dout_150=dout_115^dout_134;
   dout_151=dout_115&dout_134;
   dout_152=dout_150&dout_111;
   dout_153=dout_150^dout_111;
   dout_154=dout_151|dout_152;
   dout_155=dout_120^dout_135;
   dout_156=dout_120&dout_135;
   dout_157=dout_155&dout_116;
   dout_158=dout_155^dout_116;
   dout_159=dout_156|dout_157;
   dout_160=dout_125^dout_136;
   dout_161=dout_125&dout_136;
   dout_162=dout_160&dout_121;
   dout_163=dout_160^dout_121;
   dout_164=dout_161|dout_162;
   dout_165=dout_130^dout_137;
   dout_166=dout_130&dout_137;
   dout_167=dout_165&dout_126;
   dout_168=dout_165^dout_126;
   dout_169=dout_166|dout_167;
   dout_170=dout_96^dout_138;
   dout_171=dout_96&dout_138;
   dout_172=dout_170&dout_131;
   dout_173=dout_170^dout_131;
   dout_174=dout_171|dout_172;
   dout_175=((B >> 0)&1)&((A >> 5)&1);
   dout_176=((B >> 1)&1)&((A >> 5)&1);
   dout_177=((B >> 2)&1)&((A >> 5)&1);
   dout_178=((B >> 3)&1)&((A >> 5)&1);
   dout_179=((B >> 4)&1)&((A >> 5)&1);
   dout_180=((B >> 5)&1)&((A >> 5)&1);
   dout_181=((B >> 6)&1)&((A >> 5)&1);
   dout_182=((B >> 7)&1)&((A >> 5)&1);
   dout_183=dout_148^dout_175;
   dout_184=dout_148&dout_175;
   dout_185=dout_183&dout_141;
   dout_186=dout_183^dout_141;
   dout_187=dout_184|dout_185;
   dout_188=dout_153^dout_176;
   dout_189=dout_153&dout_176;
   dout_190=dout_188&dout_149;
   dout_191=dout_188^dout_149;
   dout_192=dout_189|dout_190;
   dout_193=dout_158^dout_177;
   dout_194=dout_158&dout_177;
   dout_195=dout_193&dout_154;
   dout_196=dout_193^dout_154;
   dout_197=dout_194|dout_195;
   dout_198=dout_163^dout_178;
   dout_199=dout_163&dout_178;
   dout_200=dout_198&dout_159;
   dout_201=dout_198^dout_159;
   dout_202=dout_199|dout_200;
   dout_203=dout_168^dout_179;
   dout_204=dout_168&dout_179;
   dout_205=dout_203&dout_164;
   dout_206=dout_203^dout_164;
   dout_207=dout_204|dout_205;
   dout_208=dout_173^dout_180;
   dout_209=dout_173&dout_180;
   dout_210=dout_208&dout_169;
   dout_211=dout_208^dout_169;
   dout_212=dout_209|dout_210;
   dout_213=dout_139^dout_181;
   dout_214=dout_139&dout_181;
   dout_215=dout_213&dout_174;
   dout_216=dout_213^dout_174;
   dout_217=dout_214|dout_215;
   dout_218=((B >> 0)&1)&((A >> 6)&1);
   dout_219=((B >> 1)&1)&((A >> 6)&1);
   dout_220=((B >> 2)&1)&((A >> 6)&1);
   dout_221=((B >> 3)&1)&((A >> 6)&1);
   dout_222=((B >> 4)&1)&((A >> 6)&1);
   dout_223=((B >> 5)&1)&((A >> 6)&1);
   dout_224=((B >> 6)&1)&((A >> 6)&1);
   dout_225=((B >> 7)&1)&((A >> 6)&1);
   dout_226=dout_191^dout_218;
   dout_227=dout_191&dout_218;
   dout_228=dout_226&dout_187;
   dout_229=dout_226^dout_187;
   dout_230=dout_227|dout_228;
   dout_231=dout_196^dout_219;
   dout_232=dout_196&dout_219;
   dout_233=dout_231&dout_192;
   dout_234=dout_231^dout_192;
   dout_235=dout_232|dout_233;
   dout_236=dout_201^dout_220;
   dout_237=dout_201&dout_220;
   dout_238=dout_236&dout_197;
   dout_239=dout_236^dout_197;
   dout_240=dout_237|dout_238;
   dout_241=dout_206^dout_221;
   dout_242=dout_206&dout_221;
   dout_243=dout_241&dout_202;
   dout_244=dout_241^dout_202;
   dout_245=dout_242|dout_243;
   dout_246=dout_211^dout_222;
   dout_247=dout_211&dout_222;
   dout_248=dout_246&dout_207;
   dout_249=dout_246^dout_207;
   dout_250=dout_247|dout_248;
   dout_251=dout_216^dout_223;
   dout_252=dout_216&dout_223;
   dout_253=dout_251&dout_212;
   dout_254=dout_251^dout_212;
   dout_255=dout_252|dout_253;
   dout_256=dout_182^dout_224;
   dout_257=dout_182&dout_224;
   dout_258=dout_256&dout_217;
   dout_259=dout_256^dout_217;
   dout_260=dout_257|dout_258;
   dout_261=((B >> 0)&1)&((A >> 7)&1);
   dout_262=((B >> 1)&1)&((A >> 7)&1);
   dout_263=((B >> 2)&1)&((A >> 7)&1);
   dout_264=((B >> 3)&1)&((A >> 7)&1);
   dout_265=((B >> 4)&1)&((A >> 7)&1);
   dout_266=((B >> 5)&1)&((A >> 7)&1);
   dout_267=((B >> 6)&1)&((A >> 7)&1);
   dout_268=((B >> 7)&1)&((A >> 7)&1);
   dout_269=dout_234^dout_261;
   dout_270=dout_234&dout_261;
   dout_271=dout_269&dout_230;
   dout_272=dout_269^dout_230;
   dout_273=dout_270|dout_271;
   dout_274=dout_239^dout_262;
   dout_275=dout_239&dout_262;
   dout_276=dout_274&dout_235;
   dout_277=dout_274^dout_235;
   dout_278=dout_275|dout_276;
   dout_279=dout_244^dout_263;
   dout_280=dout_244&dout_263;
   dout_281=dout_279&dout_240;
   dout_282=dout_279^dout_240;
   dout_283=dout_280|dout_281;
   dout_284=dout_249^dout_264;
   dout_285=dout_249&dout_264;
   dout_286=dout_284&dout_245;
   dout_287=dout_284^dout_245;
   dout_288=dout_285|dout_286;
   dout_289=dout_254^dout_265;
   dout_290=dout_254&dout_265;
   dout_291=dout_289&dout_250;
   dout_292=dout_289^dout_250;
   dout_293=dout_290|dout_291;
   dout_294=dout_259^dout_266;
   dout_295=dout_259&dout_266;
   dout_296=dout_294&dout_255;
   dout_297=dout_294^dout_255;
   dout_298=dout_295|dout_296;
   dout_299=dout_225^dout_267;
   dout_300=dout_225&dout_267;
   dout_301=dout_299&dout_260;
   dout_302=dout_299^dout_260;
   dout_303=dout_300|dout_301;
   dout_304=dout_277^dout_273;
   dout_305=dout_277&dout_273;
   dout_306=dout_282^dout_278;
   dout_307=dout_282&dout_278;
   dout_308=dout_306&dout_305;
   dout_309=dout_306^dout_305;
   dout_310=dout_307|dout_308;
   dout_311=dout_287^dout_283;
   dout_312=dout_287&dout_283;
   dout_313=dout_311&dout_310;
   dout_314=dout_311^dout_310;
   dout_315=dout_312|dout_313;
   dout_316=dout_292^dout_288;
   dout_317=dout_292&dout_288;
   dout_318=dout_316&dout_315;
   dout_319=dout_316^dout_315;
   dout_320=dout_317|dout_318;
   dout_321=dout_297^dout_293;
   dout_322=dout_297&dout_293;
   dout_323=dout_321&dout_320;
   dout_324=dout_321^dout_320;
   dout_325=dout_322|dout_323;
   dout_326=dout_302^dout_298;
   dout_327=dout_302&dout_298;
   dout_328=dout_326&dout_325;
   dout_329=dout_326^dout_325;
   dout_330=dout_327|dout_328;
   dout_331=dout_268^dout_303;
   dout_332=((A >> 7)&1)&dout_303;
   dout_333=dout_331&dout_330;
   dout_334=dout_331^dout_330;
   dout_335=dout_332|dout_333;

   O = 0;
   O |= (0&1) << 0;
   O |= (dout_218&1) << 1;
   O |= (dout_132&1) << 2;
   O |= (dout_105&1) << 3;
   O |= (dout_140&1) << 4;
   O |= (dout_186&1) << 5;
   O |= (dout_229&1) << 6;
   O |= (dout_272&1) << 7;
   O |= (dout_304&1) << 8;
   O |= (dout_309&1) << 9;
   O |= (dout_314&1) << 10;
   O |= (dout_319&1) << 11;
   O |= (dout_324&1) << 12;
   O |= (dout_329&1) << 13;
   O |= (dout_334&1) << 14;
   O |= (dout_335&1) << 15;
   return O;
}

uint64_t mult8_cgp14zr_wc7391_rcam(const uint64_t B,const uint64_t A)
{
   uint64_t O, dout_242, dout_246, dout_251, dout_252, dout_253, dout_286, dout_288, dout_289, dout_290, dout_295, dout_296, dout_297, dout_298, dout_323, dout_324, dout_326, dout_327, dout_328, dout_329, dout_330, dout_331, dout_332, dout_333, dout_334, dout_335;   int avg=0;

   dout_242=((A >> 5)&1)&((B >> 7)&1);
   dout_246=dout_242&((A >> 6)&1);
   dout_251=((B >> 5)&1)&((A >> 4)&1);
   dout_252=((B >> 6)&1)&((A >> 6)&1);
   dout_253=((B >> 7)&1)&((A >> 6)&1);
   dout_286=dout_242^dout_253;
   dout_288=((B >> 7)&1)&dout_252;
   dout_289=dout_286^dout_252;
   dout_290=dout_246|dout_288;
   dout_295=((B >> 4)&1)&((A >> 7)&1);
   dout_296=((B >> 5)&1)&((A >> 7)&1);
   dout_297=((B >> 6)&1)&((A >> 7)&1);
   dout_298=((B >> 7)&1)&((A >> 7)&1);
   dout_323=dout_296&((B >> 4)&1);
   dout_324=dout_296^dout_295;
   dout_326=dout_289^dout_297;
   dout_327=dout_289&dout_297;
   dout_328=dout_326&dout_323;
   dout_329=dout_326^dout_323;
   dout_330=dout_327|dout_328;
   dout_331=dout_290^dout_298;
   dout_332=dout_290&dout_298;
   dout_333=((B >> 7)&1)&dout_330;
   dout_334=dout_331^dout_330;
   dout_335=dout_332|dout_333;

   O = 0;
   O |= (0&1) << 0;
   O |= (dout_251&1) << 1;
   O |= (0&1) << 2;
   O |= (0&1) << 3;
   O |= (0&1) << 4;
   O |= (0&1) << 5;
   O |= (dout_332&1) << 6;
   O |= (dout_335&1) << 7;
   O |= (dout_298&1) << 8;
   O |= (0&1) << 9;
   O |= (dout_329&1) << 10;
   O |= (dout_251&1) << 11;
   O |= (dout_324&1) << 12;
   O |= (dout_329&1) << 13;
   O |= (dout_334&1) << 14;
   O |= (dout_335&1) << 15;
   return O;
}

uint32_t mul16u_2KD (uint16_t a, uint16_t b) {
    static uint16_t * cacheLL = NULL;
    static uint16_t * cacheLH = NULL;
    static uint16_t * cacheHL = NULL;
    static uint16_t * cacheHH = NULL;
    int fillData = cacheLL == NULL || cacheLH == NULL || cacheHL == NULL || cacheHH == NULL;

    if(!cacheLL) cacheLL = (uint16_t *)malloc(256 * 256 * sizeof(uint16_t));
    if(!cacheLH) cacheLH = (uint16_t *)malloc(256 * 256 * sizeof(uint16_t));
    if(!cacheHL) cacheHL = (uint16_t *)malloc(256 * 256 * sizeof(uint16_t));
    if(!cacheHH) cacheHH = (uint16_t *)malloc(256 * 256 * sizeof(uint16_t));
    
    if(fillData) {
        for(int i = 0; i < 256; i++) {
            for(int j = 0; j < 256; j++) {
                cacheLL[i * 256 + j] = mult8_cgp14zr_wc7391_rcam(i, j);
                cacheLH[i * 256 + j] = mult8_cgp14ep_ep64716_wc26_csamrca(i, j);
                cacheHL[i * 256 + j] = mult8_cgp14ep_ep64716_wc26_csamrca(i, j);
                cacheHH[i * 256 + j] = mul8_364(i, j);
            }
        }
    }

    uint32_t opt = 0;

    opt += (uint32_t)cacheLL[(a & 0xFF       ) * 256 + (b & 0xFF             )];
    opt += (uint32_t)cacheLH[(a & 0xFF       ) * 256 + ((b >> 8) & 0xFF      )] << 8;
    opt += (uint32_t)cacheHL[((a >> 8) & 0xFF) * 256 + (b & 0xFF             )] << 8;
    opt += (uint32_t)cacheHH[((a >> 8) & 0xFF) * 256 + ((b >> 8) & 0xFF      )] << 16;

    return opt;
}
