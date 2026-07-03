# Governance

## 用途
定义 OKOS 的维护、审核、发布、废弃与归档规则。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.1.0

## 引用关系
- 仓库规范：[00-system/repository-governance.md](00-system/repository-governance.md)
- 审核规范：[00-system/review-policy.md](00-system/review-policy.md)
- 版本规范：[00-system/versioning-policy.md](00-system/versioning-policy.md)
- 企业宪章：[01-strategy/enterprise-charter.md](01-strategy/enterprise-charter.md)
- 人工批准写入决策：[20-decision-records/DR-0005-human-approved-knowledge-writes.md](20-decision-records/DR-0005-human-approved-knowledge-writes.md)

## L0 Core 治理原则
OKOS 的所有建设必须遵循企业宪章。任何目录、标准、Playbook、产品规则、AI 角色或数据口径，只要与企业宪章冲突，都必须暂停并进入决策评审。

## 分层建设规则
OKOS 按层建设：

1. L0 Core。
2. L1 Knowledge。
3. L2 Playbooks。
4. L3 Product。
5. L4 AI。
6. L5 Data。

每一层完成后必须暂停，由负责人确认后才能进入下一层。未经确认，不得提前填充后续层级的正式内容。

## 决策升级规则
以下事项必须进入 Decision Record：

- 修改企业使命或愿景。
- 修改 OKOS 建设层级。
- 修改 Single Source of Truth 原则。
- 修改重大业务对象定义。
- 修改门店、赛事、战队、AI 或数据的核心边界。
- 废弃 Active 状态的核心标准。

## Owner 原则
任何正式文档必须有 Owner。没有 Owner 的文档不能成为 Active 标准。

## 审核原则
企业级标准至少需要经过 Owner 审核。跨业务域标准需要相关业务 Owner 共同审核。涉及法律、财务、数据隐私、AI 安全的内容必须经过对应负责人确认。

## 主知识库写入门禁
Codex 和其他 AI 工具不得拥有主知识库的自主修改、合并或发布权限。

所有 AI 协作变更必须遵循：

1. 需求提出。
2. AI 判断是否进入 OKOS、归属模块、影响范围、版本和 Decision Record 需求。
3. AI 生成 Draft。
4. 人类 Owner 审核。
5. 获得明确“确认采用”。
6. 由授权人员或受控流程更新 OKOS。
7. 更新版本与 Changelog。
8. 必要时新增或更新 Decision Record。

在确认采用前，Draft 不属于主知识库的 Active 标准。任何“继续”“优化”或一般性讨论不得被视为合并授权；授权必须明确针对当前 Draft。

## 后续待完成内容
- 将真实 GitHub 用户或团队配置到 CODEOWNERS。
- 在远程仓库启用主分支保护和必需审核。
