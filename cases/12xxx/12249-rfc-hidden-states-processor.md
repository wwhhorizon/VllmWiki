# vllm-project/vllm#12249: [RFC]: Hidden states processor

| 字段 | 值 |
| --- | --- |
| Issue | [#12249](https://github.com/vllm-project/vllm/issues/12249) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Hidden states processor

### Issue 正文摘录

### Motivation. Since #10674, vLLM uses Pooler to extract hidden states from the model and convert them to embeddings, class probabilities, and so on. However, this is still not user-friendly enough: - We have separate model runners for generative and pooling models. This complicates the effort to return hidden states alongside generated text (e.g.: #6165, #11397, #11577, #11606, #11905) - Setting the default Pooler based on downstream task only covers the common cases. It may be required to use `--override-pooler-config` which isn't that intuitive to use (e.g. #12085). Even so, we still lack support for custom processing of hidden states (e.g. #11065, #11881, #12162) ### Proposed Change. Similar to `LogitsProcessor` (#1469), we can pass a custom `HiddenStatesProcessor` in `SamplingParams` and `PoolingParams` to postprocess the hidden states and return them in the output. This provides maximum flexibility and enables the same model to be used for different downstream tasks. ```py # Note that we can use a different processor each time we call `llm.generate` outputs = llm.generate(..., sampling_params=SamplingParams(hidden_states_processor=...)) custom_outputs = outputs.hidden_state...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: t startup time, so it is excluded from model profiling. This may lead to OOM issues especially if the hidden states processor calls a significant portion of the model. ### Feedback Period. Around 2 weeks? See when I hav...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ation. Since #10674, vLLM uses Pooler to extract hidden states from the model and convert them to embeddings, class probabilities, and so on. However, this is still not user-friendly enough: - We have separate model run...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tes processor is not known at startup time, so it is excluded from model profiling. This may lead to OOM issues especially if the hidden states processor calls a significant portion of the model. ### Feedback Period. Ar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: so it is excluded from model profiling. This may lead to OOM issues especially if the hidden states processor calls a significant portion of the model. ### Feedback Period. Around 2 weeks? See when I have time to work o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
