# vllm-project/vllm#29622: [Bug][CPU Backend]: Incorrect and repetitive NUMA warnings (“1CPU X is on NUMA node 0, but CPU 48 is on NUMA node 0”)

| 字段 | 值 |
| --- | --- |
| Issue | [#29622](https://github.com/vllm-project/vllm/issues/29622) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CPU Backend]: Incorrect and repetitive NUMA warnings (“1CPU X is on NUMA node 0, but CPU 48 is on NUMA node 0”)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM prints incorrect and repetitive NUMA warnings when running on CPU. The warnings appear even though the machine has a single NUMA node, and the format of the message appears incorrect (1CPU 48, etc.). Command: ``` vllm bench throughput --num-prompts 64 --seed 0 --dataset-name sharegpt --max-model-len 4096 --input-len 512 --model meta-llama/Llama-3.1-8B-Instruct ``` Observed Warning Output: (Excerpt — repeats for dozens of CPUs) ``` 1127 16:55:20.451514756 utils.cpp:54] Warning: 1CPU 48 is on NUMA node 0, but CPU 48 is on NUMA node 0. All CPUs should be on the same NUMA node for optimal performance. Memory will be bound to NUMA node 0. (function init_cpu_threads_env) W1127 16:55:20.451527408 utils.cpp:54] Warning: 1CPU 49 is on NUMA node 0, but CPU 48 is on NUMA node 0. All CPUs should be on the same NUMA node for optimal performance. Memory will be bound to NUMA node 0. (function init_cpu_threads_env) W1127 16:55:20.451530153 utils.cpp:54] Warning: 1CPU 50 is on NUMA node 0, but CPU 48 is on NUMA node 0. All CPUs should be on the same NUMA node for optimal performance. Memory will be bound to NUMA node 0. (function init_cpu_t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: warnings appear even though the machine has a single NUMA node, and the format of the message appears incorrect (1CPU 48, etc.). Command: ``` vllm bench throughput --num-prompts 64 --seed 0 --dataset-name sharegpt --max...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 01 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: the message appears incorrect (1CPU 48, etc.). Command: ``` vllm bench throughput --num-prompts 64 --seed 0 --dataset-name sharegpt --max-model-len 4096 --input-len 512 --model meta-llama/Llama-3.1-8B-Instruct ``` Obser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug][CPU Backend]: Incorrect and repetitive NUMA warnings (“1CPU X is on NUMA node 0, but CPU 48 is on NUMA node 0”) bug;cpu ### Your current environment ### 🐛 Describe the bug vLLM prints incorrect and repetitive NUMA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
