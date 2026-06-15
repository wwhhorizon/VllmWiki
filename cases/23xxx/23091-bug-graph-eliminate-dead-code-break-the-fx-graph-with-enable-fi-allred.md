# vllm-project/vllm#23091: [Bug]: `graph.eliminate_dead_code()` break the fx graph with `enable_fi_allreduce_fusion` when TP == 2

| 字段 | 值 |
| --- | --- |
| Issue | [#23091](https://github.com/vllm-project/vllm/issues/23091) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `graph.eliminate_dead_code()` break the fx graph with `enable_fi_allreduce_fusion` when TP == 2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are trying to add `graph.eliminate_dead_code()` to the end of all the passes before fix_functionalization. i.e. [the code here](https://github.com/vllm-project/vllm/blob/6e672daf62e7b03ff1dcf74e4206dad07d39d4ec/vllm/compilation/pass_manager.py#L48-L50). However, when setting compilation-config to `'{"custom_ops":["+rms_norm","+quant_fp8"],"pass_config":{"enable_fi_allreduce_fusion":true}}'`, we encountered a fx graph error. Provided the reproduction steps and error back trace. Note that the issue is only reproducible on TP2 or maybe larger TP. ``` VLLM_SKIP_P2P_CHECK=1 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ \ vllm serve \ nvidia/Llama-3.3-70B-Instruct-FP8 \ --host 0.0.0.0 --port 8080 \ --tokenizer nvidia/Llama-3.3-70B-Instruct-FP8 \ --dtype auto \ --kv-cache-dtype fp8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --swap-space 16 \ --max-num-seqs 512 \ --max-model-len 9216 \ --max-num-batched-tokens 8192 \ --gpu-memory-utilization 0.9 \ --compilation-config '{"custom_ops":["+rms_norm","+quant_fp8"],"pass_config":{"enable_fi_allreduce_fusion":true}}' \ --trust-remote-code \ --enable-chunked-prefill \ --no-enable-prefi...

## 现有链接修复摘要

#24188 [torch.compile] Custom op matching | #24542 [torch.compile] Cleanup compilation tests and custom passes, add debug utils, fix DCE bug (#23091), fix test (#24376), and prep for…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: roduction steps and error back trace. Note that the issue is only reproducible on TP2 or maybe larger TP. ``` VLLM_SKIP_P2P_CHECK=1 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ \ vllm serve \ nvidia/Llama-3.3-70B-Instruct-FP8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: compilation/pass_manager.py#L48-L50). However, when setting compilation-config to `'{"custom_ops":["+rms_norm","+quant_fp8"],"pass_config":{"enable_fi_allreduce_fusion":true}}'`, we encountered a fx graph error. Provide...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e on TP2 or maybe larger TP. ``` VLLM_SKIP_P2P_CHECK=1 \ VLLM_ATTENTION_BACKEND=FLASHINFER \ \ vllm serve \ nvidia/Llama-3.3-70B-Instruct-FP8 \ --host 0.0.0.0 --port 8080 \ --tokenizer nvidia/Llama-3.3-70B-Instruct-FP8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: wever, when setting compilation-config to `'{"custom_ops":["+rms_norm","+quant_fp8"],"pass_config":{"enable_fi_allreduce_fusion":true}}'`, we encountered a fx graph error. Provided the reproduction steps and error back...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: y ERROR 08-18 07:54:17 [multiproc_executor.py:596] self.model_runner.profile_run() ERROR 08-18 07:54:17 [multiproc_executor.py:596] File "/workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 2621, in profile_run ER...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24188](https://github.com/vllm-project/vllm/pull/24188) | closes_keyword | 0.95 | [torch.compile] Custom op matching | fix #23091 - add `LazyInitPass` test utility - add env var for pattern match debugging (TODO: docs) - fix `test_sequence_parallelism.py` - add assert to `test_silu_mul_quant_fusion |
| [#24542](https://github.com/vllm-project/vllm/pull/24542) | closes_keyword | 0.95 | [torch.compile] Cleanup compilation tests and custom passes, add debug utils, fix DCE bug (#23091), fix test (#24376), and prep for custom op matching (#24604) | fix #23091 - add `LazyInitPass` test utility - add env var for pattern match debugging (TODO: docs) - fix `test_sequence_parallelism.py` - add assert to `test_silu_mul_quant_fusion |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
