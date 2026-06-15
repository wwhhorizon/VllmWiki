# vllm-project/vllm#10783: [New Model]: nvidia/Hymba-1.5B-Base

| 字段 | 值 |
| --- | --- |
| Issue | [#10783](https://github.com/vllm-project/vllm/issues/10783) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: nvidia/Hymba-1.5B-Base

### Issue 正文摘录

### The model to consider. [https://huggingface.co/nvidia/Hymba-1.5B-Base](https://huggingface.co/nvidia/Hymba-1.5B-Base) [https://huggingface.co/nvidia/Hymba-1.5B-Instruct](https://huggingface.co/nvidia/Hymba-1.5B-Instruct) ### The closest model vllm already supports. https://huggingface.co/docs/transformers/main/en/model_doc/mamba https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini ### What's your difficulty of supporting the model you want? - support for mamba and attention heads in mixed architecture - attention for both sliding window and meta (memory) tokens (a variation of blocksparse attention might be leveraged) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#18212 [V1] Support cross-layer KV sharing

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: nvidia/Hymba-1.5B-Base new-model;stale ### The model to consider. [https://huggingface.co/nvidia/Hymba-1.5B-Base](https://huggingface.co/nvidia/Hymba-1.5B-Base) [https://huggingface.co/nvidia/Hymba-1.5B-Ins...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng the model you want? - support for mamba and attention heads in mixed architecture - attention for both sliding window and meta (memory) tokens (a variation of blocksparse attention might be leveraged) ### Before subm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tention for both sliding window and meta (memory) tokens (a variation of blocksparse attention might be leveraged) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: nvidia/Hymba-1.5B-Base new-model;stale ### The model to consider. [https://huggingface.co/nvidia/Hymba-1.5B-Base](https://huggingface.co/nvidia/Hymba-1.5B-Base) [https://huggingface.co/nvidia/Hymba-1.5B-Ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache;model_support attention #18212 [V1] Support cross-laye...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18212](https://github.com/vllm-project/vllm/pull/18212) | mentioned | 0.6 | [V1] Support cross-layer KV sharing | Some models like Tencent-Hunyuan-Large (#10043) and Hymba-1.5B-Base (#10783) use cross-layer KV sharing (e.g. [Cross-Layer Attention](https://arxiv.org/abs/2405.12981)). This PR a… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
