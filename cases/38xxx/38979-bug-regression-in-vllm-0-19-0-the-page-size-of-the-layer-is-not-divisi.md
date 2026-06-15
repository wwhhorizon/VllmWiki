# vllm-project/vllm#38979: [Bug]: Regression in vllm 0.19.0 - The page size of the layer is not divisible by the maximum page size

| 字段 | 值 |
| --- | --- |
| Issue | [#38979](https://github.com/vllm-project/vllm/issues/38979) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression in vllm 0.19.0 - The page size of the layer is not divisible by the maximum page size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm 0.19.0 fails to start and throws an error "The page size of the layer is not divisible by the maximum page size" for ``` vllm serve Qwen/Qwen3.5-27B-FP8 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --download-dir workspace/models \ --host 0.0.0.0 \ --port 8080 \ --enable-prefix-caching \ --attention-backend flash_attn \ --gpu-memory-utilization 0.96 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 4}' \ --generation-config vllm \ --override-generation-config='{"temperature": 0.2, "top_p": 0.95, "top_k": 40, "min_p": 0.0, "presence_penalty": 1.7, "repetition_penalty": 1.05}' \ --enable-log-requests \ --max-num-batched-tokens 16384 \ --enable-chunked-prefill ``` but vllm 0.18.1 succeeds. Changed logging and they aren't divisible indeed: "The page size of the layer 16896 is not divisible by the maximum page size 3309568" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: divisible by the maximum page size" for ``` vllm serve Qwen/Qwen3.5-27B-FP8 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --download-dir workspace/models \ --host 0.0.0.0 \ --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the layer is not divisible by the maximum page size" for ``` vllm serve Qwen/Qwen3.5-27B-FP8 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 \ --download-dir workspace/models \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n-backend flash_attn \ --gpu-memory-utilization 0.96 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 4}' \ --generation-config vllm \ --override-generation-config='{"temperature": 0.2, "top_p": 0.95,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --port 8080 \ --enable-prefix-caching \ --attention-backend flash_attn \ --gpu-memory-utilization 0.96 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 4}' \ --generation-config vllm \ --override-gene...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
