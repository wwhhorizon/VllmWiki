# vllm-project/vllm#13401: [Bug]: When using the method, it was found that for Chinese, when processing a batch of data, there are always some data that cannot be recognized at all, or the recognized content is completely incorrect.

| 字段 | 值 |
| --- | --- |
| Issue | [#13401](https://github.com/vllm-project/vllm/issues/13401) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using the method, it was found that for Chinese, when processing a batch of data, there are always some data that cannot be recognized at all, or the recognized content is completely incorrect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the method, it was found that for Chinese, when processing a batch of data, there are always some data that cannot be recognized at all, or the recognized content is completely incorrect. `import time import librosa # Make sure to install librosa if you haven't already from vllm import LLM, SamplingParams import torch.distributed as dist # Function to load audio from a local file def load_audio(file_path): audio, sample_rate = librosa.load(file_path, sr=None) # Load audio with original sample rate return audio, sample_rate # Create a Whisper encoder/decoder model instance llm = LLM( model="/tmp/pycharm123/model/whisper-large-v3", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", ) # Load your local audio files mary_had_lamb_audio, mary_had_lamb_sr = load_audio("./zhibo.wav") winning_call_audio, winning_call_sr = load_audio("./test_16k_15s.wav") print(mary_had_lamb_audio) prompts = [ { "prompt": " 中文", "multi_modal_data": { "audio": (mary_had_lamb_audio, mary_had_lamb_sr), }, } ] # Create a sampling params object. sampling_params = SamplingParams( temperature=0, top_p=1.0, max_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e recognized at all, or the recognized content is completely incorrect. `import time import librosa # Make sure to install librosa if you haven't already from vllm import LLM, SamplingParams import torch.distributed as...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, kv_cache_dtype="fp8", ) # Load your local audio files mary_had_lamb_audio, mary_had_lamb_sr = load_audio("./zhibo.wav") winning_call_audio, winning_call_sr = load_audi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e rate return audio, sample_rate # Create a Whisper encoder/decoder model instance llm = LLM( model="/tmp/pycharm123/model/whisper-large-v3", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, kv_cac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: al sample rate return audio, sample_rate # Create a Whisper encoder/decoder model instance llm = LLM( model="/tmp/pycharm123/model/whisper-large-v3", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ()` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
