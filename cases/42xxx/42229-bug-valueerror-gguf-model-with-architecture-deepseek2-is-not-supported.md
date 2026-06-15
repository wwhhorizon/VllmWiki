# vllm-project/vllm#42229: [Bug]:  ValueError: GGUF model with architecture deepseek2 is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#42229](https://github.com/vllm-project/vllm/issues/42229) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  ValueError: GGUF model with architecture deepseek2 is not supported yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when trying to load gguf of deepseek v4 ``` python3 -m vllm.entrypoints.openai.api_server --model ./DeepSeekV4-Flash-158B-Q4_K_M.gguf --served-model-name DeepSeek-V4-Flash --max-model-len=8192 --generation-config auto --enable-sleep-mode --gpu-memory-utilization 0.85 --tokenizer deepseek-ai/DeepSeek-V4 --load-format gguf --cpu-offload-gb 100 ``` ValueError: GGUF model with architecture deepseek2 is not supported yet. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ValueError: GGUF model with architecture deepseek2 is not supported yet. bug ### Your current environment ### 🐛 Describe the bug when trying to load gguf of deepseek v4 ``` python3 -m vllm.entrypoints.openai.api_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: ValueError: GGUF model with architecture deepseek2 is not supported yet. bug ### Your current environment ### 🐛 Describe the bug when trying to load gguf of deepseek v4 ``` python3 -m vllm.entrypoints.openai.api_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: on 0.85 --tokenizer deepseek-ai/DeepSeek-V4 --load-format gguf --cpu-offload-gb 100 ``` ValueError: GGUF model with architecture deepseek2 is not supported yet. ### Before submitting a new issue... - [x] Make sure you a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
