# vllm-project/vllm#17167: [Bug]: VLLM will hang during multiple node startup, but if ‘--enforce-eager’ configuration is enabled, it can start normally

| 字段 | 值 |
| --- | --- |
| Issue | [#17167](https://github.com/vllm-project/vllm/issues/17167) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM will hang during multiple node startup, but if ‘--enforce-eager’ configuration is enabled, it can start normally

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM will hang during multiple node startup, but if ‘--enforce-eager’ configuration is enabled, it can start normally. This may be related to the capturing CUDA graph. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cache;cuda;fp8;ker...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton build_error;nan_inf dtype;env_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is enabled, it can start normally. This may be related to the capturing CUDA graph. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: VLLM will hang during multiple node startup, but if ‘--enforce-eager’ configuration is enabled, it can start normally bug ### Your current environment ### 🐛 Describe the bug VLLM will hang during multiple node startu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lative_decoding cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency;memory_layout;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
