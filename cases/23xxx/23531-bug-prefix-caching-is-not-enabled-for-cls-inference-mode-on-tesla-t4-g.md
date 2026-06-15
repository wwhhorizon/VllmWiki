# vllm-project/vllm#23531: [Bug]: Prefix Caching is not enabled for CLS inference mode on TESLA T4 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#23531](https://github.com/vllm-project/vllm/issues/23531) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix Caching is not enabled for CLS inference mode on TESLA T4 GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug config.yaml model: "/vllm-workspace/model/qwen3_0.6b_merged" host: "127.0.0.1" port: 6379 uvicorn-log-level: "info" task: "classify" enable-prefix-caching: true gpu-memory-utilization: 0.9 dtype: "float16" trust_remote_code: true Problem Description: When I launch the model using the configuration provided above, I'm unable to utilize prefix caching. Additionally, the GPU memory usage does not reach the expected 90% threshold. However, prefix caching does work correctly when I use "chat mode". ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ESLA T4 GPU bug ### Your current environment ### 🐛 Describe the bug config.yaml model: "/vllm-workspace/model/qwen3_0.6b_merged" host: "127.0.0.1" port: 6379 uvicorn-log-level: "info" task: "classify" enable-prefix-cach...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: task: "classify" enable-prefix-caching: true gpu-memory-utilization: 0.9 dtype: "float16" trust_remote_code: true Problem Description: When I launch the model using the configuration provided above, I'm unable to utiliz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e". ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
