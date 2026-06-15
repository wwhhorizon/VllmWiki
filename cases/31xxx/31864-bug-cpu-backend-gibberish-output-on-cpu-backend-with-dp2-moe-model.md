# vllm-project/vllm#31864: [Bug][CPU Backend]: Gibberish output on CPU backend with DP2 + MoE Model

| 字段 | 值 |
| --- | --- |
| Issue | [#31864](https://github.com/vllm-project/vllm/issues/31864) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CPU Backend]: Gibberish output on CPU backend with DP2 + MoE Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug When using the **vLLM CPU backend** with **Data Parallelism (DP=2)** to infer **MoE models** (e.g., Qwen/Qwen1.5-MoE-A2.7B-Chat), the generated output is garbled or repetitive. Specifically, the output from **Rank 1** is significantly more corrupted/repetitive than that of Rank 0. ## Reproduction Script This issue can be consistently reproduced in offline mode. **Note:** To run the reproduction script below on the CPU backend, a temporary modification to `vllm/platforms/cpu.py` is required to allow `external_launcher` (see the "Modification" section below). ```bash torchrun --nproc-per-node=2 Qwen1.5-MoE-dp2.py ``` ```python # Qwen1.5-MoE-dp2.py from vllm import LLM, SamplingParams # Use identical prompts to check consistency across DP ranks prompts = [ "The president of the United States is", "The president of the United States is", ] # Greedy decoding to eliminate randomness sampling_params = SamplingParams(temperature=0.0) llm = LLM( model="Qwen/Qwen1.5-MoE-A2.7B-Chat", data_parallel_size=2, distributed_executor_backend="external_launcher", max_model_len=4096, seed=1, enforce_eager=True, ) dp_rank = llm.l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: en1.5-MoE-A2.7B-Chat), the generated output is garbled or repetitive. Specifically, the output from **Rank 1** is significantly more corrupted/repetitive than that of Rank 0. ## Reproduction Script This issue can be con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: scribe the bug When using the **vLLM CPU backend** with **Data Parallelism (DP=2)** to infer **MoE models** (e.g., Qwen/Qwen1.5-MoE-A2.7B-Chat), the generated output is garbled or repetitive. Specifically, the output fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][CPU Backend]: Gibberish output on CPU backend with DP2 + MoE Model bug;cpu ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug When using the **vLLM CPU backend** with **Data Parallelism (DP=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug][CPU Backend]: Gibberish output on CPU backend with DP2 + MoE Model bug;cpu ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug When using the **vLLM CPU backend** with **Data Parallelism (DP=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mal, the bug is highly likely to be triggered when **multiple concurrent requests** are sent or when using **Chinese language prompts**. ```bash vllm serve \ "Qwen/Qwen1.5-MoE-A2.7B-Chat" \ --enforce-eager \ -dp 2 ``` `...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
