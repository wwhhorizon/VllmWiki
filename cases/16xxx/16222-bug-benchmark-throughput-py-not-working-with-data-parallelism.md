# vllm-project/vllm#16222: [Bug]: benchmark_throughput.py not working with data-parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#16222](https://github.com/vllm-project/vllm/issues/16222) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_throughput.py not working with data-parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to benchmark vllm performance for various parallelism configurations. I am using the vllm provided `benchmark_throughput.py` script to do this. I attempted to try data-parallel serving like so: ``` python benchmarks/benchmark_throughput.py --model meta-llama/Llama-2-13b-hf --dataset-name sharegpt --dataset-path kramesh/ShareGPT_V3_unfiltered_cleaned_split.json --data-parallel-size 4 --num_prompts 128 ``` and it just gets stuck. Here is the stack trace: ```text INFO 04-07 19:41:39 [__init__.py:239] Automatically detected platform cuda. Namespace(backend='vllm', dataset_name='sharegpt', dataset=None, dataset_path='/work/hdd/bcjw/kramesh/ShareGPT_V3_unfiltered_cleaned_split.json', input_len=None, output_len=N one, n=1, num_prompts=128, hf_max_batch_size=None, output_json=None, async_engine=False, disable_frontend_multiprocessing=False, disable_detokenize=False, lora_path=None, pre fix_len=None, random_range_ratio=None, hf_subset=None, hf_split=None, model='meta-llama/Llama-2-13b-hf', task='auto', tokenizer='meta-llama/Llama-2-13b-hf', hf_config_path=No ne, skip_tokenizer_init=False, revision=None, code_revision=None, tok...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: e bug I am trying to benchmark vllm performance for various parallelism configurations. I am using the vllm provided `benchmark_throughput.py` script to do this. I attempted to try data-parallel serving like so: ``` pyt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: _gpu_blocks_override=None, max_num_batche d_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantizat io...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: del_name=Non e, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling _policy='fcfs', scheduler_cls='...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: edia_path=None, down load_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', log its_processor_pattern=None, model_impl='auto', di...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: benchmark_throughput.py not working with data-parallelism bug ### Your current environment ### 🐛 Describe the bug I am trying to benchmark vllm performance for various parallelism configurations. I am using the v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
