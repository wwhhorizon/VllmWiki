# vllm-project/vllm#6777: [Performance]:  Medusa SD  have poor performance than baseline

| 字段 | 值 |
| --- | --- |
| Issue | [#6777](https://github.com/vllm-project/vllm/issues/6777) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:  Medusa SD  have poor performance than baseline

### Issue 正文摘录

### Proposal to improve performance Test new feature medusa speculative sampling with [vllm v0.5.2](vllm-openai:v0.5.2). After using Medusa speculative sampling, the performance dropped significantly(mistral 7b tokens qps from 133 -> 93). Could it be that the model formats supported by vLLM are incompatible with those trained in [FastDecoding](https://github.com/FasterDecoding/Medusa)? The same model in TensorRT-LLM achieves a 2x speedup. model download: https://huggingface.co/FasterDecoding/medusa-1.0-zephyr-7b-beta ### Report of performance regression ## Llama 13 B 84 tokens/s -> 66 tokens/s ### Without speculation Processed prompts: 100%|███████████████████| 1/1 [00:01 93 tokens/s ### Without speculation Processed prompts: 100%|██████████████████| 1/1 [00:01<00:00, 1.98s/it, est. speed input: 21.70 toks/s, output: 129.19 toks/s] Processed prompts: 100%|██████████████████| 1/1 [00:01<00:00, 1.92s/it, est. speed input: 22.34 toks/s, output: 133.02 toks/s] Processed prompts: 100%|██████████████████| 1/1 [00:01<00:00, 1.92s/it, est. speed input: 22.36 toks/s, output: 133.10 toks/s] 0.007516195066273212 text: "As the current president of the United States, Joe Biden has been leading...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ous challenges, including a global pandemic, economic uncertainty, and social unrest. Despite these obstacles, Biden has remained steadfast in his commitment to serving the American people and working to address the iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: gnificantly(mistral 7b tokens qps from 133 -> 93). Could it be that the model formats supported by vLLM are incompatible with those trained in [FastDecoding](https://github.com/FasterDecoding/Medusa)? The same model in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: erformance]: Medusa SD have poor performance than baseline performance;stale ### Proposal to improve performance Test new feature medusa speculative sampling with [vllm v0.5.2](vllm-openai:v0.5.2). After using Medusa sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
