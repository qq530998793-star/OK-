# SOP Event Registration

## 用途
定义赛事报名的标准作业流程。

## 负责人
Event Operations Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 赛事生命周期：[../06-events/event-lifecycle.md](../06-events/event-lifecycle.md)
- 赛事体系总览：[../06-events/event-system-overview.md](../06-events/event-system-overview.md)
- 城市赛事启动 Playbook：[../18-playbooks/city-event-launch-playbook.md](../18-playbooks/city-event-launch-playbook.md)
- SOP 模板：[../17-templates/sop-template.md](../17-templates/sop-template.md)

## Trigger
赛事进入报名准备或报名开放阶段时启动本 SOP。

## Inputs
- 赛事名称和类型。
- 报名对象范围。
- 报名时间。
- 资格要求。
- 赛事规则来源。
- 负责人和审核人。

## Steps
1. 确认赛事类型和报名对象。
2. 确认报名入口、报名字段和截止时间。
3. 发布报名信息。
4. 收集报名信息。
5. 审核报名资格。
6. 处理重复、缺失、异常或不符合条件的报名。
7. 确认最终参赛名单。
8. 将名单同步给赛事执行负责人和社群负责人。
9. 留存报名记录。

## Outputs
- 报名记录。
- 资格审核结果。
- 最终参赛名单。
- 异常报名处理记录。

## Exceptions
- 报名信息缺失：退回补充。
- 报名对象不符合条件：标记不通过并记录原因。
- 报名人数超出限制：按赛事规则处理候补或筛选。
- 报名争议：升级给 Event Operations Owner。

## Related Playbooks
- 城市赛事启动：[../18-playbooks/city-event-launch-playbook.md](../18-playbooks/city-event-launch-playbook.md)

## 后续待完成内容
- L3 阶段确认产品报名入口。
- L5 阶段补充报名转化指标口径。
