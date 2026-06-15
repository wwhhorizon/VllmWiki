# vllm-project/vllm#39468: [Bug]: vllm 0.19.0, gemma4, The format of the tool call returned by vllm is incorrect.

| 字段 | 值 |
| --- | --- |
| Issue | [#39468](https://github.com/vllm-project/vllm/issues/39468) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.19.0, gemma4, The format of the tool call returned by vllm is incorrect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the output tool-call content: the json string is surrounded with specific chars ` call:process{action: poll ,sessionId: calm-ridge ,timeout:20000} ", "stop_reason": 50 } ] } ``` start command: ``` VLLM_USE_MODELSCOPE=true \ vllm serve google/gemma-4-31B-it \ --port 8000 \ --tensor-parallel-size 4 \ --max-model-len 160000 \ --reasoning-parser gemma4 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --max-num-seqs 2 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: bug the output tool-call content: the json string is surrounded with specific chars ` call:process{action: poll ,sessionId: calm-ridge ,timeout:20000} ", "stop_reason": 50 } ] } ``` start command: ``` VLLM_USE_MODELSCOP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ma4 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.92 \ --max-num-seqs 2 ``` ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm 0.19.0, gemma4, The format of the tool call returned by vllm is incorrect. bug ### Your current environment ### 🐛 Describe the bug the output tool-call content: the json string is surrounded with specific ch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;mismatch;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
