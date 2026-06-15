# vllm-project/vllm#15272: [Bug]: Inconsistent Output Based on Presence of chat_template Parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#15272](https://github.com/vllm-project/vllm/issues/15272) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent Output Based on Presence of chat_template Parameter

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following code produces different outputs if chat_template is passed, got `2+2=4.` if chat_template is not passed, got `嗯，用户问2+2等于多少，这看起来是一个很简单的问题。不过，作为刚开始学习数学的人，可能需要一步步来思考。首先，我 ...` Using the same chat template from the model config. [QwQ-32B Chat Template](https://huggingface.co/Qwen/QwQ-32B/blob/main/tokenizer_config.json#L230) ```Python chat_template="{%- if tools %}\n {{- ' system\\n' }}\n {%- if messages[0]['role'] == 'system' %}\n {{- messages[0]['content'] }}\n {%- else %}\n {{- '' }}\n {%- endif %}\n {{- \"\\n\\n# Tools\\n\\nYou may call one or more functions to assist with the user query.\\n\\nYou are provided with function signatures within XML tags:\\n \" }}\n {%- for tool in tools %}\n {{- \"\\n\" }}\n {{- tool | tojson }}\n {%- endfor %}\n {{- \"\\n \\n\\nFor each function call, return a json object with function name and arguments within XML tags:\\n \\n{\\\"name\\\": , \\\"arguments\\\": }\\n \\n\" }}\n{%- else %}\n {%- if messages[0]['role'] == 'system' %}\n {{- ' system\\n' + messages[0]['content'] + ' \\n' }}\n {%- endif %}\n{%- endif %}\n{%- for message in messages %}\n {%- if (message.role == \"user\") or...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d_generation_prompt %}\n {{- ' assistant\\n \\n' }}\n{%- endif %}\n" import openai model = "/kaggle/input/qwq-32b/transformers/qwq-32b/1" base_url = 'https://...ngrok-free.app/v1/' openai.api_key = "dummy" openai.base_u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ，作为刚开始学习数学的人，可能需要一步步来思考。首先，我 ...` Using the same chat template from the model config. [QwQ-32B Chat Template](https://huggingface.co/Qwen/QwQ-32B/blob/main/tokenizer_config.json#L230) ```Python chat_template="{%- if too...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: Inconsistent Output Based on Presence of chat_template Parameter bug;stale ### Your current environment ### 🐛 Describe the bug The following code produces different outputs if chat_template is passed, got `2+2=4.` i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
