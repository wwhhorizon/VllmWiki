# vllm-project/vllm#25165: [Bug]: "pooling_type='ALL' no longer supported for embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#25165](https://github.com/vllm-project/vllm/issues/25165) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "pooling_type='ALL' no longer supported for embeddings

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to get embeddings from [`jinaai/jina-embeddings-v4-vllm-text-matching`](https://huggingface.co/jinaai/jina-embeddings-v4-vllm-text-matching) (based on the `Qwen2_5_VLForConditionalGeneration` architecture), I encounter the following error: ``` (EngineCore_DP0 pid=1671528) File "/home/admin/saba/vllm-bug/venv/lib/python3.11/site-packages/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model (EngineCore_DP0 pid=1671528) model = initialize_model(vllm_config=vllm_config, (EngineCore_DP0 pid=1671528) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1671528) File "/home/admin/saba/vllm-bug/venv/lib/python3.11/site-packages/vllm/model_executor/model_loader/utils.py", line 64, in initialize_model (EngineCore_DP0 pid=1671528) return model_class(vllm_config=vllm_config, prefix=prefix) (EngineCore_DP0 pid=1671528) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1671528) File "/home/admin/saba/vllm-bug/venv/lib/python3.11/site-packages/vllm/model_executor/models/adapters.py", line 163, in __init__ (EngineCore_DP0 pid=1671528) super().__init__(vllm_config=vllm_config, pre...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ddings-v4-vllm-text-matching#usage).) This same code worked in previous versions of vLLM, so this seems to be a recent change. Code to reproduce: ```python from vllm import LLM from vllm.config import PoolerConfig model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: embeddings from [`jinaai/jina-embeddings-v4-vllm-text-matching`](https://huggingface.co/jinaai/jina-embeddings-v4-vllm-text-matching) (based on the `Qwen2_5_VLForConditionalGeneration` architecture), I encounter the fol...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: line 260, in _init_pooler (EngineCore_DP0 pid=1671528) self.pooler = DispatchPooler( (EngineCore_DP0 pid=1671528) ^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1671528) File "/home/admin/saba/vllm-bug/venv/lib/python3.11/site-pac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4-vllm-text-matching) (based on the `Qwen2_5_VLForConditionalGeneration` architecture), I encounter the following error: ``` (EngineCore_DP0 pid=1671528) File "/home/admin/saba/vllm-bug/venv/lib/python3.11/site-packages...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: previous versions of vLLM, so this seems to be a recent change. Code to reproduce: ```python from vllm import LLM from vllm.config import PoolerConfig model = LLM( model="jinaai/jina-embeddings-v4-vllm-text-matching", t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
