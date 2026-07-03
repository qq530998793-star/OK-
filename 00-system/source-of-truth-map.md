# Source Of Truth Map

## 用途
定义 OKOS 核心知识的唯一可信来源，避免同一规则、概念或对象在多个文件中重复定义。

## 负责人
OKOS Governance Owner

## 更新时间
2026-07-03

## 版本号
v1.2.1

## 引用关系
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- 知识分类：[knowledge-taxonomy.md](knowledge-taxonomy.md)
- 内容模型：[content-model.md](content-model.md)
- 全局索引：[../OKOS-INDEX.md](../OKOS-INDEX.md)

## 使用规则
当一个主题在本文件中已有 Source of Truth，其他文件只能引用该文件，不得重新定义。

如果需要修改某个主题，必须修改 Source of Truth 文件，并检查所有引用它的文件。

## 核心知识来源
| 主题 | Source of Truth | Owner |
|---|---|---|
| 企业宪章 | `01-strategy/enterprise-charter.md` | OKOS Chief System Architect |
| 企业使命 | `01-strategy/company-mission.md` | Strategy Owner |
| 企业愿景 | `01-strategy/vision.md` | Strategy Owner |
| 战略支柱 | `01-strategy/strategic-pillars.md` | Strategy Owner |
| 核心术语 | `GLOSSARY.md` | OKOS Governance Owner |
| 内容模型 | `00-system/content-model.md` | OKOS Chief System Architect |
| 知识分类 | `00-system/knowledge-taxonomy.md` | OKOS Chief System Architect |
| OKOS 治理规则 | `GOVERNANCE.md` | OKOS Governance Owner |
| 仓库权限与协作规则 | `00-system/repository-governance.md` | OKOS Governance Owner |
| 审核规则 | `00-system/review-policy.md` | OKOS Governance Owner |
| 版本规则 | `00-system/versioning-policy.md` | OKOS Governance Owner |
| 知识库网站发布规则 | `20-decision-records/DR-0006-mkdocs-publishing-layer.md` | OKOS Governance Owner |
| 门店模型 | `04-stores/store-model.md` | Store Operations Owner |
| 战队模型 | `05-teams/team-model.md` | Team Operations Owner |
| 赛事体系 | `06-events/event-system-overview.md` | Event Operations Owner |
| 赛事类型 | `06-events/event-types.md` | Event Operations Owner |
| 社群模型 | `07-community/community-model.md` | Community Owner |
| 玩家生命周期 | `07-community/user-lifecycle.md` | Community Owner |
| 产品愿景 | `08-product/product-vision.md` | Product Owner |
| 产品体系 | `08-product/product-system.md` | Product Owner |
| 产品能力地图 | `08-product/feature-map.md` | Product Owner |
| 产品需求规则 | `08-product/product-requirements.md` | Product Owner |
| 产品发布规则 | `08-product/release-policy.md` | Product Owner |
| 合作伙伴模型 | `13-partnerships/partnership-model.md` | Partnership Owner |
| 合作伙伴类型 | `13-partnerships/partner-types.md` | Partnership Owner |
| Playbook 体系 | `18-playbooks/playbook-system.md` | Operations Owner |
| SOP 体系 | `19-sops/sop-system.md` | Operations Owner |
| 门店启动剧本 | `18-playbooks/store-launch-playbook.md` | Store Operations Owner |
| 城市赛事启动剧本 | `18-playbooks/city-event-launch-playbook.md` | Event Operations Owner |
| 赞助销售剧本 | `18-playbooks/sponsorship-sales-playbook.md` | Sales Owner |
| 社群增长剧本 | `18-playbooks/community-growth-playbook.md` | Community Owner |
| 危机响应剧本 | `18-playbooks/crisis-response-playbook.md` | Operations Owner |
| 赛事报名 SOP | `19-sops/sop-event-registration.md` | Event Operations Owner |
| 奖金发放 SOP | `19-sops/sop-prize-payment.md` | Finance Owner |
| 门店接入 SOP | `19-sops/sop-store-onboarding.md` | Store Operations Owner |
| 战队认证 SOP | `19-sops/sop-team-verification.md` | Team Operations Owner |
| 内容发布 SOP | `19-sops/sop-content-publishing.md` | Marketing Owner |
| 财务基础规则 | `15-finance/finance-policy.md` | Finance Owner |
| 合规基础规则 | `14-legal-compliance/README.md` | Compliance Owner |
| AI 基础规则 | `10-ai/README.md` | AI Owner |
| AI 员工体系 | `10-ai/ai-system.md` | AI Owner |
| AI 角色目录 | `10-ai/ai-roles.md` | AI Owner |
| AI 安全规则 | `10-ai/ai-safety-policy.md` | AI Owner |
| AI 审核规则 | `10-ai/ai-review-policy.md` | AI Owner |
| Prompt 管理规则 | `21-prompts/README.md` | AI Owner |
| Prompt 索引 | `21-prompts/prompt-index.md` | AI Owner |
| 数据基础规则 | `09-data/README.md` | 李豪大王 |
| 数据治理体系 | `09-data/data-system.md` | 李豪大王 |
| 数据字典 | `09-data/data-dictionary.md` | 李豪大王 |
| 指标口径 | `09-data/metrics-definition.md` | 李豪大王 |
| 数据质量规则 | `09-data/data-quality.md` | 李豪大王 |
| 报表体系 | `09-data/reporting-system.md` | 李豪大王 |
| 看板规格 | `09-data/dashboard-specs.md` | 李豪大王 |
| 数据隐私规则 | `09-data/privacy-policy.md` | Compliance Owner |

## 引用关系要求
引用 Source of Truth 时必须使用相对路径。

示例：

```markdown
详见 [门店模型](../04-stores/store-model.md)。
```

## 变更要求
修改 Source of Truth 时必须检查：
- 是否影响术语表。
- 是否影响内容模型。
- 是否影响业务域 README。
- 是否需要 Decision Record。
- 是否影响后续 Playbook、SOP、产品、AI 或数据。

## 后续待完成内容
- 根据真实业务复盘补充更多 Playbook 和 SOP 的 Source of Truth。
- 根据产品演进补充独立产品的 Source of Truth。
- 根据真实评测补充 Active Prompt 的 Source of Truth。
- 根据真实数据源补充物理数据血缘。
- 验证远程仓库的主分支保护与治理规则一致。
