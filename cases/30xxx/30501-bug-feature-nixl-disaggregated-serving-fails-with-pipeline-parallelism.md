# vllm-project/vllm#30501: [Bug]/[Feature]:NIXL Disaggregated Serving Fails with Pipeline Parallelism (PP > 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#30501](https://github.com/vllm-project/vllm/issues/30501) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8 |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]/[Feature]:NIXL Disaggregated Serving Fails with Pipeline Parallelism (PP > 1)

### Issue 正文摘录

### Your current environment | Component | Value | |-----------|-------| | vLLM Version | 0.11.0 (via Dynamo 0.7.0 runtime) | | Python | 3.12 | | CUDA | 12.x | | Hardware | 2× H100 80GB nodes (8 GPUs each) per worker | | Model | `deepseek-ai/DeepSeek-R1-0528` (685B parameters, FP8) | | Deployment | Kubernetes with NVIDIA Dynamo | ### 🐛 Describe the bug ## Problem Description When running disaggregated inference with: - `--tensor-parallel-size 8` - `--pipeline-parallel-size 2` - `--is-decode-worker` on decode worker - `--is-prefill-worker` on prefill worker The model loads successfully and both workers report "ready". However, **the first inference request fails** with a NIXL handshake error. ## Minimal Reproduction ### Prefill Worker Launch ```bash python3 -m vllm.entrypoints.openai.api_server \ --model deepseek-ai/DeepSeek-R1-0528 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --is-prefill-worker \ --gpu-memory-utilization 0.9 \ --max-model-len 131072 ``` ### Decode Worker Launch ```bash python3 -m vllm.entrypoints.openai.api_server \ --model deepseek-ai/DeepSeek-R1-0528 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --is-decode-worker \ --gpu-memory-utiliza...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment | Component | Value | |-----------|-------| | vLLM Version | 0.11.0 (via Dynamo 0.7.0 runtime) | | Python | 3.12 | | CUDA | 12.x | | Hardware | 2× H100 80GB nodes (8 GPUs each) per worker | | Model |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]/[Feature]:NIXL Disaggregated Serving Fails with Pipeline Parallelism (PP > 1) bug ### Your current environment | Component | Value | |-----------|-------| | vLLM Version | 0.11.0 (via Dynamo 0.7.0 runtime) | | Pyt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ith: - `--tensor-parallel-size 8` - `--pipeline-parallel-size 2` - `--is-decode-worker` on decode worker - `--is-prefill-worker` on prefill worker The model loads successfully and both workers report "ready". However, *...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: per worker | | Model | `deepseek-ai/DeepSeek-R1-0528` (685B parameters, FP8) | | Deployment | Kubernetes with NVIDIA Dynamo | ### 🐛 Describe the bug ## Problem Description When running disaggregated inference with: - `-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: e ID ``` ## Why This Matters DeepSeek-R1-0528 with FP8 requires ~640GB GPU memory: - 1 node × 8 H100 (80GB each) = 640GB → **No room for KV cache** - 2 nodes × 8 H100 = 1.28TB → **Sufficient for inference** Without PP=2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
