# vllm-project/vllm#39519: [Tracking] DFlash: Update DFlash speculators test checkpoint with a stronger model

| 字段 | 值 |
| --- | --- |
| Issue | [#39519](https://github.com/vllm-project/vllm/issues/39519) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking] DFlash: Update DFlash speculators test checkpoint with a stronger model

### Issue 正文摘录

## Update | Checkpoint | Layers | Draft Vocab | Mean AL | First-token AR | |---|---|---|---|---| | **`nm-testing/dflash-qwen3-8b-speculators` (updated)** | **5** | **32000 (reduced)** | **3.45** | **79.4%** | | `z-lab/Qwen3-8B-DFlash-b16` (reference) | 5 | 151936 (full) | 3.70 | 75.6% | ## Summary The current DFlash speculators E2E test (`tests/v1/spec_decode/test_speculators_dflash.py`) uses `nm-testing/dflash-qwen3-8b-speculators`, a 3-layer checkpoint trained with limited data. Its acceptance rate is low (mean AL ~1.84, first-token AR ~47.5%), which limits test coverage for later-token code paths in speculative decoding. Introduced in #38300. ## TODO Replace the checkpoint with a stronger model. ## Reference comparison (GSM8k-5shot, same target model Qwen3-8B) | Checkpoint | Layers | Mean AL | First-token AR | |---|---|---|---| | `nm-testing/dflash-qwen3-8b-speculators` (current test) | 3 | 1.84 | 47.5% | | `z-lab/Qwen3-8B-DFlash-b16` (reference) | 5 | 3.70 | 75.6% | cc @shanjiaz @benchislett ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://d...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t checkpoint with a stronger model bug ## Update | Checkpoint | Layers | Draft Vocab | Mean AL | First-token AR | |---|---|---|---|---| | **`nm-testing/dflash-qwen3-8b-speculators` (updated)** | **5** | **32000 (reduced...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eplace the checkpoint with a stronger model. ## Reference comparison (GSM8k-5shot, same target model Qwen3-8B) | Checkpoint | Layers | Mean AL | First-token AR | |---|---|---|---| | `nm-testing/dflash-qwen3-8b-speculato...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cking] DFlash: Update DFlash speculators test checkpoint with a stronger model bug ## Update | Checkpoint | Layers | Draft Vocab | Mean AL | First-token AR | |---|---|---|---|---| | **`nm-testing/dflash-qwen3-8b-specula...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Tracking] DFlash: Update DFlash speculators test checkpoint with a stronger model bug ## Update | Checkpoint | Layers | Draft Vocab | Mean AL | First-token AR | |---|---|---|---|---| | **`nm-testing/dflash-qwen3-8b-spe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
