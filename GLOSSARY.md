# Glossary

## 用途
统一 OKOS 核心术语，避免门店、战队、赛事、社群、数据、AI 等模块出现多套定义。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 内容模型：[00-system/content-model.md](00-system/content-model.md)
- 知识分类：[00-system/knowledge-taxonomy.md](00-system/knowledge-taxonomy.md)
- 唯一可信来源地图：[00-system/source-of-truth-map.md](00-system/source-of-truth-map.md)
- 数据口径：[09-data/metrics-definition.md](09-data/metrics-definition.md)

## 术语维护规则
术语表只定义跨业务域共用概念。单一业务域内部的细节定义，应放在对应 Source of Truth 文件中。

术语不得与 Source of Truth 冲突。如有冲突，以 Source of Truth 为准，并更新本术语表。

## 核心术语
| 术语 | 定义 | Source of Truth |
|---|---|---|
| OK赛事联盟 | 围绕电竞玩家、战队、合作门店、赛事活动、品牌合作与数字化产品持续运转的电竞运营网络 | `01-strategy/enterprise-charter.md` |
| OKOS | OK赛事联盟的企业操作系统，用于管理知识、标准、决策、执行、产品、AI 与数据 | `README.md` |
| L0 Core | 企业宪章层，定义使命、愿景、原则、治理和边界 | `01-strategy/enterprise-charter.md` |
| L1 Knowledge | 企业知识层，定义业务对象、术语、标准边界和知识来源 | `00-system/knowledge-taxonomy.md` |
| Source of Truth | 某个主题的唯一可信来源，其他文档只能引用，不得重复定义 | `00-system/source-of-truth-map.md` |
| Store | 合作门店，是线下赛事、社群触点和玩家服务节点 | `04-stores/store-model.md` |
| Team | 战队，是玩家组织化参与赛事和社群活动的基本单位 | `05-teams/team-model.md` |
| Player | 玩家，是 OK赛事联盟服务的核心用户对象 | `07-community/user-lifecycle.md` |
| Event | 赛事，是连接玩家、战队、门店和合作伙伴的核心运营载体 | `06-events/event-system-overview.md` |
| Community | 社群，是玩家、战队、门店和运营团队持续互动的关系网络 | `07-community/community-model.md` |
| Partner | 合作伙伴，是提供资源、渠道、场地、品牌或商业合作的外部组织 | `13-partnerships/partnership-model.md` |
| Sponsor | 赞助商，是通过资金、资源或品牌权益参与合作的伙伴类型 | `13-partnerships/partner-types.md` |
| SOP | 标准作业流程，用于定义单一、重复、稳定动作 | `19-sops/README.md` |
| Playbook | 执行剧本，用于定义复杂目标的跨角色打法 | `18-playbooks/README.md` |
| Prompt | 可版本管理的 AI 工作指令 | `21-prompts/README.md` |
| Metric | 指标，用于衡量业务对象、过程或结果 | `09-data/metrics-definition.md` |
| Decision Record | 记录重大决策背景、方案、取舍和影响的文档 | `20-decision-records/README.md` |

## 后续待完成内容
- L1 确认后冻结第一版核心术语。
- L2-L5 建设时补充新增术语。
- 建立术语变更审核流程。
