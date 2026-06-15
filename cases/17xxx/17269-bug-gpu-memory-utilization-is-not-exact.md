# vllm-project/vllm#17269: [Bug]: gpu-memory-utilization is not exact

| 字段 | 值 |
| --- | --- |
| Issue | [#17269](https://github.com/vllm-project/vllm/issues/17269) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpu-memory-utilization is not exact

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run this: CUDA_VISIBLE_DEVICES=1 vllm serve /app/data/gemma-3-27b-it/model \ --quantization bitsandbytes --gpu-memory-utilization 0.42 \ --max-model-len 4096 --block-size 16 \ --disable-mm-preprocessor-cache --max-num-seqs 32 \ --limit-mm-per-prompt image=1 I have A100 80GB and expect that model takes 33.6 Gb. But it takes 25414MiB. Why? I had another program that take 10 GB before running above instruction. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;gemm;operator;quantization;sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ale ### Your current environment ### 🐛 Describe the bug I run this: CUDA_VISIBLE_DEVICES=1 vllm serve /app/data/gemma-3-27b-it/model \ --quantization bitsandbytes --gpu-memory-utilization 0.42 \ --max-model-len 4096 --b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tion bitsandbytes --gpu-memory-utilization 0.42 \ --max-model-len 4096 --block-size 16 \ --disable-mm-preprocessor-cache --max-num-seqs 32 \ --limit-mm-per-prompt image=1 I have A100 80GB and expect that model takes 33....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: escribe the bug I run this: CUDA_VISIBLE_DEVICES=1 vllm serve /app/data/gemma-3-27b-it/model \ --quantization bitsandbytes --gpu-memory-utilization 0.42 \ --max-model-len 4096 --block-size 16 \ --disable-mm-preprocessor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gpu-memory-utilization is not exact bug;stale ### Your current environment ### 🐛 Describe the bug I run this: CUDA_VISIBLE_DEVICES=1 vllm serve /app/data/gemma-3-27b-it/model \ --quantization bitsandbytes --gpu-m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
