# vllm-project/vllm#8803: [Misc]: Strange `leaked shared_memory` warnings reported by multiprocessing when using vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8803](https://github.com/vllm-project/vllm/issues/8803) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Strange `leaked shared_memory` warnings reported by multiprocessing when using vLLM

### Issue 正文摘录

### Anything you want to discuss about vllm. Here is a simple example to run vLLM. When I add `import multiprocessing` and set `tensor_paralle_size > 1 `(in my code, the value is 2), I meet annoying warnings `leaked shared_memory`. When I remove the `import multiprocessing` or set `tensor_paralle_size=1`, everything is OK. (plz note that I say `or`) I am not sure whether this warning would cause future memory problems? Thx for any attention! ```python import multiprocessing # one of the variants that trigger warnings from vllm import LLM, SamplingParams from transformers import ( AutoTokenizer, ) tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-7B-Instruct") sampling_path = SamplingParams(temperature=0.7, top_p=0.8, repetition_penalty=1.05, max_tokens=512) model = LLM(model="Qwen/Qwen2.5-Coder-7B-Instruct", dtype="half", tensor_parallel_size=2) # tensor_parallel_size is the other variant that trigger warnings message = [ {"role": "system", "content": "your are a helpful assistant"}, {"role": "user", "content": "hello world!"} ] text = tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True) outputs = model.generate([text], sampling_params=sam...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: discuss about vllm. Here is a simple example to run vLLM. When I add `import multiprocessing` and set `tensor_paralle_size > 1 `(in my code, the value is 2), I meet annoying warnings `leaked shared_memory`. When I remov...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 23] Killing local vLLM worker processes [rank0]:[W925 12:12:17.096459736 CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] /root/anaconda3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mport ( AutoTokenizer, ) tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-7B-Instruct") sampling_path = SamplingParams(temperature=0.7, top_p=0.8, repetition_penalty=1.05, max_tokens=512) model = LLM(model=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 5, max_tokens=512) model = LLM(model="Qwen/Qwen2.5-Coder-7B-Instruct", dtype="half", tensor_parallel_size=2) # tensor_parallel_size is the other variant that trigger warnings message = [ {"role": "system", "content": "y...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: llo world!"} ] text = tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True) outputs = model.generate([text], sampling_params=sampling_path) print(outputs[0].outputs[0].text) ``` warning log...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
