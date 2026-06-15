# vllm-project/vllm#39784: [Bug]: ReRank API online inference doesn't work well with given template

| 字段 | 值 |
| --- | --- |
| Issue | [#39784](https://github.com/vllm-project/vllm/issues/39784) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ReRank API online inference doesn't work well with given template

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Describe the bug I am serving `Qwen/Qwen3-Reranker-4B` with `vllm serve` and a custom `--chat-template` intended for Qwen3-Reranker scoring. The template is successfully loaded at startup, but during inference: 1. The reranking scores are identical to the case where no template is specified. 2. The logged prompt does not appear to be the rendered/template-expanded prompt. 3. In debug / warning logs, I can see the template source being loaded, but the Jinja variables (for example `{{ messages | ... }}`) are still printed literally instead of being rendered into the final prompt. This makes it look like the score template is loaded but not actually applied during `/rerank` or `/score` inference. According to the docs/examples, Qwen3-Reranker should support score templates in vLLM, and the official example shows using `vllm serve ... --runner pooling --chat-template ...` for online scoring/reranking. ## How I start my online vllm ```bash CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-Reranker-4B \ --host 127.0.0.1 \ --port 8021 \ --runner pooling \ --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"],"classifier_fro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: . The reranking scores are identical to the case where no template is specified. 2. The logged prompt does not appear to be the rendered/template-expanded prompt. 3. In debug / warning logs, I can see the template sourc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment ### 🐛 Describe the bug ### Describe the bug I am serving `Qwen/Qwen3-Reranker-4B` with `vllm serve` and a custom `--chat-template` intended for Qwen3-Reranker scoring. The template is successfully loaded at sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ..` for online scoring/reranking. ## How I start my online vllm ```bash CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-Reranker-4B \ --host 127.0.0.1 \ --port 8021 \ --runner pooling \ --hf_overrides '{"architectures":["Q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ranker":true}' \ --chat-template qwen3_reranker.jinja \ --enable-log-requests ``` My request is below: ``` import requests url = "http://127.0.0.1:8021/v1/rerank" payload = { "model": "Qwen/Qwen3-Reranker-4B", "query":...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support cuda build_error env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
