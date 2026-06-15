# vllm-project/vllm#36010: [Bug]: Qwen/Qwen3.5-27B Batch Inference very slow / not working

| 字段 | 值 |
| --- | --- |
| Issue | [#36010](https://github.com/vllm-project/vllm/issues/36010) |
| 状态 | open |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3.5-27B Batch Inference very slow / not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran several prompts that are very similar. With Gemma 3 (27B), I achieve around 1,000 tokens per second, whereas with Qwen3-27B I only get about 20 tokens per second. Below is an example using a long prompt. I recommend testing both Qwen and Gemma to observe the performance difference yourself — simply replace the model name. I guess something isn't working with batch inference (and maybe guided regex ?). ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams import time import torch model_name = "Qwen/Qwen3.5-27B" # change to "google/gemma-3-27b-it" for Gemma 3 as a reference print("Loading model...", end=" ", flush=True) t0 = time.time() llm = LLM( model=model_name, quantization="bitsandbytes", dtype="bfloat16", max_model_len=16384, gpu_memory_utilization=0.88, max_num_seqs=128, trust_remote_code=True, enforce_eager=False, ) load_time = time.time() - t0 print(f"done ({load_time:.1f} s)\n") # ──────────────────────────────────────── # Prompts: Is number 1–2000 a prime number? # ──────────────────────────────────────── prompt_template = """Is the following number a prime number? Answer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: working with batch inference (and maybe guided regex ?). ``` from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams import time import torch model_name = "Qwen/Qwen3.5-27B" # chang...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =" ", flush=True) t0 = time.time() llm = LLM( model=model_name, quantization="bitsandbytes", dtype="bfloat16", max_model_len=16384, gpu_memory_utilization=0.88, max_num_seqs=128, trust_remote_code=True, enforce_eager=Fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen/Qwen3.5-27B Batch Inference very slow / not working bug ### Your current environment ### 🐛 Describe the bug I ran several prompts that are very similar. With Gemma 3 (27B), I achieve around 1,000 tokens per...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ate.format(n) for n in range(1, 2001)] # A single regex → full batching capability structured = StructuredOutputsParams( regex=r"^\s*(true|false)\s*$" ) sampling = SamplingParams( temperature=0.0, max_tokens=10, min_tok...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: print(f"Tokens per sec: {total_tokens / total_time:.1f} t/s") print(f"Requests per sec: {2000 / total_time:.1f} req/s") print(f"GPU alloc: {torch.cuda.memory_allocated() / 1e9:.1f} GB") print(f"GPU peak : {torch.cuda.ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
