# Implementation Plan - Lead Scoring Configuration UI

Implement a high-density, professional "Lead Scoring Configuration" modal for the CRM, triggered by the settings icon.

## Proposed Changes

### [CRM_Lead_v2 - Copy.html](file:///d:/AIDesign/lixi/stuff2/CRM/CRM_Lead_v2%20-%20Copy.html)

#### [MODIFY] Structure
- Add a new modal `leadScoringModal` at the end of the `<body>`.
- Implement a 3-column layout inside the modal:
    - **Cột trái (Sidebar)**: Navigation tabs for rule categories (Firmographics, Behavioral, Negative).
    - **Khu vực trung tâm (Main Canvas)**: Rule builder with dynamic rows (Property, Operator, Value, Points).
    - **Cột phải (Summary/Preview)**: Thresholds configuration table with color-coded labels.

#### [MODIFY] Header
- Title: "Quy tắc tính điểm Lead - Sales Team Miền Bắc".
- Status toggle: A modern toggle switch for [Bật / Tắt].
- Action buttons: [Lưu cấu hình] (Primary Blue), [Huỷ] (Secondary).

#### [NEW] Logic (Plain JS)
- Functions to open/close the modal.
- Tab switching logic for the rule builder categories.
- Helper functions to add and remove rule rows dynamically using `<template>` tags.
- Update the settings icon to call `openLeadScoringModal()`.

## Verification Plan

### Automated Tests
- None planned as this is a UI-only implementation in a static HTML file.

### Manual Verification
1. Open `CRM_Lead_v2 - Copy.html` in the browser.
2. Click the **Settings icon** in the primary sidebar.
3. Verify the **Lead Scoring Configuration Modal** appears with the correct 3-column layout.
4. Test **Tab Switching**: Ensure clicking sidebar items updates the Main Canvas content.
5. Test **Rule Builder**: Click "+ Thêm điều kiện" to add a new row, and click "X" to remove a row.
6. Verify **Thresholds Sidebar**: Check if it correctly displays the 4 ranges (Lead, Qualified Lead, Opportunity, Hot Opportunity) with respective colors.
7. Verify **Header**: Check title, toggle switch, and button styles.
8. Click **Huỷ** or the backdrop to close the modal.
