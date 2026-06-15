# vllm-project/vllm#13418: [Bug][v1][rocm] cuda graph gets stuck in case padding is used to meet a captured input size

| 字段 | 值 |
| --- | --- |
| Issue | [#13418](https://github.com/vllm-project/vllm/issues/13418) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][v1][rocm] cuda graph gets stuck in case padding is used to meet a captured input size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, This is a more detailed report for https://github.com/vllm-project/vllm/issues/12568#issuecomment-2663792784. Essentially, a CUDA graph recorded through torch.compile using `VllmBackend` with v1 gets stuck when replayed in case the number of scheduled tokens in GPUModelRunner.execute_model is below the largest cudagraph_capture_sizes, **in the specific case where the first `num_scheduled_tokens` is NOT a multiple of 8 (to fit a captured size)**. No issue if the first `num_scheduled_tokens` does not get padded. I am running within `rocm/dev-ubuntu-22.04:6.3` with vllm-project/vllm at ce77eb9410c694000c5da5abfa638500c6c72aeb installed from source. Reproduction: run `VLLM_USE_V1=1 vllm serve meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 1 -O3`, and run the following script: ```python import json import random import string import grequests prompts = [] for i in range(14): chars = "".join( [random.choice(string.ascii_letters) for i in range(1200)]) prompts.append(chars) headers = {'Content-type': 'application/json'} async_list = [] for prompt in prompts: print("prompt", prompt) body = {"model": "meta-llama/Llama-2-7b-chat-...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ssuecomment-2663792784. Essentially, a CUDA graph recorded through torch.compile using `VllmBackend` with v1 gets stuck when replayed in case the number of scheduled tokens in GPUModelRunner.execute_model is below the l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: lowing script: ```python import json import random import string import grequests prompts = [] for i in range(14): chars = "".join( [random.choice(string.ascii_letters) for i in range(1200)]) prompts.append(chars) heade...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: v1 gets stuck when replayed in case the number of scheduled tokens in GPUModelRunner.execute_model is below the largest cudagraph_capture_sizes, **in the specific case where the first `num_scheduled_tokens` is NOT a mul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 784. Essentially, a CUDA graph recorded through torch.compile using `VllmBackend` with v1 gets stuck when replayed in case the number of scheduled tokens in GPUModelRunner.execute_model is below the largest cudagraph_ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug][v1][rocm] cuda graph gets stuck in case padding is used to meet a captured input size bug ### Your current environment ### 🐛 Describe the bug Hi, This is a more detailed report for https://github.com/vllm-project/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | t/miniconda3/lib/python3.12/site-packages/torch/lib/libroctracer64.so #4 0x00007557698d713b in amd::roc::device::ishweventready(amd::event const&, bool, unsigned int) const () fr |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | root/miniconda3/lib/python3.12/site-packages/torch/lib/libamdhip64.so #6 0x000075576976916d in hip::ihipmemcpy(void*, void const*, unsigned long, hipmemcpykind, hip::stream&, bool, |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | root/miniconda3/lib/python3.12/site-packages/torch/lib/libamdhip64.so #7 0x0000755769784b8b in hip::hipmemcpywithstream(void*, void const*, unsigned long, hipmemcpykind, ihipstrea… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | oot/miniconda3/lib/python3.12/site-packages/torch/lib/libtorch_hip.so #12 0x0000755796a794cd in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::wrapfunctionintofunctor_… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | oot/miniconda3/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so #16 0x0000755796b3f395 in at::(anonymous namespace)::wrapper_cuda_index_out_tensor_out(at::tensor const&, c10… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
