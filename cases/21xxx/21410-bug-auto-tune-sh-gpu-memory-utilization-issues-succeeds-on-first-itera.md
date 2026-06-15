# vllm-project/vllm#21410: [Bug]: auto_tune.sh gpu_memory_utilization issues - succeeds on first iteration for HBM OOM determination, then fails during benchmarking

| 字段 | 值 |
| --- | --- |
| Issue | [#21410](https://github.com/vllm-project/vllm/issues/21410) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: auto_tune.sh gpu_memory_utilization issues - succeeds on first iteration for HBM OOM determination, then fails during benchmarking

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to run the auto_tune.sh script with the following parameters: ```shell TAG=$(date +"%Y_%m_%d_%H_%M") BASE="/vllm-workspace" MODEL="google/gemma-3-27b-it" SYSTEM="GPU" TP=1 DOWNLOAD_DIR="/vllm-workspace/models" INPUT_LEN=1500 OUTPUT_LEN=200 MIN_CACHE_HIT_PCT=50 MAX_LATENCY_ALLOWED_MS=10000 NUM_SEQS_LIST="10" NUM_BATCHED_TOKENS_LIST="512 1024 2048 4096" ``` the initial server startup to determine the highest gpu_utilization will succeed at 0.98, but then fail due to OOM issue once the actual benchmarking starts. Initial Success: ``` INFO: Started server process [18725] INFO: Waiting for application startup. INFO: Application startup complete. DEBUG 07-22 14:10:03 [async_llm.py:554] Called check_health. INFO: 127.0.0.1:35632 - "GET /health HTTP/1.1" 200 OK DEBUG 07-22 14:10:03 [launcher.py:77] port 8004 is used by process psutil.Process(pid=18725, name='vllm', status='running', started='14:08:31') launched with command: DEBUG 07-22 14:10:03 [launcher.py:77] /usr/bin/python3 /usr/local/bin/vllm serve google/gemma-3-27b-it --disable-log-requests --port 8004 --gpu-memory-utilization 0.98 --max-num-seqs 10 --max-num-batc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: py:586] File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/compiler_interface.py", line 510, in compiled_graph ERROR 07-22 14:11:18 [core.py:586] graph_output = inductor_compiled_graph(list_args) ERROR 07-22...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rameters: ```shell TAG=$(date +"%Y_%m_%d_%H_%M") BASE="/vllm-workspace" MODEL="google/gemma-3-27b-it" SYSTEM="GPU" TP=1 DOWNLOAD_DIR="/vllm-workspace/models" INPUT_LEN=1500 OUTPUT_LEN=200 MIN_CACHE_HIT_PCT=50 MAX_LATENC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: iteration for HBM OOM determination, then fails during benchmarking bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to run the auto_tune.sh script with the following parameters: ```shell TA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: succeeds on first iteration for HBM OOM determination, then fails during benchmarking bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to run the auto_tune.sh script with the following param...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ore.py:586] buf5 = empty_strided_cuda((s0, 21504), (21504, 1), torch.bfloat16) ERROR 07-22 14:11:18 [core.py:586] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-22 14:11:18 [core.py:586] torch.OutO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
