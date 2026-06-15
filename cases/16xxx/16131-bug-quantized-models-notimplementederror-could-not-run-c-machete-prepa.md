# vllm-project/vllm#16131: [Bug]: Quantized models - NotImplementedError: Could not run '_C::machete_prepack_B'

| 字段 | 值 |
| --- | --- |
| Issue | [#16131](https://github.com/vllm-project/vllm/issues/16131) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Quantized models - NotImplementedError: Could not run '_C::machete_prepack_B'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading quantized W4A16 Gemma3: https://huggingface.co/abhishekchohan/gemma-3-27b-it-quantized-W4A16 I get the following error: ``` INFO 04-06 14:45:45 [loader.py:447] Loading weights took 1.30 seconds ERROR 04-06 14:45:45 [core.py:386] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-06 14:45:45 [core.py:386] File "/workspace/vllm/vllm/v1/engine/core.py", line 377, in run_engine_core ERROR 04-06 14:45:45 [core.py:386] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-06 14:45:45 [core.py:386] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-06 14:45:45 [core.py:386] File "/workspace/vllm/vllm/v1/engine/core.py", line 319, in __init__ ERROR 04-06 14:45:45 [core.py:386] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-06 14:45:45 [core.py:386] File "/workspace/vllm/vllm/v1/engine/core.py", line 67, in __init__ ERROR 04-06 14:45:45 [core.py:386] self.model_executor = executor_class(vllm_config) ERROR 04-06 14:45:45 [core.py:386] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-06 14:45:45 [core.py:386] File "/workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__ ERROR 04-06 14:45:45 [co...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: or: Could not run '_C::machete_prepack_B' with arguments from the 'CUDA' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using cus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Quantized models - NotImplementedError: Could not run '_C::machete_prepack_B' bug;stale ### Your current environment ### 🐛 Describe the bug When loading quantized W4A16 Gemma3: https://huggingface.co/abhishekchoh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /workspace/vllm/vllm/model_executor/layers/quantization/kernels/mixed_precision/machete.py", line 96, in process_weights_after_loading ERROR 04-06 14:45:45 [core.py:386] self._transform_param(layer, self.w_q_name, trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tedError: Could not run '_C::machete_prepack_B' with arguments from the 'CUDA' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if usi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -06 14:45:45 [core.py:386] x.data = ops.machete_prepack_B(x.data.t().contiguous().t(), ERROR 04-06 14:45:45 [core.py:386] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-06 14:45:45 [core.py:386] File "/work...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
