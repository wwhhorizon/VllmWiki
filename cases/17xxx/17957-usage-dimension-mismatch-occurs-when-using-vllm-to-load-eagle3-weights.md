# vllm-project/vllm#17957: [Usage]: Dimension mismatch occurs when using vllm to load Eagle3 weights

| 字段 | 值 |
| --- | --- |
| Issue | [#17957](https://github.com/vllm-project/vllm/issues/17957) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Dimension mismatch occurs when using vllm to load Eagle3 weights

### Issue 正文摘录

### Your current environment vllm version: 0.8.5 code: https://github.com/CentML/vllm/blob/776588735d2b055b8a18da81c86132bc8d8a960b/examples/offline_inference/eagle.py [rank0]: Traceback (most recent call last): [rank0]: File "/data5/cissie.wu/7-eagle/test.04.py", line 123, in [rank0]: main() [rank0]: File "/data5/cissie.wu/7-eagle/test.04.py", line 74, in main [rank0]: llm = LLM( [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/utils.py", line 1161, in inner [rank0]: return fn(*args, **kwargs) [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 247, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 510, in from_engine_args [rank0]: return engine_cls.from_vllm_config( [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 486, in from_vllm_config [rank0]: return cls( [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 275, in __init__ [rank0]: self.model_executor = executor_class(vllm_config=vllm_config) [rank0]: File "/h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ing vllm to load Eagle3 weights usage ### Your current environment vllm version: 0.8.5 code: https://github.com/CentML/vllm/blob/776588735d2b055b8a18da81c86132bc8d8a960b/examples/offline_inference/eagle.py [rank0]: Trac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Dimension mismatch occurs when using vllm to load Eagle3 weights usage ### Your current environment vllm version: 0.8.5 code: https://github.com/CentML/vllm/blob/776588735d2b055b8a18da81c86132bc8d8a960b/example...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: , line 510, in from_engine_args [rank0]: return engine_cls.from_vllm_config( [rank0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 486, in from_vllm_config [rank0]: return cls(...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Usage]: Dimension mismatch occurs when using vllm to load Eagle3 weights usage ### Your current environment vllm version: 0.8.5 code: https://github.com/CentML/vllm/blob/776588735d2b055b8a18da81c86132bc8d8a960b/example...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nk0]: File "/home/jovyan/.local/lib/python3.10/site-packages/vllm/spec_decode/spec_decode_worker.py", line 354, in init_device [rank0]: self.proposer_worker.load_model() [rank0]: File "/home/jovyan/.local/lib/python3.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
