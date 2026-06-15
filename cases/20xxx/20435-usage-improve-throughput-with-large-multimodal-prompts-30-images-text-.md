# vllm-project/vllm#20435: [Usage]: Improve throughput with large multimodal prompts (30 images + text , single-token output) – best-practice flags?

| 字段 | 值 |
| --- | --- |
| Issue | [#20435](https://github.com/vllm-project/vllm/issues/20435) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Improve throughput with large multimodal prompts (30 images + text , single-token output) – best-practice flags?

### Issue 正文摘录

❓ What am I trying to do? I am building an application that sends very large multimodal prompts with 30 images + text, plus a long system prompt) to a vLLM server and only asks for max_tokens = 1. I’d like to confirm that my server flags are reasonable and learn what I can tweak to speed things up. Images are resized on the longer size at 300 pixels ```bash vllm serve models/gemma-3-27b-it-FP8-Dynamic \ --tensor-parallel-size 1 \ --max-model-len 18000 \ --gpu-memory-utilization 0.8 \ --limit_mm_per_prompt 'image=30' \ --mm-processor-kwargs '{"do_pan_and_scan": true}' \ --max-num-seq 100 \ --port 8000 ``` Are the flags above the right place to start for “large prompt, tiny output” workloads? Thanks a lot for your guidance! vLLM has been great for multimodal experiments; I just want to squeeze a bit more performance out of this particular usage pattern. 🙏

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Improve throughput with large multimodal prompts (30 images + text , single-token output) – best-practice flags? usage;stale ❓ What am I trying to do? I am building an application that sends very large multimod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: utput) – best-practice flags? usage;stale ❓ What am I trying to do? I am building an application that sends very large multimodal prompts with 30 images + text, plus a long system prompt) to a vLLM server and only asks...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: the longer size at 300 pixels ```bash vllm serve models/gemma-3-27b-it-FP8-Dynamic \ --tensor-parallel-size 1 \ --max-model-len 18000 \ --gpu-memory-utilization 0.8 \ --limit_mm_per_prompt 'image=30' \ --mm-processor-kw...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: are resized on the longer size at 300 pixels ```bash vllm serve models/gemma-3-27b-it-FP8-Dynamic \ --tensor-parallel-size 1 \ --max-model-len 18000 \ --gpu-memory-utilization 0.8 \ --limit_mm_per_prompt 'image=30' \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ts (30 images + text , single-token output) – best-practice flags? usage;stale ❓ What am I trying to do? I am building an application that sends very large multimodal prompts with 30 images + text, plus a long system pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
