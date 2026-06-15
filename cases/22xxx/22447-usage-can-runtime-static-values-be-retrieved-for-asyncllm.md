# vllm-project/vllm#22447: [Usage]: Can runtime static values be retrieved for `AsyncLLM`

| 字段 | 值 |
| --- | --- |
| Issue | [#22447](https://github.com/vllm-project/vllm/issues/22447) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can runtime static values be retrieved for `AsyncLLM`

### Issue 正文摘录

### Your current environment In the current v1, we have the `AsyncLLM` which starts background tasks for handling the vLLM engine. During engine initialization different important values are initialized such as `num_gpu_blocks`. In different applications, it is useful to retrieve these values later on. Although, contrary to v0, it seems we don't have a direct way to access these via the `AsyncLLM` class (or its underlying engine core). What would be the best way to retrieve these values, after initializing the `AsyncLLM`? ### How would you like to use vllm I would like to have different cache configuration values accessed by a LLM service, that monitors vLLM. This service requires knowing the `num_gpu_blocks` value, among others. Since these values are computed once at initialization, it makes sense to retrieve these values once the engine completes their calculation. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sks for handling the vLLM engine. During engine initialization different important values are initialized such as `num_gpu_blocks`. In different applications, it is useful to retrieve these values later on. Although, co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: itialization different important values are initialized such as `num_gpu_blocks`. In different applications, it is useful to retrieve these values later on. Although, contrary to v0, it seems we don't have a direct way...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### How would you like to use vllm I would like to have different cache configuration values accessed by a LLM service, that monitors vLLM. This service requires knowing the `num_gpu_blocks` value, among others. Since t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
