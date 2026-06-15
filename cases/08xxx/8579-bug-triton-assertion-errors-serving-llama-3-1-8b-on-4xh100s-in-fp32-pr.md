# vllm-project/vllm#8579: [Bug]: Triton assertion errors serving Llama-3.1-8b on 4xH100s in FP32 precision

| 字段 | 值 |
| --- | --- |
| Issue | [#8579](https://github.com/vllm-project/vllm/issues/8579) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton assertion errors serving Llama-3.1-8b on 4xH100s in FP32 precision

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to serve Llama-3.1-8b with model parallelism on 4 H100 GPUs with FP32 precision, and get the following Triton assertion error. ``` python: /project/lib/Analysis/Allocation.cpp:47: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. ``` This only seems to happen for FP32, but not FP16, BFP16 or FP8. This can be reproduced with the following script. Server side: ```bash vllm serve \ meta-llama/Meta-Llama-3.1-8B-Instruct \ --api_key test \ --tensor_parallel_size 4 \ --dtype float32 ``` Client side: ```bash import asyncio import aiohttp HOST_URL = "http://localhost:8000" API_KEY = "test" MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct" openai_request_headers = { "Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}", } timeout = aiohttp.ClientTimeout( total=60*60*24, connect=60*60*24, sock_read=60*60*24, sock_connect=60*60*24, ceil_threshold=60*60*24, ) prompts = [ "Hey, this is a prompt" ]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Bug]: Triton assertion errors serving Llama-3.1-8b on 4xH100s in FP32 precision bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to serve Llama-3.1-8b with model par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Triton assertion errors serving Llama-3.1-8b on 4xH100s in FP32 precision bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to serve Llama-3.1-8b with model pa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: failed. ``` This only seems to happen for FP32, but not FP16, BFP16 or FP8. This can be reproduced with the following script. Server side: ```bash vllm serve \ meta-llama/Meta-Llama-3.1-8B-Instruct \ --api_key test \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: API_KEY = "test" MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct" openai_request_headers = { "Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}", } timeout = aiohttp.ClientTimeout( total=60*60*24, co...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: Triton assertion errors serving Llama-3.1-8b on 4xH100s in FP32 precision bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to serve Llama-3.1-8b with model pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
