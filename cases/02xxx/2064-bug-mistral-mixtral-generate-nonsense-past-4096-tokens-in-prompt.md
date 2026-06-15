# vllm-project/vllm#2064: [BUG] Mistral/Mixtral generate nonsense past 4096 tokens in prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#2064](https://github.com/vllm-project/vllm/issues/2064) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] Mistral/Mixtral generate nonsense past 4096 tokens in prompt

### Issue 正文摘录

If the prompt contains more than 4k tokens, the model will begin generating nonsense. This seems to be true for both Mistral and Mixtral. I launched the engine at both 32k and 8k max model lengths for testing. Tested with the latest vllm release.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 096 tokens in prompt bug If the prompt contains more than 4k tokens, the model will begin generating nonsense. This seems to be true for both Mistral and Mixtral. I launched the engine at both 32k and 8k max model lengt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Mixtral. I launched the engine at both 32k and 8k max model lengths for testing. Tested with the latest vllm release.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
