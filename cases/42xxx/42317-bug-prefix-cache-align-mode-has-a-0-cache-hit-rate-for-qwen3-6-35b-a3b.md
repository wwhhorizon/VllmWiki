# vllm-project/vllm#42317: [Bug]: Prefix cache align-mode has a 0% cache hit rate for Qwen3.6-35B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#42317](https://github.com/vllm-project/vllm/issues/42317) |
| 状态 | open |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix cache align-mode has a 0% cache hit rate for Qwen3.6-35B-A3B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tested `Qwen/Qwen3.6-35B-A3B` on H800 with a total input length of 8,000 tokens and an output length of 100 tokens. Notably, `max-num-batched-tokens` was set to `8192`. The results are as follows. ### Launch commands #### no-apc ```bash vllm serve Qwen/Qwen3.6-35B-A3B \ -tp 2 \ --host 0.0.0.0 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --no-enable-prefix-caching \ --mamba-cache-mode all \ --gdn-prefill-backend triton ``` #### align-mode ``` vllm serve Qwen/Qwen3.6-35B-A3B \ -tp 2 \ --host 0.0.0.0 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --enable-prefix-caching \ --mamba-cache-mode align \ --gdn-prefill-backend triton ``` #### all-mode ``` vllm serve Qwen/Qwen3.6-35B-A3B \ -tp 2 \ --host 0.0.0.0 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --enable-prefix-caching \ --mamba-cache-mode all \ --gdn-prefill-backend triton ``` Since `all` mode currently requires the Triton GDN prefill backend, I used `--gdn-prefill-backend triton` for all runs to keep the comparison consistent. ### Benchmark command ``` vllm bench serve Qwen/Qwen3.6-35B-A3B \ --dataset-name prefix_repetition \ --nu...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 6-35B-A3B bug ### Your current environment ### 🐛 Describe the bug I tested `Qwen/Qwen3.6-35B-A3B` on H800 with a total input length of 8,000 tokens and an output length of 100 tokens. Notably, `max-num-batched-tokens` w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error;slowdown env_dependency Your curren...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: o-enable-prefix-caching \ --mamba-cache-mode all \ --gdn-prefill-backend triton ``` #### align-mode ``` vllm serve Qwen/Qwen3.6-35B-A3B \ -tp 2 \ --host 0.0.0.0 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Prefix cache align-mode has a 0% cache hit rate for Qwen3.6-35B-A3B bug ### Your current environment ### 🐛 Describe the bug I tested `Qwen/Qwen3.6-35B-A3B` on H800 with a total input length of 8,000 tokens and an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
