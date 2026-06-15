# vllm-project/vllm#19954: [Performance]: Performance decrease after upgrading from 0.8.5 to 0.9.2

| 字段 | 值 |
| --- | --- |
| Issue | [#19954](https://github.com/vllm-project/vllm/issues/19954) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;moe;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance decrease after upgrading from 0.8.5 to 0.9.2

### Issue 正文摘录

I want to use the DP multi-API feature, so I upgraded to the latest version (0.9.2). Then I ran a benchmark and found that the overall performance has decreased. I want to know why this is happening? Am I missing any features? ``` Before: Starting initial single prompt test run... Initial test run completed. Starting main benchmark run... Traffic request rate: 30.0 Burstiness factor: 1.0 (Poisson process) Maximum request concurrency: None 100%|██████████| 10000/10000 [07:31 ${VLLM_LOG} 2>&1 & python3 ~/vllm/benchmarks/benchmark_serving.py \ --backend ${BACKEND} \ --model ${MODEL_NAME} \ --random-input-len 1500 \ --random-output-len 2500 \ --random-range-ratio 0.3 \ --endpoint /v1/chat/completions \ --dataset-name ${DATASET_NAME} \ --dataset-path ${DATASET_PATH} \ --num-prompts ${NUM_PROMPTS} \ --request-rate 30 \ > ${BENCH_LOG} 2>&1 ``` I don't know what happened. I thought there was something wrong with the calculation logic of the benchmark_serving script. I switched to 0.8.5's benchmark_serving.py and the performance regressed overall. I want to know what I missed and why the performance regressed. Thanks ### Misc discussion on performance _No response_ ### Your current environ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ance I want to use the DP multi-API feature, so I upgraded to the latest version (0.9.2). Then I ran a benchmark and found that the overall performance has decreased. I want to know why this is happening? Am I missing a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: un... Initial test run completed. Starting main benchmark run... Traffic request rate: 30.0 Burstiness factor: 1.0 (Poisson process) Maximum request concurrency: None 100%|██████████| 10000/10000 [07:31 ${VLLM_LOG} 2>&1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ${VLLM_LOG} 2>&1 & python3 ~/vllm/benchmarks/benchmark_serving.py \ --backend ${BACKEND} \ --model ${MODEL_NAME} \ --random-input-len 1500 \ --random-output-len 2500 \ --random-range-ratio 0.3 \ --endpoint /v1/chat/comp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=5000, download_dir=None, load_format=LoadForm at.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --------------------------------------------------------------+ | NVIDIA-SMI 460.32.03 Driver Version: 545.23.08 CUDA Version: 12.3 | |-------------------------------+----------------------+----------------------+ | GPU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
