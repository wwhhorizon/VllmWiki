# vllm-project/vllm#10123: [Usage]: Engine iteration timed out. (during using qwen2-vl-7b)

| 字段 | 值 |
| --- | --- |
| Issue | [#10123](https://github.com/vllm-project/vllm/issues/10123) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;gemm;operator;triton |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Engine iteration timed out. (during using qwen2-vl-7b)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I I tried deploying `qwen2-vl-7b` using vllm with commands: ```bash VLLM_WORKER_MULTIPROC_METHOD=spawn CUDA_VISIBLE_DEVICES=4,5,6,7 nohup python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-VL-7B-Instruct --model MY_MODEL_PATH --pipeline-parallel-size 4 --gpu-memory-utilization 0.8 --limit-mm-per-prompt image=4 --port 11435 --disable-custom-all-reduce >> nohup_logs/vllm.log 2>&1 & ``` Please forgive me for the complex parameter settings, as I conducted numerous searches and attempts to successfully deploy and added many parameters to ensure it works. And my device configuration is as follows: ``` System: Ubuntu 20.04.4 LTS Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz Stepping: 7 CPU MHz: 3283.879 CPU max MHz: 4000.0000 CPU min MHz: 1200.0000 BogoMIPS: 6000.00 V...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Usage]: Engine iteration timed out. (during using qwen2-vl-7b) usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I I tried deploying `qwen2-vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 6.1.0 blessed 1.20.0 blinker 1.8.2 blis 0.7.11 braceexpand 0.1.7 cachetools 5.5.0 catalogue 2.0.10 certifi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 7b` using vllm with commands: ```bash VLLM_WORKER_MULTIPROC_METHOD=spawn CUDA_VISIBLE_DEVICES=4,5,6,7 nohup python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-VL-7B-Instruct --model MY_MODEL_PATH --p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Engine iteration timed out. (during using qwen2-vl-7b) usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I I tried deploying `qwen2-vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 6.0.0 ptyprocess 0.7.0 pure_eval 0.2.3 py-cpuinfo 9.0.0 py-spy 0.3.14 pyairports 2.1.1 pyarrow 17.0.0 pycocoevalcap

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
