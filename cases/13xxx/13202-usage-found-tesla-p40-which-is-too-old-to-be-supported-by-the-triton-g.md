# vllm-project/vllm#13202: [Usage]: Found Tesla P40 which is too old to be supported by the triton GPU compiler, which is used as the backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#13202](https://github.com/vllm-project/vllm/issues/13202) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Found Tesla P40 which is too old to be supported by the triton GPU compiler, which is used as the backend.

### Issue 正文摘录

### Your current environment docker images vllm-openai:v0.7.2 ### How would you like to use vllm vllm server --model", "/models/Qwen2.5-7B-Instruct", "--served-model-name", "qwen2.5-7b-instruct", "--gpu-memory-utilization", "0.90", "--dtype" ,"half" ,"--tensor-parallel-size", "2" when i run vllm , the error is raised. RuntimeError: Found Tesla P40 which is too old to be supported by the triton GPU compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.1 How to solve it？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: age]: Found Tesla P40 which is too old to be supported by the triton GPU compiler, which is used as the backend. usage ### Your current environment docker images vllm-openai:v0.7.2 ### How would you like to use vllm vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: compiler, which is used as the backend. Triton only supports devices of CUDA Capability >= 7.0, but your device is of CUDA capability 6.1 How to solve it？ ### Before submitting a new issue... - [x] Make sure you already...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Usage]: Found Tesla P40 which is too old to be supported by the triton GPU compiler, which is used as the backend. usage ### Your current environment docker images vllm-openai:v0.7.2 ### How would you like to use vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es vllm-openai:v0.7.2 ### How would you like to use vllm vllm server --model", "/models/Qwen2.5-7B-Instruct", "--served-model-name", "qwen2.5-7b-instruct", "--gpu-memory-utilization", "0.90", "--dtype" ,"half" ,"--tenso...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: el-name", "qwen2.5-7b-instruct", "--gpu-memory-utilization", "0.90", "--dtype" ,"half" ,"--tensor-parallel-size", "2" when i run vllm , the error is raised. RuntimeError: Found Tesla P40 which is too old to be supported...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
