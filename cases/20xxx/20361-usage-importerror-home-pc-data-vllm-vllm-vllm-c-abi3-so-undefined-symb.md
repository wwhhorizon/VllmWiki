# vllm-project/vllm#20361: [Usage]: ImportError: /home/pc/data/vllm/vllm/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb

| 字段 | 值 |
| --- | --- |
| Issue | [#20361](https://github.com/vllm-project/vllm/issues/20361) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ImportError: /home/pc/data/vllm/vllm/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb

### Issue 正文摘录

### Your current environment After my vllm installation was complete, I tried to run a model with it, but it kept throwing errors. I felt so sad. ```text (vllmNext) pc@pc-System-Product-Name:~/data/vllm/vllm/cmake$ VLLM_FLASH_ATTN_VERSION=2 CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_MODELSCOPE=true vllm serve Qwen/Qwen3-0.6B --enable-reasoning --reasoning-parser deepseek_r1 --port 8099 --max-model-len 32768 --gpu-memory-utilization 0.85 --max-num-seqs=32 --tensor-parallel-size 4 INFO 07-02 15:53:59 [__init__.py:244] Automatically detected platform cuda. Traceback (most recent call last): File "/home/pc/data/envs/vllmNext/bin/vllm", line 5, in from vllm.entrypoints.cli.main import main File "/home/pc/data/vllm/vllm/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/pc/data/vllm/vllm/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/home/pc/data/vllm/vllm/vllm/benchmarks/latency.py", line 16, in from vllm import LLM, SamplingParams File "/home/pc/data/vllm/vllm/vllm/__init__.py", line 64, in __getattr__ module = import_module(module_name, __p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Usage]: ImportError: /home/pc/data/vllm/vllm/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb usage;stale ### Your current environment After my vllm installation was complete, I tried to run a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t environment After my vllm installation was complete, I tried to run a model with it, but it kept throwing errors. I felt so sad. ```text (vllmNext) pc@pc-System-Product-Name:~/data/vllm/vllm/cmake$ VLLM_FLASH_ATTN_VER...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/pc/data/vllm/vllm/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.bench...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pc-System-Product-Name:~/data/vllm/vllm/cmake$ VLLM_FLASH_ATTN_VERSION=2 CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_MODELSCOPE=true vllm serve Qwen/Qwen3-0.6B --enable-reasoning --reasoning-parser deepseek_r1 --port 8099 --max-m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .py", line 20, in from vllm.config import (CompilationConfig, ModelDType, TokenizerMode, File "/home/pc/data/vllm/vllm/vllm/config.py", line 36, in from vllm.platforms import current_platform File "/home/pc/data/vllm/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
