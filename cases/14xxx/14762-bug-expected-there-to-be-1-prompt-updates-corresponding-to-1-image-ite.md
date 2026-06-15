# vllm-project/vllm#14762: [Bug]: Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#14762](https://github.com/vllm-project/vllm/issues/14762) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs

### Issue 正文摘录

### Your current environment ``` Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs, or there is a problem with your implementation of merged multi-modal processor for this model (usually arising from an inconsistency between `_call_hf_processor` and `_get_prompt_updates ``` This is my code, how do I correctly input images to support gemma3, request help thanks ``` def generate_text(prompt, image): prompt = "USER: \n{}\nASSISTANT:".format(prompt) sampling_params = SamplingParams( max_tokens=512, temperature=0.7, top_p=0.9, ) print(prompt) print(image) outputs = llm.generate( {"prompt":prompt,"multi_modal_data":{"image":image}}) generated_text = outputs[0].outputs[0].text return generated_text ``` ### 🐛 Describe the bug ``` Expected there to be 1 prompt updates corresponding to 1 image items, but instead found 0 prompt updates! Either the prompt text has missing/incorrect tokens for multi-modal inputs, or there is a problem with your implementation of merged multi-modal processor for this model (usually arising from an inconsistency between `_call_hf_pro...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: blem with your implementation of merged multi-modal processor for this model (usually arising from an inconsistency between `_call_hf_processor` and `_get_prompt_updates ``` This is my code, how do I correctly input ima...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: updates ``` This is my code, how do I correctly input images to support gemma3, request help thanks ``` def generate_text(prompt, image): prompt = "USER: \n{}\nASSISTANT:".format(prompt) sampling_params = SamplingParams...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ``` This is my code, how do I correctly input images to support gemma3, request help thanks ``` def generate_text(prompt, image): prompt = "USER: \n{}\nASSISTANT:".format(prompt) sampling_params = SamplingParams( max_to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
