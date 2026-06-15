# vllm-project/vllm#14040: [Bug]: RuntimeError: ('Quantization scheme is not supported for ', 'the current GPU. Min capability: 80. ', 'Current capability: 75.')

| 字段 | 值 |
| --- | --- |
| Issue | [#14040](https://github.com/vllm-project/vllm/issues/14040) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: ('Quantization scheme is not supported for ', 'the current GPU. Min capability: 80. ', 'Current capability: 75.')

### Issue 正文摘录

### Your current environment I am using google colab T4 GPU ### 🐛 Describe the bug from vllm.assets.audio import AudioAsset from vllm import LLM, SamplingParams # Load your local audio file audio_path = "audio.wav" # Replace with your actual file path audio_asset = AudioAsset(audio_path) # Prepare the model llm = LLM( model="Bakht123/whisper-medium-gptq-W4A16-G128", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, ) # Prepare inputs inputs = { "encoder_prompt": { "prompt": "", "multi_modal_data": { "audio": audio_asset.audio_and_sample_rate, # Pass the loaded audio }, }, "decoder_prompt": " ", } # Generate response print("========== SAMPLE GENERATION ==============") outputs = llm.generate(inputs, SamplingParams(temperature=0.0, max_tokens=64)) print(f"PROMPT : {outputs[0].prompt}") print(f"RESPONSE: {outputs[0].outputs[0].text}") print("==========================================") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ror: ('Quantization scheme is not supported for ', 'the current GPU. Min capability: 80. ', 'Current capability: 75.') bug;stale ### Your current environment I am using google colab T4 GPU ### 🐛 Describe the bug from vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 'the current GPU. Min capability: 80. ', 'Current capability: 75.') bug;stale ### Your current environment I am using google colab T4 GPU ### 🐛 Describe the bug from vllm.assets.audio import AudioAsset from vllm import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sing google colab T4 GPU ### 🐛 Describe the bug from vllm.assets.audio import AudioAsset from vllm import LLM, SamplingParams # Load your local audio file audio_path = "audio.wav" # Replace with your actual file path au...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: RuntimeError: ('Quantization scheme is not supported for ', 'the current GPU. Min capability: 80. ', 'Current capability: 75.') bug;stale ### Your current environment I am using google colab T4 GPU ### 🐛 Describe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: our actual file path audio_asset = AudioAsset(audio_path) # Prepare the model llm = LLM( model="Bakht123/whisper-medium-gptq-W4A16-G128", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, ) # Prepar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
