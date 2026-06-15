# vllm-project/vllm#33307: [Bug]: Latency spikes at input_len=1024 with batch_size=16 (TP1 & TP2)

| 字段 | 值 |
| --- | --- |
| Issue | [#33307](https://github.com/vllm-project/vllm/issues/33307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Latency spikes at input_len=1024 with batch_size=16 (TP1 & TP2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM inference with **output_len=256**, I observe a **sharp, isolated latency anomaly at input_len=1024 with batch_size=16**, reproducible on both **TP=1 and TP=2**. This shows up as: - **mean ITL / mean TPOT spike** at (batch=16, input_len=1024) vs neighboring input lengths (512, 2048) - **mean TTFT discontinuity** - **p99 TTFT extreme outlier** (very large spike) at that single point This behavior is unexpected because latency should scale smoothly/monotonically with input length and batch size (or at least not show a single-point cliff). ### Observed results (from my sweep plots) At output_len=256: - batch=16, TP=1: - mean_itl_ms jumps to ~**101ms** at input_len=1024 (vs ~86–90ms elsewhere) - p99_ttft_ms spikes to ~**7200ms** at input_len=1024 (very large outlier) - batch=16, TP=2: - mean_itl_ms increases to ~**187ms** at input_len=1024 (vs ~182–185ms elsewhere) - p99_ttft_ms also spikes at input_len=1024 (~**2.6s** range) - Other batch sizes (1/32/64) do NOT show the same single-point behavior at input_len=1024 Plots attached: mean_itl_ms, mean_tpot_ms, mean_ttft_ms, p99_tpot_ms, p99_ttft_ms vs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: isolated latency anomaly at input_len=1024 with batch_size=16**, reproducible on both **TP=1 and TP=2**. This shows up as: - **mean ITL / mean TPOT spike** at (batch=16, input_len=1024) vs neighboring input lengths (512...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ug]: Latency spikes at input_len=1024 with batch_size=16 (TP1 & TP2) bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM inference with **output_len=256**, I observe a **sh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Latency spikes at input_len=1024 with batch_size=16 (TP1 & TP2) bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM inference with **output_len=256**, I observe a **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t single point This behavior is unexpected because latency should scale smoothly/monotonically with input length and batch size (or at least not show a single-point cliff). ### Observed results (from my sweep plots) At...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: at that single point This behavior is unexpected because latency should scale smoothly/monotonically with input length and batch size (or at least not show a single-point cliff). ### Observed results (from my sweep plot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
