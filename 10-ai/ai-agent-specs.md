# AI Agent Specs

## 用途
定义 AI Agent 的角色、权限、工具、输入输出、审计和升级机制。

## 负责人
AI Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- AI 角色：[ai-roles.md](ai-roles.md)
- AI 工作流：[ai-workflows.md](ai-workflows.md)
- AI 安全规则：[ai-safety-policy.md](ai-safety-policy.md)
- Prompt 库：[../21-prompts/README.md](../21-prompts/README.md)

## 必填规格
每个 AI 员工必须记录唯一 ID、Owner、状态、目标、允许与禁止任务、知识范围、工具权限、输入输出契约、风险等级、人工审批点、Prompt 版本、测试集、日志和撤销方式。

## 默认约束
- 默认只读；写入、发布、发送或执行必须单独授权。
- 信息不足时指出缺口，不编造事实。
- 回答规则时给出文件路径，无法定位时标记“未确认”。
- 不跨门店、战队、合作方或用户边界泄露数据。
- 工具失败、权限不明或来源冲突时停止并升级人工。

## 状态
Draft 仅供设计；Pilot 限受控试用；Active 可在批准场景运行；Suspended 暂停使用；Retired 停止并归档。

## 后续待完成内容
- 为 Active 员工记录具体模型和工具配置。
- 建立 Agent 运行变更记录。
