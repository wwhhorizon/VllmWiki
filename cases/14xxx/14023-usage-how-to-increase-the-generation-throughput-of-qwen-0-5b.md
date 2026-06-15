# vllm-project/vllm#14023: [Usage]: How to increase the generation throughput of Qwen-0.5B

| 字段 | 值 |
| --- | --- |
| Issue | [#14023](https://github.com/vllm-project/vllm/issues/14023) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to increase the generation throughput of Qwen-0.5B

### Issue 正文摘录

### Your current environment I am currently utilizing vLLM serve to deploy the Qwen-0.5B model on an Nvidia H20 GPU. During this process, I've observed that the GPU utilization as reported by nvidia-smi remains at approximately 70%. Despite attempts to optimize the vLLM engine parameters, significant improvements have yet to be seen. Below are the strategies I have explored: - Enabled Prefix Caching (--enable-prefix-caching): Achieved a cache hit rate of 90%, but this did not translate into improved throughput. - Adjusted --max_num_batched_tokens: The default setting of 2048 tokens seems optimal; increasing it to 10240 did not yield any noticeable benefits. - Activated Chunked Prefill (--enable-chunked-prefill): This adjustment offered slight performance enhancements. - Optimized Request Batch Size: A batch size of around 64 or 128 appears ideal, whereas larger sizes tend to degrade performance. - Deployed Two Models Simultaneously on a Single GPU: Attempting to run two models concurrently did not enhance performance and even resulted in minor degradation. Given these findings, do you have any other recommendations for further optimization? my final serve arguments `vllm serve /mn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: dm/qiujiaji/ckpts/summary-v5-tag-0.5B-20250226_215441/checkpoint-83035 --dtype=bfloat16 --gpu-memory-utilization=0.95 --port=8080 --max-model-len 2000 --disable-log-requests --enable-chunked-prefill` ![Image](https://gi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: is process, I've observed that the GPU utilization as reported by nvidia-smi remains at approximately 70%. Despite attempts to optimize the vLLM engine parameters, significant improvements have yet to be seen. Below are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to increase the generation throughput of Qwen-0.5B usage;stale ### Your current environment I am currently utilizing vLLM serve to deploy the Qwen-0.5B model on an Nvidia H20 GPU. During this process, I've...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: How to increase the generation throughput of Qwen-0.5B usage;stale ### Your current environment I am currently utilizing vLLM serve to deploy the Qwen-0.5B model on an Nvidia H20 GPU. During this process, I've...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
