# vllm-project/vllm#24109: [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1

| 字段 | 值 |
| --- | --- |
| Issue | [#24109](https://github.com/vllm-project/vllm/issues/24109) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `deepseek-ai/DeepSeek-R1-0528` with `VLLM_USE_FLASHINFER_MOE_FP8=1` on B200 system, vllm fails with the following error: ``` (VllmWorker TP4 pid=3020312) ERROR 09-02 08:16:39 [multiproc_executor.py:574] assert layer.custom_routing_function == Llama4MoE.custom_routing_function, \ (VllmWorker TP4 pid=3020312) ERROR 09-02 08:16:39 [multiproc_executor.py:574] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker TP4 pid=3020312) ERROR 09-02 08:16:39 [multiproc_executor.py:574] AssertionError: FusedMoE flashinfer kernels are only supported for Llama4 ``` If we set `VLLM_FLASHINFER_MOE_BACKEND="latency"`, then this error does not occur. So it only happens for the default value which is `VLLM_FLASHINFER_MOE_BACKEND="throughput"`. Here are the commands to reproduce it: Run server: ``` VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve deepseek-ai/DeepSeek-R1-0528 \ --no-enable-prefix-caching \ --tensor-parallel-size 8 \ --enable-expert-parallel \ ``` Run client: ``` python ./benchmarks/benchmark_serving.py \ --model deepseek-ai/DeepSeek-R1-0528 \ --dataset-name random \ --random-input-len 1200 \ --random-outpu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1 bug;stale ### Your current environment ### 🐛 Describe the bug When running `deepseek-ai/DeepSeek-R1-0528` with `VLLM_USE_FLASHINFER_MOE_FP8=1` on B200 sys...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1 bug;stale ### Your current environment ### 🐛 Describe the bug When running `deepseek-ai/DeepSeek-R1-0528` with `VLLM_USE_FLASHINFER_MOE_FP8=1` on B200 sys...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er pid=3019416) INFO 09-02 08:15:35 [api_server.py:1882] vLLM API server version 0.10.2rc2.dev26+g38ba061f6.d20250902 (APIServer pid=3019416) INFO 09-02 08:15:35 [utils.py:328] non-default args: {'model_tag': 'deepseek-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1 bug;stale ### Your current environment ### 🐛 Describe the bug When running `deepseek-ai/DeepSeek-R1-0528` with `VLLM_USE_FLASHINFER_MOE_FP8=1` on B200 sys...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Bug]: DeepSeek fails with enabled VLLM_USE_FLASHINFER_MOE_FP8=1 bug;stale ### Your current environment ### 🐛 Describe the bug When running `deepseek-ai/DeepSeek-R1-0528` with `VLLM_USE_FLASHINFER_MOE_FP8=1` on B200 sys...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
