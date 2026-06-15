# vllm-project/vllm#38348: [Bug]: chunked prefill can't be disabled. maybe due to race condition in scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#38348](https://github.com/vllm-project/vllm/issues/38348) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: chunked prefill can't be disabled. maybe due to race condition in scheduler

### Issue 正文摘录

### Your current environment vLLM 0.17.0 python 3.12 ### 🐛 Describe the bug I want to disable chunked prefill. so i set the max_model_length to (seqlen + max_tokens), max_num_seqs to batch size, max_num_batched_tokens to (batch size * max_model_len)。However I still find the req chunked when i look at the log. But When set the os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" chunked prefill will be disabled. looks like a bug to me. ``` import os // if use VLLM_ENABLE_V1_MULTIPROCESSING will cause chunked prefill can't be disabled // only add this environment variable can make sure chunked prefill is disabled. //os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" os.environ["VLLM_LOGGING_LEVEL"] = "DEBUG" import argparse from datetime import datetime import torch from vllm import LLM, SamplingParams def main(): parser = argparse.ArgumentParser() // some args parse here args = parser.parse_args() timestamp = datetime.now().strftime("%m%d%H%M%S") profile_dir = os.path.abspath(f"profile_{timestamp}") os.makedirs(profile_dir, exist_ok=True) max_model_len = args.seqlen + args.max_tokens llm = LLM( model=args.model, tensor_parallel_size=args.tp, load_format="dummy", dtype="bfloat16", enf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: G"] = "0" chunked prefill will be disabled. looks like a bug to me. ``` import os // if use VLLM_ENABLE_V1_MULTIPROCESSING will cause chunked prefill can't be disabled // only add this environment variable can make sure...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: tensor_parallel_size=args.tp, load_format="dummy", dtype="bfloat16", enforce_eager=True, max_model_len=max_model_len, max_num_seqs=args.bs, max_num_batched_tokens=args.bs * max_model_len, enable_chunked_prefill=False, e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 🐛 Describe the bug I want to disable chunked prefill. so i set the max_model_length to (seqlen + max_tokens), max_num_seqs to batch size, max_num_batched_tokens to (batch size * max_model_len)。However I still find the r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: .parse_args() timestamp = datetime.now().strftime("%m%d%H%M%S") profile_dir = os.path.abspath(f"profile_{timestamp}") os.makedirs(profile_dir, exist_ok=True) max_model_len = args.seqlen + args.max_tokens llm = LLM( mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llm.generate(prompts=prompts, sampling_params=sampling_params) torch.cuda.synchronize() # Profile print(f"Profiling batch size {args.bs}... traces will be saved to {profile_dir}") llm.start_profile(profile_prefix=f"mixe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
