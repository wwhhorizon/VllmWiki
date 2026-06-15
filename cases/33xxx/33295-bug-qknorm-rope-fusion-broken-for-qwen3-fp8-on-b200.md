# vllm-project/vllm#33295: [Bug]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#33295](https://github.com/vllm-project/vllm/issues/33295) |
| 状态 | closed |
| 标签 | bug;help wanted;torch.compile |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 -cc.pass_config.enable_qk_norm_rope_fusion=True ... (EngineCore_DP0 pid=1446851) DEBUG 01-28 19:10:11 [compilation/qk_norm_rope_fusion.py:241] Fused QK Norm+RoPE on 0 sites ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#33967 [Bugfix] Fix QK Norm+RoPE fusion pattern matching on B200+FP8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200 bug;help wanted;torch.compile ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 -cc.pass_config.enable_qk_norm_rope_fusion=Tru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200 bug;help wanted;torch.compile ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 -cc.pass_config.enable_qk_norm_rope_fusion...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200 bug;help wanted;torch.compile ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 -cc.pass_config.enable_qk_norm_rope_fusion...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: QKNorm+RoPE fusion broken for qwen3-fp8 on B200 bug;help wanted;torch.compile ### Your current environment ### 🐛 Describe the bug ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 -cc.pass_config.enable_qk_norm_rope_fusion...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: mpling_logits;speculative_decoding activation;cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency #33967 [Bugfix] Fix QK Norm+RoPE fusion pattern matching on B200+FP8 Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33967](https://github.com/vllm-project/vllm/pull/33967) | closes_keyword | 0.95 | [Bugfix] Fix QK Norm+RoPE fusion pattern matching on B200+FP8 | Fixes #33295 On B200 with FP8-quantized models (e.g., `Qwen/Qwen3-30B-A3B-FP8`), PyTorch Inductor's CSE fails to merge identical `split_with_sizes` calls. The QK Norm+RoPE pattern |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
