# Architecture

## 用途
定义 OKOS 的整体系统架构、目录边界、知识关系与扩展原则。

## 负责人
OKOS Chief System Architect

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 全局索引：[../OKOS-INDEX.md](../OKOS-INDEX.md)
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- 内容模型：[content-model.md](content-model.md)
- 仓库治理：[repository-governance.md](repository-governance.md)

## 分层架构
OKOS 采用六层架构：

1. L0 Core：企业宪章层，定义使命、愿景、原则、治理和建设边界。
2. L1 Knowledge：企业知识层，定义业务对象、标准、术语和知识来源。
3. L2 Playbooks：执行剧本层，定义复杂目标的跨角色执行方式。
4. L3 Product：产品层，定义小程序和数字产品的功能、路径和发布机制。
5. L4 AI：AI员工层，定义 AI 角色、Prompt、工作流、权限和审核。
6. L5 Data：数据层，定义指标、报表、看板、质量和隐私规则。

## 架构约束
低层是高层的依据。后续层级不得覆盖、绕开或隐式改写前序层级。

L0 Core 是最高约束。任何与 L0 Core 冲突的后续内容，都必须暂停并进入治理评审。

## 后续待完成内容
- L0 确认后进入 L1 Knowledge 架构细化。
- L1 阶段明确业务对象和知识边界。
- L2 阶段定义 Playbook 与 SOP 的调用关系。
