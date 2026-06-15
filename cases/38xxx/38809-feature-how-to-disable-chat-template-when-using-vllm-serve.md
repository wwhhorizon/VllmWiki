# vllm-project/vllm#38809: [Feature]: How to disable chat template when using vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#38809](https://github.com/vllm-project/vllm/issues/38809) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: How to disable chat template when using vllm serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi all, I'm deploying qwen 3.5 2B model, and when we using the hf model ,we use it like this, no template is used. ` model_inputs = processor( text = prompt_text, images = images, return_tensors = "pt", ) # ────────────────────────────────── input_ids = model_inputs["input_ids"].to(device) attention_mask = model_inputs["attention_mask"].to(device) pixel_values = model_inputs["pixel_values"].to(device) image_grid_thw = model_inputs["image_grid_thw"] # 保持 CPU if image_grid_thw.dim() == 1: image_grid_thw = image_grid_thw.unsqueeze(0) if use_cache_mode: new_token_ids = _greedy_generate( model = model, input_ids = input_ids, attention_mask = attention_mask, pixel_values = pixel_values, image_grid_thw = image_grid_thw, max_new_tokens = 4, )` As far as I know, the openai completion api doesn't apply templates but it doesn't support image inputs. The openai chat api supports image inputs, but always apply a chat template, which results in the fact that, the input after the template always has some template tokens different from the huggingface usage format. Do you have has suggestions about that? Thank you! ### Alternatives _No response_ ### Additio...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e request ### 🚀 The feature, motivation and pitch Hi all, I'm deploying qwen 3.5 2B model, and when we using the hf model ,we use it like this, no template is used. ` model_inputs = processor( text = prompt_text, images...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: How to disable chat template when using vllm serve feature request ### 🚀 The feature, motivation and pitch Hi all, I'm deploying qwen 3.5 2B model, and when we using the hf model ,we use it like this, no temp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
