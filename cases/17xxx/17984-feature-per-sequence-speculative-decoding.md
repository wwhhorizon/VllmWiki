# vllm-project/vllm#17984: [Feature]: Per-sequence speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#17984](https://github.com/vllm-project/vllm/issues/17984) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Per-sequence speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### **1. Problem** Currently, increasing batch size in vLLM's Speculative Decoding inference causes inefficiency. When using the LLaMA 1B SSM model on the LLaMA 70B Original model, a performance reversal occurs at Batchsize 32. In addition, when the _num_speculative_tokens_ (SL; speculative length) is large, the inefficiency increases further as the batch size increases (Fig. 2). vLLM was also aware of the need for optimization for this. (https://docs.google.com/document/d/1T-JaS2T1NRfdP51qzqpyakoCXxSXTtORppiwaj5asxA/edit?tab=t.0#heading=h.kk7dq05lc6q8) ### **2. Previous work in vLLM** To handle the increasing batch size in SD, vLLM has been performing the following tasks: Batch Expansion https://github.com/vllm-project/vllm/pull/3103 and MQA (Multi-Query Attention) Scorer ![Image](https://github.com/user-attachments/assets/d1585ce6-67f8-4650-b1e7-8182193aca37) "Batch expansion" expands the batch by the factor of k (num_speculative_tokens). Each original sequence + one proposal token become a separate sequence in the expanded batch for the target model's scoring pass. Because of the "expansion" it has drawn backs as it increases memory usage...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ulative Decoding inference causes inefficiency. When using the LLaMA 1B SSM model on the LLaMA 70B Original model, a performance reversal occurs at Batchsize 32. In addition, when the _num_speculative_tokens_ (SL; specu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Per-sequence speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch ### **1. Problem** Currently, increasing batch size in vLLM's Speculative Decoding inference causes inefficiency...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LLM's Speculative Decoding inference causes inefficiency. When using the LLaMA 1B SSM model on the LLaMA 70B Original model, a performance reversal occurs at Batchsize 32. In addition, when the _num_speculative_tokens_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: reasing batch size in vLLM's Speculative Decoding inference causes inefficiency. When using the LLaMA 1B SSM model on the LLaMA 70B Original model, a performance reversal occurs at Batchsize 32. In addition, when the _n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache;frontend_api;model_support;speculative_decoding attent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
