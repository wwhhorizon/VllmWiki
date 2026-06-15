# vllm-project/vllm#7212: [Bug]: CUDA error when using speculative decoding with ibm-granite/granite-7b-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#7212](https://github.com/vllm-project/vllm/issues/7212) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error when using speculative decoding with ibm-granite/granite-7b-instruct

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I get a `RuntimeError: CUDA error: device-side assert triggered` error when inferencing with speculative decoding with the IBM granite 7b model: ``` vllm serve ibm-granite/granite-7b-instruct --speculative-model ibm-granite/granite-7b-instruct-accelerator --use-v2-block-manager --enforce-eager ``` The content of the request doesn't seem to matter. Any simple request fails for me such as: ``` curl http://localhost:3000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "ibm-granite/granite-7b-instruct", "prompt": "Hello", "temperature": 0 }' ``` Most relevant part of the logs: ``` ... WARNING 08-06 17:55:14 multi_step.py:57] Prompt logprob is not supported by multi step workers. (e.g., speculative decode uses multi step workers). ../aten/src/ATen/native/cuda/IndexKernel.cu:92: operator(): block: [0,0,0], thread: [0,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of bounds"` failed. ../aten/src/ATen/native/cuda/IndexKernel.cu:92: operator(): block: [0,0,0], thread: [1,0,0] Assertion `-sizes[i] <= index && index < sizes[i] && "index out of boun...

## 现有链接修复摘要

#7218 [Bugfix] Fix speculative decoding with MLPSpeculator with padded vocabulary

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: CUDA error when using speculative decoding with ibm-granite/granite-7b-instruct bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I get a `RuntimeError: CUD...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: untimeError: CUDA error: device-side assert triggered` error when inferencing with speculative decoding with the IBM granite 7b model: ``` vllm serve ibm-granite/granite-7b-instruct --speculative-model ibm-granite/grani...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;operator;quantization;sampling build_error;crash;slowdown dtype;env_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --speculative-model ibm-granite/granite-7b-instruct-accelerator --use-v2-block-manager --enforce-eager ``` The content of the request doesn't seem to matter. Any simple request fails for me such as: ``` curl http://loca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: CUDA error when using speculative decoding with ibm-granite/granite-7b-instruct bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I get a `RuntimeError: CUD...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7218](https://github.com/vllm-project/vllm/pull/7218) | closes_keyword | 0.95 | [Bugfix] Fix speculative decoding with MLPSpeculator with padded vocabulary | FIX #7212 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
