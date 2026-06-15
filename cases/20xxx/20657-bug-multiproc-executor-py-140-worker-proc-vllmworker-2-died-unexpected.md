# vllm-project/vllm#20657: [Bug]: [multiproc_executor.py:140] Worker proc VllmWorker-2 died unexpectedly, shutting down executor.

| 字段 | 值 |
| --- | --- |
| Issue | [#20657](https://github.com/vllm-project/vllm/issues/20657) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [multiproc_executor.py:140] Worker proc VllmWorker-2 died unexpectedly, shutting down executor.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GitHub address: https://github.com/moguizhizi/learning_project/tree/main/benchmarks start serving model： vllm serve /home/temp/llm_model/nm-testing/Qwen2.5-VL-72B-Instruct-quantized.w8a8 --load-format runai_streamer --tensor-parallel-size 4 --max-model-len 8192 --max-num-seqs 2048 --kv-cache auto --gpu-memory-utilization 0.5 --disable-custom-all-reduce --served-model-name qwen2_5_vl_72B_quant --disable-log-requests Send request: python3 learning_project/benchmarks/benchmark_serving.py --backend openai-chat --model /home/temp/llm_model/nm-testing/Qwen2___5-VL-72B-Instruct-quantized___w8a8 --served-model-name qwen2_5_vl_72B_quant --endpoint /v1/chat/completions --dataset-name phonetest --dataset-path /home/project/dataset/phonetest/web_nj_action_0426_grpo.json --num-prompts 128 --result_dir /home/project/learning_project/benchmarks/output/qwen2_5_vl_72B --save-result llm model url： https://modelscope.cn/models/nm-testing/Qwen2.5-VL-72B-Instruct-quantized.w8a8 error info： INFO 07-08 10:35:34 [loggers.py:118] Engine 000: Avg prompt throughput: 536.5 tokens/s, Avg generation throughput: 17.1 tokens/s, Running: 1 reqs, Waiting: 121 req...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Worker proc VllmWorker-2 died unexpectedly, shutting down executor. bug;stale ### Your current environment ### 🐛 Describe the bug GitHub address: https://github.com/moguizhizi/learning_project/tree/main/benchmarks start...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: amer --tensor-parallel-size 4 --max-model-len 8192 --max-num-seqs 2048 --kv-cache auto --gpu-memory-utilization 0.5 --disable-custom-all-reduce --served-model-name qwen2_5_vl_72B_quant --disable-log-requests Send reques...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: thub.com/moguizhizi/learning_project/tree/main/benchmarks start serving model： vllm serve /home/temp/llm_model/nm-testing/Qwen2.5-VL-72B-Instruct-quantized.w8a8 --load-format runai_streamer --tensor-parallel-size 4 --ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: GitHub address: https://github.com/moguizhizi/learning_project/tree/main/benchmarks start serving model： vllm serve /home/temp/llm_model/nm-testing/Qwen2.5-VL-72B-Instruct-quantized.w8a8 --load-format runai_streamer --t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
