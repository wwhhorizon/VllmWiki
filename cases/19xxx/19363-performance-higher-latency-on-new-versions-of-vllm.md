# vllm-project/vllm#19363: [Performance]: Higher latency on new versions of vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#19363](https://github.com/vllm-project/vllm/issues/19363) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Higher latency on new versions of vllm

### Issue 正文摘录

### Report of performance regression I am observing higher latency in new versions of vllm. I am running the script below on A100 GPU. For vllm version 0.7.3 - latency is 92ms For latest version 0.9.0.1 - latency is 105ms ```python from vllm import LLM from vllm.assets.audio import AudioAsset import time model_id = "openai/whisper-large-v3-turbo" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("mary_had_lamb").audio_and_sample_rate, }, } ] def get_transcript(llm, prompts): outputs = llm.generate(prompts) return outputs[0].outputs[0].text llm = LLM( model=model_id ) num_iters = 100 start_time = time.monotonic() for i in range(num_iters): get_transcript(llm, prompts) end_time = time.monotonic() print(f"Average latency: {1000 * (end_time - start_time) / num_iters} ms") ``` ### Your current environment (if you think it is necessary) ```text ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Performance]: Higher latency on new versions of vllm performance;stale ### Report of performance regression I am observing higher latency in new versions of vllm. I am running the script below on A100 GPU. For vllm ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: higher latency in new versions of vllm. I am running the script below on A100 GPU. For vllm version 0.7.3 - latency is 92ms For latest version 0.9.0.1 - latency is 105ms ```python from vllm import LLM from vllm.assets.a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: om vllm import LLM from vllm.assets.audio import AudioAsset import time model_id = "openai/whisper-large-v3-turbo" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("mary_had_lamb").audio_and_sample...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Higher latency on new versions of vllm performance;stale ### Report of performance regression I am observing higher latency in new versions of vllm. I am running the script below on A100 GPU. For vllm ver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.52.4 [pip3] triton==3.1.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
