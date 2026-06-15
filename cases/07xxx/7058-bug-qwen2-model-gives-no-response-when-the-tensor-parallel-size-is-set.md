# vllm-project/vllm#7058: [Bug]: Qwen2 model gives no response when the tensor_parallel_size is set to 1.

| 字段 | 值 |
| --- | --- |
| Issue | [#7058](https://github.com/vllm-project/vllm/issues/7058) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2 model gives no response when the tensor_parallel_size is set to 1.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained('/ProjectRoot/long_content_LLM/qwen/Qwen2-1___5B-Instruct') texts = [] # Prepare your prompts # 定义批量数据 prompts = [ "宪法规定的公民法律义务有", "属于专门人民法院的是", "无效婚姻的种类包括", "刑事案件定义", "税收法律制度", ] for prompt in prompts: messages = [ {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) texts.append(text) sampling_params = SamplingParams(temperature=0.1, top_p=0.5, max_tokens=4096) path = '/ProjectRoot/long_content_LLM/qwen/Qwen2-1___5B-Instruct' llm = LLM(model=path, trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=2, dtype=torch.float16) outputs = llm.generate(texts, sampling_params) # 输出结果 for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: , trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=2, dtype=torch.float16) outputs = llm.generate(texts, sampling_params) # 输出结果 for output in outputs: prompt = output.prompt generated_text = output.o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2 model gives no response when the tensor_parallel_size is set to 1. bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug from vllm import LLM, SamplingPar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: output of `python collect_env.py` ``` ### 🐛 Describe the bug from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained(...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: xt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) texts.append(text) sampling_params = SamplingParams(temperature=0.1, top_p=0.5, max_tokens=4096) path = '/ProjectRoot/long_conte...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
