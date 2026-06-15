# vllm-project/vllm#9903: [Feature]: automatically release graphics card memory

| 字段 | 值 |
| --- | --- |
| Issue | [#9903](https://github.com/vllm-project/vllm/issues/9903) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: automatically release graphics card memory

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use vllm.entrypoints.openai.api_user to start my large model, and the specific command is as follows: ```bash python3 -m vllm.entrypoints.openai.api_server --model /data/bertmodel/Qwen/Qwen2.5-32B-Instruct --served-model-name Yi-1.5-34B-Chat --max_model_len 20000 --enable-auto-tool-choice --tool-call-parser hermes ``` But I found that when I don't use model inference, the service doesn't automatically release graphics card memory. I am worried that there may be problems with OOM in the future, so I hope to add code that automatically releases graphics card memory. ![微信截图_20241101032652](https://github.com/user-attachments/assets/cf1d715c-59d6-4dcf-8f83-aefa3982915a) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tion and pitch I use vllm.entrypoints.openai.api_user to start my large model, and the specific command is as follows: ```bash python3 -m vllm.entrypoints.openai.api_server --model /data/bertmodel/Qwen/Qwen2.5-32B-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: automatically release graphics card memory feature request;stale ### 🚀 The feature, motivation and pitch I use vllm.entrypoints.openai.api_user to start my large model, and the specific command is as follows:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 52](https://github.com/user-attachments/assets/cf1d715c-59d6-4dcf-8f83-aefa3982915a) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: use vllm.entrypoints.openai.api_user to start my large model, and the specific command is as follows: ```bash python3 -m vllm.entrypoints.openai.api_server --model /data/bertmodel/Qwen/Qwen2.5-32B-Instruct --served-mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
