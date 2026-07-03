# DR-0005: Human-Approved Knowledge Writes

## 用途
记录 OKOS 采用“AI 生成 Draft、人类批准后写入主知识库”的治理决策。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 治理规则：[../GOVERNANCE.md](../GOVERNANCE.md)
- 仓库治理：[../00-system/repository-governance.md](../00-system/repository-governance.md)
- 审核规范：[../00-system/review-policy.md](../00-system/review-policy.md)
- AI 安全规则：[../10-ai/ai-safety-policy.md](../10-ai/ai-safety-policy.md)

## 状态
Accepted

## 决策日期
2026-07-03

## 背景
OKOS 是企业主知识库。AI 可以提高整理和维护效率，但若拥有自主写入或合并权限，可能把未审核内容、错误推断或跨模块冲突直接变为正式标准。

## 决策
AI 不拥有主知识库的自主修改权限。所有 AI 协作变更必须先形成 Draft，经人类 Owner 审核并明确确认采用后，才能通过受控流程更新 OKOS。

每次任务开始前必须判断归档必要性、模块归属、文档影响、版本影响和 Decision Record 需求。采用后同步更新版本、Changelog 和必要的决策记录。

## 备选方案
- 允许 AI 直接写入：效率高，但错误和权限风险不可接受。
- 完全禁止 AI 参与：风险低，但失去检索、草拟和一致性检查价值。
- 采用人类审批门禁：保留效率，同时维持最终责任和知识可信度。

## 影响
正面影响：明确责任、保留审核证据、降低主知识库污染和越权风险。

成本：增加审核步骤；GitHub 必须配置分支保护、CODEOWNERS 和人类审批人。

## 执行要求
- `main` 禁止 AI 直接推送和绕过保护。
- Draft 或 PR 必须通过人类 Owner 审核。
- 合并前完成版本、引用、影响和 Decision Record 检查。
- GitHub 实际权限配置由仓库管理员负责。

## 后续待完成内容
- 配置真实 CODEOWNERS。
- 验证远程主分支保护。
- 在首次真实 PR 后复盘门禁有效性。
