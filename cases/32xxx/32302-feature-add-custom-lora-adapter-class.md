# vllm-project/vllm#32302: [Feature]: ADD CUSTOM LORA ADAPTER CLASS

| 字段 | 值 |
| --- | --- |
| Issue | [#32302](https://github.com/vllm-project/vllm/issues/32302) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: ADD CUSTOM LORA ADAPTER CLASS

### Issue 正文摘录

### 🚀 The feature, motivation and pitch import torch import torch.nn as nn from peft import LoraModel from transformers import AutoModelForCausalLM, AutoTokenizer class GatedLoRAModel(nn.Module): def __init__(self, base_model_name, lora_config): super().__init__() # Base frozen GPT OSS model self.base_model = AutoModelForCausalLM.from_pretrained(base_model_name) self.base_model.requires_grad_(False) # LoRA adapted GPT OSS model (trainable) self.lora_model = LoraModel(self.base_model, lora_config, adapter_name="default") # Gating network: learns how much weight to give LoRA vs base hidden_size = self.base_model.config.hidden_size self.gate = nn.Sequential( nn.Linear(hidden_size, hidden_size // 2), nn.ReLU(), nn.Linear(hidden_size // 2, 1), nn.Sigmoid() # outputs value in [0,1] ) def forward(self, input_ids, attention_mask=None, labels=None): # Hidden states from base (frozen) with torch.no_grad(): base_out = self.base_model(input_ids, attention_mask=attention_mask, output_hidden_states=True) hidden_states = base_out.hidden_states # now this works base_logits = base_out.logits hidden = base_out.hidden_states[-1].float() # final hidden states # LoRA adapted output lora_out = self.lor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ation and pitch import torch import torch.nn as nn from peft import LoraModel from transformers import AutoModelForCausalLM, AutoTokenizer class GatedLoRAModel(nn.Module): def __init__(self, base_model_name, lora_config...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: ADD CUSTOM LORA ADAPTER CLASS feature request;stale ### 🚀 The feature, motivation and pitch import torch import torch.nn as nn from peft import LoraModel from transformers import AutoModelForCausalLM, AutoTok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: TER CLASS feature request;stale ### 🚀 The feature, motivation and pitch import torch import torch.nn as nn from peft import LoraModel from transformers import AutoModelForCausalLM, AutoTokenizer class GatedLoRAModel(nn....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rom_pretrained(base_model_name) self.base_model.requires_grad_(False) # LoRA adapted GPT OSS model (trainable) self.lora_model = LoraModel(self.base_model, lora_config, adapter_name="default") # Gating network: learns h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
