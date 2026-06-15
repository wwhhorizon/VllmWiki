# vllm-project/vllm#35734: [Bug]: LoRA loading fails for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers)`

| 字段 | 值 |
| --- | --- |
| Issue | [#35734](https://github.com/vllm-project/vllm/issues/35734) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA loading fails for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers)`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading a PEFT LoRA checkpoint that targets modules inside `nn.Sequential` or `nn.ModuleList` (e.g., `to_out.0`), vLLM has two related failures: 1. **Validation failure** – `check_unexpected_modules` raises `ValueError`, incorrectly treating the module as unexpected. 2. **Silent weight drop** – Even if validation is bypassed, `_get_lora_layer_weights` cannot match the LoRA weight key `to_out.0` to the vLLM model's module name `to_out`, so the LoRA weights are silently ignored. ### Error message ``` ValueError: While loading /path/to/lora, expected target modules in {'to_out', 'to_q', 'to_k', 'to_v'} but received ['transformer_blocks.0.attn.to_out.0', 'transformer_blocks.1.attn.to_out.0', ...]. Please verify that the loaded LoRA module is correct ``` ### Root cause **Validation** (`lora_model.py`, `check_unexpected_modules`): ```python # Current code extracts the last dot-segment as the module suffix: elif module_name.rsplit(".", 1)[-1] not in expected_lora_modules: unexpected_modules.append(module_name) ``` For `transformer_blocks.0.attn.to_out.0`, `rsplit(".", 1)[-1]` returns `"0"`, which is the numeric `ModuleList` index —...

## 现有链接修复摘要

#35732 [Bugfix]: Fix LoRA loading failure for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: thon # 1. Train a LoRA with PEFT targeting a ModuleList member from peft import LoraConfig config = LoraConfig(target_modules=["to_k", "to_q", "to_v", "to_out"]) # PEFT resolves to_out → to_out.0 (first child of ModuleL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: a_layer_weights` cannot match the LoRA weight key `to_out.0` to the vLLM model's module name `to_out`, so the LoRA weights are silently ignored. ### Error message ``` ValueError: While loading /path/to/lora, expected ta...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: LoRA loading fails for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers)` bug;stale ### Your current environment ### 🐛 Describe the bug When loading a PEFT LoRA checkpoint that targets modul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: les with numeric indices (e.g., to_out.0 in Diffusion Transformers)` bug;stale ### Your current environment ### 🐛 Describe the bug When loading a PEFT LoRA checkpoint that targets modules inside `nn.Sequential` or `nn.M...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35732](https://github.com/vllm-project/vllm/pull/35732) | closes_keyword | 0.95 | [Bugfix]: Fix LoRA loading failure for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers) | Fix LoRA loading failure for modules with numeric indices (e.g., to_out.0 in Diffusion Transformers) #35734 - vLLM version: latest main - PyTorch version: 2.10.0 - Python version |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
