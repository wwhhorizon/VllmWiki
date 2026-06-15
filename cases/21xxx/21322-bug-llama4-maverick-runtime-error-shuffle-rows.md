# vllm-project/vllm#21322: [Bug]: Llama4 Maverick runtime error (shuffle_rows)

| 字段 | 值 |
| --- | --- |
| Issue | [#21322](https://github.com/vllm-project/vllm/issues/21322) |
| 状态 | closed |
| 标签 | bug;llama |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Llama4 Maverick runtime error (shuffle_rows)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug llama4 maverick is failing to start due to the runtime error during shuffle_row. this can be reproduced: ``` vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.8 --disable-log-requests ``` This is likely related to #20762 @ElizaWszola this can also be reproduced with `pytest -s tests/models/multimodal/generation/test_maverick.py`, which requires only 2xH100 by running dummy version of maverick. cc @yeqcharlotte @luccafong @houseroad ``` (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multiproc_executor.py:546] File "/data/users/yming/gitrepos/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1579, in moe_forward (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multiproc_executor.py:546] return self.forward_impl(hidden_states, router_logits) (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multiproc_executor.py:546] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multiproc_executor.py:546] File "/data/users/ymin...

## 现有链接修复摘要

#20762 [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE | #21334 Revert "[Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE (#20762)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eneration/test_maverick.py`, which requires only 2xH100 by running dummy version of maverick. cc @yeqcharlotte @luccafong @houseroad ``` (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multiproc_executor.py:546] Fi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: reproduced: ``` vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.8 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 Maverick runtime error (shuffle_rows) bug;llama ### Your current environment ### 🐛 Describe the bug llama4 maverick is failing to start due to the runtime error during shuffle_row. this can be reproduced:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ts/models/multimodal/generation/test_maverick.py`, which requires only 2xH100 by running dummy version of maverick. cc @yeqcharlotte @luccafong @houseroad ``` (VllmWorker rank=0 pid=938767) ERROR 07-21 11:16:11 [multipr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.8 --disable-log-requests ``` This is likely related to #20...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20762](https://github.com/vllm-project/vllm/pull/20762) | mentioned | 0.45 | [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE | utilization 0.8 --disable-log-requests ``` this is likely related to #20762 @elizawszola this can also be reproduced with `pytest -s tests/models/multimodal/generation/test_maveri… |
| [#21334](https://github.com/vllm-project/vllm/pull/21334) | closes_keyword | 0.95 | Revert "[Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE (#20762) | fix #21322 ## Test Plan 1. pytest -v -s tests/models/multimodal/generation/test_maverick.py 2. lm_eval maverick ## Test Result 1. UT passed 2. lm_eval result: local-chat-compl |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
