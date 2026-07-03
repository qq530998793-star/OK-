# Versioning Policy

## 用途
定义 OKOS 仓库版本、文档版本、状态流转与变更记录规范。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.1.0

## 引用关系
- 变更日志：[../CHANGELOG.md](../CHANGELOG.md)
- 仓库治理：[repository-governance.md](repository-governance.md)
- 审核规范：[review-policy.md](review-policy.md)

## 语义化版本
文档使用 `vMAJOR.MINOR.PATCH`：
- MAJOR：职责、边界或既有使用方式发生不兼容变化。
- MINOR：新增向后兼容的规则、流程或能力。
- PATCH：不改变含义的纠错、澄清、链接和格式修正。

## 状态
Draft 尚未批准；In Review 正在审核；Active 已批准生效；Deprecated 已有替代方案；Archived 仅供历史追溯。

Draft 内容不因生成、保存或提交 PR 自动成为 Active。只有人类 Owner 明确确认采用并完成受控合并后才能生效。

## 变更记录
MINOR 和 MAJOR 变更必须更新 Changelog。影响重大边界、Source of Truth、权限或不可逆选择时必须新增 Decision Record。

## 后续待完成内容
- 建立仓库级 Release Tag 流程。
- 定期检查文档版本与 Changelog 一致性。
