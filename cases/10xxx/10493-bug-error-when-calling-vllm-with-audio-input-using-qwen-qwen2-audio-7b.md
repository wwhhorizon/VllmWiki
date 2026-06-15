# vllm-project/vllm#10493: [Bug]: Error when calling vLLM with audio input using Qwen/Qwen2-Audio-7B-Instruct model

| 字段 | 值 |
| --- | --- |
| Issue | [#10493](https://github.com/vllm-project/vllm/issues/10493) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when calling vLLM with audio input using Qwen/Qwen2-Audio-7B-Instruct model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I downloaded the [v0.6.4.post1](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1) Execute the command: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct --dtype=bfloat16 --port=5000 --gpu_memory_utilization=0.8 ``` I’m encountering an error when trying to use **_vLLM serve_** with the Qwen/Qwen2-Audio-7B-Instruct model to process audio input. Run the following curl command: ```bash curl https://huxtwsgqgqkueq-5000.proxy.runpod.net/v1/chat/completions \ -X POST \ -H 'Content-Type: application/json' \ -d '{ "model": "Qwen/Qwen2-Audio-7B-Instruct", "max_tokens": 1024, "temperature": 0.1, "messages": [ { "role": "user", "content": [ { "type": "audio_url", "audio_url": { "url": "http://modelscope-open.oss-cn-hangzhou.aliyuncs.com/images/weather.wav" } }, { "type": "text", "text": "Transcribe Text" } ] } ] }' ``` Observe the error output: ``` File "/workspace/miniconda3/envs/vllm/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 401, in run_asgi result = await app( # type: ignore[func-returns-value] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error when calling vLLM with audio input using Qwen/Qwen2-Audio-7B-Instruct model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I downloaded the [v0.6.4.post1](https:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tte/middleware/base.py", line 187, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Execute the command: ```bash vllm serve Qwen/Qwen2-Audio-7B-Instruct --dtype=bfloat16 --port=5000 --gpu_memory_utilization=0.8 ``` I’m encountering an error when trying to use **_vLLM serve_** with the Qwen/Qwen2-Audio-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
