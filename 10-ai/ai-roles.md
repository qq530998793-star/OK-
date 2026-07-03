# AI Roles

## 用途
定义 OKOS 中可使用的 AI 角色及其职责边界。

## 负责人
AI Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- AI 战略：[ai-strategy.md](ai-strategy.md)
- Agent 规格：[ai-agent-specs.md](ai-agent-specs.md)
- Prompt 角色目录：[../21-prompts/roles/README.md](../21-prompts/roles/README.md)

## AI 员工目录
| ID | AI 员工 | 主要职责 | 默认风险 | 状态 |
|---|---|---|---|---|
| AI-KS-001 | OKOS 知识管家 | 检索来源、回答制度问题、发现引用冲突 | 低 | Pilot |
| AI-OP-001 | 运营协作员 | 生成任务清单、检查遗漏、整理交接 | 中 | Pilot |
| AI-CT-001 | 内容助理 | 依据品牌与合规标准生成内容草案 | 中 | Pilot |
| AI-PD-001 | 产品助理 | 整理问题、需求草案和验收条件 | 中 | Pilot |
| AI-DA-001 | 数据分析员 | 基于正式指标口径生成分析 | 高 | Pilot |

## 通用边界
AI 可以检索、归纳、比较、生成草案和提出建议。未经授权不得对外发布、修改权威文档、批准需求、承诺费用、变更权限、作出法律判断或执行不可逆操作。

## 后续待完成内容
- 为 Pilot 角色建立真实任务评测样例。
- 使用脱敏数据和已批准报表评测 AI-DA-001。
