# vllm-project/vllm#15944: [Bug]: CI flake - v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output bug Something isn't working ci/build v1

| 字段 | 值 |
| --- | --- |
| Issue | [#15944](https://github.com/vllm-project/vllm/issues/15944) |
| 状态 | closed |
| 标签 | bug;ci/build;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CI flake - v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output bug Something isn't working ci/build v1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` [2025-04-02T06:06:31Z] =================================== FAILURES =================================== -- | [2025-04-02T06:06:31Z] _ test_structured_output[mistralai/Ministral-8B-Instruct-2410-guidance:disable-any-whitespace-auto] _ | [2025-04-02T06:06:31Z] | [2025-04-02T06:06:31Z] monkeypatch = | [2025-04-02T06:06:31Z] sample_json_schema = {'properties': {'age': {'type': 'integer'}, 'name': {'type': 'string'}, 'skills': {'items': {'type': 'string'}, 'type'...ition'], 'type': 'object'}, 'type': 'array'}}, 'required': ['name', 'age', 'skills', 'work_history'], 'type': 'object'} | [2025-04-02T06:06:31Z] unsupported_json_schema = {'properties': {'email': {'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$', 'type': 'string'}, 'grade': ...[a-z]{1,10}$', 'type': 'string'}, 'type': 'array'}}, 'required': ['score', 'grade', 'email', 'tags'], 'type': 'object'} | [2025-04-02T06:06:31Z] sample_sql_ebnf = '\nroot ::= select_statement\nselect_statement ::= "SELECT" column "from" table "where" condition\ncolumn ::= "col_1" \| "col_2"\ntable ::= "table_1" \| "table_2"\ncondition ::= column "=" number\nnumber ::= "1" \| "2"\n' |...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t_structured_output bug Something isn't working ci/build v1 bug;ci/build;stale ### Your current environment ### 🐛 Describe the bug ``` [2025-04-02T06:06:31Z] =================================== FAILURES ================...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: CI flake - v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output bug Something isn't working ci/build v1 bug;ci/build;stale ### Your current environment ### 🐛 Describe the bug ``` [2025-04-02T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: CI flake - v1/entrypoints/llm/test_struct_output_generate.py::test_structured_output bug Something isn't working ci/build v1 bug;ci/build;stale ### Your current environment ### 🐛 Describe the bug ``` [2025-04-02T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pt', 'C++', 'C#', 'PHP', ...] | [2025-04-02T06:06:31Z] guided_decoding_backend = 'guidance:disable-any-whitespace' | [2025-04-02T06:06:31Z] tokenizer_mode = 'auto', model_name = 'mistralai/Ministral-8B-Instruct-2410' |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 956c ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
