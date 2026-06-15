# vllm-project/vllm#3097: [v0.3.3] Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#3097](https://github.com/vllm-project/vllm/issues/3097) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.3.3] Release Tracker

### Issue 正文摘录

**ETA**: Feb 29th - Mar 1st ## Major changes * StarCoder2 support * Performance optimization and LoRA support for Gemma * Performance optimization for MoE kernel * 2/3/8-bit GPTQ support * [Experimental] AWS Inferentia2 support ## PRs to be merged before the release - [x] #2330 #2223 - [ ] ~~#2761~~ - [x] #2819 - [x] #3087 #3099 - [x] #3089

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: es * StarCoder2 support * Performance optimization and LoRA support for Gemma * Performance optimization for MoE kernel * 2/3/8-bit GPTQ support * [Experimental] AWS Inferentia2 support ## PRs to be merged before the re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es * StarCoder2 support * Performance optimization and LoRA support for Gemma * Performance optimization for MoE kernel * 2/3/8-bit GPTQ support * [Experimental] AWS Inferentia2 support ## PRs to be merged before the re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
