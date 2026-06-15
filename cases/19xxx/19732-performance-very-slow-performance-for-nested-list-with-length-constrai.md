# vllm-project/vllm#19732: [Performance]: very slow performance for nested list with length constraints

| 字段 | 值 |
| --- | --- |
| Issue | [#19732](https://github.com/vllm-project/vllm/issues/19732) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: very slow performance for nested list with length constraints

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance See this report at [xgrammar issue](https://github.com/mlc-ai/xgrammar/issues/339). - env: - vllm: `0.9.1` - xgrammar: `0.1.19` - Structured json schema: ``` class Table(BaseModel): content: conlist(conlist(str, min_length=5, max_length=10), min_length=5, max_length=10) json_schema = Table.model_json_schema() ``` This schema leads to very low thoughput (< 3 tokens/s). Is there any way to improve performance? ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance See this report at [xgrammar issue](https://github.com/mlc-ai/xgrammar/issues/339). - en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 1` - xgrammar: `0.1.19` - Structured json schema: ``` class Table(BaseModel): content: conlist(conlist(str, min_length=5, max_length=10), min_length=5, max_length=10) json_schema = Table.model_json_schema() ``` This sch...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
