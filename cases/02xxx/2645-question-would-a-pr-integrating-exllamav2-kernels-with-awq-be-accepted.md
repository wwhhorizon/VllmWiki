# vllm-project/vllm#2645: Question: Would a PR integrating ExLlamaV2 kernels with AWQ be accepted?

| 字段 | 值 |
| --- | --- |
| Issue | [#2645](https://github.com/vllm-project/vllm/issues/2645) |
| 状态 | closed |
| 标签 | performance;feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: Would a PR integrating ExLlamaV2 kernels with AWQ be accepted?

### Issue 正文摘录

Recently, ExLlamaV2 kernels were introduced into AutoAWQ. We can instantly map the AWQ packed weights to be compatible with ExLlama, and it runs decoding about 20% faster. # Performance Note that the gap in prefilling has recently been closed, so the main benefit would be during decoding. ### GEMM (AWQ kernel) | Batch Size | Prefill Length | Decode Length | Prefill tokens/s | Decode tokens/s | Memory (VRAM) | | -- | -- | -- | -- | -- | -- | | 1 | 64 | 64 | 316\.842 | 156\.038 | 4\.78 GB (20.20%) | | 1 | 128 | 128 | 4898\.86 | 154\.977 | 4\.79 GB (20.27%) | | 1 | 256 | 256 | 5366\.24 | 151\.31 | 4\.81 GB (20.35%) | | 1 | 512 | 512 | 5239\.46 | 144\.517 | 4\.85 GB (20.51%) | | 1 | 1024 | 1024 | 4573\.25 | 132\.849 | 4\.93 GB (20.83%) | | 1 | 2048 | 2048 | 3859\.42 | 114\.249 | 5\.55 GB (23.48%) | | 8 | 64 | 64 | 1733\.1 | 1176\.07 | 4\.83 GB (20.42%) | | 8 | 128 | 128 | 5359\.34 | 1167\.19 | 4\.90 GB (20.72%) | | 8 | 256 | 256 | 5145\.94 | 1130\.84 | 5\.03 GB (21.26%) | | 8 | 512 | 512 | 4802\.91 | 1070\.9 | 5\.67 GB (23.98%) | | 8 | 1024 | 1024 | 4391\.24 | 972\.987 | 7\.84 GB (33.17%) | | 8 | 2048 | 2048 | 3643 | 822\.977 | 16\.82 GB (71.12%) | ### ExLlamaV2 (AWQ mapped to ExLlama...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: integrating ExLlamaV2 kernels with AWQ be accepted? performance;feature request;stale Recently, ExLlamaV2 kernels were introduced into AutoAWQ. We can instantly map the AWQ packed weights to be compatible with ExLlama,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Question: Would a PR integrating ExLlamaV2 kernels with AWQ be accepted? performance;feature request;stale Recently, ExLlamaV2 kernels were introduced into AutoAWQ. We can instantly map the AWQ packed weights to be comp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: recently been closed, so the main benefit would be during decoding. ### GEMM (AWQ kernel) | Batch Size | Prefill Length | Decode Length | Prefill tokens/s | Decode tokens/s | Memory (VRAM) | | -- | -- | -- | -- | -- | -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
