# vllm-project/vllm#26675: [Bug]:AssertionError: assert self._connector_metadata is not None when using graph mode

| 字段 | 值 |
| --- | --- |
| Issue | [#26675](https://github.com/vllm-project/vllm/issues/26675) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:AssertionError: assert self._connector_metadata is not None when using graph mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we tried to use the SharedStorageConnector, according to the official document, we run `examples/offline_inference/disaggregated-prefill-v1/run.sh`, If not using graph mode with `enforce_eager = True`, there is no problem; However, if we remove the `enforce_eager = True`, using the graph mode, there occurs an error as following: ``` 2025-10-12 20:12:59,984 - INFO - autotuner.py:262 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 67/67 [00:02 [rank0]: main() [rank0]: File "/home/yinhanqiu1/workspace/vllm_110_adapt/vllm-110/vllm/examples/offline_inference/disaggregated-prefill-v1/prefill_example.py", line 24, in main [rank0]: llm = LLM( [rank0]: ^^^^ [rank0]: File "/home/yinhanqiu1/workspace/vllm_110_adapt/vllm-110/vllm/vllm/entrypoints/llm.py", line 297, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g When we tried to use the SharedStorageConnector, according to the official document, we run `examples/offline_inference/disaggregated-prefill-v1/run.sh`, If not using graph mode with `enforce_eager = True`, there is n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m_engine.py", line 177, in from_engine_args [rank0]: return cls(vllm_config=vllm_config, [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/yinhanqiu1/workspace/vllm_110_adapt/vllm-110/vllm/vllm/v1/engine/llm_en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: the official document, we run `examples/offline_inference/disaggregated-prefill-v1/run.sh`, If not using graph mode with `enforce_eager = True`, there is no problem; However, if we remove the `enforce_eager = True`, usi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: or as following: ``` 2025-10-12 20:12:59,984 - INFO - autotuner.py:262 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|███████████████████████████████...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .py:262 - flashinfer.jit: [Autotuner]: Autotuning process ends Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
