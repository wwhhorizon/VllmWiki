# vllm-project/vllm#20605: [Bug]: The mixed precision model lacks kernel image in the Blackwell architecture(version:0.9.2 + cu12.8 + RTX5060)

| 字段 | 值 |
| --- | --- |
| Issue | [#20605](https://github.com/vllm-project/vllm/issues/20605) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The mixed precision model lacks kernel image in the Blackwell architecture(version:0.9.2 + cu12.8 + RTX5060)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run any gptq q4 mix precision llm at Blackwell. ``` vllm serve jakiAJK/DeepSeek-R1-Distill-Qwen-7B_GPTQ-int4 ``` will get: ``` (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/kernels/mixed_precision/machete.py", line 80, in transform_w_q (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] x.data = ops.machete_prepack_B(x.data.t().contiguous().t(), (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] ^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] RuntimeError: CUDA error: no kernel image is available for execution on the device ``` I have tried the latest Docker and Master code(),In these environments, the FP16 model can work in blackwell. But when I use mixed precision, such as the gpqt q4 model, they all fail. I understand the intensity of our community work, but I also urgently need to address this issue. If it cannot be fixed in the short term, could you provide a suggestion that may allow me to participate in th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: The mixed precision model lacks kernel image in the Blackwell architecture(version:0.9.2 + cu12.8 + RTX5060) bug;stale ### Your current environment ### 🐛 Describe the bug run any gptq q4 mix precision llm at Blac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: The mixed precision model lacks kernel image in the Blackwell architecture(version:0.9.2 + cu12.8 + RTX5060) bug;stale ### Your current environment ### 🐛 Describe the bug run any gptq q4 mix precision llm at Blac...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm at Blackwell. ``` vllm serve jakiAJK/DeepSeek-R1-Distill-Qwen-7B_GPTQ-int4 ``` will get: ``` (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] File "/usr/local/lib/python3.12/dist-packages/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: multiproc_executor.py:487] x.data = ops.machete_prepack_B(x.data.t().contiguous().t(), (VllmWorker rank=1 pid=405) ERROR 07-07 03:06:15 [multiproc_executor.py:487] ^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=1 pid=405) ERR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The mixed precision model lacks kernel image in the Blackwell architecture(version:0.9.2 + cu12.8 + RTX5060) bug;stale ### Your current environment ### 🐛 Describe the bug run any gptq q4 mix precision llm at Blac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
