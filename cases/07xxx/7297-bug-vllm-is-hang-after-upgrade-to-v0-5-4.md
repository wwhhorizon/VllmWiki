# vllm-project/vllm#7297: [Bug]: vllm is hang after upgrade to v0.5.4

| 字段 | 值 |
| --- | --- |
| Issue | [#7297](https://github.com/vllm-project/vllm/issues/7297) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vllm is hang after upgrade to v0.5.4

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug command to start vllm: ```yaml command: ["python3", "-m", "vllm.entrypoints.openai.api_server"] args: [ "--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remote-code", "--disable-frontend-multiprocessing" ] securityContext: privileged: true ports: - containerPort: 8080 env: - name: OMP_NUM_THREADS value: "2" ``` Log is as following, and vllm can't response: ``` [rank1]:[E808 09:09:31.367084656 ProcessGroupNCCL.cpp:1515] [PG 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7f8c23a8af...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAExcepti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rypoints.openai.api_server"] args: [ "--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remote-code", "--disa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ] [PG 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , "-m", "vllm.entrypoints.openai.api_server"] args: [ "--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered C...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | (0x7f8c736f9609 in /usr/lib/x86_64-linux-gnu/libpthread.so.0) frame #4: clone + 0x43 (0x7f8c73833353 in /usr/lib/x86_64-linux-gnu/libc.so.6) ``` bug stale |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f8c24d906fc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xd6df4 (0x7f8c72537df4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
