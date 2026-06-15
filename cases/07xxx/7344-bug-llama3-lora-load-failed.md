# vllm-project/vllm#7344: [Bug]: LLama3 LoRA load failed

| 字段 | 值 |
| --- | --- |
| Issue | [#7344](https://github.com/vllm-project/vllm/issues/7344) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLama3 LoRA load failed

### Issue 正文摘录

### Your current environment vllm 0.5.4 ### 🐛 Describe the bug I try to load llama3-8B lora model but encounter error as bellow: ValueError: While loading /models/llama3-8b-instruct-lora-0719-r64, expected target modules in ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj', 'embed_tokens', 'lm_head'] but received ['w2', 'w3', 'w1']. Please verify that the loaded LoRA module is correct I searched the issues for problems related to LoRA and found that it might be due to the lack of support for w1, w2, and w3. Additionally, the supported_lora_modules in the model of llama doesn't include these items. If I want to properly use LoRA with LLaMA3, should I avoid these layers during model finetune, or will there be support for them in the future?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: LLama3 LoRA load failed bug ### Your current environment vllm 0.5.4 ### 🐛 Describe the bug I try to load llama3-8B lora model but encounter error as bellow: ValueError: While loading /models/llama3-8b-instruct-lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , 'w3', 'w1']. Please verify that the loaded LoRA module is correct I searched the issues for problems related to LoRA and found that it might be due to the lack of support for w1, w2, and w3. Additionally, the supporte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
