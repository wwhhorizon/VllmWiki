# vllm-project/vllm#10516: [Bug]: Model does not split in multiple Gpus instead it occupy same memory on each GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#10516](https://github.com/vllm-project/vllm/issues/10516) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model does not split in multiple Gpus instead it occupy same memory on each GPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have a node with 4 GPUs, each having 32 GB of memory. I’m loading the granite8B-code-instruct model with float16 precision, which requires approximately 16 GB of memory (8B parameters × 2 bytes). Using a tensor parallel size of 2, I plan to split the model across 2 GPUs for more efficient and faster serving. My expectation is that each GPU should load 8Gb, But Actual , it is loading 27GB on each gpu . The nvidia-smi commands shows GPU Memory-usage 0 28333MiB/32768MiB 1 28222MiB/ 32768MiB Code : vllm serve granite-8B-code-instruct --tensor-parallel-size 2 --dtype float16 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: d load 8Gb, But Actual , it is loading 27GB on each gpu . The nvidia-smi commands shows GPU Memory-usage 0 28333MiB/32768MiB 1 28222MiB/ 32768MiB Code : vllm serve granite-8B-code-instruct --tensor-parallel-size 2 --dty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: of memory. I’m loading the granite8B-code-instruct model with float16 precision, which requires approximately 16 GB of memory (8B parameters × 2 bytes). Using a tensor parallel size of 2, I plan to split the model acros...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ving 32 GB of memory. I’m loading the granite8B-code-instruct model with float16 precision, which requires approximately 16 GB of memory (8B parameters × 2 bytes). Using a tensor parallel size of 2, I plan to split the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: GB of memory. I’m loading the granite8B-code-instruct model with float16 precision, which requires approximately 16 GB of memory (8B parameters × 2 bytes). Using a tensor parallel size of 2, I plan to split the model ac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Model does not split in multiple Gpus instead it occupy same memory on each GPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have a node with 4 GPUs, each hav

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
