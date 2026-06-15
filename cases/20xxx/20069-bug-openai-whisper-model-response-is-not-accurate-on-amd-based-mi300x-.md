# vllm-project/vllm#20069: [Bug]: openai whisper model response is not accurate on AMD-based(MI300x) systems.

| 字段 | 值 |
| --- | --- |
| Issue | [#20069](https://github.com/vllm-project/vllm/issues/20069) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai whisper model response is not accurate on AMD-based(MI300x) systems.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While testing the Whisper model (openai/whisper-large-v3,openai/whisper-large-v3-turbo), I observed that the model's responses are not proper. Based on my observations, I successfully deployed the Whisper model on both AMD and NVIDIA GPUs. However, the responses to the same audio input differ significantly. On CUDA/NVIDIA, the model responds correctly. On AMD/ROCm: a. Using openai/whisper-large-v3-turbo, the output is a random string. b. Using openai/whisper-large-v3, the response is empty. Both models work as expected on NVIDIA machines, so this behavior seems specific to AMD/ROCm. ```shell vllm serve openai/whisper-large-v3-turbo --uvicorn-log-level debug --trust-remote-code --tensor-parallel-size 1 ``` Query code: ```python from openai import OpenAI from vllm.assets.audio import AudioAsset client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1") # Choose your audio file audio_path = AudioAsset("mary_had_lamb").get_local_path() with open(audio_path, "rb") as f: resp = client.audio.transcriptions.create( file=f, model="openai/whisper-large-v3-turbo", language="en", response_format="text", # or "json" temperature=0.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: th models work as expected on NVIDIA machines, so this behavior seems specific to AMD/ROCm. ```shell vllm serve openai/whisper-large-v3-turbo --uvicorn-log-level debug --trust-remote-code --tensor-parallel-size 1 ``` Qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: openai whisper model response is not accurate on AMD-based(MI300x) systems. bug;rocm ### Your current environment ### 🐛 Describe the bug While testing the Whisper model (openai/whisper-large-v3,openai/whisper-lar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: tomatically detected platform rocm. DEBUG 06-25 10:03:24 [client.py:194] Waiting for output from MQLLMEngine. INFO 06-25 10:03:25 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-25 10:03:25 [_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: :14 [config.py:923] CUDA graph is not supported for whisper on ROCm yet, fallback to eager mode. WARNING 06-25 10:03:14 [arg_utils.py:1583] --task transcription is not supported by the V1 Engine. Falling back to V0. WAR...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: bug;rocm ### Your current environment ### 🐛 Describe the bug While testing the Whisper model (openai/whisper-large-v3,openai/whisper-large-v3-turbo), I observed that the model's responses are not proper. Based on my obs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
