# vllm-project/vllm#42520: [Performance]: performance drop between versions 0.19.1 and 0.20.1 for embedding models

| 字段 | 值 |
| --- | --- |
| Issue | [#42520](https://github.com/vllm-project/vllm/issues/42520) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: performance drop between versions 0.19.1 and 0.20.1 for embedding models

### Issue 正文摘录

### Proposal to improve performance Noticed a performance drop between version 0.19.1 and 0.20.1 both in terms of troughput and latency. VLLM was deployed using bellow command: python3 -m vllm.entrypoints.openai.api_server --model BAAI/bge-base-en-v1.5 --dtype $VLLM_DTYPE --download-dir /data --host 0.0.0.0 --port 8108 and those variables: EMBEDDING_VLLM_MODEL_NAME: BAAI/bge-base-en-v1.5 EMBEDDING_VLLM_PORT: "8108" VLLM_DTYPE: bfloat16 VLLM_TARGET_DEVICE: cpu XDG_CACHE_HOME: /tmp First think that shows up in warnings and seems easy fix: When loading VLLM I can see: **vllm-embedding (APIServer pid=1) WARNING 05-13 06:34:59 [utils.py:134] To make v1/embeddings API fast, please install orjson by `pip install orjson`** can we update image and install this pkg? Results of comparison (different root cause that missing orjson) on in section Report of performance regression. ### Report of performance regression comparing version 0.19.1 and 0.20.1 deployed: python3 -m vllm.entrypoints.openai.api_server --model BAAI/bge-base-en-v1.5 --dtype $VLLM_DTYPE --download-dir /data --host 0.0.0.0 --port 8108 and those variables: EMBEDDING_VLLM_MODEL_NAME: BAAI/bge-base-en-v1.5 EMBEDDING_VLLM_PORT: "...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n3 -m vllm.entrypoints.openai.api_server --model BAAI/bge-base-en-v1.5 --dtype $VLLM_DTYPE --download-dir /data --host 0.0.0.0 --port 8108 and those variables: EMBEDDING_VLLM_MODEL_NAME: BAAI/bge-base-en-v1.5
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ce drop between version 0.19.1 and 0.20.1 both in terms of troughput and latency. VLLM was deployed using bellow command: python3 -m vllm.entrypoints.openai.api_server --model BAAI/bge-base-en-v1.5 --dtype $VLLM_DTYPE -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Performance]: performance drop between versions 0.19.1 and 0.20.1 for embedding models performance ### Proposal to improve performance Noticed a performance drop between version 0.19.1 and 0.20.1 both in terms of troug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ance]: performance drop between versions 0.19.1 and 0.20.1 for embedding models performance ### Proposal to improve performance Noticed a performance drop between version 0.19.1 and 0.20.1 both in terms of troughput and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
