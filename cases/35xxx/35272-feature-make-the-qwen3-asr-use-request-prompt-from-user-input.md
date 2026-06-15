# vllm-project/vllm#35272: [Feature]: Make the Qwen3-ASR use `request_prompt` from user input

| 字段 | 值 |
| --- | --- |
| Issue | [#35272](https://github.com/vllm-project/vllm/issues/35272) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make the Qwen3-ASR use `request_prompt` from user input

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current implementation of Qwen3-ASR for [](https://github.com/vllm-project/vllm/blob/24650715105a26b41c88f4164777b5e1a0f3200b/vllm/model_executor/models/qwen3_asr.py#L532) completely ignore user prompt, which can easily be done by just append the `request_prompt` (maybe add validation so that the `request_prompt` follow Qwen3-ASR format, e.g. `language {lang} {text}` or if language is already provided (via `to_lang`), strip the language part from the prompt. ### Alternatives Here is a simple modification in `get_generation_prompt()` for Qwen3-ASR: ```python @classmethod def get_generation_prompt( cls, audio: np.ndarray, model_config: ModelConfig, stt_config: SpeechToTextConfig, language: str | None, task_type: Literal["transcribe", "translate"], request_prompt: str, to_language: str | None, ) -> PromptType: """Get the generation prompt to be used for transcription requests. When ``request_prompt`` is provided it is appended **after** the assistant turn prefix so that the model continues from the previous transcription context (streaming / init-prompt behaviour). The expected format of ``request_prompt`` for Qwen3-ASR is the raw model output...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Make the Qwen3-ASR use `request_prompt` from user input feature request ### 🚀 The feature, motivation and pitch Current implementation of Qwen3-ASR for [](https://github.com/vllm-project/vllm/blob/24650715105...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ification in `get_generation_prompt()` for Qwen3-ASR: ```python @classmethod def get_generation_prompt( cls, audio: np.ndarray, model_config: ModelConfig, stt_config: SpeechToTextConfig, language: str | None, task_type:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: _placeholder} \n" f" assistant\n" ) else: prompt = ( f" user\n{audio_placeholder} \n" f" assistant\nlanguage {full_lang_name_to}{_ASR_TEXT_TAG}" ) # Append the request prompt (previous transcr
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Make the Qwen3-ASR use `request_prompt` from user input feature request ### 🚀 The feature, motivation and pitch Current implementation of Qwen3-ASR for [](https://github.com/vllm-project/vllm/blob/24650715105...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
