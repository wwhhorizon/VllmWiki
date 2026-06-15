# vllm-project/vllm#42687: [Bug]: Gemma-4 fails to start on GPUs with < 70GB memory due to max_num_batched_tokens < multimodal token size

| 字段 | 值 |
| --- | --- |
| Issue | [#42687](https://github.com/vllm-project/vllm/issues/42687) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-4 fails to start on GPUs with < 70GB memory due to max_num_batched_tokens < multimodal token size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma-4 (google/gemma-4-31b-it) fails to start on any GPU instance with less than 70GB memory per device when using the default max_num_batched_tokens configuration. The problem: Gemma-4 is a bidirectional multimodal model. Because of its bidirectional attention for vision tokens, vLLM disables chunked prefill for multimodal inputs. The model's transformers config defines max_multimodal_token_per_item = 2496, meaning a single multimodal input (e.g., one image) requires at least 2496 tokens to be processed as a single batch. However, vLLM auto-calculates max_num_batched_tokens = 2048 for any GPU with less than 70GB memory. Since 2496 > 2048, vLLM cannot fit even a single multimodal item into the batch budget. This causes the engine to either reject requests or fail during initialization depending on the version. This effectively blocks Gemma-4 deployment on all cost-effective GPU instances (A100 40GB, L4 24GB, A10G 24GB) without manually overriding max_num_batched_tokens. Instances confirmed working (auto-calculated value exceeds 2496): - p5en.48xlarge (H200, 141GB per GPU) - g7e.2xlarge (RTX PRO 6000, 96GB per GPU) Instances conf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma-4 fails to start on GPUs with < 70GB memory due to max_num_batched_tokens < multimodal token size bug ### Your current environment ### 🐛 Describe the bug Gemma-4 (google/gemma-4-31b-it) fails to start on an
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fectively blocks Gemma-4 deployment on all cost-effective GPU instances (A100 40GB, L4 24GB, A10G 24GB) without manually overriding max_num_batched_tokens. Instances confirmed working (auto-calculated value exceeds 2496...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: to either reject requests or fail during initialization depending on the version. This effectively blocks Gemma-4 deployment on all cost-effective GPU instances (A100 40GB, L4 24GB, A10G 24GB) without manually overridin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: of its bidirectional attention for vision tokens, vLLM disables chunked prefill for multimodal inputs. The model's transformers config defines max_multimodal_token_per_item = 2496, meaning a single multimodal input (e.g...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ail during initialization depending on the version. This effectively blocks Gemma-4 deployment on all cost-effective GPU instances (A100 40GB, L4 24GB, A10G 24GB) without manually overriding max_num_batched_tokens. Inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
