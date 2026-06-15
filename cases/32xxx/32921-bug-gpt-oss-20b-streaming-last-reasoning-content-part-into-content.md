# vllm-project/vllm#32921: [Bug]: gpt-oss-20b streaming last reasoning content part into content

| 字段 | 值 |
| --- | --- |
| Issue | [#32921](https://github.com/vllm-project/vllm/issues/32921) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-20b streaming last reasoning content part into content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```javascript { "model": "openai/gpt-oss-20b", "tools": [ ... ], "stream": true, "messages": [ { "role": "system", "content": "Current model: vllm/openai/gpt-oss-20b\nCurrent date: 2026-01-23\n Additional info for this conversation: \n\nYou are a helpful assistant." }, { "role": "user", "content": "abcd" } ], "tool_choice": "auto", "reasoning_effort": "low" } ``` ```yaml command: - openai/gpt-oss-20b - --served-model-name - openai/gpt-oss-20b - --tensor-parallel-size - "1" - --gpu-memory-utilization - "0.9" - --tool-call-parser - openai - --enable-auto-tool-choice # for decoding - --kv-cache-dtype - fp8 - --no-enable-prefix-caching - --max-cudagraph-capture-size - "2048" - --max-num-batched-tokens - "8K" # https://github.com/vllm-project/vllm/issues/31501 # - --stream-interval # - "20" - --speculative-config - '{"model":"RedHatAI/gpt-oss-20b-speculator.eagle3","num_speculative_tokens":3,"method":"eagle3"}' ``` running on 5090 and `0.14.0` using stream=false, the tool use result is ok using stream=true, the reasoning_content leak the last chunk into content e.g ```javascript { "id": "chatcmpl-9f5cc21158b1e027", "object": "chat.com...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - --enable-auto-tool-choice # for decoding - --kv-cache-dtype - fp8 - --no-enable-prefix-caching - --max-cudagraph-capture-size - "2048" - --max-num-batched-tokens - "8K" # https://github.com/vllm-project/vllm/issues/31...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss-20b streaming last reasoning content part into content bug;stale ### Your current environment ### 🐛 Describe the bug ```javascript { "model": "openai/gpt-oss-20b", "tools": [ ... ], "stream":
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cache-dtype - fp8 - --no-enable-prefix-caching - --max-cudagraph-capture-size - "2048" - --max-num-batched-tokens - "8K" # https://github.com/vllm-project/vllm/issues/31501 # - --stream-interval # - "20" - --speculative...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: gpt-oss-20b streaming last reasoning content part into content bug;stale ### Your current environment ### 🐛 Describe the bug ```javascript { "model": "openai/gpt-oss-20b", "tools": [ ... ], "stream": true, "messag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
