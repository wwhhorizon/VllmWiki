# vllm-project/vllm#30995: [Bug]: Fused MoE errors without safe serialization

| 字段 | 值 |
| --- | --- |
| Issue | [#30995](https://github.com/vllm-project/vllm/issues/30995) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fused MoE errors without safe serialization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM MoE LoRA loading errors if the lora was saved without safe_serialization: ``` RuntimeError: Worker failed with error 'While loading /vast_storage/afterburner/afterburner-20251217-fsdp2-qwen30ba3b-grpo-seed-0/lora/step_0, expected target modules in ['experts.48.gate_proj', 'experts.68.down_proj', 'experts.65.gate_proj', 'experts.48.down_proj', 'experts.91.up_proj', 'experts.61.down_proj', … 'experts.109.down_proj'] but received ['up_proj', 'down_proj', 'gate_proj']. Please verify that the loaded LoRA module is correct' ``` Script to reproduce, works if and only if `SAFE_SERIALIZATION` is set to `True`: ``` #!/usr/bin/env python3 """ Minimal script to test Qwen3-30B-A3B with LoRA adapter: 1. Load model with HF + PEFT 2. Initialize and save LoRA adapter 3. Clear memory 4. Load model with VLLM 5. Load saved LoRA adapter 6. Generate example tokens """ import gc import os import torch from peft import LoraConfig, get_peft_model from transformers import AutoModelForCausalLM, AutoTokenizer from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest # Configuration MODEL_NAME = "Qwen/Qwen3-30B-A3B" LORA_SAVE_PATH =...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rror 'While loading /vast_storage/afterburner/afterburner-20251217-fsdp2-qwen30ba3b-grpo-seed-0/lora/step_0, expected target modules in ['experts.48.gate_proj', 'experts.68.down_proj', 'experts.65.gate_proj', 'experts.4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: del with VLLM 5. Load saved LoRA adapter 6. Generate example tokens """ import gc import os import torch from peft import LoraConfig, get_peft_model from transformers import AutoModelForCausalLM, AutoTokenizer from vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: model = AutoModelForCausalLM.from_pretrained( MODEL_NAME, torch_dtype=torch.bfloat16, ) print(f"Model loaded: {MODEL_NAME}") print("\n" + "=" * 80) print("Step 2: Initialize LoRA adapter") print("=" * 80) lora_config =...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Fused MoE errors without safe serialization bug ### Your current environment ### 🐛 Describe the bug VLLM MoE LoRA loading errors if the lora was saved without safe_serialization: ``` RuntimeError: Worker failed w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ar memory") print("=" * 80) del peft_model del model gc.collect() torch.cuda.empty_cache() print("Memory cleared") print("\n" + "=" * 80) print("Step 5: Load model with VLLM") print("=" * 80) llm = LLM( model=MODEL_NAME...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
