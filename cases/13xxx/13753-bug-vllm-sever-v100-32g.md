# vllm-project/vllm#13753: [Bug]: 使用vllm sever 出现会卡住不动 v100-32g

| 字段 | 值 |
| --- | --- |
| Issue | [#13753](https://github.com/vllm-project/vllm/issues/13753) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 使用vllm sever 出现会卡住不动 v100-32g

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 每个节点五张卡使用两个节点 vllm serve /root/.cache/huggingface/deepseek \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --dtype=float16 \ --enable_chunked_prefill=False \ --max_model_len=2048 跨几点会卡住v100-32g ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --dtype=float16 \ --enable_chunked_prefill=False \ --max_model_len=2048 跨几点会卡住v100-32g ### Before submitting a new issue... - [x] Make sure you already searched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: onment ### 🐛 Describe the bug 每个节点五张卡使用两个节点 vllm serve /root/.cache/huggingface/deepseek \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --dtype=float16 \ --enable_chunked_prefill=False \ --max_model_len=2048...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 使用vllm sever 出现会卡住不动 v100-32g bug;stale ### Your current environment ### 🐛 Describe the bug 每个节点五张卡使用两个节点 vllm serve /root/.cache/huggingface/deepseek \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rm;attention_kv_cache;distributed_parallel;model_support cache dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 32g ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
