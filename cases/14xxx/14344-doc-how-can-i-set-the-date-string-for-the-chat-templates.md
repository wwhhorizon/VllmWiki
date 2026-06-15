# vllm-project/vllm#14344: [Doc]: How can I set the date_string for the chat templates

| 字段 | 值 |
| --- | --- |
| Issue | [#14344](https://github.com/vllm-project/vllm/issues/14344) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: How can I set the date_string for the chat templates

### Issue 正文摘录

### 📚 The doc issue Hello everyone, I use the chat_template like this, similar to [tool_chat_template_llama3.1_json.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.1_json.jinja): ``` {%- if not date_string is defined %} {%- set date_string = "26 Jul 2024" %} {%- endif %} ``` and I call the model like this: ``` client.chat.completions.create( messages=messages, model=model, temperature=0.0, max_completion_tokens=300, stream=True, tools=tools, tool_choice=tool_choice ) ``` So, now my question: How can I set the date_string variable? Thank you for your help. Best regards, Felix ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: yone, I use the chat_template like this, similar to [tool_chat_template_llama3.1_json.jinja](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_llama3.1_json.jinja): ``` {%- if not date_string is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
