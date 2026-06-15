# vllm-project/vllm#19554: [Bug]: vLLM fails to initialize Qwen3-32B model with AttributeError during profile_run with >=v0.9.X

| 字段 | 值 |
| --- | --- |
| Issue | [#19554](https://github.com/vllm-project/vllm/issues/19554) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to initialize Qwen3-32B model with AttributeError during profile_run with >=v0.9.X

### Issue 正文摘录

### Your current environment ## 🐛 Describe the bug When attempting to run Qwen3-32B with vLLM 0.9.1, the initialization fails during the profile_run phase with an AttributeError. The error occurs during the dummy forward pass when vLLM tries to determine available memory. This happens with tensor parallelism enabled across 2 GPUs. ## Reproduction Steps: 1. Using the vLLM OpenAI API server container: ```bash docker pull vllm/vllm-openai:v0.9.1 ``` 2. Run the container with the following configuration: ```bash docker run --gpus all \ -e NCCL_CUMEM_ENABLE=1 \ -e NCCL_DEBUG=INFO \ -e TORCH_DISTRIBUTED_DEBUG=INFO \ -e VLLM_LOG_LEVEL=DEBUG \ --shm-size=32g \ vllm/vllm-openai:v0.9.1 \ --model Qwen/Qwen3-32B \ --tensor-parallel-size 2 \ --max-model-len 32768 \ --max-seq-len-to-capture 32768 \ --enable-lora \ --max-lora-rank 32 \ --compilation-config '{"debug_dump_path":"/tmp/vllm_debug"}' ``` Hardware requirements: - 2x NVIDIA H100 GPUs (80GB each) - 128GB system memory - 32 CPU cores ## Error message: ``` ERROR 06-12 05:43:37 [core.py:515] RuntimeError: Worker failed with error ''NoneType' object has no attribute 'dict_getitem'', please check the stack trace above for the root cause Deta...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: roduction Steps: 1. Using the vLLM OpenAI API server container: ```bash docker pull vllm/vllm-openai:v0.9.1 ``` 2. Run the container with the following configuration: ```bash docker run --gpus all \ -e NCCL_CUMEM_ENABLE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: M tries to determine available memory. This happens with tensor parallelism enabled across 2 GPUs. ## Reproduction Steps: 1. Using the vLLM OpenAI API server container: ```bash docker pull vllm/vllm-openai:v0.9.1 ``` 2....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM fails to initialize Qwen3-32B model with AttributeError during profile_run with >=v0.9.X bug ### Your current environment ## 🐛 Describe the bug When attempting to run Qwen3-32B with vLLM 0.9.1, the initializ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ug]: vLLM fails to initialize Qwen3-32B model with AttributeError during profile_run with >=v0.9.X bug ### Your current environment ## 🐛 Describe the bug When attempting to run Qwen3-32B with vLLM 0.9.1, the initializat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
