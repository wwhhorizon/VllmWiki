# vllm-project/vllm#14652: [Usage]: Segmentation Fault caused by model indexing errors (token sequence length exceeding 16384) in vLLM 0.7.3 multi-node deployment for DeepSeek R1 67B

| 字段 | 值 |
| --- | --- |
| Issue | [#14652](https://github.com/vllm-project/vllm/issues/14652) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator |
| 症状 | crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Segmentation Fault caused by model indexing errors (token sequence length exceeding 16384) in vLLM 0.7.3 multi-node deployment for DeepSeek R1 67B

### Issue 正文摘录

### Your current environment Hello vLLM experts and maintainers, When deploying DeepSeek R1 67B using vLLM 0.7.3 across 4 nodes (8×L40S GPUs each), user inference requests occasionally trigger segmentation faults. Logs indicate these errors originate from input token sequences exceeding the model's maximum length limit (17052 > 16384), leading to model indexing errors and subsequent memory access violations. The index overflow issue ultimately resulted in an NCCL communication error affecting distributed training in a multi-node GPU cluster. Environment > vLLM version: 0.7.3 > Hardware: 4-node cluster (32×L40S GPUs total) > Model: DeepSeek R1 67B > Deployment: Likely Ray (inferred from logs) Key log excerpts: ``` Token indices sequence length is longer than the specified maximum sequence length for this model (17052 > 16384). Running this sequence through the model will result in indexing errors [36m(RayWorkerWrapper pid=239, ip=10.185.131.6)[0m *** SIGSEGV received at time=1741685673 on cpu 53 *** [36m(RayWorkerWrapper pid=239, ip=10.185.131.6)[0m [failure_signal_handler.cc : 345] RAW: Signal 11 raised at PC=0x7f2390049b8a while already in AbslFailureSignalHandler() [36m(Ray...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g distributed training in a multi-node GPU cluster. Environment > vLLM version: 0.7.3 > Hardware: 4-node cluster (32×L40S GPUs total) > Model: DeepSeek R1 67B > Deployment: Likely Ray (inferred from logs) Key log excerp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing 16384) in vLLM 0.7.3 multi-node deployment for DeepSeek R1 67B usage;stale ### Your current environment Hello vLLM experts and maintainers, When deploying DeepSeek R1 67B using vLLM 0.7.3 across 4 nodes (8×L40S GPUs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , markupsafe._speedups, PIL._imaging, msgspec._core, PIL._imagingft, zmq.backend.cython._zmq, multidict._multidict, yarl._quoting_c, propcache._helpers_c, aiohttp._http_writer, aiohttp._http_parser, aiohttp._websocket.m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: zenlist._frozenlist, vllm.cumem_allocator, sentencepiece._sentencepiece, cuda_utils, __triton_launcher (total: 52) [36m(RayWorkerWrapper pid=243, ip=10.185.131.5)[0m /usr/local/lib/python3.12/dist-packages/vllm/distri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Segmentation Fault caused by model indexing errors (token sequence length exceeding 16384) in vLLM 0.7.3 multi-node deployment for DeepSeek R1 67B usage;stale ### Your current environment Hello vLLM experts and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
