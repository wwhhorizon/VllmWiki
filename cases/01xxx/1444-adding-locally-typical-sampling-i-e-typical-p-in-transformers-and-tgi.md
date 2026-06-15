# vllm-project/vllm#1444: Adding Locally Typical Sampling (i.e. typical_p in transformers and TGI)

| 字段 | 值 |
| --- | --- |
| Issue | [#1444](https://github.com/vllm-project/vllm/issues/1444) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Adding Locally Typical Sampling (i.e. typical_p in transformers and TGI)

### Issue 正文摘录

Hello. First of all, thank you for your wonderful work. I was curious if adding [locally typical sampling](https://arxiv.org/abs/2202.00666) was on the roadmap. If not, would you be interested in a PR adding the functionality? I think adding `typical_p` will be trivial, but wanted to ask first before working on it. Personally, I'm having great success with `typical_p` in `transformers` and `text-generation-inference`. I want to switch to vLLM but I can't go back to `top_p`.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
