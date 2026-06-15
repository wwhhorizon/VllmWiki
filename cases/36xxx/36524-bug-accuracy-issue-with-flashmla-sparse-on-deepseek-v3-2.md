# vllm-project/vllm#36524: [Bug]: Accuracy Issue with FlashMLA Sparse on DeepSeek V3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#36524](https://github.com/vllm-project/vllm/issues/36524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Accuracy Issue with FlashMLA Sparse on DeepSeek V3.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran some eval for Deepseek V3.2 comparing flashMLA and flashinfer on both bf16 and fp8, and find that flashMLA has noticeably worse accuracy than flashinfer, particularly at fp8. Note flashMLA fp8 uses `fp8_ds_mla` whereas flashinfer uses the standard fp8 format, which could be the reason for its suboptimal performance. However, even for f16, the flashMLA performance is no better than flashinfer across the board. This may be indicative of potential bug in flashMLA integration. | KV Cache | Backend | Benchmark | pass@1 (avg-32) | majority@32 | pass@32 | | :--- | :--- | :--- | :---: | :---: | :---: | | **bf16** | **FlashMLA** | AIME25 | 88.33% | 93.33% | 93.33% | | | | GPQA-diamond | 82.89% | 85.86% | 96.46% | | **bf16** | **FlashInfer** | AIME25 | **90.83%** | 93.33% | **100.00%** | | | | GPQA-diamond | 83.14% | **87.63%** | **97.47%** | | **fp8_ds_mla** | **FlashMLA** | AIME25 | 81.98% | 88.33% | 90.00% | | | | GPQA-diamond | 78.55% | 81.82% | 94.95% | | **fp8** | **FlashInfer** | AIME25 | 89.17% | 93.33% | **100.00%** | | | | GPQA-diamond | **83.55%** | 86.36% | 96.46% | ### Before submitting a new issue... - [x] Make sure you...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Accuracy Issue with FlashMLA Sparse on DeepSeek V3.2 bug ### Your current environment ### 🐛 Describe the bug I ran some eval for Deepseek V3.2 comparing flashMLA and flashinfer on both bf16 and fp8, and find that...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: scribe the bug I ran some eval for Deepseek V3.2 comparing flashMLA and flashinfer on both bf16 and fp8, and find that flashMLA has noticeably worse accuracy than flashinfer, particularly at fp8. Note flashMLA fp8 uses...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: an some eval for Deepseek V3.2 comparing flashMLA and flashinfer on both bf16 and fp8, and find that flashMLA has noticeably worse accuracy than flashinfer, particularly at fp8. Note flashMLA fp8 uses `fp8_ds_mla` where...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Accuracy Issue with FlashMLA Sparse on DeepSeek V3.2 bug ### Your current environment ### 🐛 Describe the bug I ran some eval for Deepseek V3.2 comparing flashMLA and flashinfer on both bf16 and fp8, and find that...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: % | ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
