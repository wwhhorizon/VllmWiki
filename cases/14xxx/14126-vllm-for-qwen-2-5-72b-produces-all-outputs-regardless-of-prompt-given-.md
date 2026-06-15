# vllm-project/vllm#14126: VLLM for Qwen 2.5 72B produces all !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! outputs, regardless of prompt given GPTQ 4 bits quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#14126](https://github.com/vllm-project/vllm/issues/14126) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VLLM for Qwen 2.5 72B produces all !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! outputs, regardless of prompt given GPTQ 4 bits quantization

### Issue 正文摘录

### Your current environment I performed GPTQ quantization on Qwen 72B instruct using AutoGPTQ package, with the following configuration: group_size = 32, desc_order= 32. Then I use the model inside the VLLM using the following configuration: `llm = LLM(model = model_path, max_model_len = 20000)` ``` messages = [ { "role": "system" "content": system message }, {"role": "user", "content": user message } ] tokenized_chat = tokenizer.apply_chat_template(messages, tokenize = True, add_generation_prompt = True) output = llm.generate(. . . ) ``` However regardless of prompt the outptut is always !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! The same code works perfectly fine for llama 3.3 and 3.1 70B. Is Qwen 2.5 72B not compatible with VLLM. I have the latest version of VLLM and Transformers using ``` !pip install --upgrade vllm !pip install --upgrade transformers ``` Any help would be appreciated. ### 🐛 Describe the bug The output is always !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! no matter the input and the prompt or other configurations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: VLLM for Qwen 2.5 72B produces all !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! outputs, regardless of prompt given GPTQ 4 bits quantization bug;stale ### Your current environment I performed GPTQ quantization on Qwen 72B in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d 3.1 70B. Is Qwen 2.5 72B not compatible with VLLM. I have the latest version of VLLM and Transformers using ``` !pip install --upgrade vllm !pip install --upgrade transformers ``` Any help would be appreciated. ### 🐛...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: !!!!!!!!!!!!!!!!!!!!!!!! outputs, regardless of prompt given GPTQ 4 bits quantization bug;stale ### Your current environment I performed GPTQ quantization on Qwen 72B instruct using AutoGPTQ package, with the following...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: !!!!!!! outputs, regardless of prompt given GPTQ 4 bits quantization bug;stale ### Your current environment I performed GPTQ quantization on Qwen 72B instruct using AutoGPTQ package, with the following configuration: gr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
