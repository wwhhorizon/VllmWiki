# vllm-project/vllm#17258: [Usage]: Does whisper model support beam search?

| 字段 | 值 |
| --- | --- |
| Issue | [#17258](https://github.com/vllm-project/vllm/issues/17258) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | fp8;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Does whisper model support beam search?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` when running with beam search, error occured the running script : device: Tesla T4 ``` import time from vllm import LLM, SamplingParams from vllm.sampling_params import BeamSearchParams from vllm.assets.audio import AudioAsset import librosa # Create a Whisper encoder/decoder model instance llm = LLM( model="openai/whisper-medium", max_model_len=256, max_num_seqs=32, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", ) audio_path = "xxx.wav" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": librosa.load(audio_path, sr=None), }, } ] * 1 # Create a sampling params object. sampling_params = SamplingParams( temperature=0, top_p=1.0, max_tokens=200, ) sampling_params = BeamSearchParams(beam_width=5, max_tokens=50) start = time.time() # Generate output tokens from the prompts. The output is a list of # RequestOutput objects that contain the prompt, generated # text, and other information. #outputs = llm.generate(prompts, sampling_params) outputs = llm.beam_search(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt encoder_prompt = output.encoder_prompt g...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: max_num_seqs=32, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", ) audio_path = "xxx.wav" prompts = [ { "prompt": " ", "multi_modal_data": { "audio": librosa.load(audio_path, sr=None), }, } ] * 1 # Create a samp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: th beam search, error occured the running script : device: Tesla T4 ``` import time from vllm import LLM, SamplingParams from vllm.sampling_params import BeamSearchParams from vllm.assets.audio import AudioAsset import...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Does whisper model support beam search? usage ### Your current environment ```text The output of `python collect_env.py` ``` when running with beam search, error occured the running script : device: Tesla T4 ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ssets.audio import AudioAsset import librosa # Create a Whisper encoder/decoder model instance llm = LLM( model="openai/whisper-medium", max_model_len=256, max_num_seqs=32, limit_mm_per_prompt={"audio": 1}, kv_cache_dty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Does whisper model support beam search? usage ### Your current environment ```text The output of `python collect_env.py` ``` when running with beam search, error occured the running script : device: Tesla T4 ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
