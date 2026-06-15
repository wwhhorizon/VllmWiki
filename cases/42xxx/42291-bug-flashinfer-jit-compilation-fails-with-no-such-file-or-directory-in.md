# vllm-project/vllm#42291: [Bug]: FlashInfer JIT compilation fails with "No such file or directory" in v0.20.1/v0.20.2  (docker)

| 字段 | 值 |
| --- | --- |
| Issue | [#42291](https://github.com/vllm-project/vllm/issues/42291) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer JIT compilation fails with "No such file or directory" in v0.20.1/v0.20.2  (docker)

### Issue 正文摘录

**Title:** `[Bug] Official Docker Image v0.20.1/v0.20.2 fails to start: FlashInfer headers missing in JIT compilation` **Description:** The official Docker image `vllm/vllm-openai:v0.20.2` (and likely `v0.20.1`) fails to start due to FlashInfer JIT compilation errors. The engine cannot find essential header files like `flashinfer/page.cuh` and `flashinfer/attention/prefill.cuh`. This is a **regression** compared to `vllm/vllm-openai:v0.20.0`, which starts and runs successfully with the same configuration. Since I am using the official pre-built Docker image, this suggests a packaging or build issue in the newer images where FlashInfer C++ headers are either missing or not correctly exposed to the compiler. **Environment:** - **VLLM Version:** 0.20.1 / 0.20.2 - **Hardware:** NVIDIA GeForce RTX 2080 Ti (Compute Capability 7.5) - **CUDA Version:** 13.0 (Driver 580.95.05) - **Docker Image:** vllm/vllm-openai:v0.20.2 - **Note:** The same configuration works fine with vllm/vllm-openai:v0.20.0. **Reproduction Steps:** 1. Pull the official image: ```bash docker pull vllm/vllm-openai:v0.20.2 ``` 2. Run the container with a model that triggers FlashInfer (e.g., Qwen, Llama) and specific KV...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: compilation fails with "No such file or directory" in v0.20.1/v0.20.2 (docker) bug **Title:** `[Bug] Official Docker Image v0.20.1/v0.20.2 fails to start: FlashInfer headers missing in JIT compilation` **Description:**...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mmand: > --model=/models/Qwen3.6-27B-AWQ --dtype=float16 --tensor-parallel-size=2 --kv-cache-dtype=fp8_e5m2 --enable-chunked-prefill --enable-prefix-caching --max-model-len=262144
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: m/vllm-openai:v0.20.0`, which starts and runs successfully with the same configuration. Since I am using the official pre-built Docker image, this suggests a packaging or build issue in the newer images where FlashInfer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt:** - **VLLM Version:** 0.20.1 / 0.20.2 - **Hardware:** NVIDIA GeForce RTX 2080 Ti (Compute Capability 7.5) - **CUDA Version:** 13.0 (Driver 580.95.05) - **Docker Image:** vllm/vllm-openai:v0.20.2 - **Note:** The same...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: r with a model that triggers FlashInfer (e.g., Qwen, Llama) and specific KV cache settings: ```yaml version: "3" services: vllm-openai: runtime: nvidia image: vllm/vllm-openai:v0.20.2 command: > --model=/models/Qwen3.6-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
