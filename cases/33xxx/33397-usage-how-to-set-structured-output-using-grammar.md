# vllm-project/vllm#33397: [Usage]: How to set structured_output using grammar

| 字段 | 值 |
| --- | --- |
| Issue | [#33397](https://github.com/vllm-project/vllm/issues/33397) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to set structured_output using grammar

### Issue 正文摘录

### Your current environment How to set structured_output using grammar I tried the example in vLLM Doc using vllm v0.14.1 simplified_sql_grammar = """ root ::= select_statement select_statement ::= "SELECT " column " from " table " where " condition column ::= "col_1 " | "col_2 " table ::= "table_1 " | "table_2 " condition ::= column "= " number number ::= "1 " | "2 " """ completion = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": "Generate an SQL query to show the 'username' and 'email' from the 'users' table.", } ], extra_body={"structured_outputs": {"grammar": simplified_sql_grammar}}, ) print(completion.choices[0].message.content) BUT got the warning: The following fields were present in the request but ignored: {'extra_body'} AND the result seemed to be not influenced by response_format setting. How to set structured_output using grammar ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [doc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er ::= "1 " | "2 " """ completion = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": "Generate an SQL query to show the 'username' and 'email' from the 'users' table.", } ], extra_bod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to set structured_output using grammar usage;stale ### Your current environment How to set structured_output using grammar I tried the example in vLLM Doc using vllm v0.14.1 simplified_sql_grammar = """ roo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
