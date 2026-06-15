# vllm-project/vllm#7161: [Bug]: vllm is crashed on v0.5.3.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#7161](https://github.com/vllm-project/vllm/issues/7161) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vllm is crashed on v0.5.3.post1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` It is ### 🐛 Describe the bug I'm using Llama3.1 to do inference, and container is crashed. My command to start vllm: ```yaml image: vllm/vllm-openai:v0.5.3.post1 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"] args: ["--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--trust-remote-code"] ``` Logs when container is crashed: ``` [rank0]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7fa150ea6897 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #1: c10::deta...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAExcepti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "vllm.entrypoints.openai.api_server"] args: ["--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--trust-remote-code"] ``` Logs when c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ] [PG 2 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: f `python collect_env.py` ``` It is ### 🐛 Describe the bug I'm using Llama3.1 to do inference, and container is crashed. My command to start vllm: ```yaml image: vllm/vllm-openai:v0.5.3.post1
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG 2 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered C...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | (0x7fa19ecfe609 in /usr/lib/x86_64-linux-gnu/libpthread.so.0) frame #4: clone + 0x43 (0x7fa19ee38353 in /usr/lib/x86_64-linux-gnu/libc.so.6) ``` bug |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7fa152185dcc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xd6df4 (0x7fa19dc3cdf4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
