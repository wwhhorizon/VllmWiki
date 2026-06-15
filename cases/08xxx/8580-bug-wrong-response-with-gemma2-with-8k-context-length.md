# vllm-project/vllm#8580: [Bug]: Wrong Response with Gemma2 with 8k context length

| 字段 | 值 |
| --- | --- |
| Issue | [#8580](https://github.com/vllm-project/vllm/issues/8580) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wrong Response with Gemma2 with 8k context length

### Issue 正文摘录

serving gemma2-9b on 4 GPUs with 8k context length. I disabled the sliding window and enable flashinfer backend, however when I send a long prompt I got weird responses with repeated same first sentences!! example: - prompt is to answer a question given a paper content. - response: > "content": "\n\nThe paper you'\n\nLet me know if you'\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have any other questions about the paper.\n\nLet me know if you have a...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 4 GPUs with 8k context length. I disabled the sliding window and enable flashinfer backend, however when I send a long prompt I got weird responses with repeated same first sentences!! example: - prompt is to answer a q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Wrong Response with Gemma2 with 8k context length bug serving gemma2-9b on 4 GPUs with 8k context length. I disabled the sliding window and enable flashinfer backend, however when I send a long prompt I got weird...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Wrong Response with Gemma2 with 8k context length bug serving gemma2-9b on 4 GPUs with 8k context length. I disabled the sliding window and enable flashinfer backend, however when I send a long prompt I got weird...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
