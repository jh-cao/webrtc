// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "third_party/blink/renderer/core/layout/ng/layout_ng_progress.h"

#include "third_party/blink/renderer/core/layout/layout_object.h"

namespace blink {

LayoutNGProgress::LayoutNGProgress(Element* element)
    : LayoutNGBlockFlowMixin<LayoutProgress>(element) {}

LayoutNGProgress::~LayoutNGProgress() = default;

void LayoutNGProgress::UpdateBlockLayout(bool relayout_children) {
  UpdateNGBlockLayout();
}

bool LayoutNGProgress::IsOfType(LayoutObjectType type) const {
  return type == kLayoutObjectNGProgress ||
         LayoutNGMixin<LayoutProgress>::IsOfType(type);
}

}  // namespace blink
