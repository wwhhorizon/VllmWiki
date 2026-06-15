# vllm-project/vllm#33053: [Bug]: LongCat-Flash-Thinking-2601 still appears to be unsupported

| 字段 | 值 |
| --- | --- |
| Issue | [#33053](https://github.com/vllm-project/vllm/issues/33053) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LongCat-Flash-Thinking-2601 still appears to be unsupported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Title [Bug]: TorchDynamo compilation failure (`AttributeError: []`) when serving 'LongcatCausalLM' (LongCat-Flash-Thinking-2601) ### Description I am attempting to serve the `LongCat-Flash-Thinking-2601` model (architecture `LongcatCausalLM`) using vLLM in a multi-node Ray environment. Since `LongcatCausalLM` is not natively registered in the newest vLLM version, I manually registered it in `vllm/model_executor/models/registry.py` to reuse the existing `longcat_flash` implementation (assuming compatibility with recent LongCat logic pr/23991). **The Issue:** The model weights load successfully, but the engine crashes immediately afterwards during the **TorchDynamo graph compilation phase**. The error is an `AttributeError: []` triggered within the `forward` pass of `longcat_flash.py`. ### Reproduction Steps 1. **Model:** `LongCat-Flash-Thinking-2601` . 2. **Code Modification:** To enable the model loading, I manually added the following architecture mapping to `_model_registry` in `vllm/model_executor/models/registry.py`: ```python "LongcatCausalLM": ("longcat_flash", "LongcatFlashForCausalLM"), ``` 3. **Launch Command:** The...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: . Since `LongcatCausalLM` is not natively registered in the newest vLLM version, I manually registered it in `vllm/model_executor/models/registry.py` to reuse the existing `longcat_flash` implementation (assuming compat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: To enable the model loading, I manually added the following architecture mapping to `_model_registry` in `vllm/model_executor/models/registry.py`: ```python "LongcatCausalLM": ("longcat_flash", "LongcatFlashForCausalLM"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # Description I am attempting to serve the `LongCat-Flash-Thinking-2601` model (architecture `LongcatCausalLM`) using vLLM in a multi-node Ray environment. Since `LongcatCausalLM` is not natively registered in the newes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: iption I am attempting to serve the `LongCat-Flash-Thinking-2601` model (architecture `LongcatCausalLM`) using vLLM in a multi-node Ray environment. Since `LongcatCausalLM` is not natively registered in the newest vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: LongCat-Flash-Thinking-2601 still appears to be unsupported bug;stale ### Your current environment ### 🐛 Describe the bug ### Title [Bug]: TorchDynamo compilation failure (`AttributeError: []`) when serving 'Long...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
