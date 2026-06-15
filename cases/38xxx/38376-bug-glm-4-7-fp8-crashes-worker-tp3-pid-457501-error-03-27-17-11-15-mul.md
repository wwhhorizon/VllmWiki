# vllm-project/vllm#38376: [Bug]: glm 4.7 fp8 crashes (Worker_TP3 pid=457501) ERROR 03-27 17:11:15 [multiproc_executor.py:852] AttributeError: '_OpNamespace' '_C' object has no attribute 'per_token_group_fp8_quant'

| 字段 | 值 |
| --- | --- |
| Issue | [#38376](https://github.com/vllm-project/vllm/issues/38376) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: glm 4.7 fp8 crashes (Worker_TP3 pid=457501) ERROR 03-27 17:11:15 [multiproc_executor.py:852] AttributeError: '_OpNamespace' '_C' object has no attribute 'per_token_group_fp8_quant'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GLM 4.7 crashes on load on RTX 6000 Pro (Worker_TP3 pid=457501) ERROR 03-27 17:11:15 [multiproc_executor.py:852] AttributeError: '_OpNamespace' '_C' object has no attribute 'per_token_group_fp8_quant' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: glm 4.7 fp8 crashes (Worker_TP3 pid=457501) ERROR 03-27 17:11:15 [multiproc_executor.py:852] AttributeError: '_OpNamespace' '_C' object has no attribute 'per_token_group_fp8_quant' bug ### Your current environmen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rrent environment ### 🐛 Describe the bug GLM 4.7 crashes on load on RTX 6000 Pro (Worker_TP3 pid=457501) ERROR 03-27 17:11:15 [multiproc_executor.py:852] AttributeError: '_OpNamespace' '_C' object has no attribute 'per_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Yo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
