# vllm-project/vllm#5309: [Feature]: Support selecting chat template

| 字段 | 值 |
| --- | --- |
| Issue | [#5309](https://github.com/vllm-project/vllm/issues/5309) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support selecting chat template

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In `Mixtral-8x22B-Instruct-v0.1` there are two chat templates [here](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1/blob/main/tokenizer_config.json) ``` "chat_template": [ { "name": "default", "template": "{{bos_token}}{% for message in messages %}{% if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}{{ raise_exception('Conversation roles must alternate user/assistant/user/assistant/...') }}{% endif %}{% if message['role'] == 'user' %}{{ ' [INST] ' + message['content'] + ' [/INST]' }}{% elif message['role'] == 'assistant' %}{{ ' ' + message['content'] + ' ' + eos_token}}{% else %}{{ raise_exception('Only user and assistant roles are supported!') }}{% endif %}{% endfor %}" }, { "name": "tool_use", "template": "{{bos_token}}{% set user_messages = messages | selectattr('role', 'equalto', 'user') | list %}{% for message in messages %}{% if message['role'] == 'user' %}{% if message == user_messages[-1] %}{% if tools %}{{'[AVAILABLE_TOOLS]'+ tools|string + '[/AVAILABLE_TOOLS]'}}{% endif %}{{ '[INST]' + message['content'] + '[/INST]' }}{% else %}{{ '[INST]' + message['content'] + '[/INST]' }}{% endif %}{% elif message['role']...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Mixtral-8x22B-Instruct-v0.1` there are two chat templates [here](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1/blob/main/tokenizer_config.json) ``` "chat_template": [ { "name": "default", "template": "{{b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support selecting chat template feature request;stale ### 🚀 The feature, motivation and pitch In `Mixtral-8x22B-Instruct-v0.1` there are two chat templates [here](https://huggingface.co/mistralai/Mixtral-8x22...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: le'] == 'assistant' %}{{ ' ' + message['content'] + ' ' + eos_token}}{% else %}{{ raise_exception('Only user and assistant roles are supported!') }}{% endif %}{% endfor %}" }, { "name": "tool_use", "template": "{{bos_to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
