# OKOS V1.2.2

## 用途
OKOS 是 OK赛事联盟的企业操作系统仓库入口，用于统一管理战略、运营、门店、赛事、社群、产品、数据、AI 协同与企业标准。

## 负责人
OKOS Chief System Architect

## 更新时间
2026-07-03

## 版本号
v1.2.2

## 引用关系
- 全局索引：[OKOS-INDEX.md](OKOS-INDEX.md)
- 企业宪章：[01-strategy/enterprise-charter.md](01-strategy/enterprise-charter.md)
- 治理规则：[GOVERNANCE.md](GOVERNANCE.md)
- 术语表：[GLOSSARY.md](GLOSSARY.md)
- 系统架构：[00-system/architecture.md](00-system/architecture.md)
- 网站配置：[mkdocs.yml](mkdocs.yml)
- MkDocs 发布决策：[20-decision-records/DR-0006-mkdocs-publishing-layer.md](20-decision-records/DR-0006-mkdocs-publishing-layer.md)

## 当前状态
OKOS 的六层基线已完成并确认：

1. L0 Core：企业宪章。
2. L1 Knowledge：企业知识。
3. L2 Playbooks：执行剧本。
4. L3 Product：产品。
5. L4 AI：AI员工。
6. L5 Data：数据。

## 知识库网站
MkDocs 使用 `docs/` 作为发布入口，并在构建时读取现有权威 Markdown。网站导航包含 Quick、Playbooks、Training、Rules、Reports 和 Activity。

开发服务监听全部 OKOS 模块。服务运行期间，保存任一权威 Markdown 后，网站会自动重新构建并刷新。

本地预览：

```powershell
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

## 后续待完成内容
- 首次 GitHub Pages 部署后填写正式站点地址。
- 使用真实业务样本持续验证和迭代。
