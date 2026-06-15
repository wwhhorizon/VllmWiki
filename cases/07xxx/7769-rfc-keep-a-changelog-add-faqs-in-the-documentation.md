# vllm-project/vllm#7769: [RFC]: Keep a Changelog & Add FAQs in the Documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#7769](https://github.com/vllm-project/vllm/issues/7769) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Keep a Changelog & Add FAQs in the Documentation

### Issue 正文摘录

### Motivation. ## Changelog I frequently find myself wondering what is the difference between the latest version(s) of vLLM, and the version that I currently have deployed. It seems like it would be nice to keep a simple changelog that documents features, fixes, newly-supported hardware and updates between versions so that we can easily see what has been added in recent versions -- e.g. new CLI arguments, optimizations, quantization formats, updated hardware support for features (e.g. punica -> triton kernels, expanding hardware support for multi-lora serving) patched bugs, and so forth. A great template for this is [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) following semver - it would be super easy to implement with Markdown in the documentation site. I think this would make vLLM's newer features much more accessible, _and_ it would also help identify gaps in the documentation when we add something to the changelog that's not on the docs site ## FAQs There are a bunch of questions that are commonly asked over and over in the discord, including things such as: - Does vLLM support XYZ hardware/accelerator? - Does vLLM support tool use / when is tool use coming? - Doe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n recent versions -- e.g. new CLI arguments, optimizations, quantization formats, updated hardware support for features (e.g. punica -> triton kernels, expanding hardware support for multi-lora serving) patched bugs, an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ntization formats, updated hardware support for features (e.g. punica -> triton kernels, expanding hardware support for multi-lora serving) patched bugs, and so forth. A great template for this is [Keep a Changelog](htt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: equently find myself wondering what is the difference between the latest version(s) of vLLM, and the version that I currently have deployed. It seems like it would be nice to keep a simple changelog that documents featu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: been added in recent versions -- e.g. new CLI arguments, optimizations, quantization formats, updated hardware support for features (e.g. punica -> triton kernels, expanding hardware support for multi-lora serving) patc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ool use / when is tool use coming? - Does vLLM support XYZ model / model architecture? - How can I get my model to fit in a vRAM-constrained environment? - How do I get started with distributed inference? It seems like...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
