# vllm-project/vllm#43301: [Hybrid SSM] Investigate accuracy divergence between `mamba_chunk_scan` and `selective_state_update` kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#43301](https://github.com/vllm-project/vllm/issues/43301) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;gemm_linear;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | gemm;kernel |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Hybrid SSM] Investigate accuracy divergence between `mamba_chunk_scan` and `selective_state_update` kernels

### Issue 正文摘录

## Context PR #43186 lowered the gsm8k accuracy threshold for `ibm-granite/granite-4.0-h-tiny` under NIXL PD disagg after #42430 rerouted the D-side 1-token recompute from `mamba_chunk_scan_combined_varlen` to `selective_state_update` (SSU). The two kernels produce different bf16 outputs due (supposedly) different reduction orders: - `mamba_chunk_scan_combined_varlen` goes through bf16 matmul with intermediate bf16 casts (`tl.dot`) - `selective_state_update` keeps the SSM step in fp32 throughout As noted in [this comment](https://github.com/vllm-project/vllm/pull/43186#issuecomment-2893988543), this seems like a large accuracy drop for something meant to be algebraically equivalent. ## Goal Investigate the kernel-level numerical divergence **in isolation** to: 1. **Quantify the magnitude**: Run both kernels on identical inputs for a single prompt (prefill + decode) and measure the output divergence (max abs diff, relative error distribution). 2. **Determine hardware dependence**: Test on at least **Ampere (A100)** and **Hopper (H100)** to see if the divergence magnitude or direction is architecture-dependent. 3. **Recommend a fix or acceptable tolerance**: Based on findings, eithe...

## 现有链接修复摘要

#42430 [Bugfix] mamba: run single-token extends as decodes | #43186 [CI] Lower granite-4.0-h-tiny gsm8k threshold for Hybrid SSM NixlConnector PD accuracy tests (4 GPUs)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Hybrid SSM] Investigate accuracy divergence between `mamba_chunk_scan` and `selective_state_update` kernels ## Context PR #43186 lowered the gsm8k accuracy threshold for `ibm-granite/granite-4.0-h-tiny` under NIXL PD d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Hybrid SSM] Investigate accuracy divergence between `mamba_chunk_scan` and `selective_state_update` kernels ## Context PR #43186 lowered the gsm8k accuracy threshold for `ibm-granite/granite-4.0-h-tiny` under NIXL PD d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n` to `selective_state_update` (SSU). The two kernels produce different bf16 outputs due (supposedly) different reduction orders: - `mamba_chunk_scan_combined_varlen` goes through bf16 matmul with intermediate bf16 cast...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e magnitude**: Run both kernels on identical inputs for a single prompt (prefill + decode) and measure the output divergence (max abs diff, relative error distribution). 2. **Determine hardware dependence**: Test on at...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Hybrid SSM] Investigate accuracy divergence between `mamba_chunk_scan` and `selective_state_update` kernels ## Context PR #43186 lowered the gsm8k accuracy threshold for `ibm-granite/granite-4.0-h-tiny` under NIXL PD d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42430](https://github.com/vllm-project/vllm/pull/42430) | mentioned | 0.45 | [Bugfix] mamba: run single-token extends as decodes | ences - pr that lowered threshold: #43186 - pr that rerouted to ssu: #42430 |
| [#43186](https://github.com/vllm-project/vllm/pull/43186) | mentioned | 0.45 | [CI] Lower granite-4.0-h-tiny gsm8k threshold for Hybrid SSM NixlConnector PD accuracy tests (4 GPUs) | hopper (h100) hardware. ## references - pr that lowered threshold: #43186 - pr that rerouted to ssu: #42430 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
