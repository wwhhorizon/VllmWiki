# vllm-project/vllm#31030: [Performance]: Regression between 0.10.2 and 0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#31030](https://github.com/vllm-project/vllm/issues/31030) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Regression between 0.10.2 and 0.12.0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We run the docker version of vLLM on a node with 8 NVIDIA H200 GPUs and serve Qwen3 235b FP8 of 4 GPUs with the following arguments: ``` command: ["--served-model-name", "qwen3-235b-v2", "--model", "/models/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8", "--gpu-memory-utilization", "0.90", "--max-model-len", "100000", "--port", "80", "--enable-chunked-prefill", "--enable-prefix-caching", "--tensor-parallel-size", "4", "--guided_decoding_backend", "xgrammar", "--enable-auto-tool-choice", "--tool-call-parser", "hermes", "--disable-log-requests"] ``` and environment: ``` VLLM_USE_FLASHINFER_SAMPLER=1 ``` With v0.10.2 we achieve a generation rate of ~60tok/s but only 28tok/s after upgrading to v0.12.0. Sadly, considering this is a production environment I am unable to take time to test more and reverted to v0.10.2 until we know more about what could be the cause of this regression. I am not excluding that we missed a change in the configuration that we should but the 2 fold difference makes me believe that configuration alone can't explain our issue. ### Misc discussion on performance _No response_ ### You...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ormance _No response_ ### Report of performance regression We run the docker version of vLLM on a node with 8 NVIDIA H200 GPUs and serve Qwen3 235b FP8 of 4 GPUs with the following arguments: ``` command: ["--served-mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: r version of vLLM on a node with 8 NVIDIA H200 GPUs and serve Qwen3 235b FP8 of 4 GPUs with the following arguments: ``` command: ["--served-model-name", "qwen3-235b-v2", "--model", "/models/Qwen/Qwen3-235B-A22B-Instruc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n the docker version of vLLM on a node with 8 NVIDIA H200 GPUs and serve Qwen3 235b FP8 of 4 GPUs with the following arguments: ``` command: ["--served-model-name", "qwen3-235b-v2", "--model", "/models/Qwen/Qwen3-235B-A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nable-prefix-caching", "--tensor-parallel-size", "4", "--guided_decoding_backend", "xgrammar", "--enable-auto-tool-choice", "--tool-call-parser", "hermes", "--disable-log-requests"] ``` and environment: ``` VLLM_USE_FLA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: , "0.90", "--max-model-len", "100000", "--port", "80", "--enable-chunked-prefill", "--enable-prefix-caching", "--tensor-parallel-size", "4", "--guided_decoding_backend", "xgrammar", "--enable-auto-tool-choice", "--tool-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
