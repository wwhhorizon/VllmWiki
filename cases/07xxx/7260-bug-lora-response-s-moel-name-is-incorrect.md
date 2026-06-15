# vllm-project/vllm#7260: [Bug]: lora response's moel name is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#7260](https://github.com/vllm-project/vllm/issues/7260) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: lora response's moel name is incorrect

### Issue 正文摘录

### Your current environment ```text vllm 0.5.4 ``` ### 🐛 Describe the bug 1. start vllm server `python -m vllm.entrypoints.openai.api_server --served-model-name qwen2 --model /ai-deploy/open-models/Qwen/Qwen2-72B-Instruct/ --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --max-model-len 131072 --enable-prefix-caching --enable-lora --lora-modules test1=/ai-deploy/output/ test2=/ai-deploy/output/ test3=/ai-deploy/output/` 2. request with model name test1 3. get response with model name `qwen2` rather than `test1`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: start vllm server `python -m vllm.entrypoints.openai.api_server --served-model-name qwen2 --model /ai-deploy/open-models/Qwen/Qwen2-72B-Instruct/ --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --max-model-len 131...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: lora response's moel name is incorrect bug;stale ### Your current environment ```text vllm 0.5.4 ``` ### 🐛 Describe the bug 1. start vllm server `python -m vllm.entrypoints.openai.api_server --served-model-name q...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: lora response's moel name is incorrect bug;stale ### Your current environment ```text vllm 0.5.4 ``` ### 🐛 Describe the bug 1. start vllm server `python -m vllm.entrypoints.openai.api_server --served-model-name q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ax-model-len 131072 --enable-prefix-caching --enable-lora --lora-modules test1=/ai-deploy/output/ test2=/ai-deploy/output/ test3=/ai-deploy/output/` 2. request with model name test1 3. get response with model name `qwen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
