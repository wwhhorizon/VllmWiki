# vllm-project/vllm#36627: [Performance]: qwen3.5 vs qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#36627](https://github.com/vllm-project/vllm/issues/36627) |
| 状态 | open |
| 标签 | performance |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: qwen3.5 vs qwen3

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Why does the actual performance test show that Qwen3.5 is not better than Qwen3, especially with TTFT being much slower than Qwen3? Environment: A10 24G Driver Version: 590.48.01 CUDA Version: 13.1 VLLM Version: vllm/vllm-openai:nightly Service startup command: docker run --rm \ --name qwen-server \ --runtime nvidia \ --gpus device=0 \ -v /data/cache/huggingface:/root/.cache/huggingface \ -v /work:/models \ -p 13003:8000 \ --ipc=host \ vllm/vllm-openai:nightly \ --model /models/Qwen3-8B \ --served-model-name Qwen3-8B \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 \ --reasoning-parser qwen3 \ --enable-prefix-caching ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: actual performance test show that Qwen3.5 is not better than Qwen3, especially with TTFT being much slower than Qwen3? Environment: A10 24G Driver Version: 590.48.01 CUDA Version: 13.1 VLLM Version: vllm/vllm-openai:nig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: qwen3.5 vs qwen3 performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Why does the actual performance test sh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: much slower than Qwen3? Environment: A10 24G Driver Version: 590.48.01 CUDA Version: 13.1 VLLM Version: vllm/vllm-openai:nightly Service startup command: docker run --rm \ --name qwen-server \ --runtime nvidia \ --gpus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Why does the actual performance test show that Qwen3.5 is not better than Qwen3, especia...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
