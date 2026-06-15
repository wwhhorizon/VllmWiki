# vllm-project/vllm#9578: [Usage]: When using vllm to start the internvl2-8b(16GB) model service at A10 card(24GB), an error occurs. The command is as follows: python -m vllm.entrypoints.openai.api_serve --model ./internvl2-8b --dtype auto --gpu-memory-utilization 0.9 --trust-remote-code usage

| 字段 | 值 |
| --- | --- |
| Issue | [#9578](https://github.com/vllm-project/vllm/issues/9578) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When using vllm to start the internvl2-8b(16GB) model service at A10 card(24GB), an error occurs. The command is as follows: python -m vllm.entrypoints.openai.api_serve --model ./internvl2-8b --dtype auto --gpu-memory-utilization 0.9 --trust-remote-code usage

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug orch.OutOfMemoryError: Error in model execution (input dumped to /tmp/err_execute_model_.input_20241022-033658.pkl): CUDA out of memory. tried to allocate 1.93 G to o has a total capseity of 22.19 GiB of which 183.88 MiB 1s free. Process 3759893 has 22.00 G1B memory in use. of the allocated memory 19.99 Gi8 is allocated by pytar ad 4 6 1 x of 1yorch but unallocated. if reserved but unallocated memory is large try setting PYTORCH_CUDA ALLOC CONF=expandable segments:True to av o gtation.see documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda. html#environment-variables) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion (input dumped to /tmp/err_execute_model_.input_20241022-033658.pkl): CUDA out of memory. tried to allocate 1.93 G to o has a total capseity of 22.19 GiB of which 183.88 MiB 1s free. Process 3759893 has 22.00 G1B mem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: When using vllm to start the internvl2-8b(16GB) model service at A10 card(24GB), an error occurs. The command is as follows: python -m vllm.entrypoints.openai.api_serve --model ./internvl2-8b --dtype auto --gpu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: questions. performance model_support;scheduler_memory cuda oom dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ws: python -m vllm.entrypoints.openai.api_serve --model ./internvl2-8b --dtype auto --gpu-memory-utilization 0.9 --trust-remote-code usage usage ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Des...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: quently asked questions. performance model_support;scheduler_memory cuda oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
