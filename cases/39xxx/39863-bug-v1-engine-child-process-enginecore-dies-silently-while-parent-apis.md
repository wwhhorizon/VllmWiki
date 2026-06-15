# vllm-project/vllm#39863: [Bug]: V1 Engine: Child process (EngineCore) dies silently while parent (APIServer) remains alive and responds to health checks, causing service hang

| 字段 | 值 |
| --- | --- |
| Issue | [#39863](https://github.com/vllm-project/vllm/issues/39863) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine: Child process (EngineCore) dies silently while parent (APIServer) remains alive and responds to health checks, causing service hang

### Issue 正文摘录

### Your current environment ## Description When using vLLM V1 engine under sustained load, the EngineCore subprocess crashes or deadlocks silently. The APIServer continues to respond to health checks (`GET /version` returns 200 OK), but inference completely stops working. ### Symptoms: - Prompt/generation throughput drops to 0 - Requests accumulate in waiting queue but never get scheduled - GPU KV cache usage drops to 0% - No error logs from EngineCore - `/version` endpoint still returns 200 OK ### Log example: ```text INFO: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s Running: 0 reqs, Waiting: 3 reqs, GPU KV cache usage: 0.0% INFO: "GET /version HTTP/1.1" 200 OK INFO: "POST /v1/chat/completions HTTP/1.1" 200 OK # but actually hangs ``` ## Enviroment ```text ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.19.0 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU: Disabled GPU Topology: GPU0 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X 0-31 0 N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: cks silently. The APIServer continues to respond to health checks (`GET /version` returns 200 OK), but inference completely stops working. ### Symptoms: - Prompt/generation throughput drops to 0 - Requests accumulate in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ====================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.19.0 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU: Disabled GPU Topology: GPU0 CPU Affinity...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LLM V1 engine under sustained load, the EngineCore subprocess crashes or deadlocks silently. The APIServer continues to respond to health checks (`GET /version` returns 200 OK), but inference completely stops working. #...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: inference completely stops working. ### Symptoms: - Prompt/generation throughput drops to 0 - Requests accumulate in waiting queue but never get scheduled - GPU KV cache usage drops to 0% - No error logs from EngineCore...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: o 0 - Requests accumulate in waiting queue but never get scheduled - GPU KV cache usage drops to 0% - No error logs from EngineCore - `/version` endpoint still returns 200 OK ### Log example: ```text INFO: Avg prompt th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
