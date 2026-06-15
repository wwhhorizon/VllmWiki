# vllm-project/vllm#19183: [Usage]: Getting empty output for whsiperv3

| 字段 | 值 |
| --- | --- |
| Issue | [#19183](https://github.com/vllm-project/vllm/issues/19183) |
| 状态 | closed |
| 标签 | usage;stale;multi-modality |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Getting empty output for whsiperv3

### Issue 正文摘录

### Your current environment ```text from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset from librosa import load as load_audio # Create a Whisper encoder/decoder model instance llm = LLM( # model="openai/whisper-large-v3", model = "", trust_remote_code=True, max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", task='transcription', dtype="bfloat16", enforce_eager=False, max_logprobs=1 ) (waveform,sampling_rate)= load_audio('./sample.wav',sr=16000, mono=True) prompts = [ { "prompt": " ", "multi_modal_data": { "audio": (waveform,sampling_rate), }, } ]*1 #tried below also but same error # prompts = [ # { # "encoder_prompt":{ # "prompt":"", # "multi_modal_data":{"audio":(waveform,sampling_rate)}, # }, # "decoder_prompt":{ # "prompt_token_ids":[ # 50258, # 'en', # 50360, # 1 # ] # } # } # ] * 1 # , # { # Test explicit encoder/decoder prompt # "encoder_prompt": { # "prompt": "", # "multi_modal_data": { # "audio": (waveform,sampling_rate), # }, # }, # "decoder_prompt": " ", # } # Create a sampling params object. sampling_params = SamplingParams( temperature=0, top_p=1.0, max_tokens=400, detokenize=False, skip_special_toke...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", task='transcription', dtype="bfloat16", enforce_eager=False, max_logprobs=1 ) (waveform,sampling_rate)= load_audio('./sample.wav',sr=16000, mono=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Getting empty output for whsiperv3 usage;stale;multi-modality ### Your current environment ```text from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset from librosa import load as load_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: age;stale;multi-modality ### Your current environment ```text from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset from librosa import load as load_audio # Create a Whisper encoder/decoder model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .10 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: p8", task='transcription', dtype="bfloat16", enforce_eager=False, max_logprobs=1 ) (waveform,sampling_rate)= load_audio('./sample.wav',sr=16000, mono=True) prompts = [ { "prompt": " ", "multi_modal_data": { "audio": (wa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
