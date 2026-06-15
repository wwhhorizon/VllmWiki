# vllm-project/vllm#34380: [Bug]: GLM-5 MTP crashes with num_speculative_tokens > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#34380](https://github.com/vllm-project/vllm/issues/34380) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: GLM-5 MTP crashes with num_speculative_tokens > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This command will fail during first inference ``` vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 4 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 2 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --served-model-name glm-5-fp8 ``` Same issue as https://github.com/vllm-project/vllm/issues/31845 Replicated on B300, but would happen the same on H200 or B200. Setting to `--speculative-config.num_speculative_tokens 1` works fine ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: is command will fail during first inference ``` vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 4 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 2 \ --tool-call-parser glm47 \ --re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m/issues/31845 Replicated on B300, but would happen the same on H200 or B200. Setting to `--speculative-config.num_speculative_tokens 1` works fine ### Before submitting a new issue... - [x] Make sure you already search...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e zai-org/GLM-5-FP8 \ --tensor-parallel-size 4 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 2 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --serv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
