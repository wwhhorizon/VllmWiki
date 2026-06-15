# vllm-project/vllm#12047: [Usage]: meta/lLlama-3.1-8B-Instruct with vllm class very slow in comparision to other models

| 字段 | 值 |
| --- | --- |
| Issue | [#12047](https://github.com/vllm-project/vllm/issues/12047) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: meta/lLlama-3.1-8B-Instruct with vllm class very slow in comparision to other models

### Issue 正文摘录

### Your current environment Running 2 Nvidia A30 GPUs. Environment works perfectly fine for non-llama models. ### How would you like to use vllm I initialize models based on the following snipped: ``` llm = LLM(model=args.llm_identifier) sampling_params = llm.get_default_sampling_params() sampling_params.max_tokens = 1024 # Generate texts from the prompts outputs = llm.generate(prompts, sampling_params) ``` When using this code with [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) it is significantly faster than running [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). Also the output for the Llama Model is much longer and does not really refer to the prompt. These are my prompt templates: ``` template = """ : {system_prompt} : {user_prompt} : """ system_prompt = """ You are a helpful assistant. Your task is to extract information from the given text into a markdown table. - You MUST only Output the markdown table. Do NOT include any headers, comments, explanations, or additional text. - If the input lacks enough data for a table, output an empty markdown table with placeholder headers. Example format: | Header 1 | Header 2 |...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: meta/lLlama-3.1-8B-Instruct with vllm class very slow in comparision to other models usage ### Your current environment Running 2 Nvidia A30 GPUs. Environment works perfectly fine for non-llama models. ### How...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: at all by just concatenating system_prompt and user_prompt - define the bfloat16 dtype when initializing `LLM() ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ulting in 3-4 hours. I am asking myself why is that so? Are there any specifics regarding the llama model that is haven't considered? What i tried: - Changing the `template` to use starting and closing tags - Changing t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: () ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
