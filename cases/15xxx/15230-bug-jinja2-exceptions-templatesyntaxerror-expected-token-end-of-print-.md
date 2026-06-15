# vllm-project/vllm#15230: [Bug]: jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got 'name'

| 字段 | 值 |
| --- | --- |
| Issue | [#15230](https://github.com/vllm-project/vllm/issues/15230) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got 'name'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When manually applying [QwQ-32B Chat Template](https://huggingface.co/Qwen/QwQ-32B/blob/main/tokenizer_config.json#L230), `TemplateSyntaxError` is raised. Why does it work when it uses `tokenizer.chat_template`? ```python chat_template = """ {%- if tools %} {{- ' system\n' }} {%- if messages[0]['role'] == 'system' %} {{- messages[0]['content'] }} {%- else %} {{- '' }} {%- endif %} {{- "\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatures within XML tags:\n " }} {%- for tool in tools %} {{- "\n" }} {{- tool | tojson }} {%- endfor %} {{- "\n \n\nFor each function call, return a json object with function name and arguments within XML tags:\n \n{\"name\": , \"arguments\": }\n \n" }} {%- else %} {%- if messages[0]['role'] == 'system' %} {{- ' system\n' + messages[0]['content'] + ' \n' }} {%- endif %} {%- endif %} {%- for message in messages %} {%- if (message.role == "user") or (message.role == "system" and not loop.first) %} {{- ' ' + message.role + '\n' + message.content + ' ' + '\n' }} {%- elif message.role == "assistant" and not message.tool_calls %} {%- set...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug When manually applying [QwQ-32B Chat Template](https://huggingface.co/Qwen/QwQ-32B/blob/main/tokenizer_config.json#L230), `TemplateSyntaxError` is raised. Why does it work when it uses `tokenizer.chat_t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: add_generation_prompt %} {{- ' assistant\n \n' }} {%- endif %} """ import jinja2 template = jinja2.Template(chat_template) print(template.render(messages=[{"role": "user", "content": "2+2=?"}])) ``` Changing " to ' line...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 129 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0]['role'] == 'system' %} {{- messages[0]['content'] }} {%- else %} {{- '' }} {%- endif %} {{- "\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatur...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
