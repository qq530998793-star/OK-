# Review Policy

## 用途
定义 OKOS 文档审核、复审周期、跨部门评审与发布前检查规则。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.1.0

## 引用关系
- 治理规则：[../GOVERNANCE.md](../GOVERNANCE.md)
- 仓库治理：[repository-governance.md](repository-governance.md)
- 决策记录：[../20-decision-records/DR-0005-human-approved-knowledge-writes.md](../20-decision-records/DR-0005-human-approved-knowledge-writes.md)

## 审核状态
Draft → In Review → Approved → Active。Rejected Draft 不得进入主知识库；被替代内容按版本规范进入 Deprecated 或 Archived。

## 审核角色
| 变更类型 | 必需审核 |
|---|---|
| 单一业务域 | 文档 Owner |
| 跨业务域 | 所有受影响域 Owner |
| 治理或 Source of Truth | OKOS Governance Owner |
| 法律、财务、隐私或 AI 安全 | 对应专业 Owner |
| 重大不可逆变更 | Owner + Decision Record 批准人 |

## 确认标准
“确认采用”必须针对可识别的 Draft 或 PR。审核人应检查用途、来源、影响范围、引用关系、版本、Decision Record、敏感信息和后续维护责任。

AI 自审、自动检查通过或 Draft 生成完成均不能替代人类批准。

## 后续待完成内容
- 根据真实团队补充审批人名单。
- 建立定期复审日历。
