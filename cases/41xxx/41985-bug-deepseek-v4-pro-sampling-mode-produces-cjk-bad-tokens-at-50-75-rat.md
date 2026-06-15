# vllm-project/vllm#41985: [Bug] DeepSeek-V4-Pro sampling mode produces CJK bad tokens at ~50-75% rate; SGLang is unaffected

| 字段 | 值 |
| --- | --- |
| Issue | [#41985](https://github.com/vllm-project/vllm/issues/41985) |
| 状态 | closed |
| 标签 | DSv4 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;fp8;gemm;kernel;moe;quantization;sampling |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] DeepSeek-V4-Pro sampling mode produces CJK bad tokens at ~50-75% rate; SGLang is unaffected

### Issue 正文摘录

# [Bug] DeepSeek-V4-Pro sampling mode produces CJK bad tokens at ~50-75% rate; SGLang is unaffected ## Environment - **Model**: `deepseek-ai/DeepSeek-V4-Pro` - **Hardware**: 8× NVIDIA H200 (Hopper, SM90) - **vLLM version**: v0.20.1rc1 (nightly) and v0.20.0 (stable) - **Docker image**: `vllm/vllm-openai:nightly` and `vllm/vllm-openai:v0.20.0-cu130-ubuntu2404` ## Problem When serving DeepSeek-V4-Pro with vLLM, English code output randomly contains CJK (Chinese) tokens at a rate of ~50-75% of requests under temperature=1.0 sampling. This makes the model unusable for code generation tasks. Example bad output: ``` "nodemon": "^»接收«3.0.1 self.tokens = »充«0 rate_limit=»一枝«2.0 float = »充电«0.1 order: int = »去打«3 ``` Key characteristics: - Bad tokens almost always appear at positions expecting numbers, punctuation, or version strings - Per-token bad rate is ~0.03-0.04% - Typical bad tokens: 去打, 走出, 充电, 一枝, 丛, 电量, 全面的, 蛮, 蛁, 贯彻 - **SGLang with the same model, hardware, and marlin MoE backend produces ZERO bad tokens** - The official DeepSeek inference (tilelang FP32) has ~20% bad token rate ## Two Independent Issues ### Issue 1: FP4 Rounding Error (Greedy, already fixed by #41015) vLLM's `_e...

## 现有链接修复摘要

#41015 [DSv4] Use `cvt` PTX for FP32->FP4 conversion | #41083 [Quantization] add humming mxfp4 moe backend

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: g FP32) has ~20% bad token rate ## Two Independent Issues ### Issue 1: FP4 Rounding Error (Greedy, already fixed by #41015) vLLM's `_e2m1_nibble()` used `<=` boundary comparison instead of IEEE round-to-nearest-even. Th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /DeepSeek-V4-Pro` - **Hardware**: 8× NVIDIA H200 (Hopper, SM90) - **vLLM version**: v0.20.1rc1 (nightly) and v0.20.0 (stable) - **Docker image**: `vllm/vllm-openai:nightly` and `vllm/vllm-openai:v0.20.0-cu130-ubuntu2404...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: JK bad tokens at ~50-75% rate; SGLang is unaffected ## Environment - **Model**: `deepseek-ai/DeepSeek-V4-Pro` - **Hardware**: 8× NVIDIA H200 (Hopper, SM90) - **vLLM version**: v0.20.1rc1 (nightly) and v0.20.0 (stable) -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: , 电量, 全面的, 蛮, 蛁, 贯彻 - **SGLang with the same model, hardware, and marlin MoE backend produces ZERO bad tokens** - The official DeepSeek inference (tilelang FP32) has ~20% bad token rate ## Two Independent Issues ### Iss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: de output randomly contains CJK (Chinese) tokens at a rate of ~50-75% of requests under temperature=1.0 sampling. This makes the model unusable for code generation tasks. Example bad output: ``` "nodemon": "^»接收«3.0.1 s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41015](https://github.com/vllm-project/vllm/pull/41015) | mentioned | 0.45 | [DSv4] Use `cvt` PTX for FP32->FP4 conversion | pgemm block-scaled behavior between the two frameworks ## related - #41015 - fp4 rounding fix (solves greedy bad tokens only) - #40950 - swiglu clamp fix - #40902 - deepseek v4 ro… |
| [#41083](https://github.com/vllm-project/vllm/pull/41083) | mentioned | 0.45 | [Quantization] add humming mxfp4 moe backend | ns only) - #40950 - swiglu clamp fix - #40902 - deepseek v4 roadmap - #41083 - humming moe backend (tested, not the cause) dsv4 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
