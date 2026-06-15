# vllm-project/vllm#23517: [Bug]: EngineCore died unexpectedly When Inference llama(generate)

| 字段 | 值 |
| --- | --- |
| Issue | [#23517](https://github.com/vllm-project/vllm/issues/23517) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore died unexpectedly When Inference llama(generate)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My script runs inference on the Llama2-7b model using 2 GPUs with tensor parallelism and float16 precision. During inference, I observed: When instantiating the LLM, GPU memory usage suddenly spikes (from 7 GB → 14 GB per GPU). I’m not sure why—could it be due to CUDA Graph capture or KV cache allocation? During token generation, an error occurs: “engine core died unexpectedly”. ```python from vllm import LLM llm = LLM("/home/workspace/models/llama2-7b-hf", dtype="float16", tensor_parallel_size=2, max_seq_len_to_capture=256, max_model_len=256, gpu_memory_utilization=0.9, disable_log_stats=False) output = llm.generate("hello, my gpu! How are you feeling today? please tell") print(output) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the Llama2-7b model using 2 GPUs with tensor parallelism and float16 precision. During inference, I observed: When instantiating the LLM, GPU memory usage suddenly spikes (from 7 GB → 14 GB per GPU). I’m not sure why—co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nference on the Llama2-7b model using 2 GPUs with tensor parallelism and float16 precision. During inference, I observed: When instantiating the LLM, GPU memory usage suddenly spikes (from 7 GB → 14 GB per GPU). I’m not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: runs inference on the Llama2-7b model using 2 GPUs with tensor parallelism and float16 precision. During inference, I observed: When instantiating the LLM, GPU memory usage suddenly spikes (from 7 GB → 14 GB per GPU). I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: EngineCore died unexpectedly When Inference llama(generate) bug;unstale ### Your current environment ### 🐛 Describe the bug My script runs inference on the Llama2-7b model using 2 GPUs with tensor parallelism and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: EngineCore died unexpectedly When Inference llama(generate) bug;unstale ### Your current environment ### 🐛 Describe the bug My script runs inference on the Llama2-7b model using 2 GPUs with tensor parallelism and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
