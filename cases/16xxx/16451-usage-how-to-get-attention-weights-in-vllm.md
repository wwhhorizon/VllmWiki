# vllm-project/vllm#16451: [Usage]: How to get attention weights in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#16451](https://github.com/vllm-project/vllm/issues/16451) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get attention weights in vllm

### Issue 正文摘录

### Your current environment I use "transformers" getting attentions weights. My code is as follows： ``` from transformers import AutoModelForCausalLM model = AutoModelForCausalLM.from_pretrained( ""Qwen/Qwen2.5-1.5B-Instruct"", torch_dtype="auto", device_map="auto" ) generated_dict = model.generate( **model_input, max_new_tokens=250, return_dict_in_generate=True, output_attentions=True, early_stopping=True, ) atts_weights = generated_dict.attentions ``` Is there a function for this implementation in this VLLM? ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: entions weights. My code is as follows： ``` from transformers import AutoModelForCausalLM model = AutoModelForCausalLM.from_pretrained( ""Qwen/Qwen2.5-1.5B-Instruct"", torch_dtype="auto", device_map="auto" ) generated_d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: getting attentions weights. My code is as follows： ``` from transformers import AutoModelForCausalLM model = AutoModelForCausalLM.from_pretrained( ""Qwen/Qwen2.5-1.5B-Instruct"", torch_dtype="auto", device_map="auto" )...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rCausalLM.from_pretrained( ""Qwen/Qwen2.5-1.5B-Instruct"", torch_dtype="auto", device_map="auto" ) generated_dict = model.generate( **model_input, max_new_tokens=250, return_dict_in_generate=True, output_attentions=True...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to get attention weights in vllm usage;stale ### Your current environment I use "transformers" getting attentions weights. My code is as follows： ``` from transformers import AutoModelForCausalLM model = Au...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
