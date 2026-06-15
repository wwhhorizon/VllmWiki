# vllm-project/vllm#14763: [Bug]: Once again, there is an imbalance in memory usage in pipeline parallel deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#14763](https://github.com/vllm-project/vllm/issues/14763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Once again, there is an imbalance in memory usage in pipeline parallel deployment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using pipeline parallelism, the allocation of video memory is uneven. I observed that the peak value of VRM for some nodes (69-78 nodes) was 30GB, and the peak value of VRMA for the last node (79 nodes) was 40GB, indicating OOM. 11 nodes were launched through the container and successfully added to ray. Subsequently, the master node uses the following command to start the DeepSeeker R1-BF service： vllm serve /home/Models/DeepSeek-R1-BF16 --trust-remote-code --tensor-parallel-size 4 --pipeline-parallel-size 11 --dtype auto --gpu-memory-utilization 0.99 Out of memory has appeared： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: start the DeepSeeker R1-BF service： vllm serve /home/Models/DeepSeek-R1-BF16 --trust-remote-code --tensor-parallel-size 4 --pipeline-parallel-size 11 --dtype auto --gpu-memory-utilization 0.99 Out of memory has appeared...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rent environment ### 🐛 Describe the bug When using pipeline parallelism, the allocation of video memory is uneven. I observed that the peak value of VRM for some nodes (69-78 nodes) was 30GB, and the peak value of VRMA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: here is an imbalance in memory usage in pipeline parallel deployment bug;stale ### Your current environment ### 🐛 Describe the bug When using pipeline parallelism, the allocation of video memory is uneven. I observed th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y;speculative_decoding attention;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
