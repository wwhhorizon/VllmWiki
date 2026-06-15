# vllm-project/vllm#11118: [Bug]: grammar_is_likely_lark doesn't work correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#11118](https://github.com/vllm-project/vllm/issues/11118) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: grammar_is_likely_lark doesn't work correctly

### Issue 正文摘录

### Your current environment `grammar_is_likely_lark` identifies valid EBNF grammars as lark like. ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `grammar_is_likely_lark` is likely too loose, so even valid EBNF grammar is identified as "Lark like" grammar. For example: ``` root ::= (expr "=" term)+ expr ::= term ([-+*/] term)* term ::= num | "(" expr ")" num ::= [0-9]+ ``` This is a valid EBNF grammar, but since it has `|`, it is identified as lark like grammar. cc @mgoin ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rammar_is_likely_lark` identifies valid EBNF grammars as lark like. ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `grammar_is_likely_lark` is likely too loose, so even valid EBNF grammar is identified a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
