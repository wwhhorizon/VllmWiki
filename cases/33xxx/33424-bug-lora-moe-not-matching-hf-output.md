# vllm-project/vllm#33424: [Bug]: LoRA MoE Not Matching HF Output

| 字段 | 值 |
| --- | --- |
| Issue | [#33424](https://github.com/vllm-project/vllm/issues/33424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA MoE Not Matching HF Output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to get the outputs from the vLLM and HF LoRA implementations on MoE layers to match, but they only match for 15/25 prompts. I set the temperature to 0, use batch invariance, and set a fixed PyTorch seed. Thank you for the help! The script that I used to compare the outputs: ```python import os import torch import gc from typing import List from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest from transformers import AutoModelForCausalLM, AutoTokenizer from peft import PeftModel from peft import PeftConfig # ============================================================================== # CRITICAL FIXES FOR BLACKWELL (SM_103a) # ============================================================================== os.environ["VLLM_USE_V1"] = "0" os.environ["TORCH_COMPILE_DISABLE"] = "1" # Set seeds for reproducible results torch.manual_seed(42) # CPU if torch.cuda.is_available(): torch.cuda.manual_seed_all(42) # all GPUs # ============================================================================== # Configuration MODEL_PATH = "Qwen/Qwen1.5-MoE-A2.7B" LORA_PATH = "sai-lakkshmii/Qwen1.5-MoE-A2.7B-squa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: LoRA MoE Not Matching HF Output bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to get the outputs from the vLLM and HF LoRA implementations on MoE layers to match, but they only match f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: for the help! The script that I used to compare the outputs: ```python import os import torch import gc from typing import List from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest from transfo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: =================================================== # CRITICAL FIXES FOR BLACKWELL (SM_103a) # ============================================================================== os.environ["VLLM_USE_V1"] = "0" os.environ["T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: LoRA MoE Not Matching HF Output bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to get the outputs from the vLLM and HF LoRA implementations on MoE layers to match, but they only match f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: but they only match for 15/25 prompts. I set the temperature to 0, use batch invariance, and set a fixed PyTorch seed. Thank you for the help! The script that I used to compare the outputs: ```python import os import to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
