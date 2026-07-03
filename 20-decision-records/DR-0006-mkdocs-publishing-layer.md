# DR-0006: MkDocs Publishing Layer

## 用途
记录 OKOS 使用 MkDocs 建立网站发布层，并保持主知识库唯一来源的架构决策。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 企业治理：[../GOVERNANCE.md](../GOVERNANCE.md)
- 仓库治理：[../00-system/repository-governance.md](../00-system/repository-governance.md)
- 唯一可信来源：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- MkDocs 配置：[../mkdocs.yml](../mkdocs.yml)

## 状态
Accepted

## 决策日期
2026-07-03

## 背景
OKOS 需要提供适合团队浏览和后续部署到 GitHub Pages 的中文知识库网站，同时不能把现有权威 Markdown 复制成第二套人工维护内容。

## 决策
使用 MkDocs Material 作为发布界面，`docs/` 作为网站导航源。构建时由 `mkdocs-gen-files` 从仓库权威 Markdown 生成虚拟页面，正文仍以原文件为唯一可信来源。

网站一级导航固定为 Quick、Playbooks、Training、Rules、Reports 和 Activity。GitHub Actions 可将构建结果部署到 `gh-pages`。

## 影响
优点：不迁移现有目录、不复制业务正文、支持中文搜索和 GitHub Pages。

成本：本地预览和部署需要 Python 及文档依赖；网站导航映射需要随核心模块变化维护。

## 执行要求
- 禁止在 `docs/` 重复维护权威业务正文。
- 发布失败不得影响主知识库可读性。
- GitHub Pages 和 Actions 权限由人类仓库管理员启用。
- 导航或生成机制的重大改变必须更新本记录或新增替代决策。

## 后续待完成内容
- 首次部署后填写正式 `site_url`。
- 根据真实使用反馈优化导航。

