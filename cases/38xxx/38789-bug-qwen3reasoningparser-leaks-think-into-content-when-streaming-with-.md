# vllm-project/vllm#38789: [Bug]: Qwen3ReasoningParser leaks </think> into content when streaming with `stop` sequences (Related to #17468)

| 字段 | 值 |
| --- | --- |
| Issue | [#38789](https://github.com/vllm-project/vllm/issues/38789) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3ReasoningParser leaks </think> into content when streaming with `stop` sequences (Related to #17468)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When using `Qwen3ReasoningParser` with `stream=True` and `stop` sequences, the parser fails to properly separate `reasoning` and `content`. This bug reproduces consistently and results in the ` ` tag (and sometimes truncated reasoning text) leaking directly into the generated `content`. This only happens when `stream=True`. It works correctly when `stream=False`. As analyzed by @12lalala in #17468, providing a `stop` string sets `output_text_buffer_length`, which truncates/buffers the text in each chunk. This causes a desync in `Qwen3ReasoningParser`: when `end_token_id` arrives, the ` ` text is still buffered and hidden from `delta_text`. By the time it is flushed in subsequent chunks, the parser's logic breaks because the ID has expired from `previous_token_ids`. ### Environment / Setup Tested models: - Qwen/Qwen3.5-35B-A3B-FP8 - Qwen/Qwen3.5-122B-A10B-FP8 vLLM version: 0.18.1 Docker setup used for the test: ```bash docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:v0.18.1 \ --model Q...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed models: - Qwen/Qwen3.5-35B-A3B-FP8 - Qwen/Qwen3.5-122B-A10B-FP8 vLLM version: 0.18.1 Docker setup used for the test: ```bash docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3ReasoningParser leaks </think> into content when streaming with `stop` sequences (Related to #17468) bug ### Your current environment ### 🐛 Describe the bug ### Description When using `Qwen3ReasoningParser`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ken_ids`. ### Environment / Setup Tested models: - Qwen/Qwen3.5-35B-A3B-FP8 - Qwen/Qwen3.5-122B-A10B-FP8 vLLM version: 0.18.1 Docker setup used for the test: ```bash docker run --runtime nvidia --gpus all \ -v ~/.cache/...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: parser fails to properly separate `reasoning` and `content`. This bug reproduces consistently and results in the ` ` tag (and sometimes truncated reasoning text) leaking directly into the generated `content`. This only...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ooks like this: ```text [REASONING] Thinking Process: 1. **Analyze the Request:** * Input: "hello world" * Intent: This is a standard greeting or test input. * Expected Output: A friendly response, acknowledging the gre...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
