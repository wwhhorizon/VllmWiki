# vllm-project/vllm#11478: [Misc]: qwen2 vllm和transform 推理结果未对齐

| 字段 | 值 |
| --- | --- |
| Issue | [#11478](https://github.com/vllm-project/vllm/issues/11478) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: qwen2 vllm和transform 推理结果未对齐

### Issue 正文摘录

### Anything you want to discuss about vllm. vllm 0.6.5 transformers 4.41.2 vllm: import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from transformers import AutoTokenizer from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.from_pretrained("/data/models/Qwen2-7B-Instruct") sampling_params = SamplingParams(temperature=0.0, repetition_penalty=1.0, max_tokens=2048,best_of=1, top_k=-1, top_p=1) llm = LLM(model="/data/models/Qwen2-7B-Instruct", dtype='float16', gpu_memory_utilization=0.9, enforce_eager=True, trust_remote_code=True ) prompt = "Give me a short introduction to large language model." messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) outputs = llm.generate([text], sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") hf: import os os.environ["CUDA_VISIBLE_DEVICES"]="1" import torch from transformers import AutoModelForCausalLM, AutoTokenizer device = "cuda" model_path = "/data/models/Qwen2-7B-Inst...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Misc]: qwen2 vllm和transform 推理结果未对齐 stale ### Anything you want to discuss about vllm. vllm 0.6.5 transformers 4.41.2 vllm: import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from transformers import AutoTokenizer from
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: llm. vllm 0.6.5 transformers 4.41.2 vllm: import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from transformers import AutoTokenizer from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.from_pretrained("/data/m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ant to discuss about vllm. vllm 0.6.5 transformers 4.41.2 vllm: import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from transformers import AutoTokenizer from vllm import LLM, SamplingParams tokenizer = AutoTokenizer.fr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -1, top_p=1) llm = LLM(model="/data/models/Qwen2-7B-Instruct", dtype='float16', gpu_memory_utilization=0.9, enforce_eager=True, trust_remote_code=True ) prompt = "Give me a short introduction to large language model." m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: qwen2 vllm和transform 推理结果未对齐 stale ### Anything you want to discuss about vllm. vllm 0.6.5 transformers 4.41.2 vllm: import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from transformers import AutoTokenizer from...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
