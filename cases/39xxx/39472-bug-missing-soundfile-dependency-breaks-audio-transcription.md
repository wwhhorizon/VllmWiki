# vllm-project/vllm#39472: [Bug]: Missing `soundfile` dependency breaks audio transcription

| 字段 | 值 |
| --- | --- |
| Issue | [#39472](https://github.com/vllm-project/vllm/issues/39472) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing `soundfile` dependency breaks audio transcription

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug The `/v1/audio/transcriptions` endpoint returns `{"error": "Invalid or unsupported audio file."}` for valid audio files when `soundfile` is not installed. ## Root cause 1. `soundfile` is only in `requirements/test.in`, not in `requirements/common.txt`. A normal `uv pip install -e .` won't install it. 2. When `soundfile` is missing, it becomes a `PlaceholderModule`. The except `soundfile.LibsndfileError` in `load_audio()` (`vllm/multimodal/media/audio.py:142`) then raises an `ImportError` when evaluating the exception type. This `ImportError` is not caught by the except clause and bubbles up to `speech_to_text.py:200`, where it gets caught by a generic except Exception and replaced with the misleading "Invalid or unsupported audio file." message. ## Proposed fix 1. Add `soundfile` to `requirements/common.txt` 2. Handle `ImportError` explicitly in `load_audio()` so a missing `soundfile` either falls through to `pyav` or raises a clear message like "`Audio loading requires 'soundfile' or 'av' package. Install with: pip install soundfile`" ### Before submitting a new issue... - [x] Make sure you already searched for relevant i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Missing `soundfile` dependency breaks audio transcription bug ### Your current environment ### 🐛 Describe the bug ## Bug The `/v1/audio/transcriptions` endpoint returns `{"error": "Invalid or unsupported audio fi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Module`. The except `soundfile.LibsndfileError` in `load_audio()` (`vllm/multimodal/media/audio.py:142`) then raises an `ImportError` when evaluating the exception type. This `ImportError` is not caught by the except cl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e`" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is not installed. ## Root cause 1. `soundfile` is only in `requirements/test.in`, not in `requirements/common.txt`. A normal `uv pip install -e .` won't install it. 2. When `soundfile` is missing, it becomes a `Placehol...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;multimodal_vlm;sampling_logits;speculative_decoding cuda;sampling;triton build_error;import_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
