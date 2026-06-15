# vllm-project/vllm#4145: [Usage]: How to get the latency of each request with benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#4145](https://github.com/vllm-project/vllm/issues/4145) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to get the latency of each request with benchmark_serving.py

### Issue 正文摘录

### Proposal to improve performance I have run 3 cases with [benchmark_serving.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py) to conduct benchmark test. The server is launched with `--max-num-seqs 1` to test the performance for `bach_szie = 1`: ```bash python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8014 \ --model /data/models/vicuna-13b-v1.5 \ --dtype auto -tp 2 --max-model-len 4096 \ --max-num-seqs 1 \ --gpu-memory-utilization 0.85 \ --enable-prefix-caching \ --swap-space 16 ``` However, **the latency of each request is gradually increases**, which seems abnormal. So the `latency` of [https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py#L254](https://github.com/vllm-project/vllm/blob/main/benchmarks/backend_request_func.py#L254) refers to what? How to get the latency of each request? ![image](https://uploads.linear.app/342cff15-f40f-4cf7-8bee-343d25adb534/bd962d08-7839-47ce-a77b-69beef2482c2/e65412b4-c97c-437a-be59-f3012f6813bb?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC9iZDk2MmQwOC03ODM5LTQ3Y2UtYTc3Yi02OWJlZWYyNDgyYzIvZTY1NDEy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e-a77b-69beef2482c2/e65412b4-c97c-437a-be59-f3012f6813bb?signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRoIjoiLzM0MmNmZjE1LWY0MGYtNGNmNy04YmVlLTM0M2QyNWFkYjUzNC9iZDk2MmQwOC03ODM5LTQ3Y2UtYTc3Yi02OWJlZWYyNDgyYzIvZTY...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8014 \ --model /data/models/vicuna-13b-v1.5 \ --dtype auto -tp 2 --max-model-len 4096 \ --max-num-seqs 1 \ --gpu-memory-utilization 0.85 \ --enable-prefix-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: How to get the latency of each request with benchmark_serving.py performance ### Proposal to improve performance I have run 3 cases with [benchmark_serving.py](https://github.com/vllm-project/vllm/blob/main/ben...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to get the latency of each request with benchmark_serving.py performance ### Proposal to improve performance I have run 3 cases with [benchmark_serving.py](https://github.com/vllm-project/vllm/blob/main/ben...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
