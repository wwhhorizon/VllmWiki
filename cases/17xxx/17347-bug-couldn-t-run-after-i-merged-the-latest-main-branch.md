# vllm-project/vllm#17347: [Bug]: Couldn't run after I merged the latest main branch

| 字段 | 值 |
| --- | --- |
| Issue | [#17347](https://github.com/vllm-project/vllm/issues/17347) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Couldn't run after I merged the latest main branch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` ERROR 04-29 11:15:09 [core.py:431] EngineCore failed to start. ERROR 04-29 11:15:09 [core.py:431] Traceback (most recent call last): ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/engine/core.py", line 421, in run_engine_core ERROR 04-29 11:15:09 [core.py:431] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/engine/core.py", line 362, in __init__ ERROR 04-29 11:15:09 [core.py:431] super().__init__(vllm_config, executor_class, log_stats, ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/engine/core.py", line 64, in __init__ ERROR 04-29 11:15:09 [core.py:431] self.model_executor = executor_class(vllm_config) ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/executor/executor_base.py", line 52, in __init__ ERROR 04-29 11:15:09 [core.py:431] self._init_executor() ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/executor/uniproc_executor.py", line 46, in _init_executor ERROR 04-29 11:15:09 [core.py:431] self.collective_rpc("init_worker", args=([kwargs], )) ERROR 04-29 11:15:09 [core.py:43...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e 32, in ERROR 04-29 11:15:09 [core.py:431] from vllm.v1.attention.backends.flash_attn import FlashAttentionMetadata ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/attention/backends/flash_attn.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in __init__ ERROR 04-29 11:15:09 [core.py:431] super().__init__(vllm_config, executor_class, log_stats, ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/engine/core.py", line 64, in __init__ ERROR 0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: resolve_obj_by_qualname ERROR 04-29 11:15:09 [core.py:431] module = importlib.import_module(module_name) ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/.conda/envs/myenv/lib/python3.10/importlib/__init__.py",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 431] from vllm.v1.attention.backends.flash_attn import FlashAttentionMetadata ERROR 04-29 11:15:09 [core.py:431] File "/home/zjm.zhang/vllm/vllm/v1/attention/backends/flash_attn.py", line 26, in ERROR 04-29 11:15:09 [co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
