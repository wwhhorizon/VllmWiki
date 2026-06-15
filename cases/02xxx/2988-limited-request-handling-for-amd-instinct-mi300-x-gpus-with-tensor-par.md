# vllm-project/vllm#2988: Limited Request Handling for AMD Instinct MI300 X GPUs with Tensor Parallelism > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#2988](https://github.com/vllm-project/vllm/issues/2988) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Limited Request Handling for AMD Instinct MI300 X GPUs with Tensor Parallelism > 1

### Issue 正文摘录

Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.1](https://github.com/vllm-project/vllm/tree/v0.3.1) 2. Build the Dockerfile.rocm dockerfile with instructions from [Option 3: Build from source with docker -Installation with ROCm](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm) build command: ```sh docker build -f Dockerfile.rocm -t vllm-rocm . ``` 3. The vLLM serving command used: ```sh python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-chat-hf --dtype float16 --tensor-parallel-size 8 ``` 4. Used Apache Bench for testing with 256 concurrent requests The error below: ```sh INFO 02-21 10:31:34 metrics.py:161] Avg prompt throughput: 352.5 tokens/s, Avg generation throughput: 55.2 tokens/s, Running: 67 reqs, Swapped: 0 reqs, Pending: 130 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0% Memory access fault by GPU node-2 (Agent handle: 0x9f73a80) on address 0x7ef9eb704000. Reason: Unknown. *** SIGABRT received at time=1708511498 on cpu 37 *** PC: @ 0x7f0f63c8400b (unknown) raise @ 0x7f0f63fa1420 4224 (unknown) @ 0x7f0e76ca147c (unknown) (unknown) [2024-02-21 10:31:38,596 E 725390 7416...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ng for AMD Instinct MI300 X GPUs with Tensor Parallelism > 1 rocm Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.1](https://github.com/vllm-project/vllm/tree/v0.3.1) 2. Build the Dockerfile.rocm docke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Limited Request Handling for AMD Instinct MI300 X GPUs with Tensor Parallelism > 1 rocm Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.1](https://github.com/vllm-project/vllm/tree/v0.3.1) 2. Build the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mand used: ```sh python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-chat-hf --dtype float16 --tensor-parallel-size 8 ``` 4. Used Apache Bench for testing with 256 concurrent requests The error...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-chat-hf --dtype float16 --tensor-parallel-size 8 ``` 4. Used Apache Bench for testing with 256 concurrent requests The error below: ```sh INFO 02-21 10:31:3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: om source with docker -Installation with ROCm](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm) build command: ```sh docker build -f Dockerfile.rocm -t vllm-rocm . ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
