# vllm-project/vllm#19097: [RFC]: Response format extensions for structured outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#19097](https://github.com/vllm-project/vllm/issues/19097) |
| 状态 | closed |
| 标签 | structured-output;RFC;stale;v1 |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Response format extensions for structured outputs

### Issue 正文摘录

### Motivation. Currently, users can provide additional constraints format via `extra_body` in OpenAI client: ```python from enum import Enum from pydantic import BaseModel from openai import OpenAI simplified_sql_grammar = """ root ::= select_statement select_statement ::= "SELECT " column " from " table " where " condition column ::= "col_1 " | "col_2 " table ::= "table_1 " | "table_2 " condition ::= column "= " number number ::= "1 " | "2 " """ prompt = ( "Generate an SQL query to show the 'username' and 'email'" "from the 'users' table." ) completion = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": prompt, } ], extra_body={"guided_grammar": simplified_sql_grammar}, ``` This also applies with `guided_json`, `structural_tag`, `guided_regex`. While this is pretty convenient for most developers, these fields are still using v0 terminology wrt guided decoding. With the upcoming v0 deprecation, I think it is the time to have a usage update with this pattern. ### Proposed Change. OpenAI already recommends users to use `response_format` with [json_schema](https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat) Given that we alrea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Response format extensions for structured outputs structured-output;RFC;stale;v1 ### Motivation. Currently, users can provide additional constraints format via `extra_body` in OpenAI client: ```python from enum i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nstraints format via `extra_body` in OpenAI client: ```python from enum import Enum from pydantic import BaseModel from openai import OpenAI simplified_sql_grammar = """ root ::= select_statement select_statement ::= "S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ges ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Response format extensions for structured outputs structured-output;RFC;stale;v1 ### Motivation. Currently, users can provide additional constraints format via `extra_body` in OpenAI client: ```python from enum import E...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ructural_tag` via `response_format` ([example](https://docs.vllm.ai/en/latest/examples/online_serving/openai_chat_completion_structured_outputs_structural_tag.html?h=structural+tags)), I propose an extension to `respons...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
