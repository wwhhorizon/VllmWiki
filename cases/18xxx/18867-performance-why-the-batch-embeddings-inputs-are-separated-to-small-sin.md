# vllm-project/vllm#18867: [Performance]: why the batch-embeddings inputs are separated to small single one?

| 字段 | 值 |
| --- | --- |
| Issue | [#18867](https://github.com/vllm-project/vllm/issues/18867) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: why the batch-embeddings inputs are separated to small single one?

### Issue 正文摘录

### Proposal to improve performance ```python for i, engine_prompt in enumerate(engine_prompts): request_id_item = f"{request_id}-{i}" self._log_inputs(request_id_item, request_prompts[i], params=pooling_params, lora_request=lora_request, prompt_adapter_request=prompt_adapter_request) trace_headers = (None if raw_request is None else await self._get_trace_headers(raw_request.headers)) generator = self.engine_client.encode( engine_prompt, pooling_params, request_id_item, lora_request=lora_request, trace_headers=trace_headers, priority=request.priority, ) generators.append(generator) ``` This will not make full use of the gpu batch feature. ### Report of performance regression _No response_ ### Misc discussion on performance When bench qps exceeds a certain threshold, rt will increase significantly. eg: gpu.toCpu->cudaMemcpy, from 0ms -> 300+ms ### Your current environment (if you think it is necessary) PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3 2.17) Clang version: Could not collect CMake versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ms ### Your current environment (if you think it is necessary) PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Performance]: why the batch-embeddings inputs are separated to small single one? performance;stale ### Proposal to improve performance ```python for i, engine_prompt in enumerate(engine_prompts): request_id_item = f"{...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 GPU 1: NVIDIA A10 GPU 2: NVIDIA A10 GPU 3: NVIDIA A10 Nvidia driver version: 570.144 cuDNN version: Pro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e batch-embeddings inputs are separated to small single one? performance;stale ### Proposal to improve performance ```python for i, engine_prompt in enumerate(engine_prompts): request_id_item = f"{request_id}-{i}" self....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: not make full use of the gpu batch feature. ### Report of performance regression _No response_ ### Misc discussion on performance When bench qps exceeds a certain threshold, rt will increase significantly. eg: gpu.toCpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
