# vllm-project/vllm#22736: [Bug]: Memory Leak Issue in Load Testing Scenario

| 字段 | 值 |
| --- | --- |
| Issue | [#22736](https://github.com/vllm-project/vllm/issues/22736) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory Leak Issue in Load Testing Scenario

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We ran the service with the following command on the H20 machine. With an average **input of 400 tokens and random output ranging from 1 to 37,000 tokens**, we conducted end-to-end stress testing with all post-processing parameters enabled. After a few hours, monitoring the service process revealed that the GPU memory usage increased in a stepwise manner. ```python vllm serve /path/to/Qwen3-32B-FP8/ --served-model-name qwen --trust-remote-code -tp 4 --port 8006 --max_model_len 36768 --no-enable-prefix-caching --max-num-batched-tokens 36784 ``` The memory monitoring tool used is smem. A screenshot of the process monitoring is shown below(the green curve represents the service process)： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding cuda;fp8;operator;triton build_error dtype;env_depe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: increased in a stepwise manner. ```python vllm serve /path/to/Qwen3-32B-FP8/ --served-model-name qwen --trust-remote-code -tp 4 --port 8006 --max_model_len 36768 --no-enable-prefix-caching --max-num-batched-tokens 36784...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --max-num-batched-tokens 36784 ``` The memory monitoring tool used is smem. A screenshot of the process monitoring is shown below(the green curve represents the service process)： ### Before submitting a new issue... - [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ory usage increased in a stepwise manner. ```python vllm serve /path/to/Qwen3-32B-FP8/ --served-model-name qwen --trust-remote-code -tp 4 --port 8006 --max_model_len 36768 --no-enable-prefix-caching --max-num-batched-to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Memory Leak Issue in Load Testing Scenario bug;stale ### Your current environment ### 🐛 Describe the bug We ran the service with the following command on the H20 machine. With an average **input of 400 tokens and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
