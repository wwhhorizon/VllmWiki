# vllm-project/vllm#43444: [Performance]: Significant performance degradation  v1/reranker under concurrent requests while swiching from v.0.19.1 to v0.20.2 v0.21.1

| 字段 | 值 |
| --- | --- |
| Issue | [#43444](https://github.com/vllm-project/vllm/issues/43444) |
| 状态 | open |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Significant performance degradation  v1/reranker under concurrent requests while swiching from v.0.19.1 to v0.20.2 v0.21.1

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Model: bge-reranker-v2-m3. Here 3 runs of some sample code for 3 version of vllm. Same code, just different version of vllm. Mean Latency(T) - sec using requests Mean Latency(A) - sec using aiohttp (vllm v0.19.1) Сoncurency | Time (A) | Time(T) | RPS(A) | RPS(T) | Mean Latency(A) | Mean Latency(T) | Max Latency(A) | Max Latency(T) | Min Latency(A) | Min Latency(T) -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- 1 | 4.49 | 3.7 | 0.22 | 0.27 | 3.93 | 3.7 | 3.93 | 3.7 | 3.93 | 3.7 5 | 15.45 | 15.33 | 0.32 | 0.33 | 11.77 | 11.63 | 15.1 | 15.32 | 7.67 | 7.74 10 | 29.32 | 28.54 | 0.34 | 0.35 | 20.95 | 20.04 | 28.97 | 28.53 | 11.87 | 10.87 20 | 53.89 | 58.27 | 0.37 | 0.34 | 35.08 | 40.06 | 53.49 | 58.24 | 13.26 | 20.25 (vllm v0.20.2) Сoncurency | Time (A) | Time(T) | RPS(A) | RPS(T) | Mean Latency(A) | Mean Latency(T) | Max Latency(A) | Max Latency(T) | Min Latency(A) | Min Latency(T) -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- 1 | 5.55 | 4.89 | 0.18 | 0.2 | 5.09 | 4.88 | 5.09 | 4.88 | 5.09 | 4.88 5 | 21.44 | 20.81 | 0.23 | 0.24 | 21.11 | 20.79 | 21.12 | 20.8 | 21.09 | 20.77 10 | 42.53 |...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ession Model: bge-reranker-v2-m3. Here 3 runs of some sample code for 3 version of vllm. Same code, just different version of vllm. Mean Latency(T) - sec using requests Mean Latency(A) - sec using aiohttp (vllm v0.19.1)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mprove performance _No response_ ### Report of performance regression Model: bge-reranker-v2-m3. Here 3 runs of some sample code for 3 version of vllm. Same code, just different version of vllm. Mean Latency(T) - sec us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ance]: Significant performance degradation v1/reranker under concurrent requests while swiching from v.0.19.1 to v0.20.2 v0.21.1 performance ### Proposal to improve performance _No response_ ### Report of performance re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
