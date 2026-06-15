# vllm-project/vllm#38586: [Bug]: Whisper online benchmark with profiling error: TypeError: multi_modal_content must be a dict containing 'audio'

| 字段 | 值 |
| --- | --- |
| Issue | [#38586](https://github.com/vllm-project/vllm/issues/38586) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Whisper online benchmark with profiling error: TypeError: multi_modal_content must be a dict containing 'audio'

### Issue 正文摘录

### Your current environment The vLLM Benchmarking with profiling is failing for Whisper model in online benchmarking. ```bash INFO 03-30 20:45:39 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 03-30 20:45:39 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. Namespace(subparser='bench', bench_type='serve', dispatch_function= , trust_remote_code=False, seed=0, num_prompts=32, dataset_name='hf', no_stream=True, dataset_path='openslr/librispeech_asr', no_oversample=True, skip_chat_template=False, enable_multimodal_chat=False, disable_shuffle=False, custom_output_len=256, spec_bench_output_len=256, spec_bench_category=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, blazedit_min_distance=0.0, blazedit_max_distance=1.0, asr_max_audio_len_sec=inf, asr_min_audio_len_sec=0.0, random_input_len=1024, random_output_len=128, random_range_ratio=0.0, random_prefix_len=0, random_batch_size=1, no_reranker=False, random_mm_base_items_per_request=1, random_mm_num_mm_items_range_ratio=0.0, random_mm_limit_mm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: for Whisper model in online benchmarking. ```bash INFO 03-30 20:45:39 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 03-30 20:45:39 [imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: None, output_len=None, tokenizer=None, tokenizer_mode='auto', use_beam_search=False, logprobs=None, request_rate=inf, burstiness=1.0, disable_tqdm=False, num_warmups=0, profile=True, save_result=False, save_detailed=Fal...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment The vLLM Benchmarking with profiling is failing for Whisper model in online benchmarking. ```bash INFO 03-30 20:45:39 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disablin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Whisper online benchmark with profiling error: TypeError: multi_modal_content must be a dict containing 'audio' bug ### Your current environment The vLLM Benchmarking with profiling is failing for Whisper model i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
