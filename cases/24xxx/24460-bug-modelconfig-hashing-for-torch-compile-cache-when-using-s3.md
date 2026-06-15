# vllm-project/vllm#24460: [Bug]: ModelConfig Hashing for Torch.compile cache when using S3

| 字段 | 值 |
| --- | --- |
| Issue | [#24460](https://github.com/vllm-project/vllm/issues/24460) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModelConfig Hashing for Torch.compile cache when using S3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading model from S3 using RunAI streamer, the `self.model` and `self.tokenizer` fields in `ModelConfig` are replaced with tmp directories in the function `maybe_pull_model_tokenizer_for_s3` This becomes an issue later down the line when torch compile tries to find cache, but since the hash function for ModelConfig includes a random directory, it is never able to hit the cache. Can be replicated by running `vllm serve s3://bucket/repo/ --load-format runai_streamer` twice and noting that the cache is not used. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: ModelConfig Hashing for Torch.compile cache when using S3 bug ### Your current environment ### 🐛 Describe the bug When loading model from S3 using RunAI streamer, the `self.model` and `self.tokenizer` fields in `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ModelConfig Hashing for Torch.compile cache when using S3 bug ### Your current environment ### 🐛 Describe the bug When loading model from S3 using RunAI streamer, the `self.model` and `self.tokenizer` fields in `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
