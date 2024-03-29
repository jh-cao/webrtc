// Copyright 2021 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/** @fileoverview Definitions for chrome.settingsPrivate API */
// TODO(crbug.com/1203307): Auto-generate this file.

declare namespace chrome {
  export namespace settingsPrivate {
    export enum PrefType {
      BOOLEAN = 'BOOLEAN',
      NUMBER = 'NUMBER',
      STRING = 'STRING',
      URL = 'URL',
      LIST = 'LIST',
      DICTIONARY = 'DICTIONARY',
    }

    export enum ControlledBy {
      DEVICE_POLICY = 'DEVICE_POLICY',
      USER_POLICY = 'USER_POLICY',
      OWNER = 'OWNER',
      PRIMARY_USER = 'PRIMARY_USER',
      EXTENSION = 'EXTENSION',
      PARENT = 'PARENT',
      CHILD_RESTRICTION = 'CHILD_RESTRICTION',
    }

    export enum Enforcement {
      ENFORCED = 'ENFORCED',
      RECOMMENDED = 'RECOMMENDED',
      PARENT_SUPERVISED = 'PARENT_SUPERVISED',
    }

    export interface PrefObject {
      key: string;
      type: PrefType;
      value: any;
      controlledBy?: ControlledBy;
      controlledByName?: string;
      enforcement?: Enforcement;
      recommendedValue?: any;
      userSelectableValues?: Array<any>;
      userControlDisabled?: boolean;
      extensionId?: string;
      extensionCanBeDisabled?: boolean;
    }

    export function getDefaultZoom(callback: (zoom: number) => void): void;
    export function setDefaultZoom(zoom: number): void;
  }
}
