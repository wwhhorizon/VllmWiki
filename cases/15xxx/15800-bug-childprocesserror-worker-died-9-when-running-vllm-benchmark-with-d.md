# vllm-project/vllm#15800: [Bug]: ChildProcessError: worker died (-9) when running vLLM benchmark with DeepSeek-R1-Distill-Qwen-32B on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#15800](https://github.com/vllm-project/vllm/issues/15800) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ChildProcessError: worker died (-9) when running vLLM benchmark with DeepSeek-R1-Distill-Qwen-32B on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When benchmarking the model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B using benchmark_throughput.py on CPU, vLLM crashes with ChildProcessError: worker died. One of the workers exits with code -9. ``` bash export VLLM_CPU_OMP_THREADS_BIND="0-59|60-119" ``` ``` python python ./vllm-0.8.2/benchmarks/benchmark_throughput.py \ --backend vllm \ --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ --dataset-name sharegpt \ --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 100 \ --tensor-parallel-size 2 ``` The output of `benchmark_throughput.py` ``` text (vllm_cpu_2) [root@localhost ds32b]# python ./vllm-0.8.2/benchmarks/benchmark_throughput.py --backend vllm --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 100 --tensor-parallel-size 2 DEBUG 03-31 15:44:41 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 03-31 15:44:41 [__init__.py:34] Checking if TPU platform is available. DEBUG 03-31 15:44:41 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 03-31 15:44:41...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: m_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: odel_name=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: r: worker died (-9) when running vLLM benchmark with DeepSeek-R1-Distill-Qwen-32B on CPU bug ### Your current environment ### 🐛 Describe the bug When benchmarking the model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B using...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 03-31 15:44:41 [__init__.py:52] Checking if CUDA platform is available. DEBUG 03-31 15:44:41 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
