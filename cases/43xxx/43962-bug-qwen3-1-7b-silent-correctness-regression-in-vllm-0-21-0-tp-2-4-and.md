# vllm-project/vllm#43962: [Bug]: Qwen3-1.7B silent correctness regression in vLLM 0.21.0: TP=2/4 and Triton attention produce wrong answer

| 字段 | 值 |
| --- | --- |
| Issue | [#43962](https://github.com/vllm-project/vllm/issues/43962) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-1.7B silent correctness regression in vLLM 0.21.0: TP=2/4 and Triton attention produce wrong answer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description `Qwen/Qwen3-1.7B` on vLLM 0.21.0 gives a wrong answer to the simple arithmetic prompt `2 ** 10` when using tensor parallelism. The model outputs `512` or `81` instead of `1024`. When TP=1, the result is correct. This is a **regression** from vLLM 0.19.1, which produces correct results on all configs. ## Reproduction ```python import os; os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" from vllm import LLM, SamplingParams MODEL = "Qwen/Qwen3-1.7B" PROMPT = "In Python, what is the output of: 2 ** 10? Answer with just the number." sp = SamplingParams(temperature=0.0, top_p=1.0, seed=42, max_tokens=32) for seed in [42, 0, 100]: sp.seed = seed a = LLM(model=MODEL, enforce_eager=True).generate([PROMPT], sp)[0].outputs[0].text b = LLM(model=MODEL, enforce_eager=True, tensor_parallel_size=2).generate([PROMPT], sp)[0].outputs[0].text c = LLM(model=MODEL, enforce_eager=True, attention_backend="TRITON_ATTN").generate([PROMPT], sp)[0].outputs[0].text print(f"seed={seed}: TP=1='{a.strip()}' || TP=2='{b.strip()}' || Triton='{c.strip()}'") ``` ### Expected output (all 3 seeds) ``` seed=42: TP=1='1024' || TP=2='1024' || Triton='102...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ich produces correct results on all configs. ## Reproduction ```python import os; os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" from vllm import LLM, SamplingParams MODEL = "Qwen/Qwen3-1.7B" PROMPT = "In Python, what...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ug]: Qwen3-1.7B silent correctness regression in vLLM 0.21.0: TP=2/4 and Triton attention produce wrong answer bug ### Your current environment ### 🐛 Describe the bug ## Description `Qwen/Qwen3-1.7B` on vLLM 0.21.0 give...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wer to the simple arithmetic prompt `2 ** 10` when using tensor parallelism. The model outputs `512` or `81` instead of `1024`. When TP=1, the result is correct. This is a **regression** from vLLM 0.19.1, which produces...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-1.7B silent correctness regression in vLLM 0.21.0: TP=2/4 and Triton attention produce wrong answer bug ### Your current environment ### 🐛 Describe the bug ## Description `Qwen/Qwen3-1.7B` on vLLM 0.21.0 gi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: | TP=2 + prefix_cache | **512** | prefix_cache | 1024 | | TP=2 + chunked_prefill | **512** | chunked_prefill | 1024 | | TP=4 + prefix_cache | **512** | block_size=32 | 1024 | ## Cross-version confirmation | vLLM | TP=1...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
