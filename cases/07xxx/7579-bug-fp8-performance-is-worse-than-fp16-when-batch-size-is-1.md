# vllm-project/vllm#7579: [Bug]: fp8 performance is worse than fp16 when batch size is 1

| 字段 | 值 |
| --- | --- |
| Issue | [#7579](https://github.com/vllm-project/vllm/issues/7579) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fp8 performance is worse than fp16 when batch size is 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams import time import os import json prompts = ['What is apple?'] # Create a sampling params object. sampling_params = SamplingParams(max_tokens=256, temperature=0, top_p=0.8, top_k=40, ignore_eos=True) # Create an LLM. # the model is https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct llm = LLM(model="deepseek-ai/deepseek-coder-6.7b-instruct", max_model_len=10000, max_num_seqs=60, tensor_parallel_size=2, enforce_eager=True, quantization='fp8', distributed_executor_backend='ray') # warm up outputs = llm.generate(prompts, sampling_params) outputs = llm.generate(prompts, sampling_params) start = time.time() outputs = llm.generate(prompts, sampling_params) end = time.time() print('all_time is : {}'.format(end-start)) # Print the outputs. ``` the time of fp8 is 4.700 in l20 the time of fp16 is 3.15 in l20 fp8 performance is worse then fp16 when tp = 2 and batch_size = 1 in l20

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e ### Your current environment ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams import time import os import json prompts = ['What is apple?'] # Create a sampling params object. sampling_params = Sampling...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: fp8 performance is worse than fp16 when batch size is 1 bug;stale ### Your current environment ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams import time import os import json prompts = ['What is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rature=0, top_p=0.8, top_k=40, ignore_eos=True) # Create an LLM. # the model is https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct llm = LLM(model="deepseek-ai/deepseek-coder-6.7b-instruct", max_model_len=1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: quantization='fp8', distributed_executor_backend='ray') # warm up outputs = llm.generate(prompts, sampling_params) outputs = llm.generate(prompts, sampling_params) start = time.time() outputs = llm.generate(prompts, sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted_parallel;hardware_porting;model_support;quantization;sampling_logits cuda;fp8;operator;quantization;sampling;triton build_error dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
