# vllm-project/vllm#22225: [Bug]: VLLM v0.10.0  failed to deploy the qwen3-30b-moe model. The error is AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'.

| 字段 | 值 |
| --- | --- |
| Issue | [#22225](https://github.com/vllm-project/vllm/issues/22225) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM v0.10.0  failed to deploy the qwen3-30b-moe model. The error is AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As the title described, I tried to deploy the qwen3-30b-mo3 model using vllm=v0.10.0 but failed. The error is AttributeError: `'_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'` The command is `vllm serve /usr/local/storage/models/Qwen3-30B-A3B-Instruct-2507-FP8 --port 9850 --served-model-name "qwen3" --max-model-len 32768 --gpu-memory-utilization 0.85 --enable-auto-tool-choice --tool-call-parser hermes` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;hardware_porting;model_support;moe;quantization cuda;fp8;moe build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: and is `vllm serve /usr/local/storage/models/Qwen3-30B-A3B-Instruct-2507-FP8 --port 9850 --served-model-name "qwen3" --max-model-len 32768 --gpu-memory-utilization 0.85 --enable-auto-tool-choice --tool-call-parser herme...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: VLLM v0.10.0 failed to deploy the qwen3-30b-moe model. The error is AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'. bug;unstale ### Your current environment ### 🐛 Describe the bug...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: VLLM v0.10.0 failed to deploy the qwen3-30b-moe model. The error is AttributeError: '_OpNamespace' '_moe_C' object has no attribute 'topk_softmax'. bug;unstale ### Your current environment ### 🐛 Describe the bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
