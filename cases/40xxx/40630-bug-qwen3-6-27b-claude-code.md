# vllm-project/vllm#40630: [Bug]: qwen3.6-27B claude code使用特别慢

| 字段 | 值 |
| --- | --- |
| Issue | [#40630](https://github.com/vllm-project/vllm/issues/40630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;quantization;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cache;fp8;operator |
| 症状 | crash;import_error;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3.6-27B claude code使用特别慢

### Issue 正文摘录

### Your current environment 两三个Claude Code请求并发时，上下文还没有到特别长的时候，日志打印的Avg经常是0： Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 1.8 tokens/s, Running: 4 reqs 硬件是4090 48G单卡： 全是最新版本 qwen3.6-27B-FP8 启动命令： CUDA_VISIBLE_DEVICES=0 vllm serve /home/ma/work/models/Qwen3.6-27B-FP8 --served-model-name gpt --port 8000 --max-model-len 220000 --reasoning-parser qwen3 --max-num-seqs 32 --gpu-memory-utilization 0.92 --host 0.0.0.0 --tool-call-parser qwen3_coder --enable-auto-tool-choice --async-scheduling --performance-mode throughput --enable-prefix-caching --kv-cache-dtype fp8 --enable-chunked-prefill (vllm-qwen) ma@gpu4090d:~$ python collect_env.py Traceback (most recent call last): File "/home/ma/collect_env.py", line 20, in from vllm.envs import environment_variables File "/home/ma/miniconda3/envs/vllm-qwen/lib/python3.12/site-packages/vllm/__init__.py", line 14, in import vllm.env_override # noqa: F401 ^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ma/miniconda3/envs/vllm-qwen/lib/python3.12/site-packages/vllm/env_override.py", line 87, in import torch File "/home/ma/miniconda3/envs/vllm-qwen/lib/python3.12/site-packages/torch/__init__.py", line 431, in from torch._C import...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ast): File "/home/ma/collect_env.py", line 20, in from vllm.envs import environment_variables File "/home/ma/miniconda3/envs/vllm-qwen/lib/python3.12/site-packages/vllm/__init__.py", line 14, in import vllm.env_override...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ughput: 1.8 tokens/s, Running: 4 reqs 硬件是4090 48G单卡： 全是最新版本 qwen3.6-27B-FP8 启动命令： CUDA_VISIBLE_DEVICES=0 vllm serve /home/ma/work/models/Qwen3.6-27B-FP8 --served-model-name gpt --port 8000 --max-model-len 220000 --reaso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tokens/s, Running: 4 reqs 硬件是4090 48G单卡： 全是最新版本 qwen3.6-27B-FP8 启动命令： CUDA_VISIBLE_DEVICES=0 vllm serve /home/ma/work/models/Qwen3.6-27B-FP8 --served-model-name gpt --port 8000 --max-model-len 220000 --reasoning-parser...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: async-scheduling --performance-mode throughput --enable-prefix-caching --kv-cache-dtype fp8 --enable-chunked-prefill (vllm-qwen) ma@gpu4090d:~$ python collect_env.py Traceback (most recent call last): File "/home/ma/col...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3.6-27B claude code使用特别慢 bug ### Your current environment 两三个Claude Code请求并发时，上下文还没有到特别长的时候，日志打印的Avg经常是0： Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 1.8 tokens/s, Running: 4 r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
