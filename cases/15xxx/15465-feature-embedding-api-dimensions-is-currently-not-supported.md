# vllm-project/vllm#15465: [Feature]: Embedding API dimensions  is currently not supported.

| 字段 | 值 |
| --- | --- |
| Issue | [#15465](https://github.com/vllm-project/vllm/issues/15465) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Embedding API dimensions  is currently not supported.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed that after deploying the embedding model using vllm, the requests do not fully match the OpenAI format. This issue has always been there: ``` { "object": "error", "message": "dimensions is currently not supported", "type": "BadRequestError", "param": null, "code": 400 } ``` ### Alternatives My script: ``` vllm serve "/workspace/share_data/base_llms/bce-embedding-base_v1" \ --served-model-name "bce-embedding-base_v1" \ --task "embedding" \ --trust-remote-code \ --host "0.0.0.0" \ --port 8000 \ --dtype auto \ --gpu-memory-utilization 0.4 \ --kv-cache-dtype auto \ --enable-prefix-caching \ --tensor-parallel-size 1 \ --max-num-seqs 256 ``` vllm version: 0.7.2 ### Additional context I hope this feature can be added as soon as possible, as it will be immensely helpful for building the knowledge base. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: caching \ --tensor-parallel-size 1 \ --max-num-seqs 256 ``` vllm version: 0.7.2 ### Additional context I hope this feature can be added as soon as possible, as it will be immensely helpful for building the knowledge bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ture, motivation and pitch I noticed that after deploying the embedding model using vllm, the requests do not fully match the OpenAI format. This issue has always been there: ``` { "object": "error", "message": "dimensi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --trust-remote-code \ --host "0.0.0.0" \ --port 8000 \ --dtype auto \ --gpu-memory-utilization 0.4 \ --kv-cache-dtype auto \ --enable-prefix-caching \ --tensor-parallel-size 1 \ --max-num-seqs 256 ``` vllm version: 0.7....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: -port 8000 \ --dtype auto \ --gpu-memory-utilization 0.4 \ --kv-cache-dtype auto \ --enable-prefix-caching \ --tensor-parallel-size 1 \ --max-num-seqs 256 ``` vllm version: 0.7.2 ### Additional context I hope this featu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
