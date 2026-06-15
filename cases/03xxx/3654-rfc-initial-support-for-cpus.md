# vllm-project/vllm#3654: [RFC] Initial Support for CPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3654](https://github.com/vllm-project/vllm/issues/3654) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC] Initial Support for CPUs

### Issue 正文摘录

## Progress - [ ] Integrate CPU executor to support the basic model inference (BF16/FP32) without TP. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] Support FP16 model inference. - [x] Support TP inference for multiple CPU sockets inside the same node. - #6008 - #6125 - [ ] Support model and KV cache quantization. - #5492 - #7257 ## Features The CPU executor plans to support the following features: - Basic models of vLLM with FP16/BF16/FP32, except MoE models - Tensor-parallel model inference based on Ray - AWQ quantization, 8-bit KVCache Quantization - Others ## Design Our target is seamless porting vLLM to CPU devices and sharing most of vLLM core components (e.g., **schedular**, **cache management**, **model definitions**, **Megatron-style model partitioning**, ...). The CPU executor will depend on Pytorch CPU and leverage optimized kernels and features from [intel-extension-for-pytorch](https://github.com/intel/intel-extension-for-pytorch). The main changes to vLLM include: ### Torch APIs Adaption CPU device is supported in PyTorch by default. It allows the CPU Executor to share the same model definitions with the GPU Executor. Thanks to recent code refactors, many hard...

## 现有链接修复摘要

#3634 [Hardware][Intel] Add CPU inference backend | #3824 [Hardware][Intel] Isolate CPUModelRunner and ModelRunner for better maintenance | #3992 [HARDWARE] enable async_engine for CPU backend | #4113 [CI/BUILD] enable intel queue for longer CPU tests | #4971 [Hardware][Intel] Optimize CPU backend and add more performance tips | #5446 [Hardware][Intel] Generate custom activation ops using torch.compile for CPU backend. | #5492 [Hardware][Intel] fp8 kv cache support for CPU | #6008 [Hardware][Intel CPU] Adding intel openmp tunings in Docker file | #6125 [Hardware] [Intel] Enable Multiprocessing and tensor parallel in CPU backend and update documentation | #6212 [Hardware][Intel CPU][DOC] Update docs for CPU backend | #7257 [Hardware][Intel] Support compressed-tensor W8A8 for CPU backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ecutor to easily support new models and features in vLLM (e.g., ```torch.compile```). ### Custom Ops Adaption vLLM implemented many efficient CUDA kernels and packaged as ```_C``` library by pybind. These kernels are po...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ress - [ ] Integrate CPU executor to support the basic model inference (BF16/FP32) without TP. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] Support FP16 model inference. - [x] Support TP inference for multiple...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC] Initial Support for CPUs RFC;unstale ## Progress - [ ] Integrate CPU executor to support the basic model inference (BF16/FP32) without TP. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] Support FP16 model i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y hardcoded ```cuda``` device flags have been removed and Torch APIs are dispatched based on the device flag from ```DeviceConfig```. For the CPU executor, a new ```cpu``` device flag is added. Sharing the same model de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: C;unstale ## Progress - [ ] Integrate CPU executor to support the basic model inference (BF16/FP32) without TP. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] Support FP16 model inference. - [x] Support TP infere...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3634](https://github.com/vllm-project/vllm/pull/3634) | mentioned | 0.6 | [Hardware][Intel] Add CPU inference backend | ry allocation. - Added documents with install instructions. RFC: #3654 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw htm |
| [#3824](https://github.com/vllm-project/vllm/pull/3824) | mentioned | 0.45 | [Hardware][Intel] Isolate CPUModelRunner and ModelRunner for better maintenance | t the basic model inference (bf16/fp32) without tp. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] support fp16 model inference. - [x] support tp infer |
| [#3992](https://github.com/vllm-project/vllm/pull/3992) | mentioned | 0.6 | [HARDWARE] enable async_engine for CPU backend | HERE Enable the async engine code path for CPU backend related: #3654 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <detail |
| [#4113](https://github.com/vllm-project/vllm/pull/4113) | closes_keyword | 0.95 | [CI/BUILD] enable intel queue for longer CPU tests | fix the bug on pos_encoding kernel - enable part of the tests under `models` - skip for tests for cuda only on CPU related: #3654 **BEFORE SUBMITTING, PLEASE READ THE CHE |
| [#4971](https://github.com/vllm-project/vllm/pull/4971) | mentioned | 0.45 | [Hardware][Intel] Optimize CPU backend and add more performance tips | nce (bf16/fp32) without tp. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] support fp16 model inference. - [x] support tp inference for multiple cpu so |
| [#5446](https://github.com/vllm-project/vllm/pull/5446) | mentioned | 0.45 | [Hardware][Intel] Generate custom activation ops using torch.compile for CPU backend. | tp. - #3634 - #3824 - #4113 - #4971 - #5452 - #5446 - [ ] support fp16 model inference. - [x] support tp inference for multiple cpu sockets inside the same no |
| [#5492](https://github.com/vllm-project/vllm/pull/5492) | mentioned | 0.45 | [Hardware][Intel] fp8 kv cache support for CPU | 008 - #6125 - [ ] support model and kv cache quantization. - #5492 - #7257 ## features the cpu executor plans to support the following features: - basic models of |
| [#6008](https://github.com/vllm-project/vllm/pull/6008) | mentioned | 0.45 | [Hardware][Intel CPU] Adding intel openmp tunings in Docker file | ort tp inference for multiple cpu sockets inside the same node. - #6008 - #6125 - [ ] support model and kv cache quantization. - #5492 - #7257 ## features the cp |
| [#6125](https://github.com/vllm-project/vllm/pull/6125) | mentioned | 0.45 | [Hardware] [Intel] Enable Multiprocessing and tensor parallel in CPU backend and update documentation  | ence for multiple cpu sockets inside the same node. - #6008 - #6125 - [ ] support model and kv cache quantization. - #5492 - #7257 ## features the cpu executor p |
| [#6212](https://github.com/vllm-project/vllm/pull/6212) | mentioned | 0.6 | [Hardware][Intel CPU][DOC] Update docs for CPU backend | CPU backend, since it's different with the GPU backend. related #3654 https://vllm--6212.org.readthedocs.build/en/6212/ **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW |
| [#7257](https://github.com/vllm-project/vllm/pull/7257) | mentioned | 0.45 | [Hardware][Intel] Support compressed-tensor W8A8 for CPU backend | 125 - [ ] support model and kv cache quantization. - #5492 - #7257 ## features the cpu executor plans to support the following features: - basic models of vllm with f |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
