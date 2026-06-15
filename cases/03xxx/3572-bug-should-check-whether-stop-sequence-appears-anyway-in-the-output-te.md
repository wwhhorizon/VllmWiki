# vllm-project/vllm#3572: [Bug]: Should check whether stop sequence appears anyway in the output text instead of just endswith

| 字段 | 值 |
| --- | --- |
| Issue | [#3572](https://github.com/vllm-project/vllm/issues/3572) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Should check whether stop sequence appears anyway in the output text instead of just endswith

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Using mistral-7b-instruct model, and prompt `Here is the English alphabet: ABC`, temperature 0, stop sequence `DE`, model would still output `DEFGHIJKLMNOPQRSTUVWXYZ...` this is because `DEF` is a token, and stop sequence is only checked with `endswith` https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L717 I think instead of we should check string contain.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n collect_env.py` ``` ### 🐛 Describe the bug Using mistral-7b-instruct model, and prompt `Here is the English alphabet: ABC`, temperature 0, stop sequence `DE`, model would still output `DEFGHIJKLMNOPQRSTUVWXYZ...` this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
