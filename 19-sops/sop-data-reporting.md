# SOP Data Reporting

## 用途
定义数据报表产出、校验、发布和复盘的标准作业流程。

## 负责人
Data Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 报表体系：[../09-data/reporting-system.md](../09-data/reporting-system.md)
- 数据质量：[../09-data/data-quality.md](../09-data/data-quality.md)
- SOP 模板：[../17-templates/sop-template.md](../17-templates/sop-template.md)

## Trigger
到达固定报表周期，或经授权提出临时报表需求。

## Inputs
- 已批准的报表规格与统计周期。
- 指标定义和版本。
- 数据截止时间、组织范围和接收权限。

## Steps
1. 确认报表 ID、周期、指标版本和接收人。
2. 检查数据是否到齐并运行强制质量规则。
3. 对异常、重复、测试和作废记录进行隔离。
4. 生成报表并核对总量、趋势和筛选范围。
5. 由 Data Owner 或指定审核人确认。
6. 按权限发布，记录生成时间与数据状态。
7. 对更正、反馈和异常建立处理记录。

## Outputs
- 带版本、截止时间和完整状态的正式报表。
- 质量检查结果、审核记录和发布记录。

## Exceptions
P0/P1 异常停止发布；数据不完整但允许发布时必须标记 `Incomplete`。更正已发布报表必须保留旧版本。

## 后续待完成内容
- 接入真实报表工具后补充操作界面步骤。
- 根据首轮月报复盘校验清单。
