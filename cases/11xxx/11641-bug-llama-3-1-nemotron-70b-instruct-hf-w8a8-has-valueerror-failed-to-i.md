# vllm-project/vllm#11641: [Bug]: Llama-3.1-Nemotron-70B-Instruct-HF W8A8 has ValueError: Failed to invert hessian due to numerical instability.

| 字段 | 值 |
| --- | --- |
| Issue | [#11641](https://github.com/vllm-project/vllm/issues/11641) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.1-Nemotron-70B-Instruct-HF W8A8 has ValueError: Failed to invert hessian due to numerical instability.

### Issue 正文摘录

### Your current environment ### Your pip package version ### Model Input Dumps 2024-12-30T08:30:40.393240-0800 | compress_module | INFO - Compressing model.layers.3.model.layers.3.mlp.up_proj... 2024-12-30T08:30:42.984565-0800 | compress | METRIC - time 2.59 2024-12-30T08:30:42.986384-0800 | compress | METRIC - error 7.39 2024-12-30T08:30:42.986655-0800 | compress | METRIC - GPU 0 | usage: 33.10% | total memory: 85 GB 2024-12-30T08:30:42.986693-0800 | compress | METRIC - GPU 1 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986717-0800 | compress | METRIC - GPU 2 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986745-0800 | compress | METRIC - GPU 3 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986764-0800 | compress | METRIC - GPU 4 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986780-0800 | compress | METRIC - GPU 5 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986802-0800 | compress | METRIC - GPU 6 | usage: 23.62% | total memory: 85 GB 2024-12-30T08:30:42.986823-0800 | compress | METRIC - GPU 7 | usage: 15.54% | total memory: 85 GB 2024-12-30T08:30:42.986875-0800 | compress | METRIC - Compressed layer size: 469.848064 MB...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l instability. bug ### Your current environment ### Your pip package version ### Model Input Dumps 2024-12-30T08:30:40.393240-0800 | compress_module | INFO - Compressing model.layers.3.model.layers.3.mlp.up_proj... 2024...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Llama-3.1-Nemotron-70B-Instruct-HF W8A8 has ValueError: Failed to invert hessian due to numerical instability. bug ### Your current environment ### Your pip package version ### Model Input Dumps 2024-12-30T08:30
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ron-70B-Instruct-HF W8A8 has ValueError: Failed to invert hessian due to numerical instability. bug ### Your current environment ### Your pip package version ### Model Input Dumps 2024-12-30T08:30:40.393240-0800 | compr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er exception occurred: Traceback (most recent call last): File "/code/smooth_quant.py", line 43, in oneshot( File "/usr/local/lib/python3.12/dist-packages/llmcompressor/transformers/finetune/text_generation.py", line 82...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: File "/usr/local/lib/python3.12/dist-packages/llmcompressor/modifiers/quantization/gptq/utils/gptq_wrapper.py", line 176, in compress self.H = torch.linalg.cholesky(self.H, upper=True) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
