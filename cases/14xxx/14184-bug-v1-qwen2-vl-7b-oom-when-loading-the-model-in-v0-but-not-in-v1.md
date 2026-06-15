# vllm-project/vllm#14184: [Bug][V1]: Qwen2-VL-7B OOM when loading the model in v0 but not in v1

| 字段 | 值 |
| --- | --- |
| Issue | [#14184](https://github.com/vllm-project/vllm/issues/14184) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: Qwen2-VL-7B OOM when loading the model in v0 but not in v1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to load Qwen2-VL model with this config: When I tried to load it using vllm v0.7.2, I could load the model with GPU RTX 4090 with full token length (32768) and not getting OOM. But, after update it to main git, I got OOM saying that maximum token length that I could get is around 12500. But, if I set the environment variable `VLLM_USE_V1=1`, I could load the model without OOM. Why is this happening? Here is the command how I load the model: ```bash vllm serve /models/Qwen2-VL-7B-INT8 --host 0.0.0.0 --served-model-name Qwen2-VL-7B-Int8 --port 8000 --limit-mm-per-prompt image=3,video=1 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding activation;cuda;gemm;operator;quant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: en I tried to load it using vllm v0.7.2, I could load the model with GPU RTX 4090 with full token length (32768) and not getting OOM. But, after update it to main git, I got OOM saying that maximum token length that I c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][V1]: Qwen2-VL-7B OOM when loading the model in v0 but not in v1 bug ### Your current environment ### 🐛 Describe the bug I'm trying to load Qwen2-VL model with this config: When I tried to load it using vllm v0.7.2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: on_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding activation;cuda;gemm;operator;quantization;sampling;triton build_error;nan_inf;oom dtype;env_dep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: speculative_decoding activation;cuda;gemm;operator;quantization;sampling;triton build_error;nan_inf;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
