# vllm-project/vllm#19439: [Performance]: Higher latency after using tensor parallelism on whisper turbo

| 字段 | 值 |
| --- | --- |
| Issue | [#19439](https://github.com/vllm-project/vllm/issues/19439) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Higher latency after using tensor parallelism on whisper turbo

### Issue 正文摘录

### Report of performance regression I am observing higher latency after using tensor parallelism. I am running the script below on A100x2 GPU. For tensor_parallel_size=1, the latency comes out to be 92ms and for tensor_parallel_size=2, the latency is 112ms which is counter intutive. ```python from vllm import LLM from vllm.assets.audio import AudioAsset import time model_id = "openai/whisper-large-v3-turbo" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("mary_had_lamb").audio_and_sample_rate, }, } ] def get_transcript(llm, prompts): outputs = llm.generate(prompts) return outputs[0].outputs[0].text llm = LLM( model=model_id, dtype="bfloat16", tensor_parallel_size=2, ) num_iters = 100 start_time = time.monotonic() for i in range(num_iters): get_transcript(llm, prompts) end_time = time.monotonic() print(f"Average latency: {1000 * (end_time - start_time) / num_iters} ms") ``` ### Your current environment (if you think it is necessary) ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: =2, the latency is 112ms which is counter intutive. ```python from vllm import LLM from vllm.assets.audio import AudioAsset import time model_id = "openai/whisper-large-v3-turbo" prompts = [ { "prompt": " ", "multi_moda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: Higher latency after using tensor parallelism on whisper turbo performance;stale ### Report of performance regression I am observing higher latency after using tensor parallelism. I am running the script...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: return outputs[0].outputs[0].text llm = LLM( model=model_id, dtype="bfloat16", tensor_parallel_size=2, ) num_iters = 100 start_time = time.monotonic() for i in range(num_iters): get_transcript(llm, prompts) end_time = t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: om vllm import LLM from vllm.assets.audio import AudioAsset import time model_id = "openai/whisper-large-v3-turbo" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("mary_had_lamb").audio_and_sample...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Higher latency after using tensor parallelism on whisper turbo performance;stale ### Report of performance regression I am observing higher latency after using tensor parallelism. I am running the script...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
