# vllm-project/vllm#16157: [Bug]: V1 engine Index Error When Single Request Near Max Context Length LLaMA 4

| 字段 | 值 |
| --- | --- |
| Issue | [#16157](https://github.com/vllm-project/vllm/issues/16157) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine Index Error When Single Request Near Max Context Length LLaMA 4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a single request is near the set max context length, about within 500~1000 tokens, the exact number is kind of random in each test, but generally about this range, it triggers a device side assertion of index range checking. This happens on both 0.8.3 and PR #16113. The device side error: ```cpp /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [91,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [92,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [93,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [94,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. // And more of other threads and blocks, but all the same error message... ``` The stack trace: ```py ERROR 04-07...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y", line 547, in __call__ ERROR 04-07 05:43:20 [core.py:390] return _compile( ERROR 04-07 05:43:20 [core.py:390] ^^^^^^^^^ ERROR 04-07 05:43:20 [core.py:390] File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: PR #16113. The device side error: ```cpp /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [91,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` fai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: V1 engine Index Error When Single Request Near Max Context Length LLaMA 4 bug ### Your current environment ### 🐛 Describe the bug When a single request is near the set max context length, about within 500~1000 to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ```cpp /pytorch/aten/src/ATen/native/cuda/IndexKernel.cu:94: operator(): block: [0,0,0], thread: [91,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. /pytorch/aten/src/ATen/native...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: V1 engine Index Error When Single Request Near Max Context Length LLaMA 4 bug ### Your current environment ### 🐛 Describe the bug When a single request is near the set max context length, about within 500~1000 to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
