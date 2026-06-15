# vllm-project/vllm#12250: [Feature]: loading model from remote KV store such as Redis

| 字段 | 值 |
| --- | --- |
| Issue | [#12250](https://github.com/vllm-project/vllm/issues/12250) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: loading model from remote KV store such as Redis

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, loading models in `vLLM` takes such a long time, up to several minutes. 3 steps are needed: 1. Downloading model files from `S3` or `HuggingFace` or your own repo. 2. Reading, decoding and loading `Tensor` from disk file into CPU memory. 3. Copy `Tensor` into GPU memory. I wonder whether it is a good idea to introduce a new class named `RemoteModelLoader` in `model_loader.py`. By doing so, we just need to store model tensors and metadata into remote database only once. After that, we could load models from remote database directly, and also faster than traditional way since local disk is not involved. Besides `Redis`, I noticed that some companies and organization are working on RDMA-based KV database, which is much faster theoretically. And step 3 is not necessary if using `GDR`. Those databases in the future may also become available by `RemoteModelLoader`, similar as how `Redis` is used. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pag...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: loading model from remote KV store such as Redis feature request;stale ### 🚀 The feature, motivation and pitch Currently, loading models in `vLLM` takes such a long time, up to several minutes. 3 steps are ne...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: loading model from remote KV store such as Redis feature request;stale ### 🚀 The feature, motivation and pitch Currently, loading models in `vLLM` takes such a long time, up to several minutes. 3 steps are ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: d loading `Tensor` from disk file into CPU memory. 3. Copy `Tensor` into GPU memory. I wonder whether it is a good idea to introduce a new class named `RemoteModelLoader` in `model_loader.py`. By doing so, we just need...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: `model_loader.py`. By doing so, we just need to store model tensors and metadata into remote database only once. After that, we could load models from remote database directly, and also faster than traditional way since...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
