# vllm-project/vllm#36493: [Bug]: The hit rate of prefix caching in Qwen3.5 35BA3B is very low, always less than 0.1%

| 字段 | 值 |
| --- | --- |
| Issue | [#36493](https://github.com/vllm-project/vllm/issues/36493) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The hit rate of prefix caching in Qwen3.5 35BA3B is very low, always less than 0.1%

### Issue 正文摘录

### Your current environment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug I used an intention to identify the test set, and 20% of the characters in front of them were consistent. On qwen3-30ba3b, the hit rate of prefix caching was about 20%. But in qwen3-35ba3b, most of the time it is 0%, and occasionally it has a hit rate of 0.1%. My startup script: vllm serve /data/models/Qwen3.5-35B-A3B \ --host 0.0.0.0 \ --served-model-name default \ --port 8889 \ --language-model-only \ --max-num-seqs 128 \ --enable-prefix-caching \ --max-model-len auto ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ways less than 0.1% bug ### Your current environment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug I used an intention to identify the test set, and 20% of the characters in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The hit rate of prefix caching in Qwen3.5 35BA3B is very low, always less than 0.1% bug ### Your current environment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug I us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nvironment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug I used an intention to identify the test set, and 20% of the characters in front of them were consistent. On qwen3-30...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 17.0 docker ### 🐛 Describe the bug I used an intention to identify the test set, and 20% of the characters in front of them were consistent. On qwen3-30ba3b, the hit rate of prefix caching was about 20%. But in qwen3-35...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
