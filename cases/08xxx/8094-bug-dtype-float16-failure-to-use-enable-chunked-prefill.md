# vllm-project/vllm#8094: [Bug]: dtype float16 Failure to use enable-chunked-prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#8094](https://github.com/vllm-project/vllm/issues/8094) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: dtype float16 Failure to use enable-chunked-prefill

### Issue 正文摘录

### Your current environment ``` python3 -u -m vllm.entrypoints.openai.api_server --model /model/models/Meta-Llama-3.1-405B-Instruct-gptq-4bit --port xxxxxx --api-key xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -tp 16 --seed 7 --served-model-name Llama-3-405B-Instruct --dtype float16 --enable-chunked-prefill --max-num-batched-tokens 4096 --enforce-eager --gpu-memory-utilization 0.98 --tokenizer-pool-size 8 --block-size 32 --trust-remote-code --distributed-executor-backend ray --swap-space 8 --disable-custom-all-reduce --max-model-len 32768 ``` ### 🐛 Describe the bug ``` (RayWorkerWrapper pid=1335677, ip=23.248.165.188) ethod: /project/lib/Analysis/Allocation.cpp:47: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. (RayWorkerWrapper pid=1335677, ip=23.248.165.188) *** SIGABRT received at time=1725325639 on cpu 85 *** (RayWorkerWrapper pid=1335677, ip=23.248.165.188) PC: @ 0x7f1d16bb29fc (unknown) pthread_kill (RayWorkerWrapper pid=1335677, ip=23.248.165.188) @ 0x7f1d16b5e520 (unknown) (unknown) (RayWorkerWr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ut && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. (RayWorkerWrapper pid=1335677, ip=23.248.165.188) *** SIGABRT received at time=1725325639 on cpu 85...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: dtype float16 Failure to use enable-chunked-prefill bug;stale ### Your current environment ``` python3 -u -m vllm.entrypoints.openai.api_server --model /model/models/Meta-Llama-3.1-405B-Instruct-gptq-4bit --port...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 5.188) ethod: /project/lib/Analysis/Allocation.cpp:47: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere())...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pool-size 8 --block-size 32 --trust-remote-code --distributed-executor-backend ray --swap-space 8 --disable-custom-all-reduce --max-model-len 32768 ``` ### 🐛 Describe the bug ``` (RayWorkerWrapper pid=1335677, ip=23.248...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: dtype float16 Failure to use enable-chunked-prefill bug;stale ### Your current environment ``` python3 -u -m vllm.entrypoints.openai.api_server --model /model/models/Meta-Llama-3.1-405B-Instruct-gptq-4bit --port...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
