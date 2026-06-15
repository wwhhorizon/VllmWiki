# vllm-project/vllm#33873: [Bug]: BGE-M3 pooling endpoint fails with short inputs (< 4 tokens) in token_classify task

| 字段 | 值 |
| --- | --- |
| Issue | [#33873](https://github.com/vllm-project/vllm/issues/33873) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: BGE-M3 pooling endpoint fails with short inputs (< 4 tokens) in token_classify task

### Issue 正文摘录

### Your current environment - **vLLM Version**: v0.15.0 - **Model**: BAAI/bge-m3 - **Task**: token_classify - **Endpoint**: /pooling ### 🐛 Describe the bug The `/pooling` endpoint with `task: token_classify` returns 400 error for inputs that tokenize to fewer than 4 tokens (including CLS and SEP special tokens). The backend returns a single float value instead of a list of floats, causing Pydantic validation to fail. ### Reproduction **Failing case ( = 4 tokens):** - "hello" → 4 tokens → Status 200 - "hello world" → 5 tokens → Status 200 - "a b" → 4 tokens → Status 200 - "abcd" → 4 tokens → Status 200 **Pattern:** 100% failure rate for < 4 tokens, 100% success rate for ≥ 4 tokens. ### Expected behavior Either: 1. Return proper list format for all token counts, OR 2. Return clear error message about minimum input length requirement ### Model Configuration ```bash vllm serve BAAI/bge-m3 \ --hf-overrides '{"architectures":["BgeM3EmbeddingModel"]}' \ --gpu-memory-utilization 0.2 \ --trust-remote-code ``` ### Additional context This appears to be a validation issue in the response schema. When input has fewer than 4 tokens, the backend returns a scalar float instead of a list, which f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ssify task ### Your current environment - **vLLM Version**: v0.15.0 - **Model**: BAAI/bge-m3 - **Task**: token_classify - **Endpoint**: /pooling ### 🐛 Describe the bug The `/pooling` endpoint with `task: token_classify`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 4 tokens) in token_classify task ### Your current environment - **vLLM Version**: v0.15.0 - **Model**: BAAI/bge-m3 - **Task**: token_classify - **Endpoint**: /pooling ### 🐛 Describe the bug The `/pooling` endpoint with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: enize to fewer than 4 tokens (including CLS and SEP special tokens). The backend returns a single float value instead of a list of floats, causing Pydantic validation to fail. ### Reproduction **Failing case ( = 4 token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: odel Configuration ```bash vllm serve BAAI/bge-m3 \ --hf-overrides '{"architectures":["BgeM3EmbeddingModel"]}' \ --gpu-memory-utilization 0.2 \ --trust-remote-code ``` ### Additional context This appears to be a validat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: trary length. ### Before submitting - [x] This is a bug, not a feature request - [x] I have searched existing issues - [x] I have provided reproduction steps - [x] I have included environment details

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
