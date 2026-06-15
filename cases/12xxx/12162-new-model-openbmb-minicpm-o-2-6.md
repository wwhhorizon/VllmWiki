# vllm-project/vllm#12162: [New Model]: openbmb/MiniCPM-o-2_6

| 字段 | 值 |
| --- | --- |
| Issue | [#12162](https://github.com/vllm-project/vllm/issues/12162) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: openbmb/MiniCPM-o-2_6

### Issue 正文摘录

### The model to consider. Adding support for MiniCPM-o-2, please review. HuggingFace Page: https://huggingface.co/openbmb/MiniCPM-o-2_6 MiniCPM-o 2.6 is the latest and most capable model in the MiniCPM-o series. The model is built in an end-to-end fashion based on SigLip-400M, Whisper-medium-300M, ChatTTS-200M, and Qwen2.5-7B with a total of 8B parameters. It exhibits a significant performance improvement over MiniCPM-V 2.6, and introduces new features for real-time speech conversation and multimodal live streaming. Notable features of MiniCPM-o 2.6 include ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/minicpmv.py ### What's your difficulty of supporting the model you want? ``` File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 421, in inspect_model_cls return self._raise_for_unsupported(architectures) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 382, in _raise_for_unsupported raise ValueError( ValueError: Model architectures ['MiniCPMO'] are not supported for now. ``` ### Before...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: openbmb/MiniCPM-o-2_6 new-model ### The model to consider. Adding support for MiniCPM-o-2, please review. HuggingFace Page: https://huggingface.co/openbmb/MiniCPM-o-2_6 MiniCPM-o 2.6 is the latest and most...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ", line 421, in inspect_model_cls return self._raise_for_unsupported(architectures) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ge: https://huggingface.co/openbmb/MiniCPM-o-2_6 MiniCPM-o 2.6 is the latest and most capable model in the MiniCPM-o series. The model is built in an end-to-end fashion based on SigLip-400M, Whisper-medium-300M, ChatTTS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
