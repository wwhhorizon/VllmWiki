# vllm-project/vllm#10444: [Bug]: request reward model report 500 Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#10444](https://github.com/vllm-project/vllm/issues/10444) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: request reward model report 500 Internal Server Error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug following the instruction https://github.com/vllm-project/vllm/issues/8700#issuecomment-2366884425 , the reward model https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward-HF is a LlamaForCausalLM model, so I serve it with vllm add parameter --task embedding. when I send a request, it encounter en error: INFO: "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error ERROR 11-19 17:55:16 engine.py:135] TypeError("object of type 'NoneType' has no len()") and then the server terminated the shell script: ```bash curl http://host:port/v1/embeddings \ -H "Content-Type: application/json" \ -d '{ "model": "Llama-3.1-Nemotron-70B-Reward-HF", "input": "Your text string goes here" }' ``` or use python code same as https://github.com/vllm-project/vllm/blob/main/examples/openai_embedding_client.py has the same error ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: request reward model report 500 Internal Server Error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug following the instruction https://github.com/vllm-project/vllm/iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: request reward model report 500 Internal Server Error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug following the instruction https://github.com/vllm-project/vllm/issu
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
