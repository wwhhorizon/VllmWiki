# vllm-project/vllm#15077: [Doc]: new attention layer

| 字段 | 值 |
| --- | --- |
| Issue | [#15077](https://github.com/vllm-project/vllm/issues/15077) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: new attention layer

### Issue 正文摘录

### 📚 The doc issue [https://docs.vllm.ai/en/latest/contributing/model/basic.html#new-model-basic](url) > Currently, vLLM supports the basic multi-head attention mechanism and its variant with rotary positional embeddings. If your model employs a different attention mechanism, you will need to implement a new attention layer in vLLM. Can you explain in detail how to implement a new attention layer in vllm, mainly how the kv cache should be done to be compatible with vllm? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ](url) > Currently, vLLM supports the basic multi-head attention mechanism and its variant with rotary positional embeddings. If your model employs a different attention mechanism, you will need to implement a new atten...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: in detail how to implement a new attention layer in vllm, mainly how the kv cache should be done to be compatible with vllm? ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ;stale ### 📚 The doc issue [https://docs.vllm.ai/en/latest/contributing/model/basic.html#new-model-basic](url) > Currently, vLLM supports the basic multi-head attention mechanism and its variant with rotary positional e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: new attention layer documentation;stale ### 📚 The doc issue [https://docs.vllm.ai/en/latest/contributing/model/basic.html#new-model-basic](url) > Currently, vLLM supports the basic multi-head attention mechanism...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ayer documentation;stale ### 📚 The doc issue [https://docs.vllm.ai/en/latest/contributing/model/basic.html#new-model-basic](url) > Currently, vLLM supports the basic multi-head attention mechanism and its variant with r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
