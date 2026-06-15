# vllm-project/vllm#14682: [Bug]: Phi-4-mini function calling support

| 字段 | 值 |
| --- | --- |
| Issue | [#14682](https://github.com/vllm-project/vllm/issues/14682) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-4-mini function calling support

### Issue 正文摘录

### 🐛 Describe the bug ```bash vllm serve microsoft/Phi-4-mini-instruct --enable-auto-tool-choice --tool-call-parser llama3_json --chat-template /Users/lokinfey/Desktop/NIM/phi-4-mini.jinja ``` I have set phi-4-mini.jinja,but can not generation phi-4-mini function calling ```txt {%- if messages %} {%- if system_message or tools %} {%- if system_message %} {{ system_message }} {%- endif %} You are a helpful assistant using the provided tools. In addition to plain text responses, you can choose to call one or more of the provided functions. Use the following rule to decide when to call a function: * if the response can be generated from your internal knowledge (e.g., as in the case of queries like "What is the capital of Poland?"), do so * if you need external information that can be obtained by calling one or more of the provided functions, generate function calls If you decide to call functions: * prefix function calls with functools marker (no closing marker required) * all function calls should be generated in a single JSON list formatted as [{"name": [function name], "arguments": [function arguments as JSON]}, ...] * follow the provided JSON schema. Do not hallucinate arguments...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: crosoft/Phi-4-mini-instruct --enable-auto-tool-choice --tool-call-parser llama3_json --chat-template /Users/lokinfey/Desktop/NIM/phi-4-mini.jinja ``` I have set phi-4-mini.jinja,but can not generation phi-4-mini functio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: call one or more of the provided functions. Use the following rule to decide when to call a function: * if the response can be generated from your internal knowledge (e.g., as in the case of queries like "What is the ca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: {%- endif %} {%- endif %} {%- endfor %} {%- else %} {%- if system_message %} {{ system_message }} {%- endif %} {%- if prompt %} {{ prompt }} {%- endif %} {%- endif %} {{ response }} {%- if response %} {% endif %} ``` ca...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
