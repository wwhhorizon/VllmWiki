# vllm-project/vllm#16911: [Bug]: guided_grammar example syntax does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#16911](https://github.com/vllm-project/vllm/issues/16911) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: guided_grammar example syntax does not work

### Issue 正文摘录

### Your current environment I'm using vllm hosted on a K8s instance and was not able to execute the environment collection python file there. But this is the error I get: ### 🐛 Describe the bug I'm trying to use guided grammar as found in [documentation](https://docs.vllm.ai/en/latest/features/structured_outputs.html). All examples about structured outputs worked as presented but the one with EBNF. I tried to remove the tabstops in front of the lines, to rename the start node to root but it did not help. ``` wrong_simplified_sql_grammar = """ ?start: select_statement ?select_statement: "SELECT " column_list " FROM " table_name ?column_list: column_name ("," column_name)* ?table_name: identifier ?column_name: identifier ?identifier: /[a-zA-Z_][a-zA-Z0-9_]*/ """ prompt = ("Generate an SQL query to show the 'username' and 'email'" "from the 'users' table.") completion = client.chat.completions.create( model="Qwen/Qwen2.5-7B", messages=[{ "role": "user", "content": prompt, }], extra_body={ "guided_grammar": wrong_simplified_sql_grammar }, ) print(completion.choices[0].message.content) ``` Because I got some messages about wrong escape sequences in other examples I added an r in front...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: om the 'users' table.") completion = client.chat.completions.create( model="Qwen/Qwen2.5-7B", messages=[{ "role": "user", "content": prompt, }], extra_body={ "guided_grammar": wrong_simplified_sql_grammar }, ) print(com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: guided_grammar example syntax does not work bug;structured-output;stale ### Your current environment I'm using vllm hosted on a K8s instance and was not able to execute the environment collection python file ther...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: use guided grammar as found in [documentation](https://docs.vllm.ai/en/latest/features/structured_outputs.html). All examples about structured outputs worked as presented but the one with EBNF. I tried to remove the tab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
