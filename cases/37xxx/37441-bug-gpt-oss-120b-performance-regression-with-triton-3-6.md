# vllm-project/vllm#37441: [Bug]: GPT OSS 120B performance regression with Triton 3.6

| 字段 | 值 |
| --- | --- |
| Issue | [#37441](https://github.com/vllm-project/vllm/issues/37441) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT OSS 120B performance regression with Triton 3.6

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running GPT OSS 120B on H200 GPU become slower with upgrade to vLLM 0.17.0 compared to 0.16.0 with ~20% latency regression. After profiling execution with nsys, found that 0.17.1 uses new kernel `_reduce` in 0.17.1 (Triton 3.6) vs `reduce_grouped` in 0.16 (Triton 3.5), which are coming from Triton MoE kernels. The `_reduce` takes 6.4 times longer than `reduce_grouped`. Then we tried to revert back Triton 3.5 kernels while keeping vLLM 0.17.1 and updating `gpt_oss_triton_kernels_moe.py` to always `use_legacy_triton_kernels = True` ([link](https://github.com/vllm-project/vllm/blob/releases/v0.17.0/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py#L55)), this recovered the previous GPT OSS performance fully. Running vLLM with: ``` vllm serve {PATH_TO_MODEL} --host 0.0.0.0 --port 8000 --served-model-name oss --tensor-parallel-size 2 --uvicorn_log_level error --max_num_seqs 2 --trust-remote-code --gpu-memory-utilization 0.9 --max-model-len 131072 --enable-chunked-prefill --max-num-batched-tokens 8192 --speculative-config.method eagle --speculative-config.num_speculative_tokens 3 --max-cudagraph-capture-size 4096 --ena...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 8: [Bug]: GPT OSS 120B performance regression with Triton 3.6 bug ### Your current environment ### 🐛 Describe the bug Running GPT OSS 120B on H200 GPU become slower with upgrade to vLLM 0.17.0 compared to 0.16.0 with ~20%...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ss_triton_kernels_moe.py` to always `use_legacy_triton_kernels = True` ([link](https://github.com/vllm-project/vllm/blob/releases/v0.17.0/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py#L55)), this re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ode --gpu-memory-utilization 0.9 --max-model-len 131072 --enable-chunked-prefill --max-num-batched-tokens 8192 --speculative-config.method eagle --speculative-config.num_speculative_tokens 3 --max-cudagraph-capture-size...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ) vs `reduce_grouped` in 0.16 (Triton 3.5), which are coming from Triton MoE kernels. The `_reduce` takes 6.4 times longer than `reduce_grouped`. Then we tried to revert back Triton 3.5 kernels while keeping vLLM 0.17.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: GPT OSS 120B performance regression with Triton 3.6 bug ### Your current environment ### 🐛 Describe the bug Running GPT OSS 120B on H200 GPU become slower with upgrade to vLLM 0.17.0 compared to 0.16.0 with ~20%...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
