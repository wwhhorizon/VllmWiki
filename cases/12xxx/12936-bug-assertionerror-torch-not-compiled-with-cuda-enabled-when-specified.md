# vllm-project/vllm#12936: [Bug]: AssertionError: Torch not compiled with CUDA enabled when specified --device tpu

| 字段 | 值 |
| --- | --- |
| Issue | [#12936](https://github.com/vllm-project/vllm/issues/12936) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: Torch not compiled with CUDA enabled when specified --device tpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug program crashes withAssertionError: Torch not compiled with CUDA enabled when specified --device tpu command: `vllm serve arcee-ai/DeepSeek-R1-bf16 --device tpu --trust-remote-code --download-dir .` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: AssertionError: Torch not compiled with CUDA enabled when specified --device tpu bug ### Your current environment ### 🐛 Describe the bug program crashes withAssertionError: Torch not compiled with CUDA enabled wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d when specified --device tpu command: `vllm serve arcee-ai/DeepSeek-R1-bf16 --device tpu --trust-remote-code --download-dir .` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AssertionError: Torch not compiled with CUDA enabled when specified --device tpu bug ### Your current environment ### 🐛 Describe the bug program crashes withAssertionError: Torch not compiled with CUDA enabled wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: che;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
