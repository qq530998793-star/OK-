# Content Model

## 用途
定义 OKOS 的核心内容对象与业务对象，例如 Store、Team、Player、Event、Metric、SOP、Playbook、Prompt、Decision。

## 负责人
OKOS Chief System Architect

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 系统架构：[architecture.md](architecture.md)
- 知识分类：[knowledge-taxonomy.md](knowledge-taxonomy.md)
- 唯一可信来源地图：[source-of-truth-map.md](source-of-truth-map.md)
- 术语表：[../GLOSSARY.md](../GLOSSARY.md)

## L1 内容模型原则
内容模型定义 OKOS 中长期稳定的企业对象。后续 Playbook、产品、AI 和数据都必须基于这些对象展开。

在 L1 阶段，内容模型只定义对象含义和对象关系，不定义执行步骤、产品功能、AI Prompt 或数据公式。

## 核心业务对象
| 对象 | 含义 | Source of Truth |
|---|---|---|
| Store | 合作门店，是线下赛事、社群触点和玩家服务节点 | `../04-stores/store-model.md` |
| Team | 战队，是玩家组织化参与赛事和社群活动的基本单位 | `../05-teams/team-model.md` |
| Player | 玩家，是 OK赛事联盟服务的核心用户对象 | `../07-community/user-lifecycle.md` |
| Event | 赛事，是连接玩家、战队、门店和合作伙伴的核心运营载体 | `../06-events/event-system-overview.md` |
| Community | 社群，是玩家、战队、门店和运营团队持续互动的关系网络 | `../07-community/community-model.md` |
| Partner | 合作伙伴，是向 OK赛事联盟提供资源、品牌、场地或商业合作的外部组织 | `../13-partnerships/partnership-model.md` |
| Sponsor | 赞助商，是以资金、资源或品牌权益交换赛事和社群合作价值的合作伙伴 | `../13-partnerships/partner-types.md` |
| Product | 数字产品，是承载报名、信息、运营和数据闭环的小程序或系统能力 | `../08-product/product-vision.md` |
| Knowledge | 企业知识，是可长期复用、可被引用、可被审核的组织资产 | `knowledge-taxonomy.md` |
| Standard | 标准，是被确认后可作为执行依据的规则或定义 | `source-of-truth-map.md` |
| SOP | 标准作业流程，是单一、重复、稳定动作的操作流程 | `../19-sops/README.md` |
| Playbook | 执行剧本，是面向复杂目标的跨角色打法 | `../18-playbooks/README.md` |
| Prompt | AI Prompt，是可版本管理的 AI 工作指令 | `../21-prompts/README.md` |
| Metric | 指标，是衡量业务对象和业务结果的口径 | `../09-data/metrics-definition.md` |
| Decision | 决策记录，是重大取舍的组织记忆 | `../20-decision-records/README.md` |

## 核心对象关系
- Store 承载 Event，也连接本地 Player 和 Community。
- Team 由 Player 组成，并通过 Event 形成成绩、声誉和成长记录。
- Event 连接 Player、Team、Store、Community、Partner 和 Sponsor。
- Community 维持 Player 和 Team 的长期活跃。
- Partner 和 Sponsor 通过 Event、Store、Community 获得合作价值。
- Product 将 Store、Team、Player、Event 和 Community 的动作线上化。
- Metric 用于衡量上述对象，但正式公式在 L5 Data 定义。
- SOP 和 Playbook 调用这些对象，但具体执行在 L2 定义。
- Prompt 读取这些对象和标准，但正式 Prompt 在 L4 定义。

## 对象变更规则
修改核心业务对象定义时，必须检查：
- `GLOSSARY.md`
- `source-of-truth-map.md`
- 相关业务域模型文档
- 可能受影响的 SOP、Playbook、产品、AI 和数据文档

## 后续待完成内容
- L1 确认后冻结核心业务对象第一版。
- L2 阶段补充 SOP 与 Playbook 对象调用方式。
- L5 阶段补充 Metric 的正式数据口径。
