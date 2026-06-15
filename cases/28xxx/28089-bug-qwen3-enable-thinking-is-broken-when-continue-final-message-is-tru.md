# vllm-project/vllm#28089: [Bug]: Qwen3 enable_thinking is broken when continue_final_message is true

| 字段 | 值 |
| --- | --- |
| Issue | [#28089](https://github.com/vllm-project/vllm/issues/28089) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 enable_thinking is broken when continue_final_message is true

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Server docker compose command to deploy the server: ``` command: --model /data/model --served-model-name demo-gpt --host 0.0.0.0 --port 8000 -tp 2 --tokenizer-mode auto --trust-remote-code --gpu-memory-utilization 0.95 --max-model-len 8192 --max-num-seqs=100 --safetensors-load-strategy eager --enable-log-requests --enable-log-outputs --reasoning-parser qwen3 ``` ## Request with continue_final_message is False ``` { "model": "qwen3-32b", "messages": [ { "role": "system", "content": "You are an AI" }, { "role": "user", "content": "1+1=?" } ], "chat_template_kwargs": {"enable_thinking": true}, } ``` prompt from server log: ``` prompt: ' system\nYou are an AI \n user\n1+1=? \n assistant\n' ``` ## Request with continue_final_message is True ``` { "model": "qwen3-32b", "messages": [ { "role": "system", "content": "You are an AI" }, { "role": "user", "content": "1+1=?" }, { "role": "assistant", "content": " \nGood Question" } ], "add_generation_prompt": false, "continue_final_message": true, "chat_template_kwargs": {"enable_thinking": true} } ``` prompt from server log: ``` prompt: ' system\nYou are an AI \n user\n1+1=? \n assistant\...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 enable_thinking is broken when continue_final_message is true bug;stale ### Your current environment ### 🐛 Describe the bug ## Server docker compose command to deploy the server: ``` command: --model /data/m
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Qwen3 enable_thinking is broken when continue_final_message is true bug;stale ### Your current environment ### 🐛 Describe the bug ## Server docker compose command to deploy the server: ``` command: --model /data/model -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tale ### Your current environment ### 🐛 Describe the bug ## Server docker compose command to deploy the server: ``` command: --model /data/model --served-model-name demo-gpt --host 0.0.0.0 --port 8000 -tp 2 --tokenizer-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: --reasoning-parser qwen3 ``` ## Request with continue_final_message is False ``` { "model": "qwen3-32b", "messages": [ { "role": "system", "content": "You are an AI" }, { "role": "user", "content": "1+1=?"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
