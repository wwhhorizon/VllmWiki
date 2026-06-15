# vllm-project/vllm#10627: [Bug]: Crash with Qwen2-Audio Model in vLLM During Audio Processing

| 字段 | 值 |
| --- | --- |
| Issue | [#10627](https://github.com/vllm-project/vllm/issues/10627) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash with Qwen2-Audio Model in vLLM During Audio Processing

### Issue 正文摘录

### Your current environment ### Model Input Dumps [dump.zip](https://github.com/user-attachments/files/17899909/dump.zip) ### 🐛 Describe the bug When running the Qwen2-Audio model with vLLM for audio transcription tasks, the process may crash with a RuntimeError due to a shape mismatch during tensor operations. Host the Qwen2-Audio Server: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct--dtype=bfloat16 --port=5000 --served-model-name qwen2-audio-7b-instruct --gpu_memory_utilization=0.95 ``` Submit an audio file for text transcription: ```bash curl https://mtt0f4kcgk6iw5-5000.proxy.runpod.net//v1/chat/completions \ -X POST \ -H 'Content-Type: application/json' \ -d '{ "model": "qwen2-audio-7b-instruc", "max_tokens":512, "temperature":0.01, "messages" : [{ "role": "user", "content": [ {"type": "audio_url", "audio_url": {"url": "xxx.mp3"}}, {"type": "text", "text": “提取文本"}]}] }' ``` Error log: ```bash NFO 11-24 17:46:31 logger.py:37] Received request chatcmpl-247fa5bbcca64896b269dc58fe916d23: prompt: ' system\nYou are responsible for transcribing audio recordings into text. \n user\nAudio 1: \n提取文字 \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Crash with Qwen2-Audio Model in vLLM During Audio Processing bug;stale ### Your current environment ### Model Input Dumps [dump.zip](https://github.com/user-attachments/files/17899909/dump.zip) ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: x_tokens=512, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: No...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the Qwen2-Audio Server: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct--dtype=bfloat16 --port=5000 --served-model-name qwen2-audio-7b-instruct --gpu_memory_utilization=0.95 ``` Submit an audio file for text transcripti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: iption tasks, the process may crash with a RuntimeError due to a shape mismatch during tensor operations. Host the Qwen2-Audio Server: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct--dtype=bfloat16 --port=5000 --served...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Crash with Qwen2-Audio Model in vLLM During Audio Processing bug;stale ### Your current environment ### Model Input Dumps [dump.zip](https://github.com/user-attachments/files/17899909/dump.zip) ### 🐛 Describe the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
