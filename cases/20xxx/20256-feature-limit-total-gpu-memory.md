# vllm-project/vllm#20256: [Feature]: Limit total GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#20256](https://github.com/vllm-project/vllm/issues/20256) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Limit total GPU memory

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Even with appropriate arguments to lower memory usage specified, as suggested in docs: ``` --enforce-eager --max-model-len=8192 --max-num-batched-tokens=8192 --max-num-seqs=16 ``` the rest of the GPU memory still gets eaten up by KV cache, so even when running a tiny 1B model that needs 3 GB of VRAM, VLLM takes 71GB on A100 to run this model. This makes VLLM an impractical solution for mixed-GPU clusters. Suggestions: - add flag to specify max gpu memory in absolute units - add ability to explicitly limit/disable KV cache ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: when running a tiny 1B model that needs 3 GB of VRAM, VLLM takes 71GB on A100 to run this model. This makes VLLM an impractical solution for mixed-GPU clusters. Suggestions: - add flag to specify max gpu memory in absol...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Limit total GPU memory feature request;stale ### 🚀 The feature, motivation and pitch Even with appropriate arguments to lower memory usage specified, as suggested in docs: ``` --enforce-eager --max-model-len=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Limit total GPU memory feature request;stale ### 🚀 The feature, motivation and pitch Even with appropriate arguments to lower memory usage specified, as suggested in docs: ``` --enforce-eager --max-model-len=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion and pitch Even with appropriate arguments to lower memory usage specified, as suggested in docs: ``` --enforce-eager --max-model-len=8192 --max-num-batched-tokens=8192 --max-num-seqs=16 ``` the rest of the GPU memo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: memory usage specified, as suggested in docs: ``` --enforce-eager --max-model-len=8192 --max-num-batched-tokens=8192 --max-num-seqs=16 ``` the rest of the GPU memory still gets eaten up by KV cache, so even when running...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
