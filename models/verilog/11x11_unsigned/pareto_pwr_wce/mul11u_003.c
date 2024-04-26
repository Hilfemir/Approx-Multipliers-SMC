/***
* This code is a part of EvoApproxLib library (ehw.fit.vutbr.cz/approxlib) distributed under The MIT License.
* When used, please cite the following article(s): V. Mrazek, S. S. Sarwar, L. Sekanina, Z. Vasicek and K. Roy, "Design of power-efficient approximate multipliers for approximate artificial neural networks," 2016 IEEE/ACM International Conference on Computer-Aided Design (ICCAD), Austin, TX, 2016, pp. 1-7. doi: 10.1145/2966986.2967021 
* This file contains a circuit from a sub-set of pareto optimal circuits with respect to the pwr and wce parameters
***/
// MAE% = 0.00 %
// MAE = 0 
// WCE% = 0.00 %
// WCE = 0 
// WCRE% = 0.00 %
// EP% = 0.00 %
// MRE% = 0.00 %
// MSE = 0 
// PDK45_PWR = 0.930 mW
// PDK45_AREA = 1340.8 um2
// PDK45_DELAY = 2.08 ns
#include <stdint.h>
#include <stdlib.h>

uint64_t mul11u_003(uint64_t a, uint64_t b) {
  int wa[11];
  int wb[11];
  uint64_t y = 0;
  wa[0] = (a >> 0) & 0x01;
  wb[0] = (b >> 0) & 0x01;
  wa[1] = (a >> 1) & 0x01;
  wb[1] = (b >> 1) & 0x01;
  wa[2] = (a >> 2) & 0x01;
  wb[2] = (b >> 2) & 0x01;
  wa[3] = (a >> 3) & 0x01;
  wb[3] = (b >> 3) & 0x01;
  wa[4] = (a >> 4) & 0x01;
  wb[4] = (b >> 4) & 0x01;
  wa[5] = (a >> 5) & 0x01;
  wb[5] = (b >> 5) & 0x01;
  wa[6] = (a >> 6) & 0x01;
  wb[6] = (b >> 6) & 0x01;
  wa[7] = (a >> 7) & 0x01;
  wb[7] = (b >> 7) & 0x01;
  wa[8] = (a >> 8) & 0x01;
  wb[8] = (b >> 8) & 0x01;
  wa[9] = (a >> 9) & 0x01;
  wb[9] = (b >> 9) & 0x01;
  wa[10] = (a >> 10) & 0x01;
  wb[10] = (b >> 10) & 0x01;
  int sig_22 = wa[0] & wb[0];
  int sig_23 = wa[1] & wb[0];
  int sig_24 = wa[2] & wb[0];
  int sig_25 = wa[3] & wb[0];
  int sig_26 = wa[4] & wb[0];
  int sig_27 = wa[5] & wb[0];
  int sig_28 = wa[6] & wb[0];
  int sig_29 = wa[7] & wb[0];
  int sig_30 = wa[8] & wb[0];
  int sig_31 = wa[9] & wb[0];
  int sig_32 = wa[10] & wb[0];
  int sig_33 = wa[0] & wb[1];
  int sig_34 = wa[1] & wb[1];
  int sig_35 = wa[2] & wb[1];
  int sig_36 = wa[3] & wb[1];
  int sig_37 = wa[4] & wb[1];
  int sig_38 = wa[5] & wb[1];
  int sig_39 = wa[6] & wb[1];
  int sig_40 = wa[7] & wb[1];
  int sig_41 = wa[8] & wb[1];
  int sig_42 = wa[9] & wb[1];
  int sig_43 = wa[10] & wb[1];
  int sig_44 = sig_23 ^ sig_33;
  int sig_45 = sig_23 & sig_33;
  int sig_46 = sig_24 ^ sig_34;
  int sig_47 = sig_24 & sig_34;
  int sig_48 = sig_25 ^ sig_35;
  int sig_49 = sig_25 & sig_35;
  int sig_50 = sig_26 ^ sig_36;
  int sig_51 = sig_26 & sig_36;
  int sig_52 = sig_27 ^ sig_37;
  int sig_53 = sig_27 & sig_37;
  int sig_54 = sig_28 ^ sig_38;
  int sig_55 = sig_28 & sig_38;
  int sig_56 = sig_29 ^ sig_39;
  int sig_57 = sig_29 & sig_39;
  int sig_58 = sig_30 ^ sig_40;
  int sig_59 = sig_30 & sig_40;
  int sig_60 = sig_31 ^ sig_41;
  int sig_61 = sig_31 & sig_41;
  int sig_62 = sig_32 ^ sig_42;
  int sig_63 = sig_32 & sig_42;
  int sig_64 = wa[0] & wb[2];
  int sig_65 = wa[1] & wb[2];
  int sig_66 = wa[2] & wb[2];
  int sig_67 = wa[3] & wb[2];
  int sig_68 = wa[4] & wb[2];
  int sig_69 = wa[5] & wb[2];
  int sig_70 = wa[6] & wb[2];
  int sig_71 = wa[7] & wb[2];
  int sig_72 = wa[8] & wb[2];
  int sig_73 = wa[9] & wb[2];
  int sig_74 = wa[10] & wb[2];
  int sig_75 = sig_46 ^ sig_64;
  int sig_76 = sig_46 & sig_64;
  int sig_77 = sig_75 & sig_45;
  int sig_78 = sig_75 ^ sig_45;
  int sig_79 = sig_76 | sig_77;
  int sig_80 = sig_48 ^ sig_65;
  int sig_81 = sig_48 & sig_65;
  int sig_82 = sig_80 & sig_47;
  int sig_83 = sig_80 ^ sig_47;
  int sig_84 = sig_81 | sig_82;
  int sig_85 = sig_50 ^ sig_66;
  int sig_86 = sig_50 & sig_66;
  int sig_87 = sig_85 & sig_49;
  int sig_88 = sig_85 ^ sig_49;
  int sig_89 = sig_86 | sig_87;
  int sig_90 = sig_52 ^ sig_67;
  int sig_91 = sig_52 & sig_67;
  int sig_92 = sig_90 & sig_51;
  int sig_93 = sig_90 ^ sig_51;
  int sig_94 = sig_91 | sig_92;
  int sig_95 = sig_54 ^ sig_68;
  int sig_96 = sig_54 & sig_68;
  int sig_97 = sig_95 & sig_53;
  int sig_98 = sig_95 ^ sig_53;
  int sig_99 = sig_96 | sig_97;
  int sig_100 = sig_56 ^ sig_69;
  int sig_101 = sig_56 & sig_69;
  int sig_102 = sig_100 & sig_55;
  int sig_103 = sig_100 ^ sig_55;
  int sig_104 = sig_101 | sig_102;
  int sig_105 = sig_58 ^ sig_70;
  int sig_106 = sig_58 & sig_70;
  int sig_107 = sig_105 & sig_57;
  int sig_108 = sig_105 ^ sig_57;
  int sig_109 = sig_106 | sig_107;
  int sig_110 = sig_60 ^ sig_71;
  int sig_111 = sig_60 & sig_71;
  int sig_112 = sig_110 & sig_59;
  int sig_113 = sig_110 ^ sig_59;
  int sig_114 = sig_111 | sig_112;
  int sig_115 = sig_62 ^ sig_72;
  int sig_116 = sig_62 & sig_72;
  int sig_117 = sig_115 & sig_61;
  int sig_118 = sig_115 ^ sig_61;
  int sig_119 = sig_116 | sig_117;
  int sig_120 = sig_43 ^ sig_73;
  int sig_121 = sig_43 & sig_73;
  int sig_122 = sig_120 & sig_63;
  int sig_123 = sig_120 ^ sig_63;
  int sig_124 = sig_121 | sig_122;
  int sig_125 = wa[0] & wb[3];
  int sig_126 = wa[1] & wb[3];
  int sig_127 = wa[2] & wb[3];
  int sig_128 = wa[3] & wb[3];
  int sig_129 = wa[4] & wb[3];
  int sig_130 = wa[5] & wb[3];
  int sig_131 = wa[6] & wb[3];
  int sig_132 = wa[7] & wb[3];
  int sig_133 = wa[8] & wb[3];
  int sig_134 = wa[9] & wb[3];
  int sig_135 = wa[10] & wb[3];
  int sig_136 = sig_83 ^ sig_125;
  int sig_137 = sig_83 & sig_125;
  int sig_138 = sig_136 & sig_79;
  int sig_139 = sig_136 ^ sig_79;
  int sig_140 = sig_137 | sig_138;
  int sig_141 = sig_88 ^ sig_126;
  int sig_142 = sig_88 & sig_126;
  int sig_143 = sig_141 & sig_84;
  int sig_144 = sig_141 ^ sig_84;
  int sig_145 = sig_142 | sig_143;
  int sig_146 = sig_93 ^ sig_127;
  int sig_147 = sig_93 & sig_127;
  int sig_148 = sig_146 & sig_89;
  int sig_149 = sig_146 ^ sig_89;
  int sig_150 = sig_147 | sig_148;
  int sig_151 = sig_98 ^ sig_128;
  int sig_152 = sig_98 & sig_128;
  int sig_153 = sig_151 & sig_94;
  int sig_154 = sig_151 ^ sig_94;
  int sig_155 = sig_152 | sig_153;
  int sig_156 = sig_103 ^ sig_129;
  int sig_157 = sig_103 & sig_129;
  int sig_158 = sig_156 & sig_99;
  int sig_159 = sig_156 ^ sig_99;
  int sig_160 = sig_157 | sig_158;
  int sig_161 = sig_108 ^ sig_130;
  int sig_162 = sig_108 & sig_130;
  int sig_163 = sig_161 & sig_104;
  int sig_164 = sig_161 ^ sig_104;
  int sig_165 = sig_162 | sig_163;
  int sig_166 = sig_113 ^ sig_131;
  int sig_167 = sig_113 & sig_131;
  int sig_168 = sig_166 & sig_109;
  int sig_169 = sig_166 ^ sig_109;
  int sig_170 = sig_167 | sig_168;
  int sig_171 = sig_118 ^ sig_132;
  int sig_172 = sig_118 & sig_132;
  int sig_173 = sig_171 & sig_114;
  int sig_174 = sig_171 ^ sig_114;
  int sig_175 = sig_172 | sig_173;
  int sig_176 = sig_123 ^ sig_133;
  int sig_177 = sig_123 & sig_133;
  int sig_178 = sig_176 & sig_119;
  int sig_179 = sig_176 ^ sig_119;
  int sig_180 = sig_177 | sig_178;
  int sig_181 = sig_74 ^ sig_134;
  int sig_182 = sig_74 & sig_134;
  int sig_183 = sig_181 & sig_124;
  int sig_184 = sig_181 ^ sig_124;
  int sig_185 = sig_182 | sig_183;
  int sig_186 = wa[0] & wb[4];
  int sig_187 = wa[1] & wb[4];
  int sig_188 = wa[2] & wb[4];
  int sig_189 = wa[3] & wb[4];
  int sig_190 = wa[4] & wb[4];
  int sig_191 = wa[5] & wb[4];
  int sig_192 = wa[6] & wb[4];
  int sig_193 = wa[7] & wb[4];
  int sig_194 = wa[8] & wb[4];
  int sig_195 = wa[9] & wb[4];
  int sig_196 = wa[10] & wb[4];
  int sig_197 = sig_144 ^ sig_186;
  int sig_198 = sig_144 & sig_186;
  int sig_199 = sig_197 & sig_140;
  int sig_200 = sig_197 ^ sig_140;
  int sig_201 = sig_198 | sig_199;
  int sig_202 = sig_149 ^ sig_187;
  int sig_203 = sig_149 & sig_187;
  int sig_204 = sig_202 & sig_145;
  int sig_205 = sig_202 ^ sig_145;
  int sig_206 = sig_203 | sig_204;
  int sig_207 = sig_154 ^ sig_188;
  int sig_208 = sig_154 & sig_188;
  int sig_209 = sig_207 & sig_150;
  int sig_210 = sig_207 ^ sig_150;
  int sig_211 = sig_208 | sig_209;
  int sig_212 = sig_159 ^ sig_189;
  int sig_213 = sig_159 & sig_189;
  int sig_214 = sig_212 & sig_155;
  int sig_215 = sig_212 ^ sig_155;
  int sig_216 = sig_213 | sig_214;
  int sig_217 = sig_164 ^ sig_190;
  int sig_218 = sig_164 & sig_190;
  int sig_219 = sig_217 & sig_160;
  int sig_220 = sig_217 ^ sig_160;
  int sig_221 = sig_218 | sig_219;
  int sig_222 = sig_169 ^ sig_191;
  int sig_223 = sig_169 & sig_191;
  int sig_224 = sig_222 & sig_165;
  int sig_225 = sig_222 ^ sig_165;
  int sig_226 = sig_223 | sig_224;
  int sig_227 = sig_174 ^ sig_192;
  int sig_228 = sig_174 & sig_192;
  int sig_229 = sig_227 & sig_170;
  int sig_230 = sig_227 ^ sig_170;
  int sig_231 = sig_228 | sig_229;
  int sig_232 = sig_179 ^ sig_193;
  int sig_233 = sig_179 & sig_193;
  int sig_234 = sig_232 & sig_175;
  int sig_235 = sig_232 ^ sig_175;
  int sig_236 = sig_233 | sig_234;
  int sig_237 = sig_184 ^ sig_194;
  int sig_238 = sig_184 & sig_194;
  int sig_239 = sig_237 & sig_180;
  int sig_240 = sig_237 ^ sig_180;
  int sig_241 = sig_238 | sig_239;
  int sig_242 = sig_135 ^ sig_195;
  int sig_243 = sig_135 & sig_195;
  int sig_244 = sig_242 & sig_185;
  int sig_245 = sig_242 ^ sig_185;
  int sig_246 = sig_243 | sig_244;
  int sig_247 = wa[0] & wb[5];
  int sig_248 = wa[1] & wb[5];
  int sig_249 = wa[2] & wb[5];
  int sig_250 = wa[3] & wb[5];
  int sig_251 = wa[4] & wb[5];
  int sig_252 = wa[5] & wb[5];
  int sig_253 = wa[6] & wb[5];
  int sig_254 = wa[7] & wb[5];
  int sig_255 = wa[8] & wb[5];
  int sig_256 = wa[9] & wb[5];
  int sig_257 = wa[10] & wb[5];
  int sig_258 = sig_205 ^ sig_247;
  int sig_259 = sig_205 & sig_247;
  int sig_260 = sig_258 & sig_201;
  int sig_261 = sig_258 ^ sig_201;
  int sig_262 = sig_259 | sig_260;
  int sig_263 = sig_210 ^ sig_248;
  int sig_264 = sig_210 & sig_248;
  int sig_265 = sig_263 & sig_206;
  int sig_266 = sig_263 ^ sig_206;
  int sig_267 = sig_264 | sig_265;
  int sig_268 = sig_215 ^ sig_249;
  int sig_269 = sig_215 & sig_249;
  int sig_270 = sig_268 & sig_211;
  int sig_271 = sig_268 ^ sig_211;
  int sig_272 = sig_269 | sig_270;
  int sig_273 = sig_220 ^ sig_250;
  int sig_274 = sig_220 & sig_250;
  int sig_275 = sig_273 & sig_216;
  int sig_276 = sig_273 ^ sig_216;
  int sig_277 = sig_274 | sig_275;
  int sig_278 = sig_225 ^ sig_251;
  int sig_279 = sig_225 & sig_251;
  int sig_280 = sig_278 & sig_221;
  int sig_281 = sig_278 ^ sig_221;
  int sig_282 = sig_279 | sig_280;
  int sig_283 = sig_230 ^ sig_252;
  int sig_284 = sig_230 & sig_252;
  int sig_285 = sig_283 & sig_226;
  int sig_286 = sig_283 ^ sig_226;
  int sig_287 = sig_284 | sig_285;
  int sig_288 = sig_235 ^ sig_253;
  int sig_289 = sig_235 & sig_253;
  int sig_290 = sig_288 & sig_231;
  int sig_291 = sig_288 ^ sig_231;
  int sig_292 = sig_289 | sig_290;
  int sig_293 = sig_240 ^ sig_254;
  int sig_294 = sig_240 & sig_254;
  int sig_295 = sig_293 & sig_236;
  int sig_296 = sig_293 ^ sig_236;
  int sig_297 = sig_294 | sig_295;
  int sig_298 = sig_245 ^ sig_255;
  int sig_299 = sig_245 & sig_255;
  int sig_300 = sig_298 & sig_241;
  int sig_301 = sig_298 ^ sig_241;
  int sig_302 = sig_299 | sig_300;
  int sig_303 = sig_196 ^ sig_256;
  int sig_304 = sig_196 & sig_256;
  int sig_305 = sig_303 & sig_246;
  int sig_306 = sig_303 ^ sig_246;
  int sig_307 = sig_304 | sig_305;
  int sig_308 = wa[0] & wb[6];
  int sig_309 = wa[1] & wb[6];
  int sig_310 = wa[2] & wb[6];
  int sig_311 = wa[3] & wb[6];
  int sig_312 = wa[4] & wb[6];
  int sig_313 = wa[5] & wb[6];
  int sig_314 = wa[6] & wb[6];
  int sig_315 = wa[7] & wb[6];
  int sig_316 = wa[8] & wb[6];
  int sig_317 = wa[9] & wb[6];
  int sig_318 = wa[10] & wb[6];
  int sig_319 = sig_266 ^ sig_308;
  int sig_320 = sig_266 & sig_308;
  int sig_321 = sig_319 & sig_262;
  int sig_322 = sig_319 ^ sig_262;
  int sig_323 = sig_320 | sig_321;
  int sig_324 = sig_271 ^ sig_309;
  int sig_325 = sig_271 & sig_309;
  int sig_326 = sig_324 & sig_267;
  int sig_327 = sig_324 ^ sig_267;
  int sig_328 = sig_325 | sig_326;
  int sig_329 = sig_276 ^ sig_310;
  int sig_330 = sig_276 & sig_310;
  int sig_331 = sig_329 & sig_272;
  int sig_332 = sig_329 ^ sig_272;
  int sig_333 = sig_330 | sig_331;
  int sig_334 = sig_281 ^ sig_311;
  int sig_335 = sig_281 & sig_311;
  int sig_336 = sig_334 & sig_277;
  int sig_337 = sig_334 ^ sig_277;
  int sig_338 = sig_335 | sig_336;
  int sig_339 = sig_286 ^ sig_312;
  int sig_340 = sig_286 & sig_312;
  int sig_341 = sig_339 & sig_282;
  int sig_342 = sig_339 ^ sig_282;
  int sig_343 = sig_340 | sig_341;
  int sig_344 = sig_291 ^ sig_313;
  int sig_345 = sig_291 & sig_313;
  int sig_346 = sig_344 & sig_287;
  int sig_347 = sig_344 ^ sig_287;
  int sig_348 = sig_345 | sig_346;
  int sig_349 = sig_296 ^ sig_314;
  int sig_350 = sig_296 & sig_314;
  int sig_351 = sig_349 & sig_292;
  int sig_352 = sig_349 ^ sig_292;
  int sig_353 = sig_350 | sig_351;
  int sig_354 = sig_301 ^ sig_315;
  int sig_355 = sig_301 & sig_315;
  int sig_356 = sig_354 & sig_297;
  int sig_357 = sig_354 ^ sig_297;
  int sig_358 = sig_355 | sig_356;
  int sig_359 = sig_306 ^ sig_316;
  int sig_360 = sig_306 & sig_316;
  int sig_361 = sig_359 & sig_302;
  int sig_362 = sig_359 ^ sig_302;
  int sig_363 = sig_360 | sig_361;
  int sig_364 = sig_257 ^ sig_317;
  int sig_365 = sig_257 & sig_317;
  int sig_366 = sig_364 & sig_307;
  int sig_367 = sig_364 ^ sig_307;
  int sig_368 = sig_365 | sig_366;
  int sig_369 = wa[0] & wb[7];
  int sig_370 = wa[1] & wb[7];
  int sig_371 = wa[2] & wb[7];
  int sig_372 = wa[3] & wb[7];
  int sig_373 = wa[4] & wb[7];
  int sig_374 = wa[5] & wb[7];
  int sig_375 = wa[6] & wb[7];
  int sig_376 = wa[7] & wb[7];
  int sig_377 = wa[8] & wb[7];
  int sig_378 = wa[9] & wb[7];
  int sig_379 = wa[10] & wb[7];
  int sig_380 = sig_327 ^ sig_369;
  int sig_381 = sig_327 & sig_369;
  int sig_382 = sig_380 & sig_323;
  int sig_383 = sig_380 ^ sig_323;
  int sig_384 = sig_381 | sig_382;
  int sig_385 = sig_332 ^ sig_370;
  int sig_386 = sig_332 & sig_370;
  int sig_387 = sig_385 & sig_328;
  int sig_388 = sig_385 ^ sig_328;
  int sig_389 = sig_386 | sig_387;
  int sig_390 = sig_337 ^ sig_371;
  int sig_391 = sig_337 & sig_371;
  int sig_392 = sig_390 & sig_333;
  int sig_393 = sig_390 ^ sig_333;
  int sig_394 = sig_391 | sig_392;
  int sig_395 = sig_342 ^ sig_372;
  int sig_396 = sig_342 & sig_372;
  int sig_397 = sig_395 & sig_338;
  int sig_398 = sig_395 ^ sig_338;
  int sig_399 = sig_396 | sig_397;
  int sig_400 = sig_347 ^ sig_373;
  int sig_401 = sig_347 & sig_373;
  int sig_402 = sig_400 & sig_343;
  int sig_403 = sig_400 ^ sig_343;
  int sig_404 = sig_401 | sig_402;
  int sig_405 = sig_352 ^ sig_374;
  int sig_406 = sig_352 & sig_374;
  int sig_407 = sig_405 & sig_348;
  int sig_408 = sig_405 ^ sig_348;
  int sig_409 = sig_406 | sig_407;
  int sig_410 = sig_357 ^ sig_375;
  int sig_411 = sig_357 & sig_375;
  int sig_412 = sig_410 & sig_353;
  int sig_413 = sig_410 ^ sig_353;
  int sig_414 = sig_411 | sig_412;
  int sig_415 = sig_362 ^ sig_376;
  int sig_416 = sig_362 & sig_376;
  int sig_417 = sig_415 & sig_358;
  int sig_418 = sig_415 ^ sig_358;
  int sig_419 = sig_416 | sig_417;
  int sig_420 = sig_367 ^ sig_377;
  int sig_421 = sig_367 & sig_377;
  int sig_422 = sig_420 & sig_363;
  int sig_423 = sig_420 ^ sig_363;
  int sig_424 = sig_421 | sig_422;
  int sig_425 = sig_318 ^ sig_378;
  int sig_426 = sig_318 & sig_378;
  int sig_427 = sig_425 & sig_368;
  int sig_428 = sig_425 ^ sig_368;
  int sig_429 = sig_426 | sig_427;
  int sig_430 = wa[0] & wb[8];
  int sig_431 = wa[1] & wb[8];
  int sig_432 = wa[2] & wb[8];
  int sig_433 = wa[3] & wb[8];
  int sig_434 = wa[4] & wb[8];
  int sig_435 = wa[5] & wb[8];
  int sig_436 = wa[6] & wb[8];
  int sig_437 = wa[7] & wb[8];
  int sig_438 = wa[8] & wb[8];
  int sig_439 = wa[9] & wb[8];
  int sig_440 = wa[10] & wb[8];
  int sig_441 = sig_388 ^ sig_430;
  int sig_442 = sig_388 & sig_430;
  int sig_443 = sig_441 & sig_384;
  int sig_444 = sig_441 ^ sig_384;
  int sig_445 = sig_442 | sig_443;
  int sig_446 = sig_393 ^ sig_431;
  int sig_447 = sig_393 & sig_431;
  int sig_448 = sig_446 & sig_389;
  int sig_449 = sig_446 ^ sig_389;
  int sig_450 = sig_447 | sig_448;
  int sig_451 = sig_398 ^ sig_432;
  int sig_452 = sig_398 & sig_432;
  int sig_453 = sig_451 & sig_394;
  int sig_454 = sig_451 ^ sig_394;
  int sig_455 = sig_452 | sig_453;
  int sig_456 = sig_403 ^ sig_433;
  int sig_457 = sig_403 & sig_433;
  int sig_458 = sig_456 & sig_399;
  int sig_459 = sig_456 ^ sig_399;
  int sig_460 = sig_457 | sig_458;
  int sig_461 = sig_408 ^ sig_434;
  int sig_462 = sig_408 & sig_434;
  int sig_463 = sig_461 & sig_404;
  int sig_464 = sig_461 ^ sig_404;
  int sig_465 = sig_462 | sig_463;
  int sig_466 = sig_413 ^ sig_435;
  int sig_467 = sig_413 & sig_435;
  int sig_468 = sig_466 & sig_409;
  int sig_469 = sig_466 ^ sig_409;
  int sig_470 = sig_467 | sig_468;
  int sig_471 = sig_418 ^ sig_436;
  int sig_472 = sig_418 & sig_436;
  int sig_473 = sig_471 & sig_414;
  int sig_474 = sig_471 ^ sig_414;
  int sig_475 = sig_472 | sig_473;
  int sig_476 = sig_423 ^ sig_437;
  int sig_477 = sig_423 & sig_437;
  int sig_478 = sig_476 & sig_419;
  int sig_479 = sig_476 ^ sig_419;
  int sig_480 = sig_477 | sig_478;
  int sig_481 = sig_428 ^ sig_438;
  int sig_482 = sig_428 & sig_438;
  int sig_483 = sig_481 & sig_424;
  int sig_484 = sig_481 ^ sig_424;
  int sig_485 = sig_482 | sig_483;
  int sig_486 = sig_379 ^ sig_439;
  int sig_487 = sig_379 & sig_439;
  int sig_488 = sig_486 & sig_429;
  int sig_489 = sig_486 ^ sig_429;
  int sig_490 = sig_487 | sig_488;
  int sig_491 = wa[0] & wb[9];
  int sig_492 = wa[1] & wb[9];
  int sig_493 = wa[2] & wb[9];
  int sig_494 = wa[3] & wb[9];
  int sig_495 = wa[4] & wb[9];
  int sig_496 = wa[5] & wb[9];
  int sig_497 = wa[6] & wb[9];
  int sig_498 = wa[7] & wb[9];
  int sig_499 = wa[8] & wb[9];
  int sig_500 = wa[9] & wb[9];
  int sig_501 = wa[10] & wb[9];
  int sig_502 = sig_449 ^ sig_491;
  int sig_503 = sig_449 & sig_491;
  int sig_504 = sig_502 & sig_445;
  int sig_505 = sig_502 ^ sig_445;
  int sig_506 = sig_503 | sig_504;
  int sig_507 = sig_454 ^ sig_492;
  int sig_508 = sig_454 & sig_492;
  int sig_509 = sig_507 & sig_450;
  int sig_510 = sig_507 ^ sig_450;
  int sig_511 = sig_508 | sig_509;
  int sig_512 = sig_459 ^ sig_493;
  int sig_513 = sig_459 & sig_493;
  int sig_514 = sig_512 & sig_455;
  int sig_515 = sig_512 ^ sig_455;
  int sig_516 = sig_513 | sig_514;
  int sig_517 = sig_464 ^ sig_494;
  int sig_518 = sig_464 & sig_494;
  int sig_519 = sig_517 & sig_460;
  int sig_520 = sig_517 ^ sig_460;
  int sig_521 = sig_518 | sig_519;
  int sig_522 = sig_469 ^ sig_495;
  int sig_523 = sig_469 & sig_495;
  int sig_524 = sig_522 & sig_465;
  int sig_525 = sig_522 ^ sig_465;
  int sig_526 = sig_523 | sig_524;
  int sig_527 = sig_474 ^ sig_496;
  int sig_528 = sig_474 & sig_496;
  int sig_529 = sig_527 & sig_470;
  int sig_530 = sig_527 ^ sig_470;
  int sig_531 = sig_528 | sig_529;
  int sig_532 = sig_479 ^ sig_497;
  int sig_533 = sig_479 & sig_497;
  int sig_534 = sig_532 & sig_475;
  int sig_535 = sig_532 ^ sig_475;
  int sig_536 = sig_533 | sig_534;
  int sig_537 = sig_484 ^ sig_498;
  int sig_538 = sig_484 & sig_498;
  int sig_539 = sig_537 & sig_480;
  int sig_540 = sig_537 ^ sig_480;
  int sig_541 = sig_538 | sig_539;
  int sig_542 = sig_489 ^ sig_499;
  int sig_543 = sig_489 & sig_499;
  int sig_544 = sig_542 & sig_485;
  int sig_545 = sig_542 ^ sig_485;
  int sig_546 = sig_543 | sig_544;
  int sig_547 = sig_440 ^ sig_500;
  int sig_548 = sig_440 & sig_500;
  int sig_549 = sig_547 & sig_490;
  int sig_550 = sig_547 ^ sig_490;
  int sig_551 = sig_548 | sig_549;
  int sig_552 = wa[0] & wb[10];
  int sig_553 = wa[1] & wb[10];
  int sig_554 = wa[2] & wb[10];
  int sig_555 = wa[3] & wb[10];
  int sig_556 = wa[4] & wb[10];
  int sig_557 = wa[5] & wb[10];
  int sig_558 = wa[6] & wb[10];
  int sig_559 = wa[7] & wb[10];
  int sig_560 = wa[8] & wb[10];
  int sig_561 = wa[9] & wb[10];
  int sig_562 = wa[10] & wb[10];
  int sig_563 = sig_510 ^ sig_552;
  int sig_564 = sig_510 & sig_552;
  int sig_565 = sig_563 & sig_506;
  int sig_566 = sig_563 ^ sig_506;
  int sig_567 = sig_564 | sig_565;
  int sig_568 = sig_515 ^ sig_553;
  int sig_569 = sig_515 & sig_553;
  int sig_570 = sig_568 & sig_511;
  int sig_571 = sig_568 ^ sig_511;
  int sig_572 = sig_569 | sig_570;
  int sig_573 = sig_520 ^ sig_554;
  int sig_574 = sig_520 & sig_554;
  int sig_575 = sig_573 & sig_516;
  int sig_576 = sig_573 ^ sig_516;
  int sig_577 = sig_574 | sig_575;
  int sig_578 = sig_525 ^ sig_555;
  int sig_579 = sig_525 & sig_555;
  int sig_580 = sig_578 & sig_521;
  int sig_581 = sig_578 ^ sig_521;
  int sig_582 = sig_579 | sig_580;
  int sig_583 = sig_530 ^ sig_556;
  int sig_584 = sig_530 & sig_556;
  int sig_585 = sig_583 & sig_526;
  int sig_586 = sig_583 ^ sig_526;
  int sig_587 = sig_584 | sig_585;
  int sig_588 = sig_535 ^ sig_557;
  int sig_589 = sig_535 & sig_557;
  int sig_590 = sig_588 & sig_531;
  int sig_591 = sig_588 ^ sig_531;
  int sig_592 = sig_589 | sig_590;
  int sig_593 = sig_540 ^ sig_558;
  int sig_594 = sig_540 & sig_558;
  int sig_595 = sig_593 & sig_536;
  int sig_596 = sig_593 ^ sig_536;
  int sig_597 = sig_594 | sig_595;
  int sig_598 = sig_545 ^ sig_559;
  int sig_599 = sig_545 & sig_559;
  int sig_600 = sig_598 & sig_541;
  int sig_601 = sig_598 ^ sig_541;
  int sig_602 = sig_599 | sig_600;
  int sig_603 = sig_550 ^ sig_560;
  int sig_604 = sig_550 & sig_560;
  int sig_605 = sig_603 & sig_546;
  int sig_606 = sig_603 ^ sig_546;
  int sig_607 = sig_604 | sig_605;
  int sig_608 = sig_501 ^ sig_561;
  int sig_609 = sig_501 & sig_561;
  int sig_610 = sig_608 & sig_551;
  int sig_611 = sig_608 ^ sig_551;
  int sig_612 = sig_609 | sig_610;
  int sig_613 = sig_571 ^ sig_567;
  int sig_614 = sig_571 & sig_567;
  int sig_615 = sig_576 ^ sig_572;
  int sig_616 = sig_576 & sig_572;
  int sig_617 = sig_615 & sig_614;
  int sig_618 = sig_615 ^ sig_614;
  int sig_619 = sig_616 | sig_617;
  int sig_620 = sig_581 ^ sig_577;
  int sig_621 = sig_581 & sig_577;
  int sig_622 = sig_620 & sig_619;
  int sig_623 = sig_620 ^ sig_619;
  int sig_624 = sig_621 | sig_622;
  int sig_625 = sig_586 ^ sig_582;
  int sig_626 = sig_586 & sig_582;
  int sig_627 = sig_625 & sig_624;
  int sig_628 = sig_625 ^ sig_624;
  int sig_629 = sig_626 | sig_627;
  int sig_630 = sig_591 ^ sig_587;
  int sig_631 = sig_591 & sig_587;
  int sig_632 = sig_630 & sig_629;
  int sig_633 = sig_630 ^ sig_629;
  int sig_634 = sig_631 | sig_632;
  int sig_635 = sig_596 ^ sig_592;
  int sig_636 = sig_596 & sig_592;
  int sig_637 = sig_635 & sig_634;
  int sig_638 = sig_635 ^ sig_634;
  int sig_639 = sig_636 | sig_637;
  int sig_640 = sig_601 ^ sig_597;
  int sig_641 = sig_601 & sig_597;
  int sig_642 = sig_640 & sig_639;
  int sig_643 = sig_640 ^ sig_639;
  int sig_644 = sig_641 | sig_642;
  int sig_645 = sig_606 ^ sig_602;
  int sig_646 = sig_606 & sig_602;
  int sig_647 = sig_645 & sig_644;
  int sig_648 = sig_645 ^ sig_644;
  int sig_649 = sig_646 | sig_647;
  int sig_650 = sig_611 ^ sig_607;
  int sig_651 = sig_611 & sig_607;
  int sig_652 = sig_650 & sig_649;
  int sig_653 = sig_650 ^ sig_649;
  int sig_654 = sig_651 | sig_652;
  int sig_655 = sig_562 ^ sig_612;
  int sig_656 = sig_562 & sig_612;
  int sig_657 = sig_655 & sig_654;
  int sig_658 = sig_655 ^ sig_654;
  int sig_659 = sig_656 | sig_657;
  y |=  (sig_22 & 0x01) << 0; // default output
  y |=  (sig_44 & 0x01) << 1; // default output
  y |=  (sig_78 & 0x01) << 2; // default output
  y |=  (sig_139 & 0x01) << 3; // default output
  y |=  (sig_200 & 0x01) << 4; // default output
  y |=  (sig_261 & 0x01) << 5; // default output
  y |=  (sig_322 & 0x01) << 6; // default output
  y |=  (sig_383 & 0x01) << 7; // default output
  y |=  (sig_444 & 0x01) << 8; // default output
  y |=  (sig_505 & 0x01) << 9; // default output
  y |=  (sig_566 & 0x01) << 10; // default output
  y |=  (sig_613 & 0x01) << 11; // default output
  y |=  (sig_618 & 0x01) << 12; // default output
  y |=  (sig_623 & 0x01) << 13; // default output
  y |=  (sig_628 & 0x01) << 14; // default output
  y |=  (sig_633 & 0x01) << 15; // default output
  y |=  (sig_638 & 0x01) << 16; // default output
  y |=  (sig_643 & 0x01) << 17; // default output
  y |=  (sig_648 & 0x01) << 18; // default output
  y |=  (sig_653 & 0x01) << 19; // default output
  y |=  (sig_658 & 0x01) << 20; // default output
  y |=  (sig_659 & 0x01) << 21; // default output
   return y;
}
