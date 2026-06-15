# vllm-project/vllm#1231: Chinese and emojis not supported via OpenAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#1231](https://github.com/vllm-project/vllm/issues/1231) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Chinese and emojis not supported via OpenAI API

### Issue 正文摘录

Top-left is vLLM. I don't see any way with OpenAI API version of vLLM to get actual tokens. TGI (top-middle) handles this already on its own end. OpenAI itself has no issues for same exact code. ![image](https://github.com/vllm-project/vllm/assets/2249614/404be205-f5ac-4e1a-b9f2-2d042397b7e6) In h2oGPT for native torch we do this: https://github.com/h2oai/h2ogpt/blob/549340ce78f1ecfeaec16b9f1e3b1428bec3776b/src/gen.py#L3079-L3097 vLLM could do similar.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed via OpenAI API Top-left is vLLM. I don't see any way with OpenAI API version of vLLM to get actual tokens. TGI (top-middle) handles this already on its own end. OpenAI itself has no issues for same exact code. ![imag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
