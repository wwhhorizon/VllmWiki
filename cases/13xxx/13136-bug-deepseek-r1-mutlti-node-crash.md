# vllm-project/vllm#13136: [Bug]: deepseek-r1 mutlti-node crash

| 字段 | 值 |
| --- | --- |
| Issue | [#13136](https://github.com/vllm-project/vllm/issues/13136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek-r1 mutlti-node crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use 2x8H100 to deploy the deepseek-r1 model in kubenet, but when I test the bbh test set with a concurrency count of 3, the service will run for a while and then crash. The nvidia-smi check will show that the gpu memory of a process has dropped from more than 60G to 2G, and the server log has the following error. ``` ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m *** SIGSEGV received at time=1739339449 on cpu 57 *** ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m PC: @ 0x7ee184049b8a (unknown) addProxyOpIfNeeded() ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m @ 0x7f11ab22d520 (unknown) (unknown) ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m @ 0x80000 (unknown) (unknown) ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m [2025-02-11 21:50:49,831 E 4823 4823] logging.cc:460: *** SIGSEGV received at time=1739339449 on cpu 57 *** ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m [2025-02-11 21:50:49,831 E 4823 4823] logging.cc:460: PC: @ 0x7ee184049b8a (unknown) addProxyOpIfNeeded() ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m [2025-02-11 21:50:49,832 E 4823 4823] lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 68.253)^[[0m File "/usr/local/lib/python3.12/dist-packages/ray/util/tracing/tracing_helper.py", line 463 in _resume_span ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m File "/usr/local/lib/python3.12/dist-pack...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ;stale ### Your current environment ### 🐛 Describe the bug I use 2x8H100 to deploy the deepseek-r1 model in kubenet, but when I test the bbh test set with a concurrency count of 3, the service will run for a while and t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: deepseek-r1 mutlti-node crash bug;stale ### Your current environment ### 🐛 Describe the bug I use 2x8H100 to deploy the deepseek-r1 model in kubenet, but when I test the bbh test set with a concurrency count of 3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 253)^[[0m File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/mla/utils.py", line 541 in _forward_prefill_flash ^[[36m(RayWorkerWrapper pid=4823, ip=10.233.68.253)^[[0m File "/usr/local/lib/python3.12/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ug I use 2x8H100 to deploy the deepseek-r1 model in kubenet, but when I test the bbh test set with a concurrency count of 3, the service will run for a while and then crash. The nvidia-smi check will show that the gpu m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
