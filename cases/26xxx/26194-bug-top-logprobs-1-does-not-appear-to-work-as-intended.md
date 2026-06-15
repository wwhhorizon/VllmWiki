# vllm-project/vllm#26194: [Bug]: `top_logprobs: -1` does not appear to work as intended

| 字段 | 值 |
| --- | --- |
| Issue | [#26194](https://github.com/vllm-project/vllm/issues/26194) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `top_logprobs: -1` does not appear to work as intended

### Issue 正文摘录

### 🐛 Describe the bug This was enabled in https://github.com/vllm-project/vllm/pull/25031 with unit test here: https://github.com/vllm-project/vllm/blob/main/tests/entrypoints/openai/test_chat_echo.py. Logprobs for all tokens should be returned in this case but it appears that `top_logprobs` contains 0 entries in the API responses. The test doesn't actually check the length of that field. I have some concern that if this was working correctly, the response payload would be huge. We probably want to change the test to only generate one or two tokens. cc @chaunceyjiang

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: was enabled in https://github.com/vllm-project/vllm/pull/25031 with unit test here: https://github.com/vllm-project/vllm/blob/main/tests/entrypoints/openai/test_chat_echo.py. Logprobs for all tokens should be returned i...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
