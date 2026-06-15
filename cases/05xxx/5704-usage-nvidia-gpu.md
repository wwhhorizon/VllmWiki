# vllm-project/vllm#5704: [Usage]: NVIDIA多型号的GPU如何利用到？

| 字段 | 值 |
| --- | --- |
| Issue | [#5704](https://github.com/vllm-project/vllm/issues/5704) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: NVIDIA多型号的GPU如何利用到？

### Issue 正文摘录

### Your current environment ![gpu](https://github.com/vllm-project/vllm/assets/47100639/772cf312-d447-472c-918f-b3e495c04a9b) vllm本地部署模型加载的时候只用到了RTX3060显存，跑9B的模型无法跑起来，有没有办法可以实现在多个卡上面实现并行？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 行？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: assets/47100639/772cf312-d447-472c-918f-b3e495c04a9b) vllm本地部署模型加载的时候只用到了RTX3060显存，跑9B的模型无法跑起来，有没有办法可以实现在多个卡上面实现并行？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
