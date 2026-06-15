# vllm-project/vllm#22750: [Bug]: Non-functional max_capture_size of gpt-oss causes OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#22750](https://github.com/vllm-project/vllm/issues/22750) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Non-functional max_capture_size of gpt-oss causes OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered an out-of-memory error while running gpt-oss-20b on two 4090s, following [this tutorial](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#gpt-oss-vllm-usage-guide). The error occurs during CUDA graph capture. Debugging revealed that the `max_capture_size` parameter appears to be ineffective. I'm wondering if `cuda_graph_sizes` should be constrained by `max_capture_size`. Related snippet on main branch: https://github.com/vllm-project/vllm/blob/e5d3d63c42aa85025dfb1b5dec369c0c856a4efa/vllm/model_executor/models/config.py#L266-L272 Do we need a quick fix like this? ```python cuda_graph_sizes = [1, 2, 4] # Step size 8 for small batch sizes cuda_graph_sizes += [i for i in range(8, max_capture_size, 8)] # Step size 16 for larger batch sizes cuda_graph_sizes += [i for i in range(256, max_capture_size, 16)] ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t/OpenAI/GPT-OSS.html#gpt-oss-vllm-usage-guide). The error occurs during CUDA graph capture. Debugging revealed that the `max_capture_size` parameter appears to be ineffective. I'm wondering if `cuda_graph_sizes` should...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Non-functional max_capture_size of gpt-oss causes OOM bug;stale ### Your current environment ### 🐛 Describe the bug I encountered an out-of-memory error while running gpt-oss-20b on two 4090s, following [this tut...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on two 4090s, following [this tutorial](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#gpt-oss-vllm-usage-guide). The error occurs during CUDA graph capture. Debugging revealed that the `max_capture...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Non-functional max_capture_size of gpt-oss causes OOM bug;stale ### Your current environment ### 🐛 Describe the bug I encountered an out-of-memory error while running gpt-oss-20b on two 4090s, following [this tut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Non-functional max_capture_size of gpt-oss causes OOM bug;stale ### Your current environment ### 🐛 Describe the bug I encountered an out-of-memory error while running gpt-oss-20b on two 4090s, following [this tut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
