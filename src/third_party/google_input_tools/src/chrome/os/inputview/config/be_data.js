// Copyright 2014 The ChromeOS IME Authors. All Rights Reserved.
// limitations under the License.
// See the License for the specific language governing permissions and
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// distributed under the License is distributed on an "AS-IS" BASIS,
// Unless required by applicable law or agreed to in writing, software
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// You may obtain a copy of the License at
// you may not use this file except in compliance with the License.
// Licensed under the Apache License, Version 2.0 (the "License");
//
goog.require('i18n.input.chrome.inputview.content.ContextlayoutUtil');
goog.require('i18n.input.chrome.inputview.content.compact.letter');
goog.require('i18n.input.chrome.inputview.content.compact.more');
goog.require('i18n.input.chrome.inputview.content.compact.numberpad');
goog.require('i18n.input.chrome.inputview.content.compact.symbol');
goog.require('i18n.input.chrome.inputview.content.compact.util');
goog.require('i18n.input.chrome.inputview.content.util');
goog.require('i18n.input.chrome.message.ContextType');

(function() {
  var ContextType = i18n.input.chrome.message.ContextType;
  var viewIdPrefix_ = '102kbd-k-';

  var keyCharacters = [
    ['\u00b2', '\u00b3', '\u00ac', '\u00ac'], // TLDE
    ['\u0026', '\u0031', '\u007c', '\u00a1'], // AE01
    ['\u00e9', '\u0032', '\u0040', '\u215b'], // AE02
    ['\u0022', '\u0033', '\u0023', '\u00a3'], // AE03
    ['\u0027', '\u0034', '\u00bc', '\u0024'], // AE04
    ['\u0028', '\u0035', '\u00bd', '\u215c'], // AE05
    ['\u00a7', '\u0036', '\u005e', '\u215d'], // AE06
    ['\u00e8', '\u0037', '\u007b', '\u215e'], // AE07
    ['\u0021', '\u0038', '\u005b', '\u2122'], // AE08
    ['\u00e7', '\u0039', '\u007b', '\u00b1'], // AE09
    ['\u00e0', '\u0030', '\u007d', '\u00b0'], // AE10
    ['\u0029', '\u00b0', '\u005c', '\u00bf'], // AE11
    ['\u002d', '\u005f', '\u0327', '\u0328'], // AE12
    ['\u0061', '\u0041', '\u0040', '\u03a9'], // AD01
    ['\u007a', '\u005a', '\u0142', '\u0141'], // AD02
    ['\u0065', '\u0045', '\u20ac', '\u00a2'], // AD03
    ['\u0072', '\u0052', '\u00b6', '\u00ae'], // AD04
    ['\u0074', '\u0054', '\u0167', '\u0166'], // AD05
    ['\u0079', '\u0059', '\u2190', '\u00a5'], // AD06
    ['\u0075', '\u0055', '\u2193', '\u2191'], // AD07
    ['\u0069', '\u0049', '\u2192', '\u0131'], // AD08
    ['\u006f', '\u004f', '\u0153', '\u0152'], // AD09
    ['\u0070', '\u0050', '\u00fe', '\u00de'], // AD10
    ['\u0302', '\u0308', '\u005b', '\u030a'], // AD11
    ['\u0024', '\u002a', '\u005d', '\u0304'], // AD12
    ['\u0071', '\u0051', '\u00e6', '\u00c6'], // AC01
    ['\u0073', '\u0053', '\u00df', '\u00a7'], // AC02
    ['\u0064', '\u0044', '\u00f0', '\u00d0'], // AC03
    ['\u0066', '\u0046', '\u0111', '\u00aa'], // AC04
    ['\u0067', '\u0047', '\u014b', '\u014a'], // AC05
    ['\u0068', '\u0048', '\u0127', '\u0126'], // AC06
    ['\u006a', '\u004a', '\u0309', '\u031b'], // AC07
    ['\u006b', '\u004b', '\u0138', '\u0026'], // AC08
    ['\u006c', '\u004c', '\u0142', '\u0141'], // AC09
    ['\u006d', '\u004d', '\u0301', '\u030b'], // AC10
    ['\u00f9', '\u0025', '\u0301', '\u030c'], // AC11
    ['\u00b5', '\u00a3', '\u0300', '\u0306'], // BKSL
    ['\u003c', '\u003e', '\u005c', '\u005c'], // LSGT
    ['\u0077', '\u0057', '\u00ab', '\u003c'], // AB01
    ['\u0078', '\u0058', '\u00bb', '\u003e'], // AB02
    ['\u0063', '\u0043', '\u00a2', '\u00a9'], // AB03
    ['\u0076', '\u0056', '\u201c', '\u2018'], // AB04
    ['\u0062', '\u0042', '\u201d', '\u2019'], // AB05
    ['\u006e', '\u004e'], // AB06
    ['\u002c', '\u003f', '\u0327', '\u00ba'], // AB07
    ['\u003b', '\u002e', '\u0000', '\u00d7'], // AB08
    ['\u003a', '\u002f', '\u00b7', '\u00f7'], // AB09
    ['\u003d', '\u002b', '\u0303', '\u0307'], // AB10
    ['\u0020', '\u0020'] // SPCE
  ];

  var keyCodes = [
    0xDE, // TLDE
    0x31, // AE01
    0x32, // AE02
    0x33, // AE03
    0x34, // AE04
    0x35, // AE05
    0x36, // AE06
    0x37, // AE07
    0x38, // AE08
    0x39, // AE09
    0x30, // AE10
    0xDB, // AE11
    0xBD, // AE12
    0x41, // AD01
    0x5A, // AD02
    0x45, // AD03
    0x52, // AD04
    0x54, // AD05
    0x59, // AD06
    0x55, // AD07
    0x49, // AD08
    0x4F, // AD09
    0x50, // AD10
    0xDD, // AD11
    0xBA, // AD12
    0x51, // AC01
    0x53, // AC02
    0x44, // AC03
    0x46, // AC04
    0x47, // AC05
    0x48, // AC06
    0x4A, // AC07
    0x4B, // AC08
    0x4C, // AC09
    0x4D, // AC10
    0xC0, // AC11
    0xDC, // BKSL
    0xE2, // LTGT
    0x57, // AB01
    0x58, // AB02
    0x43, // AB03
    0x56, // AB04
    0x42, // AB05
    0x4E, // AB06
    0xBC, // AB07
    0xBE, // AB08
    0xBF, // AB09
    0xBB, // AB10
    0x20  // SPCE
  ];

  var data = i18n.input.chrome.inputview.content.util.createData(
      keyCharacters, viewIdPrefix_, true, true, keyCodes);
  data['id'] = 'be';
  google.ime.chrome.inputview.onConfigLoaded(data);

}) ();
