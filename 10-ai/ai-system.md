# AI System

## 用途
定义 OKOS L4 AI 员工体系的治理结构、运行边界、文档关系和扩展规则。

## 负责人
AI Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- AI 战略：[ai-strategy.md](ai-strategy.md)
- AI 角色：[ai-roles.md](ai-roles.md)
- Agent 规格：[ai-agent-specs.md](ai-agent-specs.md)
- AI 工作流：[ai-workflows.md](ai-workflows.md)
- 安全规则：[ai-safety-policy.md](ai-safety-policy.md)
- 审核规则：[ai-review-policy.md](ai-review-policy.md)
- Prompt 库：[../21-prompts/README.md](../21-prompts/README.md)

## L4 AI 定义
L4 AI 把 OKOS 权威知识、执行剧本和产品规则转化为可控的 AI 协作能力。AI 员工是具有明确职责、输入、权限、输出、审核和升级路径的软件角色，不是组织责任主体。

## 基本原则
- AI 不拥有最终决策权，业务 Owner 对结果负责。
- AI 必须引用唯一可信来源，不得把推断写成已确认规则。
- 默认只读并按最小权限运行。
- 事实、推断与建议必须可区分，关键结论必须可追溯。
- 高风险输出先审后用，对外发布和执行动作必须人工确认。
- Prompt、模型、工具或知识范围变化必须版本化并重新评测。

## 文档关系
1. AI 战略定义组织定位。
2. AI 角色定义员工目录与职责。
3. Agent 规格定义运行契约。
4. AI 工作流定义协作过程。
5. 安全与审核规则定义风险边界。
6. `21-prompts/` 保存 Prompt 的唯一版本。

## L4 边界
L4 可以定义 AI 角色、Prompt、上下文、工具权限、工作流、评测和审核。

L4 不改变 L0-L3 的权威规则，不定义正式指标公式、数据模型或看板口径；这些属于 L5 Data。

## 扩展规则
新增 AI 员工必须先建立角色条目和 Agent 规格，再创建 Prompt、测试样例和审核责任。未完成风险分级与评测的员工只能处于 Draft。

## 后续待完成内容
- L4 确认后用真实工作样本建立评测集。
- L5 完成后启用数据分析类 AI 员工。

