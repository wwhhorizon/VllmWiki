# vllm-project/vllm#16948: [Bug]: Run Llama4 Scout 16E w/ 10000 input length trigger vllm crashing, but run fine if use FA2.

| 字段 | 值 |
| --- | --- |
| Issue | [#16948](https://github.com/vllm-project/vllm/issues/16948) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run Llama4 Scout 16E w/ 10000 input length trigger vllm crashing, but run fine if use FA2.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using `benchmark_serving.py` to test against Llama4 BF16 checkpoint, and as long as I make input model length > 10000, the vLLM server would crash. However, if I switch back to use FA2 by setting `VLLM_FLASH_ATTN_VERSION=2`, vLLM server runs fine. vLLM server cmd ``` VLLM_USE_MODELSCOPE=False SAFETENSORS_FAST_GPU=1 vllm serve \ meta-llama/Llama-4-Scout-17B-16E-Instruct \ --disable-log-requests -tp 8 \ --max-num-seqs 64 \ --no-enable-prefix-caching \ --max_num_batched_tokens=80000 \ --max-model-len 30000 ``` Benchmark cmd ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model meta-llama/Llama-4-Scout-17B-16E-Instruct \ --dataset-name random \ --max-concurrency 64 \ --num-prompts 256 \ --random-input-len 10000 \ --random-output-len 1000 ``` Error log ``` [1;36m(VllmWorker rank=1 pid=2920557)[0;0m ERROR 04-21 14:16:49 [multiproc_executor.py:470] File "/data/users/zijingliu/gitrepos/liuzijing2014/vllm/vllm/v1/executor/multiproc_executor.py", line 465, in worker_busy_loop [1;36m(VllmWorker rank=1 pid=2920557)[0;0m ERROR 04-21 14:16:49 [multiproc_executor.py:470] output = func(*args, **kwargs) [1;36m(VllmWorker...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: crash. However, if I switch back to use FA2 by setting `VLLM_FLASH_ATTN_VERSION=2`, vLLM server runs fine. vLLM server cmd ``` VLLM_USE_MODELSCOPE=False SAFETENSORS_FAST_GPU=1 vllm serve \ meta-llama/Llama-4-Scout-17B-1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0 ``` Benchmark cmd ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model meta-llama/Llama-4-Scout-17B-16E-Instruct \ --dataset-name random \ --max-concurrency 64 \ --num-prompts 256 \ --random-input-len...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: scribe the bug I am using `benchmark_serving.py` to test against Llama4 BF16 checkpoint, and as long as I make input model length > 10000, the vLLM server would crash. However, if I switch back to use FA2 by setting `VL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Run Llama4 Scout 16E w/ 10000 input length trigger vllm crashing, but run fine if use FA2. bug ### Your current environment ### 🐛 Describe the bug I am using `benchmark_serving.py` to test against Llama4 BF16 che...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 1 vllm serve \ meta-llama/Llama-4-Scout-17B-16E-Instruct \ --disable-log-requests -tp 8 \ --max-num-seqs 64 \ --no-enable-prefix-caching \ --max_num_batched_tokens=80000 \ --max-model-len 30000 ``` Benchmark cmd ``` pyt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
