# vllm-project/vllm#11271: [Bug]: AttributeError: 'CachedPreTrainedTokenizerFast' object has no attribute 'default_chat_template'. Did you mean: 'get_chat_template'?

| 字段 | 值 |
| --- | --- |
| Issue | [#11271](https://github.com/vllm-project/vllm/issues/11271) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'CachedPreTrainedTokenizerFast' object has no attribute 'default_chat_template'. Did you mean: 'get_chat_template'?

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when i run `python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-3-70B --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --num-prompts 2`, it gives me ``` AttributeError: 'CachedPreTrainedTokenizerFast' object has no attribute 'default_chat_template'. Did you mean: 'get_chat_template'? ``` So I tried to check the environment with `python collect_env.py`, then I got vllm is not complete. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: you mean: 'get_chat_template'? bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when i run `python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: l Input Dumps _No response_ ### 🐛 Describe the bug when i run `python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-3-70B --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --num-p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 🐛 Describe the bug when i run `python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-3-70B --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --num-prompts 2`, it gives me ``` Attri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
