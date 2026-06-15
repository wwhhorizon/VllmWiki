# vllm-project/vllm#21250: [Usage]: Abnormal LoRA kernel performance

| 字段 | 值 |
| --- | --- |
| Issue | [#21250](https://github.com/vllm-project/vllm/issues/21250) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;kernel;operator |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Abnormal LoRA kernel performance

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm currently testing the performance of LoRA shrink expand kernel. My running cmd: python3 3rd_party/vllm/benchmarks/kernels/benchmark_lora.py list_bench --arg-pool-size 32 --batch-sizes 32 --dtype torch.float16 --hidden-sizes 4096 --lora-ranks 128 --num-loras 64 --op-types lora_shrink lora_expand --seq-lengths 1 --sort-by-lora-id 1 --cuda-graph-nops 32 32 tokens and totally 64 LoRAs, lora_rank=128. Not sure if I'm using it correctly? And I got following output: INFO 07-20 18:24:30 [__init__.py:244] Automatically detected platform cuda. Namespace(cmd='list_bench', hidden_sizes=[4096], lora_ranks=[128], dtype=torch.float16, arg_pool_size=32, cuda_graph_nops=32, num_loras=[64], num_active_loras=None, sort_by_lora_id=[True], op_types=[ , ], seq_lengths=[1], batch_sizes=[32], expand_fn_add_inputs=[True, False], output_directory=None, test_correctness=False, func= ) List bench : Hidden Sizes [4096] LoRA Ranks [128] Benchmarking 32 invocations inside a CUDA Graph [---------------------------------------------------------------------------------------------------------------...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --op-types lora_shrink lora_expand --seq-lengths 1 --sort-by-lora-id 1 --cuda-graph-nops 32 32 tokens and totally 64 LoRAs, lora_rank=128. Not sure if I'm using it correctly? And I got following output: INFO 07-20 18:24...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rnels/benchmark_lora.py list_bench --arg-pool-size 32 --batch-sizes 32 --dtype torch.float16 --hidden-sizes 4096 --lora-ranks 128 --num-loras 64 --op-types lora_shrink lora_expand --seq-lengths 1 --sort-by-lora-id 1 --c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n collect_env.py` ``` ### How would you like to use vllm I'm currently testing the performance of LoRA shrink expand kernel. My running cmd: python3 3rd_party/vllm/benchmarks/kernels/benchmark_lora.py list_bench --arg-p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns. performance gemm_linear cuda;gemm;kernel;operator slowdown dtype;env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [ , ], seq_lengths=[1], batch_sizes=[32], expand_fn_add_inputs=[True, False], output_directory=None, test_correctness=False, func= ) List bench : Hidden Sizes [4096] LoRA Ranks [128] Benchmarking 32 invocations inside a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
