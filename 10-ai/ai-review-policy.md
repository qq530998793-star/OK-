# AI Review Policy

## 用途
定义 AI 输出在进入 OKOS、对外发布或执行前的审核规则。

## 负责人
AI Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- AI 安全规则：[ai-safety-policy.md](ai-safety-policy.md)
- 审核规范：[../00-system/review-policy.md](../00-system/review-policy.md)
- Prompt 审核目录：[../21-prompts/review/README.md](../21-prompts/review/README.md)

## 风险等级
| 等级 | 示例 | 使用要求 |
|---|---|---|
| R1 低 | 内部检索、格式整理、无敏感信息摘要 | 可直接使用，保留抽检 |
| R2 中 | 运营清单、产品草案、内部建议 | 业务 Owner 使用前复核 |
| R3 高 | 对外内容、资格判断、敏感信息、重要经营建议 | 指定 Owner 明确审批 |
| R4 禁止自动执行 | 合同承诺、付款、权限授予、处罚、不可逆操作 | AI 只能准备材料，授权人员决定和执行 |

## 审核检查
审核人必须检查来源、事实准确性、完整性、权限、敏感信息、品牌合规、异常处理和输出是否超出 AI 职责。

## Prompt 发布门禁
Prompt 进入 Active 前必须完成 Owner 审核、典型样例、边界样例、安全样例和失败处理测试。模型、工具、知识范围或关键指令变化后必须重新评测。

## 事故处理
错误输出已被发布或执行时，应立即停止相关 Agent，保留版本和日志，纠正影响，并按严重程度进入危机响应或 Decision Record。

## 后续待完成内容
- 建立各 Active Prompt 的评测记录。
- 根据试运行数据调整风险等级。
