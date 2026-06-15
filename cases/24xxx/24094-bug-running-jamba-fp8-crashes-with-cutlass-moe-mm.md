# vllm-project/vllm#24094: [Bug]: Running Jamba FP8 crashes with cutlass_moe_mm

| 字段 | 值 |
| --- | --- |
| Issue | [#24094](https://github.com/vllm-project/vllm/issues/24094) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running Jamba FP8 crashes with cutlass_moe_mm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Jamba Large FP8 version (I suppose it happens on other MOE FP8 models) Im getting an error from `cutlass_moe_mm` onm high load and reltaively large context (30K input) on v0.10.1.X ```python VLLM_TRACE_FUNCTION=1 \ CUDA_LAUNCH_BLOCKING=1 \ VLLM_USE_V1=0 \ vllm bench latency \ --model ai21labs/AI21-Jamba-Mini-1.7-FP8 \ --input-len 31500 \ --output-len 128 \ --batch-size 1 \ --num-iters-warmup 3 \ --num-iters 3 ``` This is the trace log ```bash Warmup iterations: 33% 1/3 [01:01 [rank0]: sys.exit(main()) [rank0]: ^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 54, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/benchmark/latency.py", line 21, in cmd [rank0]: main(args) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/benchmarks/latency.py", line 142, in main [rank0]: run_to_completion(profile_dir=None) [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/benchmarks/latency.py", line 135, in run_to_completion [rank0]: llm_generate() [rank0]: File "/usr/local/lib/python3.12/dist-pac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent environment ### 🐛 Describe the bug When running Jamba Large FP8 version (I suppose it happens on other MOE FP8 models) Im getting an error from `cutlass_moe_mm` onm high load and reltaively large context (30K input)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Running Jamba FP8 crashes with cutlass_moe_mm bug;stale ### Your current environment ### 🐛 Describe the bug When running Jamba Large FP8 version (I suppose it happens on other MOE FP8 models) Im getting an error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Running Jamba FP8 crashes with cutlass_moe_mm bug;stale ### Your current environment ### 🐛 Describe the bug When running Jamba Large FP8 version (I suppose it happens on other MOE FP8 models) Im getting an error...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Running Jamba FP8 crashes with cutlass_moe_mm bug;stale ### Your current environment ### 🐛 Describe the bug When running Jamba Large FP8 version (I suppose it happens on other MOE FP8 models) Im getting an error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: _TRACE_FUNCTION=1 \ CUDA_LAUNCH_BLOCKING=1 \ VLLM_USE_V1=0 \ vllm bench latency \ --model ai21labs/AI21-Jamba-Mini-1.7-FP8 \ --input-len 31500 \ --output-len 128 \ --batch-size 1 \ --num-iters-warmup 3 \ --num-iters 3 `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
