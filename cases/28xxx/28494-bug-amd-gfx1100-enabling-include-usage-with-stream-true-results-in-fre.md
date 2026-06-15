# vllm-project/vllm#28494: [Bug][AMD gfx1100] Enabling `include_usage` with stream=True results in freeze after 3 iterations

| 字段 | 值 |
| --- | --- |
| Issue | [#28494](https://github.com/vllm-project/vllm/issues/28494) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][AMD gfx1100] Enabling `include_usage` with stream=True results in freeze after 3 iterations

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Problem**: When using openai chat completions v1 with stream=True, adding `include_usage` causes inference to silently freeze after 3rd iteration. Without the `include_usage` option, inference is successful across many iterations. This issue is observed in gfx1100 arch on AMD Ryzen 7 PHX HPT (GPU 780M), ROCM7.0.2, vllm0.11.1rc5 We also tested with gfx942 (MI300x) and we do not see this issue (able to run 10+ inference calls sequentially **Debugging**: - Enabled `VLLM_LOGGING_LEVEL=DEBUG` but there is no output error on the server end. - Also tried with latest vllm 0.11.1rc6, same error persists **Code Snippet**: Model: Qwen2.5-VL-7B-Instruct-AWQ ```python response = client.chat.completions.create( max_completion_tokens=n_output_tokens, model=model, stream=True, messages=[{"role": "user", "content": content_parts}], stream_options={"include_usage": True}, # This line causes inference to freeze ) ``` **Observed results:** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/)...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: include_usage` with stream=True results in freeze after 3 iterations bug;rocm ### Your current environment ### 🐛 Describe the bug **Problem**: When using openai chat completions v1 with stream=True, adding `include_usag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tried with latest vllm 0.11.1rc6, same error persists **Code Snippet**: Model: Qwen2.5-VL-7B-Instruct-AWQ ```python response = client.chat.completions.create( max_completion_tokens=n_output_tokens, model=model, stream=T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: stions. correctness ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your curren...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
