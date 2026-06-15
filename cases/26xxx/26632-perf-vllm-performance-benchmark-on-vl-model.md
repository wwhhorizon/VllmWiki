# vllm-project/vllm#26632: [Perf]: vllm performance benchmark on vl model

| 字段 | 值 |
| --- | --- |
| Issue | [#26632](https://github.com/vllm-project/vllm/issues/26632) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Perf]: vllm performance benchmark on vl model

### Issue 正文摘录

### Proposal to improve performance I tried to launch vllm and ran a benchmark, encountered some issues and eventually resolved them. Here goes the steps: ``` $ vllm serve /home/admin/Qwen2.5-VL-72B-Instruct \ --disable-log-requests \ --max-num-seqs 1024 \ --tensor-parallel-size 8 ..... (EngineCore_DP0 pid=54228) INFO 10-11 20:40:37 [kv_cache_utils.py:1091] Maximum concurrency for 128,000 tokens per request: 10.92x Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 67/67 [00:14 , seed=12345, num_prompts=768, dataset_name='random', no_stream=False, dataset_path=None, no_oversample=False, custom_output_len=256, custom_skip_chat_template=False, spec_bench_output_len=256, spec_bench_category=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, blazedit_min_distance=0.0, blazedit_max_distance=1.0, random_input_len=4000, random_output_len=1, random_range_ratio=0.0, random_prefix_len=0, random_batch_size=1, random_mm_base_items_per_request=1, random_mm_num_mm_items_range_ratio=0.0, random_mm_limit_mm_per_prompt={'imag...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Perf]: vllm performance benchmark on vl model performance ### Proposal to improve performance I tried to launch vllm and ran a benchmark, encountered some issues and eventually resolved them. Here goes the steps: ``` $...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Perf]: vllm performance benchmark on vl model performance ### Proposal to improve performance I tried to launch vllm and ran a benchmark, encountered some issues and eventually resolved them. Here goes the steps: ``` $...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ``` $ vllm serve /home/admin/Qwen2.5-VL-72B-Instruct \ --disable-log-requests \ --max-num-seqs 1024 \ --tensor-parallel-size 8 ..... (EngineCore_DP0 pid=54228) INFO 10-11 20:40:37 [kv_cache_utils.py:1091] Maximum concur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: █████████████████████████████████| 768/768 [08:12<00:00, 1.56it/s] tip: install termplotlib and gnuplot to plot the metrics ============ Serving Benchmark Result ============ Successful requests: 768 Maximum request con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 91] Maximum concurrency for 128,000 tokens per request: 10.92x Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
