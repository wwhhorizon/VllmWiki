# vllm-project/vllm#33643: [Bug]: serve qwen3-asr-1.7b error

| 字段 | 值 |
| --- | --- |
| Issue | [#33643](https://github.com/vllm-project/vllm/issues/33643) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: serve qwen3-asr-1.7b error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen3/Qwen3-ASR-1.7B ``` using curl ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "messages": [ {"role": "user", "content": [ {"type": "audio_url", "audio_url": {"url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"}} ]} ] }' ``` ![Image](https://github.com/user-attachments/assets/07a53bd7-7646-464a-84f2-0c011a9c470a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build cuda env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: serve qwen3-asr-1.7b error bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve Qwen3/Qwen3-ASR-1.7B ``` using curl ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: applica...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
