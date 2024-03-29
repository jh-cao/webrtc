// Copyright 2016 The Closure Library Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

goog.module('goog.dom.DomCompileTest');
goog.setTestOnly();

const TagName = goog.require('goog.dom.TagName');
const googDom = goog.require('goog.dom');
const testSuite = goog.require('goog.testing.testSuite');

testSuite({
  /** Checks types with TagName. */
  testDomTagNameTypes() {
    /** @type {!HTMLAnchorElement} */
    const a = googDom.createDom(TagName.A);

    /** @type {!HTMLAnchorElement} */
    const el = googDom.createElement(TagName.A);

    /** @type {!IArrayLike<!HTMLAnchorElement>} */
    const anchors = googDom.getElementsByTagNameAndClass(TagName.A);

    // Check that goog.dom.HtmlElement is assignable to HTMLElement.
    /** @type {!HTMLElement} */
    const b = googDom.createElement(TagName.B);

    /** @type {?HTMLAnchorElement} */
    const anchor = googDom.getElementByTagNameAndClass(TagName.A);
  },

  /** Checks types with TagName. */
  testDomHelperTagNameTypes() {
    const dom = googDom.getDomHelper();

    /** @type {!HTMLAnchorElement} */
    const a = dom.createDom(TagName.A);

    /** @type {!HTMLAnchorElement} */
    const el = dom.createElement(TagName.A);

    /** @type {!IArrayLike<!HTMLAnchorElement>} */
    const anchors = dom.getElementsByTagNameAndClass(TagName.A);

    /** @type {?HTMLAnchorElement} */
    const anchor = dom.getElementByTagNameAndClass(TagName.A);
  },
});
