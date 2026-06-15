# vllm-project/vllm#17155: [Bug]: DeepSeek Lora inference has no effect.

| 字段 | 值 |
| --- | --- |
| Issue | [#17155](https://github.com/vllm-project/vllm/issues/17155) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek Lora inference has no effect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm currently fine-tuning DeepSeekV2 for self-awareness using LLaMA-Factory and Lora. However, when I deploy and infer with VLLM, I find that the Lora model has no effect. Why is that? But when I use the conventional transformers + PEFT for inference, there's no problem. When I merge DeepSeekV2 with the Lora model and then deploy it through VLLM, I find that the merged model now has the fine-tuning effect. I have modified this file to support Lora inference. Besides this, do I need to make any other changes? vllm/model_executor/models/deepseek_v2.py ```python class DeepseekV2ForCausalLM(nn.Module, SupportsPP, SupportsLoRA): packed_modules_mapping = { "gate_up_proj": [ "gate_proj", "up_proj", ], } ``` This is transformers+peft inference script ```python from transformers import AutoModelForCausalLM, AutoTokenizer import torch from peft import PeftModel mode_path = '/root/model/deepseek-ai/DeepSeek-V2-Lite-Chat' lora_path = '/root/saves/deepseek/lora/sft-global' tokenizer = AutoTokenizer.from_pretrained(mode_path, trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained(mode_path, device_map="auto",torch_dtype=torch.bfl...

## 现有链接修复摘要

#31105 [Bugfix][LoRA] Fix LoRA weight mapping for DeepSeek MLA attention and…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: This is transformers+peft inference script ```python from transformers import AutoModelForCausalLM, AutoTokenizer import torch from peft import PeftModel mode_path = '/root/model/deepseek-ai/DeepSeek-V2-Lite-Chat' lora_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: AutoModelForCausalLM.from_pretrained(mode_path, device_map="auto",torch_dtype=torch.bfloat16, trust_remote_code=True).eval() model.generation_config.pad_token_id = model.generation_config.eos_token_id prompt = "who are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e the bug I'm currently fine-tuning DeepSeekV2 for self-awareness using LLaMA-Factory and Lora. However, when I deploy and infer with VLLM, I find that the Lora model has no effect. Why is that? But when I use the conve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: DeepSeek Lora inference has no effect. bug;stale ### Your current environment ### 🐛 Describe the bug I'm currently fine-tuning DeepSeekV2 for self-awareness using LLaMA-Factory and Lora. However, when I deploy an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: return_dict=True ).to('cuda') gen_kwargs = {"max_new_tokens": 2500, "do_sample": True, "top_k": 1} with torch.no_grad(): outputs = model.generate(**inputs, **gen_kwargs) outputs = outputs[:, inputs['input_ids'].shape[1]...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31105](https://github.com/vllm-project/vllm/pull/31105) | closes_keyword | 0.95 | [Bugfix][LoRA] Fix LoRA weight mapping for DeepSeek MLA attention and… | Fixes #17155 This PR fixes three issues with LoRA adapters on DeepSeek V2/V3 models: 1. **MLA Attention Path Mapping**: DeepSeek V2/V3 models wrap attention modules in `mla_attn` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
