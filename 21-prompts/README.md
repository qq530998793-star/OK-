# 21 Prompts

## 用途
管理 AI Prompt 的角色、工作流、审核、内容、数据和归档分类。

## 负责人
AI Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- Prompt 模板：[../17-templates/prompt-template.md](../17-templates/prompt-template.md)
- AI 体系：[../10-ai/README.md](../10-ai/README.md)
- AI 审核规则：[../10-ai/ai-review-policy.md](../10-ai/ai-review-policy.md)
- AI 阅读指南：[../00-system/ai-reading-guide.md](../00-system/ai-reading-guide.md)

## 管理规则
- 每个 Prompt 必须有唯一 ID、语义化版本、Owner、状态和风险等级。
- Prompt 正文只保存在一个文件中，其他文档通过相对路径引用。
- 角色 Prompt 放入 `roles/`，跨步骤编排放入 `workflows/`，内容专用放入 `content/`，审核专用放入 `review/`。
- `data/` 在 L5 前只保留目录，不放置正式分析 Prompt。
- 失效 Prompt 移入 `archived/`，保留替代版本与停用原因。

## 生命周期
Draft → Pilot → Active → Deprecated → Archived。只有通过评测和 Owner 审核的版本才能进入 Active。

## 版本规则
破坏性职责或输出变化升级主版本；新增兼容能力升级次版本；不改变行为的修正升级修订版本。

## 后续待完成内容
- 根据真实任务建立首批可执行 Prompt。
- 持续维护 Prompt 索引和评测记录。
