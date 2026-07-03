# Repository Governance

## 用途
定义 OKOS 在 GitHub 中的分支、提交、Pull Request、Issue、Owner 与审核规则。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.1.0

## 引用关系
- 治理规则：[../GOVERNANCE.md](../GOVERNANCE.md)
- 审核规范：[review-policy.md](review-policy.md)
- 版本规范：[versioning-policy.md](versioning-policy.md)
- 人工批准写入决策：[../20-decision-records/DR-0005-human-approved-knowledge-writes.md](../20-decision-records/DR-0005-human-approved-knowledge-writes.md)

## 分支规则
- `main` 是主知识库，只保存已批准的 Active 内容。
- AI 生成内容必须进入 Draft 分支或 Pull Request，不得直接提交到 `main`。
- Draft 分支建议使用 `draft/<topic>`，正式变更建议使用 `docs/<topic>`。
- 禁止 AI 账号拥有绕过分支保护、管理员合并或直接推送权限。

## Pull Request 门禁
合并前必须有：
- 变更目的、模块、影响文档和 Source of Truth 说明。
- Owner 审核及明确“确认采用”记录。
- 版本影响和 Decision Record 判断。
- 引用、链接、元数据和冲突检查。
- 必需 CODEOWNERS 审核通过。

## GitHub 设置要求
远程仓库应对 `main` 启用禁止直接推送、至少一名人类审批、CODEOWNERS 必需审核、解决全部讨论后才能合并，并限制可绕过保护的角色。

仓库文档只能声明治理要求，实际权限必须在 GitHub 仓库设置中启用。

## Codex 权限
Codex 可以读取知识库、生成 Draft、执行检查和准备 PR；未经明确批准，不得修改主知识库、合并 PR、发布版本或改变保护规则。

## 后续待完成内容
- 替换 CODEOWNERS 中的占位账号。
- 在 GitHub 验证主分支保护已启用。
