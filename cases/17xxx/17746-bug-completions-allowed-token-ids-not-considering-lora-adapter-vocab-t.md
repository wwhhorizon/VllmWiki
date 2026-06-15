# vllm-project/vllm#17746: [Bug]: completions allowed_token_ids not considering lora adapter vocab tokens in v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17746](https://github.com/vllm-project/vllm/issues/17746) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: completions allowed_token_ids not considering lora adapter vocab tokens in v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the completions API with the `allowed_token_ids` parameter with token ids that come from lora adapter tokenizers, the v1 engine is giving an out-of-vocab error while the v0 engine does not. The issue appears to be that the v1 engine isn't checking whether this is a lora request to load the lora adapter's tokenizer before checking the allowed token id range. I hit this with some lora adapters that are not publicly available, so I cannot fully share a reproducer right now, but I'm adding the details I can below. Here's an example of how I am serving the base model plus lora adapters: ``` vllm serve /path/to/models/mixtral-8x7b-instruct-v0-1 \ --max-num-seqs 512 --enable-lora --enable-prefix-caching \ --max-lora-rank 64 --dtype bfloat16 --lora-dtype bfloat16 \ --fully-sharded-loras \ --lora-modules \ skill-classifier-v3-clm=/path/to/models/skills-adapter-v3 \ text-classifier-knowledge-v3-clm=/path/to/models/knowledge-adapter-v3 \ --tensor-parallel-size 8 ``` Sending a request such as this triggers the error in the v1 engine. Note that all the token ids sent in `allowed_token_ids` are defined in my lora adapter's tokenizer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: max_tokens=1, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [1, 1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -seqs 512 --enable-lora --enable-prefix-caching \ --max-lora-rank 64 --dtype bfloat16 --lora-dtype bfloat16 \ --fully-sharded-loras \ --lora-modules \ skill-classifier-v3-clm=/path/to/models/skills-adapter-v3 \ text-cla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e appears to be that the v1 engine isn't checking whether this is a lora request to load the lora adapter's tokenizer before checking the allowed token id range. I hit this with some lora adapters that are not publicly...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
