# vllm-project/vllm#9353: [Installation]: When can release the WHL package for version v0.6.3 of cu118?

| 字段 | 值 |
| --- | --- |
| Issue | [#9353](https://github.com/vllm-project/vllm/issues/9353) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: When can release the WHL package for version v0.6.3 of cu118?

### Issue 正文摘录

It seems that every previous version has a corresponding cu118 whl package, except for v0.6.3 and v0.6.2. My CUDA version is cu118, and I want to install VLLM through the WHL package. Thank you for releasing the WHL package of cu118.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: When can release the WHL package for version v0.6.3 of cu118? installation;stale It seems that every previous version has a corresponding cu118 whl package, except for v0.6.3 and v0.6.2. My CUDA version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: has a corresponding cu118 whl package, except for v0.6.3 and v0.6.2. My CUDA version is cu118, and I want to install VLLM through the WHL package. Thank you for releasing the WHL package of cu118. development cuda env_d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: en can release the WHL package for version v0.6.3 of cu118? installation;stale It seems that every previous version has a corresponding cu118 whl package, except for v0.6.3 and v0.6.2. My CUDA version is cu118, and I wa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
