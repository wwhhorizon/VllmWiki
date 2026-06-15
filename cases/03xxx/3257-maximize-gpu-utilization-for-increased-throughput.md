# vllm-project/vllm#3257: Maximize GPU utilization for increased throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#3257](https://github.com/vllm-project/vllm/issues/3257) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Maximize GPU utilization for increased throughput

### Issue 正文摘录

I am using vLLM endpoint with OpenAI API to send concurrent requests to Llama2-7B model that's deployed on a single A100 GPU. Regardless of the values I set for `--block-size`, `--swap-space`, `--max-num-seqs` or `--max-num-batched-tokens`, the GPU utilization always fluctuates between 65%-75% (momentarily, also goes lower or higher than this range) . Is there a way optimize GPU utilization and consequently enhance throughput? I am testing with 400 prompts (i.e. 400 concurrent requests) and also scaling up to 1200 requests but to no effect. Configuration: ``` vLLM==0.3.3 (pulled using latest docker image) Model: Llama2-7B Cuda 12.0 1 x A100 80GB GPU ``` Any help would be appreciated!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: but to no effect. Configuration: ``` vLLM==0.3.3 (pulled using latest docker image) Model: Llama2-7B Cuda 12.0 1 x A100 80GB GPU ``` Any help would be appreciated! performance ci_build;frontend_api;model_support cuda sl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I am using vLLM endpoint with OpenAI API to send concurrent requests to Llama2-7B model that's deployed on a single A100 GPU. Regardless of the values I set for `--block-size`, `--swap-space`, `--max-num-seqs` or `--max...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: send concurrent requests to Llama2-7B model that's deployed on a single A100 GPU. Regardless of the values I set for `--block-size`, `--swap-space`, `--max-num-seqs` or `--max-num-batched-tokens`, the GPU utilization al...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: deployed on a single A100 GPU. Regardless of the values I set for `--block-size`, `--swap-space`, `--max-num-seqs` or `--max-num-batched-tokens`, the GPU utilization always fluctuates between 65%-75% (momentarily, also...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Maximize GPU utilization for increased throughput stale I am using vLLM endpoint with OpenAI API to send concurrent requests to Llama2-7B model that's deployed on a single A100 GPU. Regardless of the values I set for `-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
