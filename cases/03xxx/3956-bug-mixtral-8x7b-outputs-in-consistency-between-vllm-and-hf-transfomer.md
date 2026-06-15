# vllm-project/vllm#3956: [Bug]: mixtral 8x7b outputs in-consistency between vllm and HF transfomers

| 字段 | 值 |
| --- | --- |
| Issue | [#3956](https://github.com/vllm-project/vllm/issues/3956) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: mixtral 8x7b outputs in-consistency between vllm and HF transfomers

### Issue 正文摘录

### Your current environment vllm version: 0.4.0 HF transfomers versaion: 4.39.2 model: https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 GPU: V100 32G*4 ### 🐛 Describe the bug Hi , Iam trying to check mixtral 8x7b outputs consistency between vllm and HF transfomers without sampling but in some prompts , result is not consist. In my observation, prompt with Chinese words has possibility cause in-consistency results. but pure English words prompt since not to happen in-consistency results. follow is my code to test: from vllm import LLM, SamplingParams import contextlib import torch from transformers import AutoModelForCausalLM, AutoTokenizer from typing import List from accelerate import load_checkpoint_and_dispatch model_path="/models/Mixtral-8x7B-v0.1" def vllm(prompt : str): with contextlib.nullcontext(): llm = LLM(model=model_path, tokenizer=model_path, dtype="float16" ,tensor_parallel_size=4) sampling_params = SamplingParams(max_tokens=100, temperature=0) gen_res = llm.generate(prompt, sampling_params)[0].outputs[0].text print(prompt, gen_res) return prompt + gen_res def huggingface(prompt : str): model = AutoModelForCausalLM.from_pretrained(model_path, device_map='auto') to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: een vllm and HF transfomers bug;stale ### Your current environment vllm version: 0.4.0 HF transfomers versaion: 4.39.2 model: https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 GPU: V100 32G*4 ### 🐛 Describe the bug Hi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: mixtral 8x7b outputs in-consistency between vllm and HF transfomers bug;stale ### Your current environment vllm version: 0.4.0 HF transfomers versaion: 4.39.2 model: https://huggingface.co/mistralai/Mixtral-8x7B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lib.nullcontext(): llm = LLM(model=model_path, tokenizer=model_path, dtype="float16" ,tensor_parallel_size=4) sampling_params = SamplingParams(max_tokens=100, temperature=0) gen_res = llm.generate(prompt, sampling_param...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mixtral 8x7b outputs in-consistency between vllm and HF transfomers bug;stale ### Your current environment vllm version: 0.4.0 HF transfomers versaion: 4.39.2 model: https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nizer from typing import List from accelerate import load_checkpoint_and_dispatch model_path="/models/Mixtral-8x7B-v0.1" def vllm(prompt : str): with contextlib.nullcontext(): llm = LLM(model=model_path, tokenizer=model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
