# vllm-project/vllm#25756: [Usage]: how to do token prune

| 字段 | 值 |
| --- | --- |
| Issue | [#25756](https://github.com/vllm-project/vllm/issues/25756) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to do token prune

### Issue 正文摘录

### Your current environment ``` git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` ### How would you like to use vllm I am trying to perform token pruning on the Qwen2.5-7B model during the prefill stage in vLLM. Specifically, I prune 100 hidden_state tokens at layer 20. However, after pruning, the generated outputs are completely garbled, which should not happen. My prompt length is 6k tokens. Do I need to manually modify the KV cache, slot_mapping, or other parameters to make token pruning work correctly during the prefill stage? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ` git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` ### How would you like to use vllm I am trying to perform token pruning on the Qwen2.5-7B model during...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: prompt length is 6k tokens. Do I need to manually modify the KV cache, slot_mapping, or other parameters to make token pruning work correctly during the prefill stage? ### Before submitting a new issue... - [x] Make sur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: would you like to use vllm I am trying to perform token pruning on the Qwen2.5-7B model during the prefill stage in vLLM. Specifically, I prune 100 hidden_state tokens at layer 20. However, after pruning, the generated...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to do token prune usage;stale ### Your current environment ``` git clone https://github.com/vllm-project/vllm.git cd vllm VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` ### How would you like to use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
