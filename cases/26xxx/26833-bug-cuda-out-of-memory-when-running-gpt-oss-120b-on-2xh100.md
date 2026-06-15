# vllm-project/vllm#26833: [Bug]: CUDA out of memory when running gpt-oss-120b on 2xH100

| 字段 | 值 |
| --- | --- |
| Issue | [#26833](https://github.com/vllm-project/vllm/issues/26833) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA out of memory when running gpt-oss-120b on 2xH100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve openai/gpt-oss-120b --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --max-num-seqs 2048 --async-scheduling ``` Setting gpu memory utilization to 0.8 successfully serves the model without OOM, and in this case `nvidia-smi` shows memory usage 78737MiB / 81559MiB per GPU. cc @benchislett ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA out of memory when running gpt-oss-120b on 2xH100 bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve openai/gpt-oss-120b --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --max-num-se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;trit...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: y-utilization 0.9 --max-num-seqs 2048 --async-scheduling ``` Setting gpu memory utilization to 0.8 successfully serves the model without OOM, and in this case `nvidia-smi` shows memory usage 78737MiB / 81559MiB per GPU....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: CUDA out of memory when running gpt-oss-120b on 2xH100 bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve openai/gpt-oss-120b --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --max-num-se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;triton build_error;crash;oom env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
