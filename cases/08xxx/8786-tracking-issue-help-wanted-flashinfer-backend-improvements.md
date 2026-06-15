# vllm-project/vllm#8786: [Tracking Issue][Help Wanted]: FlashInfer backend improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#8786](https://github.com/vllm-project/vllm/issues/8786) |
| 状态 | closed |
| 标签 | help wanted;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue][Help Wanted]: FlashInfer backend improvements

### Issue 正文摘录

This issue tracks the progress and roadmap of integrating new FlashInfer kernels and enabling more vLLM features in FlashInfer backend. Items listed in Milestone 1 is a part of re-arch #8779 . If you want any features available in FlashInfer backend but not listed here, or if you're interested in taking items, please feel free to comment. ## Milestone 1 - [ ] Unify FlashInfer backend with multi-level cascade attention kernel. #8132 - [ ] Support in-batch prefix sharing with 2-level cascade attention. @raywanb - [ ] Support prefix caching. ## Milestone 2 - [ ] Support chunked prefill. - [ ] Support FP8 E4M3 kv-cache with kv scale. - [ ] Support batch expansion in speculative decoding. - [ ] Integrate RaggedTensor kernel. cc @yzh119 @LiuXiaoxuanPKU @raywanb @simon-mo @WoosukKwon @pavanimajety

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: racking Issue][Help Wanted]: FlashInfer backend improvements help wanted;stale This issue tracks the progress and roadmap of integrating new FlashInfer kernels and enabling more vLLM features in FlashInfer backend. Item...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Tracking Issue][Help Wanted]: FlashInfer backend improvements help wanted;stale This issue tracks the progress and roadmap of integrating new FlashInfer kernels and enabling more vLLM features in FlashInfer backend. It...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ix caching. ## Milestone 2 - [ ] Support chunked prefill. - [ ] Support FP8 E4M3 kv-cache with kv scale. - [ ] Support batch expansion in speculative decoding. - [ ] Integrate RaggedTensor kernel. cc @yzh119 @LiuXiaoxua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tures in FlashInfer backend. Items listed in Milestone 1 is a part of re-arch #8779 . If you want any features available in FlashInfer backend but not listed here, or if you're interested in taking items, please feel fr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: g. ## Milestone 2 - [ ] Support chunked prefill. - [ ] Support FP8 E4M3 kv-cache with kv scale. - [ ] Support batch expansion in speculative decoding. - [ ] Integrate RaggedTensor kernel. cc @yzh119 @LiuXiaoxuanPKU @ray...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
