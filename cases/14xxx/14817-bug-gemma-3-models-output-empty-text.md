# vllm-project/vllm#14817: [Bug]:  Gemma-3 models output empty text.

| 字段 | 值 |
| --- | --- |
| Issue | [#14817](https://github.com/vllm-project/vllm/issues/14817) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Gemma-3 models output empty text.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` curl http://localhost:8000/v1/completions \ > -H "Content-Type: application/json" \ > -d '{ > "model": "google/gemma-3-4b-it", > "prompt": "who are you?", > "stream": true > }' data: {"id":"cmpl-39c393fdbc284c8fbc31de7db7c50770","object":"text_completion","created":1741949943,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null} data: {"id":"cmpl-39c393fdbc284c8fbc31de7db7c50770","object":"text_completion","created":1741949943,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null} data: {"id":"cmpl-39c393fdbc284c8fbc31de7db7c50770","object":"text_completion","created":1741949943,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null} data: {"id":"cmpl-39c393fdbc284c8fbc31de7db7c50770","object":"text_completion","created":1741949943,"model":"google/gemma-3-4b-it","choices":[{"index":0,"text":"","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null} data: {"id":"cmpl-39c393fd...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma-3 models output empty text. bug ### Your current environment ### 🐛 Describe the bug ``` curl http://localhost:8000/v1/completions \ > -H "Content-Type: application/json" \ > -d '{ > "model": "g
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rformance distributed_parallel;frontend_api;model_support cuda dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: stions. performance distributed_parallel;frontend_api;model_support cuda dtype;env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma-3 models output empty text. bug ### Your current environment ### 🐛 Describe the bug ``` curl http://localhost:8000/v1/completions \ > -H "Content-Type: application/json" \ > -d '{ > "model": "g

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
