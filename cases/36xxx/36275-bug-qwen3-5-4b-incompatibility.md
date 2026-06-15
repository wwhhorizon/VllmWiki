# vllm-project/vllm#36275: [Bug]: Qwen3.5 4b incompatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#36275](https://github.com/vllm-project/vllm/issues/36275) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 4b incompatibility

### Issue 正文摘录

### Description ## Environment - vLLM: 0.16.1rc1 (nightly) - TRL: 0.28.x - Model: Qwen/Qwen3.5-4B (text-only checkpoint) - Mode: GRPOTrainer with `vllm_mode="colocate"` ## Problem When using a Qwen3.5 text-only checkpoint with vLLM's colocate mode in TRL's GRPOTrainer, vLLM instantiates `Qwen3_5ForConditionalGeneration` (the full VLM class) — the only registered class for this architecture. This causes a hard weight naming mismatch: - vLLM expects weights under: `language_model.model.layers.*` - Text-only checkpoint has weights at: `model.layers.*` (no `language_model.` prefix) ## Root Cause There is no `Qwen3_5ForCausalLM` text-only class registered in vLLM. The entire Qwen3.5 family uses a hybrid architecture (Gated DeltaNet + sparse MoE), and vLLM currently only exposes the full multimodal class `Qwen3_5ForConditionalGeneration`. When a text-only checkpoint is loaded through this class, the weight prefix mismatch causes a hard failure. This is distinct from the standalone vLLM server use case (e.g., serving `Qwen3.5-27B` as a full VLM), which works correctly because the checkpoint includes the vision encoder and weight names match. ## Expected Behavior Either: 1. A `Qwen3_5ForC...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3.5 4b incompatibility bug ### Description ## Environment - vLLM: 0.16.1rc1 (nightly) - TRL: 0.28.x - Model: Qwen/Qwen3.5-4B (text-only checkpoint) - Mode: GRPOTrainer with `vllm_mode="colocate"` ## Problem W...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ts with vLLM today? ### Reproduction ``` """Base Modal container image builder.""" import modal from shared.constants.modal import CLOUD_SQL_PROXY_URL BASE_PIP_PACKAGES: list[str] = [ "trl>=0.28.0, =0.18.0", "accelerate...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: nalGeneration` (the full VLM class) — the only registered class for this architecture. This causes a hard weight naming mismatch: - vLLM expects weights under: `language_model.model.layers.*` - Text-only checkpoint has...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: --language-model-only` flag correctly handles text-only checkpoints by remapping the weight prefix (`model.layers.*` → `language_model.model.layers.*`) and skipping vision encoder initialization ## Impact This completel...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: und None currently. Disabling vLLM (`use_vllm=False`) and accepting the throughput penalty. ## Question for maintainers Is `--language-model-only` support with correct weight prefix remapping planned for 0.17.0? Is ther...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
