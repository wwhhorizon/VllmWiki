# vllm-project/vllm#28959: [Bug]: IMA with Spec/Dec on H200

| 字段 | 值 |
| --- | --- |
| Issue | [#28959](https://github.com/vllm-project/vllm/issues/28959) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: IMA with Spec/Dec on H200

### Issue 正文摘录

### Your current environment - H200 - FLASH_ATTN_MLA ### 🐛 Describe the bug ``` MODEL := "deepseek-ai/DeepSeek-V3.1" launch_vllm_tp: VLLM_ALLREDUCE_USE_SYMM_MEM=0 VLLM_MOE_USE_DEEP_GEMM=0 VLLM_USE_DEEP_GEMM=1 VLLM_TORCH_PROFILER_DIR=$(pwd)/profiles_tp chg run --gpus 8 -- vllm serve \ {{MODEL}} --tensor-parallel-size 8 --speculative-config '{"num_speculative_tokens": 1, "method":"mtp"}' eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model={{MODEL}},base_url=http://localhost:8000/v1/completions,num_concurrent=100,tokenized_requests=False \ --limit 200 start_profile: curl -X POST http://localhost:8000/start_profile stop_profile: curl -X POST http://localhost:8000/stop_profile ``` ```bash (Worker_TP5 pid=2482335) ERROR 11-18 19:28:55 [multiproc_executor.py:815] WorkerProc hit an exception. (Worker_TP5 pid=2482335) ERROR 11-18 19:28:55 [multiproc_executor.py:815] Traceback (most recent call last): (Worker_TP5 pid=2482335) ERROR 11-18 19:28:55 [multiproc_executor.py:815] File "/home/robertgshaw2-redhat/vllm/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop (Worker_TP5 pid=2482335) ERROR 11-18 19:28:55 [multiproc_executor.py:815] output = fu...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: un --gpus 8 -- vllm serve \ {{MODEL}} --tensor-parallel-size 8 --speculative-config '{"num_speculative_tokens": 1, "method":"mtp"}' eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model={{MODEL}...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 8 19:28:55 [multiproc_executor.py:815] attn_metadata = attn_metadata_builder.build_for_drafting( (Worker_TP5 pid=2482335) ERROR 11-18 19:28:55 [multiproc_executor.py:815] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model={{MODEL}},base_url=http://localhost:8000/v1/completions,num_concurrent=100,tokenized_requests=False \ --limit 200 start_profile: curl -X POS...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ://localhost:8000/v1/completions,num_concurrent=100,tokenized_requests=False \ --limit 200 start_profile: curl -X POST http://localhost:8000/start_profile stop_profile: curl -X POST http://localhost:8000/stop_profile ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urrent environment - H200 - FLASH_ATTN_MLA ### 🐛 Describe the bug ``` MODEL := "deepseek-ai/DeepSeek-V3.1" launch_vllm_tp: VLLM_ALLREDUCE_USE_SYMM_MEM=0 VLLM_MOE_USE_DEEP_GEMM=0 VLLM_USE_DEEP_GEMM=1 VLLM_TORCH_PROFILER_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | n function> + 0xdbae4 (0x7f600eadbae4 in /lib64/libstdc++.so.6) frame #4: <unknown function> + 0x8b2fa (0x7f601748b2fa in /lib64/libc.so.6) frame #5: <unknown function> + 0x110540… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | venv/lib64/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdbae4 (0x7f600eadbae4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n function> + 0xdbae4 (0x7f600eadbae4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8b2fa (0x7f601748b2fa in /lib64/libc.so.6) frame #8: <unknown function> + 0x110540… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
