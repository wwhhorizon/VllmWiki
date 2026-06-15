# vllm-project/vllm#25013: [Bug]: benchmark_lora.py run fail with RuntimeError: vllm::lora_shrink() is missing value for argument 'no_lora_flag_cpu' error

| 字段 | 值 |
| --- | --- |
| Issue | [#25013](https://github.com/vllm-project/vllm/issues/25013) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_lora.py run fail with RuntimeError: vllm::lora_shrink() is missing value for argument 'no_lora_flag_cpu' error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run the following command to reproduce the error: ```Python python3 benchmarks/kernels/benchmark_lora.py model_bench --models meta-llama/Llama-3-8b --arg-pool-size 32 --batch-sizes 32 --dtype torch.float16 --lora-ranks 16 --num-loras 1 4 --op-types lora_shrink lora_expand --seq-lengths 16 --sort-by-lora-id 1 --cuda-graph-nops 32 ``` Error output: ``` Benchmarking 32 invocations inside a CUDA Graph Traceback (most recent call last): File "/home/ec2-user/vllm/benchmarks/kernels/benchmark_lora.py", line 1065, in args.func(args) File "/home/ec2-user/vllm/benchmarks/kernels/benchmark_lora.py", line 918, in run_model_bench run(args, bench_contexts) File "/home/ec2-user/vllm/benchmarks/kernels/benchmark_lora.py", line 793, in run bench_optype( File "/home/ec2-user/vllm/benchmarks/kernels/benchmark_lora.py", line 642, in bench_optype op_type.bench_fn()(**kwargs) File "/home/ec2-user/.local/lib/python3.9/site-packages/torch/_ops.py", line 1243, in __call__ return self._op(*args, **kwargs) RuntimeError: vllm::lora_shrink() is missing value for argument 'no_lora_flag_cpu'. Declaration: vllm::lora_shrink(Tensor inputs, Tensor[] lora_a_weight...

## 现有链接修复摘要

#25014 [BugFix] Fix the missing value for argument 'no_lora_flag_cpu' error when running benchmark_lora.py

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;kernel;operator;sampling;triton build_error;crash;nan_inf dtype;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ch --models meta-llama/Llama-3-8b --arg-pool-size 32 --batch-sizes 32 --dtype torch.float16 --lora-ranks 16 --num-loras 1 4 --op-types lora_shrink lora_expand --seq-lengths 16 --sort-by-lora-id 1 --cuda-graph-nops 32 ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -op-types lora_shrink lora_expand --seq-lengths 16 --sort-by-lora-id 1 --cuda-graph-nops 32 ``` Error output: ``` Benchmarking 32 invocations inside a CUDA Graph Traceback (most recent call last): File "/home/ec2-user/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oduce the error: ```Python python3 benchmarks/kernels/benchmark_lora.py model_bench --models meta-llama/Llama-3-8b --arg-pool-size 32 --batch-sizes 32 --dtype torch.float16 --lora-ranks 16 --num-loras 1 4 --op-types lor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark_lora.py run fail with RuntimeError: vllm::lora_shrink() is missing value for argument 'no_lora_flag_cpu' error bug ### Your current environment ### 🐛 Describe the bug Run the following command to reprod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25014](https://github.com/vllm-project/vllm/pull/25014) | closes_keyword | 0.95 | [BugFix] Fix the missing value for argument 'no_lora_flag_cpu' error when running benchmark_lora.py | FIx the bug #25013 by adding the argument `no_lora_flag_cpu` when preparing the input arguments in `as_lora_shrink_kwargs` and `as_lora_expand_kwargs`. ## Test Plan ```python pyth |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
