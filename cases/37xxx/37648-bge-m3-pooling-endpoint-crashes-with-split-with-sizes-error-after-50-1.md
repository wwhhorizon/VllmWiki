# vllm-project/vllm#37648: BGE-M3 /pooling endpoint crashes with split_with_sizes error after ~50-100 requests

| 字段 | 值 |
| --- | --- |
| Issue | [#37648](https://github.com/vllm-project/vllm/issues/37648) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BGE-M3 /pooling endpoint crashes with split_with_sizes error after ~50-100 requests

### Issue 正文摘录

## Description The `/pooling` endpoint for BGE-M3 (`BgeM3EmbeddingModel`) crashes after approximately 50-100 sequential requests. Both `embed` (dense) and `token_classify` (sparse) tasks are affected. The error kills the engine entirely (`EngineDeadError`), requiring a full container restart. Single requests work fine. The crash occurs only after accumulating multiple requests. ## Environment - **vLLM versions tested:** `v0.15.1` and `latest` (v0.17.x as of 2026-03-20) - **Model:** `BAAI/bge-m3` with `--hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}'` - **GPU:** NVIDIA B200 (183GB) - **Docker image:** `vllm/vllm-openai:v0.15.1` and `vllm/vllm-openai:latest` ## Steps to Reproduce ```bash # Launch docker run --gpus '"device=0"' -d --network host \ --entrypoint vllm vllm/vllm-openai:v0.15.1 \ serve BAAI/bge-m3 --host 0.0.0.0 --port 9001 \ --trust-remote-code \ --hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}' # Wait for model to load, then send ~100 sequential requests for i in $(seq 1 100); do curl -s http://localhost:9001/pooling \ -H "Content-Type: application/json" \ -d '{"model": "BAAI/bge-m3", "task": "embed", "input": ["test sentence number '$i'"]}' > /dev/...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ** `vllm/vllm-openai:v0.15.1` and `vllm/vllm-openai:latest` ## Steps to Reproduce ```bash # Launch docker run --gpus '"device=0"' -d --network host \ --entrypoint vllm vllm/vllm-openai:v0.15.1 \ serve BAAI/bge-m3 --host...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 7.x as of 2026-03-20) - **Model:** `BAAI/bge-m3` with `--hf-overrides '{"architectures": ["BgeM3EmbeddingModel"]}'` - **GPU:** NVIDIA B200 (183GB) - **Docker image:** `vllm/vllm-openai:v0.15.1` and `vllm/vllm-openai:lat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: urs only after accumulating multiple requests. ## Environment - **vLLM versions tested:** `v0.15.1` and `latest` (v0.17.x as of 2026-03-20) - **Model:** `BAAI/bge-m3` with `--hf-overrides '{"architectures": ["BgeM3Embed...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uests ## Description The `/pooling` endpoint for BGE-M3 (`BgeM3EmbeddingModel`) crashes after approximately 50-100 sequential requests. Both `embed` (dense) and `token_classify` (sparse) tasks are affected. The error ki...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: after accumulating multiple requests. ## Environment - **vLLM versions tested:** `v0.15.1` and `latest` (v0.17.x as of 2026-03-20) - **Model:** `BAAI/bge-m3` with `--hf-overrides '{"architectures": ["BgeM3EmbeddingModel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
