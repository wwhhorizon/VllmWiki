# vllm-project/vllm#22290: [Bug]: gpt-oss on Ampere

| 字段 | 值 |
| --- | --- |
| Issue | [#22290](https://github.com/vllm-project/vllm/issues/22290) |
| 状态 | closed |
| 标签 | bug;gpt-oss |
| 评论 | 64; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss on Ampere

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` uv venv --python 3.12 --seed source venv/bin/activate uv pip install \ --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match vllm serve openai/gpt-oss-120b -tp 8 ``` AssertionError: Sinks are only supported in FlashAttention 3 I also tried: ``` VLLM_FLASH_ATTN_VERSION=2 vllm serve openai/gpt-oss-120b -tp 8 --hf-overrides '{"sink_token_len": 0, "use_sliding_window": false}' ``` AssertionError: Sinks are only supported in FlashAttention 3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: he bug ``` uv venv --python 3.12 --seed source venv/bin/activate uv pip install \ --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: gpt-oss on Ampere bug;gpt-oss ### Your current environment ### 🐛 Describe the bug ``` uv venv --python 3.12 --seed source venv/bin/activate uv pip install \ --pre vllm==0.10.1+gptoss \ --extra-index-url https://w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss on Ampere bug;gpt-oss ### Your current environment ### 🐛 Describe the bug ``` uv venv --python 3.12 --seed source venv/bin/activate uv pip install \ --pre vllm==0.10.1+gptoss \ --extra-index-url http
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: enai/gpt-oss-120b -tp 8 ``` AssertionError: Sinks are only supported in FlashAttention 3 I also tried: ``` VLLM_FLASH_ATTN_VERSION=2 vllm serve openai/gpt-oss-120b -tp 8 --hf-overrides '{"sink_token_len": 0, "use_slidin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 120b -tp 8 --hf-overrides '{"sink_token_len": 0, "use_sliding_window": false}' ``` AssertionError: Sinks are only supported in FlashAttention 3 ### Before submitting a new issue... - [x] Make sure you already searched f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
