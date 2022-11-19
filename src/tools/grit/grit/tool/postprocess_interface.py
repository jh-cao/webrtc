# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

''' Base class for postprocessing of RC files.
'''

from __future__ import print_function

class PostProcessor(object):
  ''' Base class for postprocessing of the RC file data before being
  output through the RC2GRD tool. You should implement this class if
  you want GRIT to do specific things to the RC files after it has
  converted the data into GRD format, i.e. change the content of the
  RC file, and put it into a P4 changelist, etc.'''


  def Process(self, rctext, rcpath, grdnode):
    ''' Processes the data in rctext and grdnode.
    Args:
      rctext: string containing the contents of the RC file being processed.
      rcpath: the path used to access the file.
      grdtext: the root node of the grd xml data generated by
      the rc2grd tool.

    Return:
      The root node of the processed GRD tree.
    '''
    raise NotImplementedError()
