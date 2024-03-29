// Copyright 2010 The Closure Library Authors. All Rights Reserved.
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

goog.module('goog.string.pathTest');
goog.setTestOnly();

const path = goog.require('goog.string.path');
const testSuite = goog.require('goog.testing.testSuite');

// Some test data comes from Python's posixpath tests.
// See http://svn.python.org/view/python/trunk/Lib/test/test_posixpath.py

testSuite({
  testBasename() {
    assertEquals('bar', path.baseName('/foo/bar'));
    assertEquals('', path.baseName('/'));
    assertEquals('foo', path.baseName('foo'));
    assertEquals('foo', path.baseName('////foo'));
    assertEquals('bar', path.baseName('//foo//bar'));
  },

  testDirname() {
    assertEquals('/foo', path.dirname('/foo/bar'));
    assertEquals('/', path.dirname('/'));
    assertEquals('', path.dirname('foo'));
    assertEquals('////', path.dirname('////foo'));
    assertEquals('//foo', path.dirname('//foo//bar'));
  },

  testJoin() {
    assertEquals('/bar/baz', path.join('/foo', 'bar', '/bar', 'baz'));
    assertEquals('/foo/bar/baz', path.join('/foo', 'bar', 'baz'));
    assertEquals('/foo/bar/baz', path.join('/foo/', 'bar', 'baz'));
    assertEquals('/foo/bar/baz/', path.join('/foo/', 'bar/', 'baz/'));
  },

  testNormalizePath() {
    assertEquals('.', path.normalizePath(''));
    assertEquals('.', path.normalizePath('./'));
    assertEquals('/', path.normalizePath('/'));
    assertEquals('//', path.normalizePath('//'));
    assertEquals('/', path.normalizePath('///'));
    assertEquals('/foo/bar', path.normalizePath('///foo/.//bar//'));
    assertEquals(
        '/foo/baz', path.normalizePath('///foo/.//bar//.//..//.//baz'));
    assertEquals('/foo/bar', path.normalizePath('///..//./foo/.//bar'));
    assertEquals('../../cat/dog', path.normalizePath('../../cat/dog/'));
    assertEquals('../dog', path.normalizePath('../cat/../dog/'));
    assertEquals('/cat/dog', path.normalizePath('/../cat/dog/'));
    assertEquals('/dog', path.normalizePath('/../cat/../dog'));
    assertEquals('/dog', path.normalizePath('/../../../dog'));
  },

  testSplit() {
    assertArrayEquals(['/foo', 'bar'], path.split('/foo/bar'));
    assertArrayEquals(['/', ''], path.split('/'));
    assertArrayEquals(['', 'foo'], path.split('foo'));
    assertArrayEquals(['////', 'foo'], path.split('////foo'));
    assertArrayEquals(['//foo', 'bar'], path.split('//foo//bar'));
  },

  testExtension() {
    assertEquals('jpg', path.extension('././foo/bar/baz.jpg'));
    assertEquals('jpg', path.extension('././foo bar/baz.jpg'));
    assertEquals('jpg', path.extension('foo/bar/baz/blah blah.jpg'));
    assertEquals('', path.extension('../../foo/bar/baz baz'));
    assertEquals('', path.extension('../../foo bar/baz baz'));
    assertEquals('', path.extension('foo/bar/.'));
    assertEquals('', path.extension('  '));
    assertEquals('', path.extension(''));
    assertEquals('', path.extension('/home/username/.bashrc'));

    // Tests cases taken from python os.path.splitext().
    assertEquals('bar', path.extension('foo.bar'));
    assertEquals('bar', path.extension('foo.boo.bar'));
    assertEquals('bar', path.extension('foo.boo.biff.bar'));
    assertEquals('rc', path.extension('.csh.rc'));
    assertEquals('', path.extension('nodots'));
    assertEquals('', path.extension('.cshrc'));
    assertEquals('', path.extension('...manydots'));
    assertEquals('ext', path.extension('...manydots.ext'));
    assertEquals('', path.extension('.'));
    assertEquals('', path.extension('..'));
    assertEquals('', path.extension('........'));
    assertEquals('', path.extension(''));
  },
});
