# vllm-project/vllm#40144: [Bug]: vllm/vllm-openai:nightly-18013df6ae27c3fb941307c46c975227126d641f Missing pandas package

| 字段 | 值 |
| --- | --- |
| Issue | [#40144](https://github.com/vllm-project/vllm/issues/40144) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:nightly-18013df6ae27c3fb941307c46c975227126d641f Missing pandas package

### Issue 正文摘录

### Your current environment docker run -d \ --name vllm \ --runtime nvidia \ --gpus '"device=0,1,2,3,4,5,6,7"' \ --shm-size 64g \ -p 5678:8000 \ -v /root/.cache/huggingface:/root/.cache/huggingface \ -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ --entrypoint bash \ vllm/vllm-openai:nightly \ -c "vllm serve global_step_70/actor \ --host 0.0.0.0 \ --port 8000 \ --served-model-name qwen3-rl-latest \ --trust-remote-code \ --dtype bfloat16 \ --max-model-len 81920 \ --tensor-parallel-size 1 \ --data-parallel-size 8 \ --max-num-seqs 24 \ --max-num-batched-tokens 163840 \ --gpu-memory-utilization 0.95 \ --enable-chunked-prefill \ --enable-prefix-caching" ### 🐛 Describe the bug When I deployed Qwen3 using the latest official Docker image of vllm, an error occurred： Traceback (most recent call last): File "/usr/local/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/__init__.py", line 4, in from vllm.entrypoints.cli.benchmark.mm_processor import ( File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/benchmark/mm_processor.py", line 5, in from vllm.benchmarks.mm_processor import add_cli_args, main File "/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: c975227126d641f Missing pandas package bug ### Your current environment docker run -d \ --name vllm \ --runtime nvidia \ --gpus '"device=0,1,2,3,4,5,6,7"' \ --shm-size 64g \ -p 5678:8000 \ -v /root/.cache/huggingface:/r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name qwen3-rl-latest \ --trust-remote-code \ --dtype bfloat16 \ --max-model-len 81920 \ --tensor-parallel-size 1 \ --data-parallel-size 8 \ --max-num-seqs 24 \ --max-num-batched-tokens 163840 \ --gpu-memo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ,4,5,6,7"' \ --shm-size 64g \ -p 5678:8000 \ -v /root/.cache/huggingface:/root/.cache/huggingface \ -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ --entrypoint bash \ vllm/vllm-openai:nightly \ -c "vllm serve global_step_70/actor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ecutor/layers/utils.py", line 11, in from vllm._aiter_ops import rocm_aiter_ops File "/usr/local/lib/python3.12/dist-packages/vllm/_aiter_ops.py", line 6, in import pandas as pd ModuleNotFoundError: No module named 'pan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: --host 0.0.0.0 \ --port 8000 \ --served-model-name qwen3-rl-latest \ --trust-remote-code \ --dtype bfloat16 \ --max-model-len 81920 \ --tensor-parallel-size 1 \ --data-parallel-size 8 \ --max-num-seqs 24 \ --max-num-bat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
