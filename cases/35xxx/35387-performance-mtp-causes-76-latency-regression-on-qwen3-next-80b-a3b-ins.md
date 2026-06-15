# vllm-project/vllm#35387: [Performance]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#35387](https://github.com/vllm-project/vllm/issues/35387) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8

### Issue 正文摘录

### Environment - **vLLM commit:** `ee59a7c61574485cf4ddbc6037ba557941be5c56` (main branch) - **Model:** `Qwen/Qwen3-Next-80B-A3B-Instruct-FP8` - **Config:** TP=4, max-model-len=262144, num_speculative_tokens=2 ### Benchmark Results **Baseline (no MTP, no prefix caching):** ```bash vllm bench latency --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tensor-parallel-size 4 --max-model-len 262144 ``` - Avg latency: 0.894s - P50: 0.895s, P90: 0.901s, P99: 0.907s **With MTP:** ```bash vllm bench latency --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tensor-parallel-size 4 --max-model-len 262144 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` - Avg latency: 1.578s (**+76.5%**) - P50: 1.573s, P90: 1.621s, P99: 1.670s **With MTP + prefix caching:** ```bash vllm bench latency --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tensor-parallel-size 4 --max-model-len 262144 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' \ --enable-prefix-caching ``` - Avg latency: 1.629s (**+82.2%**) - P50: 1.628s, P90: 1.673s, P99: 1.691s ### Notes I suspect this regression is related to copying `num_accepted_tokens` back to CPU before we d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Red Hat Enterprise Linux 9.6 (Plow) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ==========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.10.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8 performance ### Environment - **vLLM commit:** `ee59a7c61574485cf4ddbc6037ba557941be5c56` (main branch) - **Model:** `Qwen/Qwen3-Next-8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mance]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8 performance ### Environment - **vLLM commit:** `ee59a7c61574485cf4ddbc6037ba557941be5c56` (main branch) - **Model:** `Qwen/Qwen3-Next-80B-A3B-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8 performance ### Environment - **vLLM commit:** `ee59a7c61574485cf4ddbc6037ba557941be5c56` (main branch) - **Model:** `Qwen/Qwen3-Next-8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
