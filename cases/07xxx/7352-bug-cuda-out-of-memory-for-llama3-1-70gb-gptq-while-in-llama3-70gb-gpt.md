# vllm-project/vllm#7352: [Bug]: CUDA out of memory for llama3.1 70gb gptq, while in llama3 70gb gptq doesn't

| 字段 | 值 |
| --- | --- |
| Issue | [#7352](https://github.com/vllm-project/vllm/issues/7352) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA out of memory for llama3.1 70gb gptq, while in llama3 70gb gptq doesn't

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to load LLAMA3.1 70B GPTQ and get cuda out of memory on A6000 48GB, when LLAMA3 70B GPTQ is working great. They both have 39.8gb safetensors, and 37.096gb when loading into memory, almost identical sizes. Tried a range of values of gpu_memory_utilization from 0.1 to 0.9 (I knew it won't change anything, as the regular info message of 'try reduce gpu utilization..' hasn't been shown, which means it didn't get to this stage, while in llama3 I am using 0.9 and it works great. I avoided using marlin kernels, to avoid additional problems with the tests. This is the llama3.1 70 gptq one https://huggingface.co/shuyuej/Meta-Llama-3.1-70B-Instruct-GPTQ/tree/main This is the llama3 70 gptq one https://huggingface.co/TechxGenus/Meta-Llama-3-70B-Instruct-GPTQ/tree/main ``` import os from vllm import LLM, SamplingParams os.environ["CUDA_VISIBLE_DEVICES"] = "0" # to be sure using only A6000 and not GT1030 prompts = [ "Hello, my name is" ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # llm = LLM(model="shuyuej/Meta-Llama-3.1-70B-Instruct-GPTQ", gpu_memory_utilization=0.9, dtype='float16', quantization='gptq') # does not...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /huggingface.co/TechxGenus/Meta-Llama-3-70B-Instruct-GPTQ/tree/main ``` import os from vllm import LLM, SamplingParams os.environ["CUDA_VISIBLE_DEVICES"] = "0" # to be sure using only A6000 and not GT1030 prompts = [ "H...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ="shuyuej/Meta-Llama-3.1-70B-Instruct-GPTQ", gpu_memory_utilization=0.9, dtype='float16', quantization='gptq') # does not load llm = LLM(model="TechxGenus/Meta-Llama-3-70B-Instruct-GPTQ", gpu_memory_utilization=0.9, dty...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: CUDA out of memory for llama3.1 70gb gptq, while in llama3 70gb gptq doesn't bug ### Your current environment ### 🐛 Describe the bug Trying to load LLAMA3.1 70B GPTQ and get cuda out of memory on A6000 48GB, when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf;oom dtype;env_dependency Your current...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: r_memory;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
