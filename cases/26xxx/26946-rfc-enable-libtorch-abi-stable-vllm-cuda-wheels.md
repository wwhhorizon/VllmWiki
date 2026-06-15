# vllm-project/vllm#26946: [RFC]: Enable libtorch-ABI-stable vLLM cuda wheels

| 字段 | 值 |
| --- | --- |
| Issue | [#26946](https://github.com/vllm-project/vllm/issues/26946) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Enable libtorch-ABI-stable vLLM cuda wheels

### Issue 正文摘录

### Motivation. PyTorch is building out a limited ABI through which custom ops writers can build extensions that build with one torch version and run on another. vLLM is an important part of the ecosystem that depends on torch. We'd like to help enable building vLLM wheels that would not be tied to a specific torch version to promote build system simplicity and general developer experience. ### Proposed Change. As PyTorch increases our ABI surface, we'd love vLLM's collaboration in testing out our stable APIs. We've gone through the repo and gathered the following torch APIs that we are working to make stable. The hope is that once we have the stable versions of these ops, we can build vLLM cuda wheels in a libtorch stable manner, similar to what we did in FA3 here: https://github.com/Dao-AILab/flash-attention/pull/1791 The APIs: - [ ] Various TORCH_LIBRARY registrations [[link](https://github.com/vllm-project/vllm/blob/main/csrc/torch_bindings.cpp)] - [ ] at::Tag [[link](https://github.com/vllm-project/vllm/blob/1c63a16b653d1f3f4260e862f01eaffed283c4c8/csrc/torch_bindings.cpp#L30)] - [ ] Device stuff - [ ] torch::kDevice - [ ] at::Device - [ ] t.device().type() - [ ] Get_device -...

## 现有链接修复摘要

#28756 Use narrow over indexing in `hadacore_transform` to prep for ABI stable | #29027 Simplify `from_blob` usage in `get_cuda_view_from_cpu_tensor`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [RFC]: Enable libtorch-ABI-stable vLLM cuda wheels RFC ### Motivation. PyTorch is building out a limited ABI through which custom ops writers can build extensions that build with one torch version and run on another. vL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vLLM cuda wheels in a libtorch stable manner, similar to what we did in FA3 here: https://github.com/Dao-AILab/flash-attention/pull/1791 The APIs: - [ ] Various TORCH_LIBRARY registrations [[link](https://github.com/vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Enable libtorch-ABI-stable vLLM cuda wheels RFC ### Motivation. PyTorch is building out a limited ABI through which custom ops writers can build extensions that build with one torch version and run on another. vL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: :indexing::Slice(...)) - [ ] torch::empty(..., TensorOptions.device(...).dtype(...)) - [ ] tensor.sum(dim) - [ ] Equivalent_scalar_type_v - [ ] Tensor.const_data_ptr Questions for vLLM maintainers: 1. How does the plan...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be feasible to support vLLM CUDA kernels by PyTorch 2.10 (branch cut is slotted for early December), so we'd like to get started on this as soon as possible. ### CC List. @mikaylagawarecki @zou3519 @albanD ### Any Other...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28756](https://github.com/vllm-project/vllm/pull/28756) | mentioned | 0.6 | Use narrow over indexing in `hadacore_transform` to prep for ABI stable | dacore_transform` kernel. They compute the same slice. Contributes to #26946. ## Test Plan ` pytest tests/kernels/quantization/test_hadacore.py ` ## Test Result ``` (vllm) [janeyx… |
| [#29027](https://github.com/vllm-project/vllm/pull/29027) | mentioned | 0.6 | Simplify `from_blob` usage in `get_cuda_view_from_cpu_tensor` | t does not take in a deleter (so this contributes a bit indirectly to #26946). ## Test Plan Locally ran test_uva.py ## Test Result ``` (vllm) [janeyx@devgpu007.eag6 /data/users/ja… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
