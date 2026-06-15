# vllm-project/vllm#25256: [Bug]: Make FlexAttention compatible with hybrid allocator

| 字段 | 值 |
| --- | --- |
| Issue | [#25256](https://github.com/vllm-project/vllm/issues/25256) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Make FlexAttention compatible with hybrid allocator

### Issue 正文摘录

### Your current environment Null ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] self.impl.forward(self, (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] File "/home/mozf/develop-projects/vllm/vllm/v1/attention/backends/flex_attention.py", line 805, in forward (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] out = flex_attention_compiled( (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] ^^^^^^^^^^^^^^^^^^^^^^^^ ... (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] File "/home/mozf/develop-projects/vllm/.venv/lib/python3.12/site-packages/torch/_subclasses/meta_utils.py", line 312, in describe_tensor (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] storage = self.describe_storage(t.untyped_storage(), trace=trace) (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] ^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] torch._dynamo.exc.InternalTorchDynamoError: RuntimeError: Error: accessing tensor output of CUDAGraphs that has been overwritten by a subsequent run. Stack trace: File "/home/mozf/develop-projects/vllm/.venv/lib/...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nternalTorchDynamoError: RuntimeError: Error: accessing tensor output of CUDAGraphs that has been overwritten by a subsequent run. Stack trace: File "/home/mozf/develop-projects/vllm/.venv/lib/python3.12/site-packages/t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [core.py:720] File "/home/mozf/develop-projects/vllm/vllm/v1/attention/backends/flex_attention.py", line 805, in forward (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] out = flex_attention_compiled( (En...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pid=3629297) ERROR 09-16 23:53:40 [core.py:720] out = flex_attention_compiled( (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:40 [core.py:720] ^^^^^^^^^^^^^^^^^^^^^^^^ ... (EngineCore_DP0 pid=3629297) ERROR 09-16 23:53:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: site-packages/torch/nn/attention/flex_attention.py", line 903, in create_block_mask ``` - Reference: https://github.com/vllm-project/vllm/pull/24089#issuecomment-3299436314, https://github.com/vllm-project/vllm/pull/240...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: will trigger above exception. - This issue significantly affected hybrid models performance (needs to disable hybrid allocator currently) and blocked whisper v1 support on old GPUs. - We should investigate this issue an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
