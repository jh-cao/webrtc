// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "third_party/blink/renderer/core/layout/ng/layout_ng_text_control_multi_line.h"

#include "third_party/blink/renderer/core/html/forms/text_control_element.h"
#include "third_party/blink/renderer/core/layout/layout_text_control.h"

namespace blink {

LayoutNGTextControlMultiLine::LayoutNGTextControlMultiLine(Element* element)
    : LayoutNGBlockFlow(element) {}

HTMLElement* LayoutNGTextControlMultiLine::InnerEditorElement() const {
  return To<TextControlElement>(GetNode())->InnerEditorElement();
}

bool LayoutNGTextControlMultiLine::IsOfType(LayoutObjectType type) const {
  return type == kLayoutObjectNGTextControlMultiLine ||
         LayoutNGBlockFlow::IsOfType(type);
}

void LayoutNGTextControlMultiLine::StyleDidChange(
    StyleDifference style_diff,
    const ComputedStyle* old_style) {
  LayoutNGBlockFlow::StyleDidChange(style_diff, old_style);
  LayoutTextControl::StyleDidChange(InnerEditorElement(), old_style,
                                    StyleRef());
}

bool LayoutNGTextControlMultiLine::NodeAtPoint(
    HitTestResult& result,
    const HitTestLocation& hit_test_location,
    const PhysicalOffset& accumulated_offset,
    HitTestAction hit_test_action) {
  if (!LayoutNGBlockFlow::NodeAtPoint(result, hit_test_location,
                                      accumulated_offset, hit_test_action))
    return false;

  const LayoutObject* stop_node = result.GetHitTestRequest().GetStopNode();
  if (stop_node && stop_node->NodeForHitTest() == result.InnerNode())
    return true;

  HTMLElement* inner_editor = InnerEditorElement();
  if (result.InnerNode() == GetNode() || result.InnerNode() == inner_editor) {
    LayoutTextControl::HitInnerEditorElement(
        *this, *inner_editor, result, hit_test_location, accumulated_offset);
  }
  return true;
}

}  // namespace blink
