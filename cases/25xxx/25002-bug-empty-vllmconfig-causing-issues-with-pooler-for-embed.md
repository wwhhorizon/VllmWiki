# vllm-project/vllm#25002: [Bug]: Empty VllmConfig causing issues with Pooler.for_embed

| 字段 | 值 |
| --- | --- |
| Issue | [#25002](https://github.com/vllm-project/vllm/issues/25002) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty VllmConfig causing issues with Pooler.for_embed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `EmbeddingPoolerHead`'s init function: ``` from vllm.config import get_current_vllm_config from vllm.model_executor.models.adapters import _load_st_projector vllm_config = get_current_vllm_config() self.projector: Optional[nn.Module] = _load_st_projector( vllm_config.model_config) if vllm_config else None self.head_dtype = vllm_config.model_config.head_dtype ``` The `get_current_vllm_config` seems to get the default empty VllmConfig, resulting in an error ``` Traceback (most recent call last): File "/Users/prashantgupta/Documents/code/ibm/vllm/test_logits_processor.py", line 9, in pooler = Pooler.for_embed(pooler_config=pooler_config) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/prashantgupta/Documents/code/ibm/vllm/vllm/model_executor/layers/pooler.py", line 85, in for_embed return SimplePooler.from_config(resolved_config) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/prashantgupta/Documents/code/ibm/vllm/vllm/model_executor/layers/pooler.py", line 536, in from_config head = EmbeddingPoolerHead() ^^^^^^^^^^^^^^^^^^^^^ File "/Users/prashantgupta/Documents/code/ibm/vllm/vllm/model_executor/layers/pooler.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ug `EmbeddingPoolerHead`'s init function: ``` from vllm.config import get_current_vllm_config from vllm.model_executor.models.adapters import _load_st_projector vllm_config = get_current_vllm_config() self.projector: Op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mb! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Empty VllmConfig causing issues with Pooler.for_embed bug;stale ### Your current environment ### 🐛 Describe the bug `EmbeddingPoolerHead`'s init function: ``` from vllm.config import get_current_vllm_config f
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: vllm_config.model_config) if vllm_config else None self.head_dtype = vllm_config.model_config.head_dtype ``` The `get_current_vllm_config` seems to get the default empty VllmConfig, resulting in an error ``` Traceback (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: load_st_projector( vllm_config.model_config) if vllm_config else None self.head_dtype = vllm_config.model_config.head_dtype ``` The `get_current_vllm_config` seems to get the default empty VllmConfig, resulting in an er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
