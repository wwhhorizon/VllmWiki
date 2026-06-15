# vllm-project/vllm#19909: [Bug]: file in `vllm/benchmarks/kernels/benchmark_marlin.py` cannot execute

| 字段 | 值 |
| --- | --- |
| Issue | [#19909](https://github.com/vllm-project/vllm/issues/19909) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: file in `vllm/benchmarks/kernels/benchmark_marlin.py` cannot execute

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the vllm/benchmarks/kernels/benchmark_marlin.py script using: use ```bash python benchmark_marlin.py ``` it cannot run. And print that ```bash INFO 06-20 21:54:24 [__init__.py:244] Automatically detected platform cuda. Benchmarking models: [0] meta-llama/Llama-2-7b-hf/TP1 Testing: meta-llama/Llama-2-7b-hf/TP1, act=False k_full=False, q=uint4b8, g=-1, MKN=(1x4096x12288) Traceback (most recent call last): File "/root/vllm/benchmarks/kernels/benchmark_marlin.py", line 342, in main(args) File "/root/vllm/benchmarks/kernels/benchmark_marlin.py", line 301, in main bench_run( File "/root/vllm/benchmarks/kernels/benchmark_marlin.py", line 200, in bench_run ).blocked_autorange(min_run_time=min_run_time) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm_cp312/lib/python3.12/site-packages/torch/utils/benchmark/utils/timer.py", line 376, in blocked_autorange number = self._estimate_block_size(min_run_time) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm_cp312/lib/python3.12/site-packages/torch/utils/benchmark/utils/timer.py", line 323, in _estimate_block_size time_taken = self._...

## 现有链接修复摘要

#19929 [Bugfix][Benchmark] Fix Marlin benchmark

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nfirm whether this is a bug in the benchmark script, or if I’m missing a dependency or type definition? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: :24 [__init__.py:244] Automatically detected platform cuda. Benchmarking models: [0] meta-llama/Llama-2-7b-hf/TP1 Testing: meta-llama/Llama-2-7b-hf/TP1, act=False k_full=False, q=uint4b8, g=-1, MKN=(1x4096x12288) Traceb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh INFO 06-20 21:54:24 [__init__.py:244] Automatically detected platform cuda. Benchmarking models: [0] meta-llama/Llama-2-7b-hf/TP1 Testing: meta-llama/Llama-2-7b-hf/TP1, act=False k_full=False, q=uint4b8, g=-1, MKN=(1...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: eta-llama/Llama-2-7b-hf/TP1 Testing: meta-llama/Llama-2-7b-hf/TP1, act=False k_full=False, q=uint4b8, g=-1, MKN=(1x4096x12288) Traceback (most recent call last): File "/root/vllm/benchmarks/kernels/benchmark_marlin.py",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ^^^^^^^^^^^ AttributeError: 'int' object has no attribute 'id' ``` 🙏 Request Could you please confirm whether this is a bug in the benchmark script, or if I’m missing a dependency or type definition? ### Before submitti...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19929](https://github.com/vllm-project/vllm/pull/19929) | closes_keyword | 0.95 | [Bugfix][Benchmark] Fix Marlin benchmark | Fix #19909 ## Test Plan ```bash python benchmarks/kernels/benchmark_marlin.py --batch-sizes 1 ``` ## Test Result ``` [------------------------------------------------------------ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
