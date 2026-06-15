# vllm-project/vllm#25985: [Bug]: IMA with the prefix_prefill::context_attention_fwd kernel when capturing full cudagraphs

| 字段 | 值 |
| --- | --- |
| Issue | [#25985](https://github.com/vllm-project/vllm/issues/25985) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: IMA with the prefix_prefill::context_attention_fwd kernel when capturing full cudagraphs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In order to repro the bug, you'll have to undo the fix in `vllm/v1/attention/backends/rocm_attn.py`. Simply cut out the following lines in `build_for_cudagraph_capture` ``` if envs.VLLM_V1_USE_PREFILL_DECODE_ATTENTION: # Here we set the query start locs to 0. This is to # cover up an invalid memory access in the prefix_prefil kernel # that we run into during graph capture common_attn_metadata.query_start_loc.zero_() common_attn_metadata.query_start_loc_cpu.zero_() ``` Once those lines are cut out, you can repro the IMA by running the following command ` VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --max-num-seqs 256 --compilation-config='{"cudagraph_mode":"FULL"}'` This bug was introduced in #24845 which added proper setup of query_start_locs to the _dummy_run in the GpuModelRunner. Something about this causes the prefix_prefill kernel to trigger an IMA when writing to it's output tensor. It would be good to investigate this further and fix the IMA in the kernel. Then we can get rid of the bandaid fix inside of `build_for_cudagraph_capture` ### Before submitting a new issue... - [x] Make sure...

## 现有链接修复摘要

#24845 [Core/DBO][2/N] Dual-Batch Overlap add DeepEP High Throughput support and Prefill support

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: IMA with the prefix_prefill::context_attention_fwd kernel when capturing full cudagraphs bug;rocm;stale ### Your current environment ### 🐛 Describe the bug In order to repro the bug, you'll have to undo the fix i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: attention/backends/rocm_attn.py`. Simply cut out the following lines in `build_for_cudagraph_capture` ``` if envs.VLLM_V1_USE_PREFILL_DECODE_ATTENTION: # Here we set the query start locs to 0. This is to # cover up an i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ith the prefix_prefill::context_attention_fwd kernel when capturing full cudagraphs bug;rocm;stale ### Your current environment ### 🐛 Describe the bug In order to repro the bug, you'll have to undo the fix in `vllm/v1/a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llowing command ` VLLM_V1_USE_PREFILL_DECODE_ATTENTION=1 vllm serve meta-llama/Llama-3.1-8B-Instruct --max-num-seqs 256 --compilation-config='{"cudagraph_mode":"FULL"}'` This bug was introduced in #24845 which added pro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rder to repro the bug, you'll have to undo the fix in `vllm/v1/attention/backends/rocm_attn.py`. Simply cut out the following lines in `build_for_cudagraph_capture` ``` if envs.VLLM_V1_USE_PREFILL_DECODE_ATTENTION: # He...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24845](https://github.com/vllm-project/vllm/pull/24845) | mentioned | 0.45 | [Core/DBO][2/N] Dual-Batch Overlap add DeepEP High Throughput support and Prefill support | ation-config='{"cudagraph_mode":"full"}'` this bug was introduced in #24845 which added proper setup of query_start_locs to the _dummy_run in the gpumodelrunner. something about t… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
