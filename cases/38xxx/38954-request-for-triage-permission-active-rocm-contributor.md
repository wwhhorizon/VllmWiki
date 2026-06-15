# vllm-project/vllm#38954: Request for triage permission — active ROCm contributor

| 字段 | 值 |
| --- | --- |
| Issue | [#38954](https://github.com/vllm-project/vllm/issues/38954) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Request for triage permission — active ROCm contributor

### Issue 正文摘录

Hi maintainers, I'm requesting **triage** permission on this repository. I'm an active ROCm/AMD contributor with 12+ open PRs covering AITER integration, MLA attention backends, MXFP4 quantization, and GLM-5 model support on MI355X. ### Why triage permission? - **Request reviewers** on my own PRs — currently blocked because fork-contributors cannot use `requested_reviewers` API - **Manage labels** to keep ROCm-related PRs properly categorized - **Faster review cycles** for customer-facing work (e.g. GLM-5 on MI355X) Triage permission is read-only for code — it only allows managing issues/PRs metadata (labels, reviewers, milestones). ### My contribution history Open PRs (partial list): - #38665 — Dual-stream shared experts + GLM-5 MXFP4/FP8 support - #36855 — Sparse MLA head repeat fix for < 16 heads - #38947 — AITER MLA prefill kernel integration - #37800 — MXFP4 linear method + shared expert fusion - #37353 — Skip head repeat for AITER MLA decode - #36851 — Sequence parallelism for AMD GPUs - #36425 — AITER fused allreduce + RMSNorm - #36227 — Cascade attention for AITER FlashAttention - #36092 — AITER ops fake impl fixes GitHub: [@ChuanLi1101](https://github.com/ChuanLi1101) cc...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: or with 12+ open PRs covering AITER integration, MLA attention backends, MXFP4 quantization, and GLM-5 model support on MI355X. ### Why triage permission? - **Request reviewers** on my own PRs — currently blocked becaus...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: epository. I'm an active ROCm/AMD contributor with 12+ open PRs covering AITER integration, MLA attention backends, MXFP4 quantization, and GLM-5 model support on MI355X. ### Why triage permission? - **Request reviewers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Request for triage permission — active ROCm contributor rocm Hi maintainers, I'm requesting **triage** permission on this repository. I'm an active ROCm/AMD contributor with 12+ open PRs covering AITER integration, MLA
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Request for triage permission — active ROCm contributor rocm Hi maintainers, I'm requesting **triage** permission on this repository. I'm an active ROCm/AMD contributor with 12+ open PRs covering AITER integration, MLA...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: hy triage permission? - **Request reviewers** on my own PRs — currently blocked because fork-contributors cannot use `requested_reviewers` API - **Manage labels** to keep ROCm-related PRs properly categorized - **Faster...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
